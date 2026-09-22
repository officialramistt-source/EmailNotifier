import os
import sys
from datetime import datetime, timezone, timedelta

# Fix UTF-8 output encoding for Windows/Linux terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from notifier_core import NotifierCore

def main():
    notifier = NotifierCore()

    # Если запуск в облаке (GitHub Actions / Render / VPS), переопределяем конфиг из переменных окружения
    env_sender = os.environ.get("SENDER_EMAIL")
    env_recipient = os.environ.get("RECIPIENT_EMAIL")
    env_password = os.environ.get("APP_PASSWORD")

    if env_sender and env_recipient and env_password:
        notifier.config["email"]["sender_email"] = env_sender
        notifier.config["email"]["recipient_email"] = env_recipient
        notifier.config["email"]["app_password"] = env_password

    # Определяем слот по аргументу командной строки или по текущему времени МСК (UTC+3)
    if len(sys.argv) > 1:
        slot = sys.argv[1].lower()
    else:
        # Автоматическое определение слота по московскому времени (UTC+3)
        msk_tz = timezone(timedelta(hours=3))
        now_msk = datetime.now(msk_tz)
        hour = now_msk.hour
        minute = now_msk.minute
        weekday = now_msk.weekday() # 6 = Sunday

        if hour < 11:
            slot = "kickoff"
        elif hour < 15:
            slot = "pulse"
        elif hour < 18:
            slot = "networking"
        elif hour < 20:
            if weekday == 6 and hour >= 19:
                slot = "weekly"
            else:
                slot = "energy"
        else:
            slot = "evening"

    print(f"[CloudRunner] Запуск слота: '{slot}' (Время МСК: {datetime.now(timezone(timedelta(hours=3))).strftime('%Y-%m-%d %H:%M:%S')})")

    if slot == "kickoff":
        subject, html = notifier.generate_morning_kickoff()
    elif slot == "pulse":
        subject, html = notifier.generate_midday_pulse()
    elif slot == "networking":
        subject, html = notifier.generate_networking_ping()
    elif slot == "energy":
        subject, html = notifier.generate_energy_finance()
    elif slot == "evening":
        subject, html = notifier.generate_evening_recap()
    elif slot == "weekly":
        subject, html = notifier.generate_weekly_shift_review()
    elif slot == "test":
        subject, html = notifier.generate_custom_reminder(
            "ОБЛАЧНЫЙ ТЕСТ 24/7",
            "Уведомление успешно отправлено из облака! Система работает автономно даже при выключенном компьютере."
        )
    else:
        print(f"[CloudRunner] Неизвестный слот: {slot}")
        return

    success, status = notifier.send_email(subject, html)
    print(f"[CloudRunner] Результат отправки: {status}")
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
