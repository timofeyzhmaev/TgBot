import os
import telebot
import tempfile
from PIL import ImageGrab
from telebot import types
import subprocess
import pyautogui


API_TOKEN = '6339019598:AAE4pGXvXZnWz9as29xd5VMidl8Omp7ga-Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=[''])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот")
    markup.add("Открыть...")
    markup.add("Перемещение мыши")
    markup.add("Командная строка")
    bot.send_message(message.chat.id, '👋', reply_markup=markup)

@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("shutdown -s -t 0")

@bot.message_handler(regexp='Перемещение мыши')
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    RCM = types.InlineKeyboardButton("ЛКМ")
    up = types.InlineKeyboardButton("🔼")
    LCM = types.InlineKeyboardButton("ПКМ")
    left = types.InlineKeyboardButton("◀️")
    down = types.InlineKeyboardButton("🔽")
    righr = types.InlineKeyboardButton("▶️")
    scup = types.InlineKeyboardButton("⬆️")
    scdown = types.InlineKeyboardButton("⬇️")
    back = types.InlineKeyboardButton("Вернуться в главное меню")
    markup.add(RCM, up, LCM)
    markup.add(left, down, righr)
    markup.add(scup, scdown)
    markup.add(back)

    bot.send_message(message.chat.id, 'Стрелочка перемещает курсор на 50 пикселей в ту сторону, куда  показывает, ПКМ - правая кнопка мыши, ЛКМ - левая кнопка мыши. Длинные стрелочки отвечают за колесико мыши. После каждого нажатия вым будет отправлен скриншот', reply_markup=markup)

    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))
# Ниже управление мышкой
# region
@bot.message_handler(regexp='ЛКМ')
def echo_message(message):
    pyautogui.click()

@bot.message_handler(regexp='ПКМ')
def echo_message(message):
    pyautogui.click(button='right')


@bot.message_handler(regexp='⬆️')
def echo_message(message):
    pyautogui.scroll(1000)


@bot.message_handler(regexp='⬇️')
def echo_message(message):
    pyautogui.scroll(-1000)


@bot.message_handler(regexp='🔼')
def echo_message(message):
    x1, y1 = pyautogui.position()
    x = int(str(x1).rjust(4))
    y = int(str(y1).rjust(4))
    pyautogui.moveTo(x, y - 50)

@bot.message_handler(regexp='🔽')
def echo_message(message):
    x1, y1 = pyautogui.position()
    x = int(str(x1).rjust(4))
    y = int(str(y1).rjust(4))
    pyautogui.moveTo(x, y + 50)

@bot.message_handler(regexp='◀️')
def echo_message(message):
    x1, y1 = pyautogui.position()
    x = int(str(x1).rjust(4))
    y = int(str(y1).rjust(4))
    pyautogui.moveTo(x - 50, y)

@bot.message_handler(regexp='▶️')
def echo_message(message):
    x1, y1 = pyautogui.position()
    x = int(str(x1).rjust(4))
    y = int(str(y1).rjust(4))
    pyautogui.moveTo(x + 50, y)

# endregion

@bot.message_handler(regexp='Командная строка')
def echo_message(message):
    bot.send_message(message.chat.id, 'Введите команду')
    @bot.message_handler()
    def echo_message(message):
        subprocess.run(message.text, shell=True)
        bot.send_message(message.chat.id, 'Исполнил')

@bot.message_handler(regexp='получить скриншот')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))

@bot.message_handler(regexp='Открыть...')
def echo_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("YouTube")
    btn2 = types.KeyboardButton("PyCharm")
    btn3 = types.KeyboardButton("Яндекс")
    btn4 = types.KeyboardButton("Блокнот")
    btn5 = types.KeyboardButton("Калькулятор")
    btn6 = types.KeyboardButton("О разработчике")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    markup.add(back)
    bot.send_message(message.chat.id, text="Выберите приложение которое хотите открыть:", reply_markup=markup)

@bot.message_handler(regexp='О разработчике')
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Перейти на его страницу")
    markup.add("Вернуться в главное меню")
    bot.send_message(message.chat.id, 'Мой разработчик - Жмаев Тимофей, он не только хороший программист, но и компьютерный мастер, нажав на кнопку "Перейти на его страницу" вы увидите его профиль на Авито', reply_markup=markup)

@bot.message_handler(regexp='Вернуться в главное меню')
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот")
    markup.add("Открыть...")
    markup.add("Перемещение мыши")
    markup.add("Командная строка")
    bot.send_message(message.chat.id,'Вы вернулись в главное меню', reply_markup=markup)

@bot.message_handler(regexp='Перейти на его страницу')
def send_welcome(message):
    bot.send_message(message.chat.id,'<i><b>https://www.avito.ru/votkinsk/predlozheniya_uslug/sborka_chistka_kompyutera_kompyuternyy_master_2914250987</b></i>', parse_mode='html')

# Ниже открытие и закрытие приложений
# region
@bot.message_handler(regexp='YouTube')
def echo_message(message):
    browser_path = r"C:\Users\timzh\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    url = "https://www.youtube.com/feed/subscriptions"
    subprocess.Popen([browser_path, url])
    bot.send_message(message.chat.id, 'Открыл')

@bot.message_handler(regexp='Pycharm')
def echo_message(message):
    Genshin = r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.1\bin\pycharm64.exe"
    subprocess.Popen([Genshin])
    bot.send_message(message.chat.id, 'Запустил')

@bot.message_handler(regexp='Яндекс')
def echo_message(message):
    Yandex = r"C:\Users\timzh\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    subprocess.Popen([Yandex])
    bot.send_message(message.chat.id, 'Открыл')

@bot.message_handler(regexp='Блокнот')
def echo_message(message):
    notepad = r"notepad.exe"
    subprocess.Popen([notepad])
    bot.send_message(message.chat.id, 'Запустил')

@bot.message_handler(regexp='Калькулятор')
def echo_message(message):
    calc = r"calc.exe"
    subprocess.Popen([calc])
    bot.send_message(message.chat.id, 'Открыл')

@bot.message_handler(regexp='Закрой')
def echo_message(message):
    pyautogui.hotkey('alt', 'f4')
    bot.send_message(message.chat.id, 'Закрыл активное приложение')
# endregion

bot.infinity_polling()