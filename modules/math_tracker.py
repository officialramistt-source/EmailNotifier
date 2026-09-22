import os
from datetime import datetime, date

class MathTracker:
    def __init__(self, workspace_root=None):
        if workspace_root is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.workspace_root = os.path.dirname(base_dir)
        else:
            self.workspace_root = workspace_root

        self.schedule_by_date = {
            "2026-08-21": {
                "day_num": 1,
                "topic": "Телескопические ряды (Шаг k=1 и k=3)",
                "task": "Найти сумму ряда: sum(n=0 to inf) 36/(n^2 + 7n + 10)",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "n^2+7n+10 = (n+2)(n+5). Разложи методом прикрытия: A/(n+2) + B/(n+5). Старт с n=0!"
            },
            "2026-08-22": {
                "day_num": 2,
                "topic": "Телескопические ряды со смещением шага k=2",
                "task": "Найти сумму ряда: sum(n=1 to inf) 24/(n^2 + 4n + 3)",
                "variant": "Вариант 3 (май 2026)",
                "formula_tip": "(n+1)(n+3). Не сокращаются первые 2 дроби: 1/2 и 1/3!"
            },
            "2026-08-23": {
                "day_num": 3,
                "topic": "Знакопостоянные ряды: Признаки сравнения и эталоны Дирихле",
                "task": "Исследовать на сходимость: sum(n=1 to inf) (3 + sin n) / (n^3 - n)^(1/3)",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "3 + sin n >= 2 (константа). Знаменатель ~ n. Сравниваем с расходящимся рядом sum 1/n."
            },
            "2026-08-24": {
                "day_num": 4,
                "topic": "Знакопостоянные ряды с логарифмами",
                "task": "Исследовать на сходимость: sum(n=2 to inf) ln(sqrt(n^2+3n)) / sqrt(n^2 - n)",
                "variant": "Вариант 3 (май 2026)",
                "formula_tip": "ln(sqrt(n^2+3n)) = 1/2 * ln(n^2+3n) > 1. Знаменатель ~ n. Ряд расходится."
            },
            "2026-08-25": {
                "day_num": 5,
                "topic": "Признак Даламбера (Факториалы)",
                "task": "Исследовать на сходимость: sum(n=1 to inf) 4^n * n! / (3n)!",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "l = lim (a_(n+1) / a_n). (3n+3)! = (3n)!(3n+1)(3n+2)(3n+3). l = 0 < 1 -> Сходится!"
            },
            "2026-08-26": {
                "day_num": 6,
                "topic": "Радикальный признак Коши (n-е степени)",
                "task": "Исследовать: sum n^4 * (2n / (3n+5))^n и sum (n / (10n+5))^(n^2)",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "l = lim (a_n)^(1/n). lim (2n/(3n+5)) = 2/3 < 1 -> Сходится!"
            },
            "2026-08-27": {
                "day_num": 7,
                "topic": "Неопределенные интегралы: подведение под дифференциал",
                "task": "Вычислить: integral (x - arctg x)^4 / (1 + x^2) dx",
                "variant": "Вариант 28 (май 2026)",
                "formula_tip": "dx / (1+x^2) = d(arctg x). Замена u = x - arctg x."
            },
            "2026-08-28": {
                "day_num": 8,
                "topic": "Интегрирование тригонометрии и дробей",
                "task": "Вычислить: integral dx / (sin x * (1 + cos x))",
                "variant": "Вариант 28 (май 2026)",
                "formula_tip": "Умножь на sin x / sin x -> d(cos x) / ((1 - cos^2 x)(1 + cos x))."
            },
            "2026-08-29": {
                "day_num": 9,
                "topic": "Двойные интегралы: построение области D и расстановка пределов",
                "task": "Построить область D: x = 1, y = x^(1/3), y = -x^2",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "x in [0, 1]. Нижняя граница y = -x^2, верхняя y = x^(1/3)."
            },
            "2026-08-30": {
                "day_num": 10,
                "topic": "Вычисление двойного интеграла от многочленов",
                "task": "Вычислить: iintegral_D (18x^2y^2 + 32x^3y^3) dx dy",
                "variant": "Вариант 11 (май 2026)",
                "formula_tip": "Сначала интегрируем по y (x константа), затем по x от 0 до 1."
            }
        }

    def get_today_math_plan(self):
        today_str = date.today().strftime("%Y-%m-%d")
        return self.schedule_by_date.get(today_str, {
            "day_num": "Спринт",
            "topic": "Повторение задач из билетов",
            "task": "Решение билета целиком (4 задачи)",
            "variant": "Вариант 11 / 3 / 2",
            "formula_tip": "Соблюдай 4-шаговый алгоритм: корни -> разложение -> частичная сумма -> предел."
        })

    def get_deadlines_countdown(self):
        today = date.today()
        deadlines = [
            {"title": "🚀 Заявка в Avito Tech (Backend Python)", "target_date": date(2026, 8, 30)},
            {"title": "🚗 Автошкола (40 билетов ПДД)", "target_date": date(2026, 8, 31)},
            {"title": "🎓 Сдача зачета по Вышмату (Допка)", "target_date": date(2026, 9, 10)}
        ]

        results = []
        for d in deadlines:
            delta = (d["target_date"] - today).days
            status_emoji = "⏳"
            if delta <= 3:
                status_emoji = "🔥"
            elif delta <= 7:
                status_emoji = "⚠️"

            results.append({
                "title": d["title"],
                "target_date_str": d["target_date"].strftime("%d.%m.%Y"),
                "days_left": delta,
                "emoji": status_emoji
            })
        return results
