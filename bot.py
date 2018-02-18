import config
import telebot
import random

bot = telebot.TeleBot(config.token)
messages = []

@bot.message_handler (content_types = ["text"])
def repeat_all_messages(message):
	messages.append(message)

	msg = random.choice([x for x in messages if x.chat.id == message.chat.id])
	bot.send_message(message.chat.id, msg.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)