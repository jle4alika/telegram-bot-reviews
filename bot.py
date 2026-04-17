import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Приветствие пользователя"""
    bot.reply_to(message, "Добро пожаловать!")

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.reply_to(message, "Справка")

@bot.message_handler(commands=['tasks'])
def show_tasks(message):
    bot.reply_to(message, "Задания")

if __name__ == "__main__":
    bot.polling()
