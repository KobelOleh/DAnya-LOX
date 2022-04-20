import telebot

bot = telebot.TeleBot("5036250739:AAHs5zVnWKxXHDUYi2Ii2dCisMx7Erfk2Qg")

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Саламалейкум', parse_mode='html')


bot.polling(none_stop=True)

