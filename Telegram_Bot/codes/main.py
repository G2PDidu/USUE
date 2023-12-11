import telebot
from telebot import types
import webbrowser
import random
import requests

bot = telebot.TeleBot('6780154862:AAHNV0CQPozJWkhwW_HgCAn0Mu0_rRj7pJ4')
API_KEY = '47aba5e36f718e9a099ccba318daf875'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['weather'])
def handle_weather(message):
    location = message.text.split(' ', 1)

    if len(location) == 1:
        bot.reply_to(message, 'Пожалуйста, укажите местоположение.')
        return

    location = location[1]

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = round(weather_data['main']['temp'] - 273.15,
                            1)
        description = weather_data['weather'][0]['description']

        weather_message = f'Погода в {location} {temperature}°C.'
        bot.reply_to(message, weather_message)
    else:
        bot.reply_to(message, 'Не удается получить данные о погоде.')

@bot.message_handler(commands=['coin'])
def coin_flip(message):
    result = random.randint(0, 1)
    if result == 0:
        flip_result = "Орел"
    else:
        flip_result = "Решка"
    bot.reply_to(message, f"Выпало: {flip_result}")

@bot.message_handler(commands=['github'])
def site(message):
    webbrowser.open('https://github.com/G2PDidu/usue')

@bot.message_handler(commands=['usue'])
def site(message):
    webbrowser.open('https://www.usue.ru/raspisanie/#')

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Поздороваться"):
        bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user))
    elif(message.text == "Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn10 = types.KeyboardButton("Как меня зовут?")
        btn20 = types.KeyboardButton("Что я могу?")
        markup.row(btn10, btn20)
        back11 = types.KeyboardButton("Вернуться в главное меню")
        markup.row(back11)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Что я могу?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("Использовать команды")
        markup.row(btn11)
        back22 = types.KeyboardButton("Вернуться в главное меню")
        markup.row(back22)
        bot.send_message(message.chat.id, text="⬇️⬇️⬇️", reply_markup=markup)

    elif (message.text == "Использовать команды"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("/github")
        btn22 = types.KeyboardButton("/usue")
        btn33 = types.KeyboardButton("/coin")
        btn44 = types.KeyboardButton("/weather")
        markup.row(btn11, btn22, btn33, btn44)
        back22 = types.KeyboardButton("Что я могу?")
        markup.row(back22)
        bot.send_message(message.chat.id, text="Команды которые могу использовать", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "Bot for usue (BFU)")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Поздороваться")
        btn2 = types.KeyboardButton("Задать вопрос")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

bot.polling(non_stop=True)