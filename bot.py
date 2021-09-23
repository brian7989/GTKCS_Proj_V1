import telebot
from helper import CheggHelper
import os

bot = telebot.TeleBot('1972159767:AAFv6s_5_Yi-ynC4Z94JTEiYdeZnWlLUbr4')
obj = CheggHelper()

# @bot.message_handler(commands=['ans'])
# def send_ans(message):
#     try:
#         ques_link = message.text.split(' ')[1]
#         print(ques_link)
#         stat, filex, captionx = obj.getQAns(ques_link)
#         if stat == True:
#             bot.send_document(message.chat.id, open(filex, 'rb'), caption=captionx, reply_to_message_id=message.message_id)
#             os.remove(filex)
#         else:
#             bot.reply_to(message, captionx)
#     except Exception as e:
#         bot.reply_to(message, str(e))
#
# bot.polling()

quesLink = "https://www.chegg.com/homework-help/questions-and-answers/matlab-arrays-1-create-2x3-array-m1-whose-first-row-contains-values-4-7-2-whose-second-row-q61395369"
stat, filex, captionx = obj.getQAns(quesLink)
print(stat, filex, captionx)