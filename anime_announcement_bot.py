from Tele import *
import re
# import Tele

bot_tocken = '5161532691:AAGUPXJHaU7llBHUsdQa6QYh4XiF5NlG1xM'
my_tg = '187921540'
announcement_chanel = '-1001511816090'
main_chanel = '-1001765295395'
dubbers = ['akainu19', 'Jakob', 'Taneria']
subbers = ['KingGalant', 'Lawwy', 'Aloe']
episod_counter = ['']

announcement_title = '🪨 ❗️ Додано 13, 14-ий епізоди «Доктора Стоуна»'
sound_by = dubbers[1]
subbed_by = subbers[1]

# announcement_post = str(announcement_title) + ' \nОзвучили: ' + sound_by + ' \nПереклали: ' + subbed_by
announcement_post = 'subbed_by'

# print(announcement_post)

# sendMessage(chat_id = '-1001765295395' , text = 'announcement_post')

# Tele.account(bot_tocken)
# Tele.sendMessage(chat_id=main_chanel, text='hello')


def print_message():
    sendMessage(chat_id=main_chanel, text='Testing function')


@bot()
def get_info(update):
    print(update)
    # print('Here chat id: ' + str(update.chat.id))
    # sendMessage(chat_id=main_chanel , text=str(update.text))
    # print('Working')
    print_message()    
    episod_counter[0] = re.findall(r'\b\d+\b', update.caption)
    sendMessage(chat_id=main_chanel, text=episod_counter)
    sendVideo(chat_id=main_chanel, file=update.video.file_id, caption='Some name')

account(bot_tocken)
bot_run()