from telebot import types, TeleBot

# Create your handlers here.

def echo_handler(message: types.Message, bot: TeleBot):
    bot.send_message(message.chat.id, message.text)