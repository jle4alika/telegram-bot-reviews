import telebot
from config import BOT_TOKEN, DB_HOST, DB_NAME

bot = telebot.TeleBot(BOT_TOKEN)

# Глобальные переменные
user_tasks = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start"""
    welcome_text = (
        f"Добро пожаловать, {message.from_user.first_name}!\n"
        "Я бот для заработка на отзывах.\n"
        "Используйте /help для получения помощи."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['help'])
def show_help(message):
    """Показ справки"""
    help_text = (
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/tasks - показать доступные задания\n"
        "/balance - проверить баланс\n"
        "/withdraw - вывести средства\n"
        "/help - показать справку"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['tasks'])
def show_tasks(message):
    """Показ доступных заданий"""
    tasks_text = "Доступные задания:\n\n"
    tasks_text += "1. Оставить отзыв на Яндекс.Картах - 50₽\n"
    tasks_text += "2. Оставить отзыв на Google Maps - 60₽\n\n"
    tasks_text += "Используйте /take <номер> для взятия задания"
    bot.reply_to(message, tasks_text)

@bot.message_handler(commands=['balance'])
def check_balance(message):
    """Проверка баланса пользователя"""
    user_id = message.from_user.id
    # Здесь будет запрос к базе данных
    balance = 0  # Заглушка
    bot.reply_to(message, f"Ваш баланс: {balance}₽")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
