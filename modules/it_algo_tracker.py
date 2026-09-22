import os
from datetime import datetime, date

class ItAlgoTracker:
    def __init__(self, workspace_root=None):
        if workspace_root is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.workspace_root = os.path.dirname(base_dir)
        else:
            self.workspace_root = workspace_root

        # Ежедневные алгоритмические паттерны для Avito Tech (Backend Python / LeetCode)
        self.algo_tips = {
            "2026-08-21": {
                "topic": "Python Hash Map & Подсчет элементов",
                "pattern": "collections.Counter и collections.defaultdict",
                "snippet": "from collections import Counter\ncounts = Counter(nums)\n# O(N) время, O(N) память для поиска дубликатов и частот",
                "task_idea": "LeetCode #1: Two Sum (через словарь complement = target - num)"
            },
            "2026-08-22": {
                "topic": "Два указателя (Two Pointers)",
                "pattern": "Схождение слева и справа в отсортированном массиве",
                "snippet": "left, right = 0, len(arr) - 1\nwhile left < right:\n    s = arr[left] + arr[right]\n    if s == target: return [left, right]\n    elif s < target: left += 1\n    else: right -= 1",
                "task_idea": "LeetCode #167: Two Sum II (Input array is sorted)"
            },
            "2026-08-23": {
                "topic": "Скользящее окно (Sliding Window)",
                "pattern": "Поиск подстроки / подотрезка максимальной/минимальной длины",
                "snippet": "left = 0\nfor right in range(len(s)):\n    # расширяем окно\n    while condition_violated:\n        # сжимаем окно слева: left += 1",
                "task_idea": "LeetCode #3: Longest Substring Without Repeating Characters"
            },
            "2026-08-24": {
                "topic": "Стек и проверка скобочных последовательностей",
                "pattern": "Использование list в Python как LIFO стек (append/pop)",
                "snippet": "stack = []\nmapping = {')': '(', '}': '{', ']': '['}\nfor ch in s:\n    if ch in mapping:\n        if not stack or stack.pop() != mapping[ch]: return False\n    else: stack.append(ch)",
                "task_idea": "LeetCode #20: Valid Parentheses"
            },
            "2026-08-25": {
                "topic": "Основы SQL: Быстрые агрегации и JOIN",
                "pattern": "INNER vs LEFT JOIN + GROUP BY + HAVING",
                "snippet": "SELECT u.id, COUNT(o.id) as orders_count\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id\nGROUP BY u.id\nHAVING COUNT(o.id) > 5;",
                "task_idea": "Повтори разницу между WHERE (фильтр до агрегации) и HAVING (после)"
            }
        }

    def get_today_algo_tip(self):
        today_str = date.today().strftime("%Y-%m-%d")
        tip = self.algo_tips.get(today_str, {
            "topic": "Алгоритмический паттерн дня",
            "pattern": "Разбор структур данных (Массивы, Хэш-таблицы, Деревья)",
            "snippet": "# 1 задача в день держит мозг в тонусе!",
            "task_idea": "LeetCode Easy/Medium — 30 минут практики"
        })
        return tip
