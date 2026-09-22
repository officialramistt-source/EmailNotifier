import os
import re
from datetime import datetime, date

class NetworkingTracker:
    def __init__(self, workspace_root=None, config=None):
        if workspace_root is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.workspace_root = os.path.dirname(base_dir)
        else:
            self.workspace_root = workspace_root

        self.graph_dir = os.path.join(self.workspace_root, "Networking", "graph")
        self.config = config or {}
        self.thresholds = self.config.get("networking", {}).get("thresholds_days", {
            "1-й круг": 10,
            "2-й круг": 14,
            "3-й круг": 21,
            "default": 14
        })

    def generate_starter_phrase(self, name, sphere, role, notes):
        name_clean = name.split()[0]
        sphere_lower = (sphere or "").lower()
        notes_lower = (notes or "").lower()

        if "java" in notes_lower or "самат" in name_clean.lower():
            return f"«Привет, {name_clean}! Как твои комнатные растения и лимон? Получается на этой неделе пересечься попить чаю?»"
        elif "инсаф" in name_clean.lower() or "ивмиит" in notes_lower:
            return f"«Привет, {name_clean}! Как успехи с проектами для ИВМиИТ? Будешь на этой неделе на волейболе?»"
        elif "алмаз" in name_clean.lower() or "bmw" in notes_lower:
            return f"«Привет, {name_clean}! Как дела? Планируете на этой неделе сборы на Цирке?»"
        elif "айнур" in name_clean.lower() or "рилс" in notes_lower or "блог" in notes_lower:
            return f"«Привет, {name_clean}! Как учеба в КГМУ и съемки рилсов? Что нового?»"
        elif "серег" in name_clean.lower() or "сергей" in name_clean.lower() or "sandbox" in notes_lower:
            return f"«Привет, Серёга! Как дела по Alpha Sandbox? Давай сверимся по статусу на выходных!»"
        elif "бег" in sphere_lower or "волейбол" in sphere_lower:
            return f"«Привет, {name_clean}! Как форма, тренируешься? Будешь на следующей тренировке?»"
        else:
            return f"«Привет, {name_clean}! Давно не общались, как твои дела и проекты? Давай переспросимся!»"

    def get_overdue_contacts(self):
        if not os.path.exists(self.graph_dir):
            return []

        contacts = []
        today = date.today()

        for file_name in os.listdir(self.graph_dir):
            if not file_name.endswith(".md") or file_name in ["Инструкция.md", "Я.md"]:
                continue

            file_path = os.path.join(self.graph_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                contact_name = file_name.replace(".md", "")

                closeness = "2-й круг"
                sphere = "Общение"
                contact_info = "@telegram"
                last_contact_str = None

                m_closeness = re.search(r'closeness:\s*([^\n]+)', content)
                if m_closeness: closeness = m_closeness.group(1).strip()

                m_sphere = re.search(r'sphere:\s*([^\n]+)', content)
                if m_sphere: sphere = m_sphere.group(1).strip()

                m_info = re.search(r'contact_info:\s*([^\n]+)', content)
                if m_info: contact_info = m_info.group(1).strip()

                m_lc = re.search(r'last_contact:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', content)
                if m_lc:
                    last_contact_str = m_lc.group(1).strip()

                if not last_contact_str:
                    m_date = re.search(r'Дата знакомства:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', content)
                    if m_date:
                        last_contact_str = m_date.group(1).strip()

                if last_contact_str:
                    try:
                        last_date = datetime.strptime(last_contact_str, "%Y-%m-%d").date()
                        days_passed = (today - last_date).days
                    except ValueError:
                        days_passed = 30
                else:
                    days_passed = 30

                threshold = self.thresholds.get(closeness, self.thresholds.get("default", 14))
                is_overdue = days_passed >= threshold

                starter = self.generate_starter_phrase(contact_name, sphere, "", content)

                contacts.append({
                    "name": contact_name,
                    "closeness": closeness,
                    "sphere": sphere,
                    "contact_info": contact_info,
                    "days_passed": days_passed,
                    "threshold": threshold,
                    "is_overdue": is_overdue,
                    "starter_phrase": starter
                })
            except Exception as e:
                print(f"[NetworkingTracker] Error parsing {file_name}: {e}")

        # Сортируем: сначала просроченные по убыванию дней
        contacts.sort(key=lambda x: (not x["is_overdue"], -x["days_passed"]))
        return contacts
