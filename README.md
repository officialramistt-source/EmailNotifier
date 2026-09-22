# 📧 EmailNotifier

> **Serverless Cloud Dispatcher & Daily Focus Digest Engine**  
> *Developed by Ramis Khayrutdinov ([@officialramistt-source](https://github.com/officialramistt-source))*

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![SMTP](https://img.shields.io/badge/Protocol-Secure%20SMTP%20SSL-EA4335?style=for-the-badge)](https://github.com/officialramistt-source/EmailNotifier)
[![Cost](https://img.shields.io/badge/Cost-Zero%20Serverless-00FF88?style=for-the-badge)](https://github.com/officialramistt-source/EmailNotifier)

---

## 🎯 Overview

**EmailNotifier** is an automated zero-maintenance cloud notifier that keeps high-performing engineers on track with their daily goals, study sessions, sports routines, and career deadlines. Running on automated GitHub Actions cron schedules, it executes 4 times a day without requiring an active VPS server.

---

## ⏰ Cron Schedule

* 🌅 **08:30 MSK:** Morning Kickoff (Primary daily goals, focus items)
* ☕ **13:00 MSK:** Midday Pulse (Traffic laws / Higher math checkpoint)
* 👥 **16:30 MSK:** Networking & Outreach Radar
* 🏋️ **19:00 MSK:** Sports, Physical Recovery & Financial Check

---

## 🚀 Setup

1. Add your credentials in **Settings -> Secrets and variables -> Actions**:
   * `SENDER_EMAIL` (e.g. Yandex Mail)
   * `RECIPIENT_EMAIL` (`officialramistt@gmail.com`)
   * `APP_PASSWORD` (App password for mail)
2. Workflow runs automatically according to `.github/workflows/daily_schedule.yml`.

---

## 👤 Author
* **Ramis Khayrutdinov**
* GitHub: [@officialramistt-source](https://github.com/officialramistt-source)
* Telegram: [@gel_yee](https://t.me/gel_yee)
* Email: officialramistt@gmail.com
