import os

class FinanceTracker:
    def __init__(self):
        self.target_total = 250000
        self.target_credit = 100000
        self.target_travel = 150000

    def get_finance_summary(self):
        return {
            "target_total": self.target_total,
            "target_credit": self.target_credit,
            "target_travel": self.target_travel,
            "credit_title": "Закрытие кредита (снятие стресса)",
            "travel_title": "Совместное путешествие с девушкой (Коренное Зачем)",
            "reminder": "Не забудь зафиксировать сегодняшние доходы и расходы в WebPlanner!"
        }
