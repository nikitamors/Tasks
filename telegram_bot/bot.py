from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

API_URL = "http://backend:8000/api/tasks/"


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот для управления задачами.")


def get_tasks(update: Update, context: CallbackContext) -> None:
    response = requests.get(API_URL)
    tasks = response.json()
    message = "\n".join([f"{task['title']} - {task['due_date']}" for task in tasks])
    update.message.reply_text(message)


def main():
    updater = Updater("7835063516:AAE2lNPU8USIp619Mx0NlUoysrq6BKYKRsk")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tasks", get_tasks))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
