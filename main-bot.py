from tracemalloc import Filter
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters
import os 
import logging
import re
import requests
import json

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)


logger = logging.getLogger(__name__)

TOKEN = "5572878452:AAHjXEfZKkX6ivbMCnKomkKw4mQBP3tljeI"


def menus(update: Update, context: CallbackContext):
    
    update.callback_query.answer()

    choose = update.callback_query.data

    if choose == "register":
        # update.callback_query.edit_message_reply_markup(
        #     reply_markup = InlineKeyboardMarkup([])
        # )
        return register(update, context)

    if choose == "events":
        return events(update, context)

def choices(update: Update, context: CallbackContext):
    verbose_text = ""
    print(context.user_data)
    if context.user_data == {}:
        reply_buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("register", callback_data="register")],
            [InlineKeyboardButton("events", callback_data="events")],
        ])
        verbose_text = "Salam Istifadeci. Ne etmek isterdiniz?"

    else:
        verbose_text = f"Salam {update.effective_user.first_name}. Heleki edecek bir sey yoxdur."

        reply_buttons = InlineKeyboardMarkup([])
    update.message.reply_text(
        verbose_text,
        reply_markup=reply_buttons
    )
    return menus


INFO_REGEX = r"^Qeydiyyat (.+), (.+), (.+)$"
def register(update: Update, context: CallbackContext) -> int:
    print(INFO_REGEX,"sa")
    # print(info = re.match(INFO_REGEX, update.message.text).groups())
    reply_list = ["Xahis edilir melumatlarinizi asagidaki formada, vergul ve bosluqlara diqqet ederek qeyd edesiniz: \nQeydiyyat Yas, Ad, Soyad \nMeselen: \nQeydiyyat 22, Mehemmed, Mustafazade"]
    if context.user_data:
        reply_list.extend([f"Yasiniz: {context.user_data[0]}, Adiniz: {context.user_data[1]} ve soyadiniz {context.user_data[2]} Olaraq qeyd edildi"])

    update.callback_query.message.reply_text('\n'.join(reply_list))


def events(update: Update, context: CallbackContext):
    url = "http://localhost:8000/event/api/list-event"
    response = requests.get(url)
    # event_list = {}
    # for count, event in enumerate(response.json()):
    #     event_list["*Eventin Adi:*"] = event['name']
    #     event_list["Eventin'in Kecirileceyi Yerin Adresi:"] =  event['event_place_address']
    # print(json.dumps(response))
    event_list = []
    for count, event in enumerate(response.json()):
        event_list.append(f"*Eventin Adi* 👉🏻: {event['name']}")
        event_list.append(" ")
        event_list.append(f"*Eventin'in Kecirileceyi Yerin Adi* 👉🏻: {event['event_place_name']}")
        event_list.append(f"*Eventin'in Kecirileceyi Yerin Adresi* 👉🏻: {event['event_place_address']}")
        # print(json.dumps(response.json())[0]["is_entering_price"])
        # print(a)
        print(event["entering_price"])
        if event["is_entering_price"] == True:
            event_list.append(f"*Eventin'in Giris Qiymeti* 👉🏻: {event['entering_price']} ")
            print("True")
        else:
            event_list.append("*Eventin'in Giris Qiymeti* 👉🏻: Pulsuzdur")
            print("False")
        event_list.append("----------------------------------------------------------")
        event_list.append(" ")
        

        



    # for i in event_list:
    #     print(i)
    update.callback_query.message.reply_text("*👇🏻Butun Eventler👇🏻: *",parse_mode=ParseMode.MARKDOWN)
    update.callback_query.message.reply_text('\n'.join(event_list),parse_mode=ParseMode.MARKDOWN)
    # print(response.json())


print(INFO_REGEX)
def receive_info(update: Update, context: CallbackContext):
    is_acceptable = False
    reply_text = ""
    info = re.match(INFO_REGEX, update.message.text).groups()

    print(is_acceptable,"a")

    if context.user_data == {}:
        try:
            age = int(info[0])
            first_name = str(info[1])
            last_name = str(info[2])
            context.user_data['user_data'] = (first_name, last_name, age)

            # Quote the information in the reply
            reply_text = f'Yasiniz: {info[0]}, Adiniz: {info[1]} ve soyadiniz {info[2]} Olaraq qeyd edildi'
            is_acceptable = True

        except ValueError:
            reply_text = "Xahis Edilir Melumatlari Duzgun Bir formada, vergul ve bosluqlara diqqed ederek, Asagidaki Formada Qeyd Edin: \nQeydiyyat Yas, Ad, Soyad \nMeselen: \nQeydiyyat 22, Mehemmed, Mustafazade"
        
        if is_acceptable == False:
            reply_text = "Xahis Edilir Melumatlari Duzgun Bir formada, vergul ve bosluqlara diqqed ederek, Asagidaki Formada Qeyd Edin: \nQeydiyyat Yas, Ad, Soyad \nMeselen: \nQeydiyyat 22, Mehemmed, Mustafazade"
        update.message.reply_text(
            reply_text
        )
        print(is_acceptable,"b")
        

print(INFO_REGEX)


# def button(update: Update, context: CallbackContext):
#     update.callback_query.answer()
#     update.callback_query.message.edit_reply_markup(
#         reply_markup=InlineKeyboardMarkup([])
#     )
#     update.callback_query


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("start", choices))
updater.dispatcher.add_handler(CommandHandler("register", register))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(INFO_REGEX), receive_info))
updater.dispatcher.add_handler(CallbackQueryHandler(menus))
updater.start_polling()
updater.idle()