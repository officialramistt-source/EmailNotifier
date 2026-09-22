import os
from datetime import datetime, date

class PddTracker:
    def __init__(self, workspace_root=None):
        if workspace_root is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.workspace_root = os.path.dirname(base_dir)
        else:
            self.workspace_root = workspace_root

        # График 40 билетов ПДД на август
        self.pdd_schedule = {
            "2026-08-21": {"tickets": "Билеты 1 – 3", "focus": "Общие положения, обязанности водителей, сигналы светофора"},
            "2026-08-22": {"tickets": "Билеты 4 – 7", "focus": "Начало движения, маневрирование, расположение ТС на проезжей части"},
            "2026-08-23": {"tickets": "Билеты 8 – 11", "focus": "Скорость движения, обгон, опережение, встречный разъезд"},
            "2026-08-24": {"tickets": "Билеты 12 – 15", "focus": "Остановка и стоянка, проезд перекрестков (равнозначные и неравнозначные)"},
            "2026-08-25": {"tickets": "Билеты 16 – 19", "focus": "Пешеходные переходы, движение через ж/д пути, автомагистрали"},
            "2026-08-26": {"tickets": "Билеты 20 – 23", "focus": "Жилые зоны, приоритет маршрутных ТС, буксировка"},
            "2026-08-27": {"tickets": "Билеты 24 – 27", "focus": "Учебная езда, перевозка людей и грузов, неисправности ТС"},
            "2026-08-28": {"tickets": "Билеты 28 – 31", "focus": "Дорожные знаки и разметка (сложные ловушки)"},
            "2026-08-29": {"tickets": "Билеты 32 – 35", "focus": "Основы безопасности движения и первая помощь"},
            "2026-08-30": {"tickets": "Билеты 36 – 40", "focus": "Ответственность водителя + Марафон всех 40 билетов (симуляция экзамена)"}
        }

    def get_today_pdd_plan(self):
        today_str = date.today().strftime("%Y-%m-%d")
        plan = self.pdd_schedule.get(today_str, {
            "tickets": "3–4 билета на выбор",
            "focus": "Работа над ошибками в приложении ПДД"
        })
        return plan
