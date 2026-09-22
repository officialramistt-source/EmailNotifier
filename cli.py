import sys
import os
import argparse

# Fix UTF-8 output encoding for Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from notifier_core import NotifierCore

def main():
    parser = argparse.ArgumentParser(description="projectAnti 24/7 Email Notifier CLI")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Command: preview
    subparsers.add_parser("preview", help="Сгенерировать HTML-превью всех писем в папке проекта")

    # Command: test
    subparsers.add_parser("test", help="Отправить тестовое письмо на указанную в config.json почту")

    # Command: kickoff
    subparsers.add_parser("kickoff", help="[08:30] Отправить утренний запуск (фокус, вышмат, дедлайны)")

    # Command: pulse
    subparsers.add_parser("pulse", help="[13:00] Отправить дневной пульс (ПДД билеты, алгоритм дня)")

    # Command: networking
    subparsers.add_parser("networking", help="[16:30] Отправить радар нетворкинга и фразы для связи")

    # Command: energy
    subparsers.add_parser("energy", help="[19:00] Отправить напоминание спорт и финансы")

    # Command: evening
    subparsers.add_parser("evening", help="[21:30] Отправить вечерний отчет по привычкам")

    # Command: weekly
    subparsers.add_parser("weekly", help="[ВС 19:00] Отправить Воскресный Ритуал Сдвига")

    # Command: custom
    custom_parser = subparsers.add_parser("custom", help="Отправить произвольное напоминание")
    custom_parser.add_argument("title", type=str, help="Заголовок напоминания")
    custom_parser.add_argument("message", type=str, help="Текст напоминания")

    args = parser.parse_args()
    notifier = NotifierCore()

    if args.command == "preview":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 1. Kickoff
        s1, h1 = notifier.generate_morning_kickoff()
        f1 = os.path.join(base_dir, "preview_kickoff.html")
        with open(f1, "w", encoding="utf-8") as f: f.write(h1)
        print(f"[OK] 1. Утренний запуск сохранен в: {f1}")

        # 2. Pulse
        s2, h2 = notifier.generate_midday_pulse()
        f2 = os.path.join(base_dir, "preview_pulse.html")
        with open(f2, "w", encoding="utf-8") as f: f.write(h2)
        print(f"[OK] 2. Дневной пульс сохранен в: {f2}")

        # 3. Networking
        s3, h3 = notifier.generate_networking_ping()
        f3 = os.path.join(base_dir, "preview_networking.html")
        with open(f3, "w", encoding="utf-8") as f: f.write(h3)
        print(f"[OK] 3. Радар нетворкинга сохранен в: {f3}")

        # 4. Energy & Finance
        s4, h4 = notifier.generate_energy_finance()
        f4 = os.path.join(base_dir, "preview_energy.html")
        with open(f4, "w", encoding="utf-8") as f: f.write(h4)
        print(f"[OK] 4. Спорт и финансы сохранены в: {f4}")

        # 5. Evening
        s5, h5 = notifier.generate_evening_recap()
        f5 = os.path.join(base_dir, "preview_evening.html")
        with open(f5, "w", encoding="utf-8") as f: f.write(h5)
        print(f"[OK] 5. Вечерний отчет сохранен в: {f5}")

        # 6. Weekly
        s6, h6 = notifier.generate_weekly_shift_review()
        f6 = os.path.join(base_dir, "preview_weekly.html")
        with open(f6, "w", encoding="utf-8") as f: f.write(h6)
        print(f"[OK] 6. Воскресный ритуал сохранен в: {f6}")

        print("\n[SUCCESS] Все 6 расширенных превью успешно сгенерированы!")

    elif args.command == "test":
        subject = "🧪 Тестовое уведомление: Связь с projectAnti установлена!"
        title = "ТЕСТОВОЕ ПОДКЛЮЧЕНИЕ"
        msg = """
        Привет! Твоя автономная система напоминаний <strong>EmailNotifier</strong> успешно настроена и готова к работе 24/7.<br><br>
        Теперь ты будешь получать утренние запуски, дневные пульсы с ПДД и IT-алгоритмами, радары связей и вечерние рефлексии прямо на телефон.
        """
        s, html = notifier.generate_custom_reminder(title, msg)
        success, status = notifier.send_email(subject, html)
        print(f"Результат: {status}")

    elif args.command == "kickoff":
        subject, html = notifier.generate_morning_kickoff()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки утреннего запуска: {status}")

    elif args.command == "pulse":
        subject, html = notifier.generate_midday_pulse()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки дневного пульса (ПДД/IT): {status}")

    elif args.command == "networking":
        subject, html = notifier.generate_networking_ping()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки радара нетворкинга: {status}")

    elif args.command == "energy":
        subject, html = notifier.generate_energy_finance()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки спорта и финансов: {status}")

    elif args.command == "evening":
        subject, html = notifier.generate_evening_recap()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки вечернего отчета: {status}")

    elif args.command == "weekly":
        subject, html = notifier.generate_weekly_shift_review()
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки Воскресного Ритуала: {status}")

    elif args.command == "custom":
        subject, html = notifier.generate_custom_reminder(args.title, args.message)
        success, status = notifier.send_email(subject, html)
        print(f"Результат отправки кастомного напоминания: {status}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
