import telebot

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

# print(type(TOKEN))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/help")

bot.infinity_polling()
