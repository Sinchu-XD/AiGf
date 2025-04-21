from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from pyrogram import Client

IST = timezone("Asia/Kolkata")

def schedule_daily_messages(app: Client, user_ids: list[int]):
    scheduler = BackgroundScheduler(timezone=IST)

    def send_gm():
        for uid in user_ids:
            app.send_message(uid, "🌞 Good Morning baby! Hope you slept well 😘")

    def send_gn():
        for uid in user_ids:
            app.send_message(uid, "🌙 Good Night sweetheart! Dream of us 💖")

    scheduler.add_job(send_gm, "cron", hour=8, minute=0)
    scheduler.add_job(send_gn, "cron", hour=22, minute=0)

    scheduler.start()
  
