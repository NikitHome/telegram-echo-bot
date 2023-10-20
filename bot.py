import telebot


# create bot
bot = telebot.TeleBot('#')


# handler command /start
@bot.message_handler(commands = ["start"])
def start(m, res = False):
	bot.send_message(m.chat.id, 'Привет, напиши мне что-нибудь :)')


# user message handler
@bot.message_handler(content_types = ["text"])
def handler_text(message):
	bot.send_message(message.chat.id, message.text)


# start bot
bot.polling(non_stop = True, interval = 0)
