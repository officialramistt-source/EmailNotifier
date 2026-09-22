import os
import json
from datetime import datetime

class PlannerTracker:
    def __init__(self, workspace_root=None):
        if workspace_root is None:
            # EmailNotifier/modules -> EmailNotifier -> projectAnti
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.workspace_root = os.path.dirname(base_dir)
        else:
            self.workspace_root = workspace_root
            
        self.planner_db_path = os.path.join(self.workspace_root, "WebPlanner", "db", "planner_state.json")

    def load_planner_state(self):
        if not os.path.exists(self.planner_db_path):
            return None
        try:
            with open(self.planner_db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[PlannerTracker] Error loading planner state: {e}")
            return None

    def get_today_key(self):
        # 0 = Monday, 6 = Sunday
        weekday_map = {
            0: "monday",
            1: "tuesday",
            2: "wednesday",
            3: "thursday",
            4: "friday",
            5: "saturday",
            6: "sunday"
        }
        return weekday_map[datetime.now().weekday()]

    def get_today_tasks_and_habits(self):
        state = self.load_planner_state()
        if not state:
            return {
                "focus": "Нет данных",
                "tasks": [],
                "habits": [],
                "completed_tasks_count": 0,
                "total_tasks_count": 0
            }

        focus = state.get("focus", "Двигаться вперед!")
        today_key = self.get_today_key()
        weekly_tasks = state.get("weeklyTasks", {})
        today_tasks = weekly_tasks.get(today_key, [])

        tasks_summary = []
        completed_count = 0
        for t in today_tasks:
            is_done = t.get("done", False)
            if is_done:
                completed_count += 1
            priority = t.get("priority", "important")
            priority_icon = "🔴" if priority == "critical" else ("🟠" if priority == "important" else "🟢")
            tasks_summary.append({
                "id": t.get("id"),
                "text": t.get("text", "Без названия"),
                "done": is_done,
                "priority": priority,
                "priority_icon": priority_icon
            })

        # Habits status
        habits = state.get("habits", [])
        weekday_idx = datetime.now().weekday()
        habits_summary = []
        for h in habits:
            history = h.get("history", [False] * 7)
            is_done_today = history[weekday_idx] if weekday_idx < len(history) else False
            habits_summary.append({
                "id": h.get("id"),
                "name": h.get("name", "Привычка"),
                "category": h.get("category", "mind"),
                "done_today": is_done_today
            })

        return {
            "focus": focus,
            "today_name": today_key.capitalize(),
            "tasks": tasks_summary,
            "habits": habits_summary,
            "completed_tasks_count": completed_count,
            "total_tasks_count": len(tasks_summary)
        }
