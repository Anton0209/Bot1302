import telebot
token = '5208733321:AAGqzpcwMQs3oM31FmE2Ns9HeCq9d3ExA0E'
bot = telebot.TeleBot(token)

@bot.massage_handler(content_types=["texst"])
def repeat_all_massages(massage):
    bot.send_massage(massage.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
