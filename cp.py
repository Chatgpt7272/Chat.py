import requests
from telebot import types
import telebot

token = input('Token: ')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("programmer", url="https://t.me/z3_2q")
    markup.add(btn)

    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Welcome {user_name} to the AI bot. Send your question for an answer.", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_handler(message):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Get help information\n"
        "Just send a message and I'll do my best to answer it!"
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    headers = {
        'authority': 'api.binjie.fun',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://chat18.aichatos8.com',
        'referer': 'https://chat18.aichatos8.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'prompt': user_input,
        'network': True,
        'system': '',
        'withoutContext': False,
        'stream': False,
    }

    try:
        response = requests.post('https://api.binjie.fun/api/generateStream', headers=headers, json=json_data)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            bot.send_message(message.chat.id, response.text)
        else:
            bot.send_message(message.chat.id, "Failed to get a valid response from the AI.")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred: " + str(e))

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, f"You said: {message.text}")

bot.infinity_polling()
