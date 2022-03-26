import telebot
from telebot import types
token = '5208733321:AAGqzpcwMQs3oM31FmE2Ns9HeCq9d3ExA0E'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,text="Привет, {0.first_name}!". format(message.from_user))
    
    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1= types.KeyboardButton("Игрок идет налево")
    item2= types.KeyboardButton("Игрок идет направо")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Выберите куда идти', reply_markup=markup)
    
 
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if(message.text=="Игрок идет налево"):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3= types.KeyboardButton("Взять тяжелое оружие")
        item4= types.KeyboardButton("Взять легкое оружие")
        item5= types.KeyboardButton("Взять холодное оружие")
        markup.add(item3, item4, item5)
        bot.send_message(message.chat.id,"Можете снарядиться", reply_markup=markup)
    elif(message.text=="Игрок идет направо"):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6= types.KeyboardButton("автомобиль")
        item7= types.KeyboardButton("танк") 
        markup.add(item6, item7)
        bot.send_message(message.chat.id,"Можете выбрать транспорт", reply_markup=markup)
        
        

        



if __name__ == '__main__':
     bot.infinity_polling()
        
