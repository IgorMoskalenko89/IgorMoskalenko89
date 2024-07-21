import webbrowser
import telebot
#mylist = []
#itog = ''
from telebot import types
bot = telebot.TeleBot('############################################')
@bot.message_handler(content_types=['text'])



#@bot.message_handler(content_types=['text', 'document', 'audio'])
#def main(message):
#    bot.send_message(message.chat.id, 'Привет')
 #   if message.text == "Привет":
#        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напиши привет")
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

###############################################################################################################
#def menu(message):
#    markup = types.InlineKeyboardMarkup()
#    markup.add(types.InlineKeyboardButton('Открыть чат техподдержки', url = 'https://t.me/###########'))
#    markup.add(types.InlineKeyboardButton('Заполнить форму заявки', callback_data='anketa'))
#   bot.reply_to(message, 'Добрый день! Вы попали в главное меню бота. Выберите действие:', reply_markup=markup)


#@bot.callback_query_handler(func=lambda call: True)
#def callback_message(callback):
 #   if callback.data == 'anketa':
#bot.send_message(callback.from_user, "начало регистрации")
###################################################################################################################
@bot.message_handler(content_types=['text'])

def started_fire(message):
    bot.send_message(message.from_user.id, 'Добрый день! \nДля получения ссылки на чат техподдержки введите цифру 1 \
                                               \nДля заполнения формы регистрации введите цифру 2  ')
    bot.register_next_step_handler(message, get_number)  # следующий шаг – функция get_name
def get_number(message):
    global number
    number = message.text
    if message.text == "1":
        url='https://t.me/worldychathelp'
        #webbrowser.open(url, new=0, autoraise=False)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Открыть чат техподдержки', url = 'https://t.me/###############'))
        bot.reply_to(message, 'Направляю ссылку на чат техподдержки', reply_markup=markup)

    if message.text == "2":
 #       bot.register_next_step_handler(message, get_start)
#def get_start(message):
        bot.send_message(message.from_user.id, "Введите своё имя и фамилию")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
def get_name(message):  # получаем имя и фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите свой номер телефона')
    bot.register_next_step_handler(message, get_phone)
def get_phone(message):
    global phone
    phone = message.text
    bot.send_message(message.from_user.id, 'Введите свой e-mail:')
    bot.register_next_step_handler(message, get_email)
def get_email(message):
    global email
    email = message.text
    bot.send_message(message.from_user.id, 'Введите цифру, соответствующую своему уровню английского: \
                                           \n1-Beginner; \n2-Elementary; \
                                            \n3-Pre-Intermediate; \n4-Intermediate; \
                                           \n5-Upper-Intermediate')
    bot.register_next_step_handler(message, get_level)
def get_level(message):
    global level
    global leveltext
    global itog
    global mylist
    mylist1 = ['111', '222', '333']
    level = message.text
    #itog = ';'.join(mylist)
    bot.send_message(message.from_user.id, 'Большое спасибо! Данные сохранены.')
   # bot.register_next_step_handler(message, send_path)
#def send_path(message):
    #bot.send_message(message.from_user.id, level)
    if level =="1":
        bot.send_message(message.from_user.id, 'Ссылка для работы: https://miro.com/app/board/#############################1')
        leveltext = 'Beginner'
    if level =="2":
        bot.send_message(message.from_user.id, 'Ссылка для работы: https://miro.com/app/board/#############################2')
        leveltext = 'Elementary'
    if level =="3":
        bot.send_message(message.from_user.id, 'Ссылка для работы: https://miro.com/app/board/#############################3')
        leveltext = 'Pre-Intermediate'
    if level =="4":
        bot.send_message(message.from_user.id, 'К сожалению, доска для Вашего уровня пока в разработке. Мы обязательно с Вами свяжемся')
        leveltext = 'Intermediate'
    if level =="5":
        bot.send_message(message.from_user.id, 'К сожалению, доска для Вашего уровня пока в разработке. Мы обязательно с Вами свяжемся')
        leveltext = 'Upper-Intermediate'
    mylist = name + '; ' + phone + '; ' + email + '; ' + leveltext + '.'
    bot.send_message(############, 'Внимание! поступил запрос от нового пользователя!')
    bot.send_message(############, mylist)
    # if callback.data == 'anketa':
    #def handle_message(message):
    #bot.send_message(message.from_user.id, text='Введите своё имя и фамилию')
    #bot.register_next_step_handler(message, process_text)
    #def process_text(message):
    #    global name
    #    name = message.text

   # def handle_message(message):
   #     bot.send_message(message.from_user.id, text='Введите свой номер телефона')
   #     bot.register_next_step_handler(message, process_text)
   # def process_text(message):
   #     global phone
    #    phone = message.text
     #bot.send_message(message.from_user.id, 'Введите свой e-mail:')
     #def get_mail(message):
     #    global mail
     #    mail = message.text
    #bot.send_message(message.from_user.id, 'Введите цифру, соответствующую своему уровню английского: \
     #                                   \n1-Beginner; \n2-Elementary; \
     #                                   \n3-Pre-Intermediate; \n4-Intermediate; \
      #                                  \n5-Upper-Intermediate')
    #.send_message(message.from_user.id, 'Большое спасибо! Данные сохранены.')
    #bot.send_message(message.from_user.id, 'Ссылка на доступ к рабочему столу:')

#@bot.message_handler(content_types=['text'])
#def main(message):
#    bot.send_message(message.chat.id, 'Введите своё имя и фамилию')
 #   global name
 #   name = message.text
#    bot.register_next_step_handler(message, get_name)


bot.polling(none_stop=True)