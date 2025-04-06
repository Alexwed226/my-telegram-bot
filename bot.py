import telebot

bot = telebot.TeleBot("ВАШ_ТОКЕН_БОТА")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Отправь /sell, чтобы продать идею.")

@bot.message_handler(commands=['sell'])
def sell(message):
    bot.reply_to(message, "Опиши свою идею:")
    bot.register_next_step_handler(message, save_idea)

def save_idea(message):
    with open("ideas.txt", "a") as file:
        file.write(f"{message.from_user.username}: {message.text}\n")
    bot.reply_to(message, "✅ Идея сохранена!")

bot.polling()
