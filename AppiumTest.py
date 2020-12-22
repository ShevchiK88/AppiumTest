import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

#Тап по экрану, по умолчанию 20 тапов
def tapOnScreen(x=720,y=2600,repeat=20):
    i = 0
    while i < repeat:
        action = TouchAction(driver).tap(None, x, y, 1).perform()
        i = i + 1
        time.sleep(3)

#Параметры устройства
capabilities = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'Android Emulator',
    'app': 'C:\\Users\\Vitalii\\PycharmProjects\\AppiumTest\\App\\Romance Fate Stories and Choices_v2.2.9_apkpure.com.apk'
}

#Подключились к эмулятору запустили приложение
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

#Ждем загрузки
print("I am wait")
time.sleep(50)

#Чтобы не потерять соединение тапаем по экрану
print("Tap for conection")
action = TouchAction(driver).tap(None, 720, 2600, 1).perform()
time.sleep(30)

#Начинаем взаиможействовать с приложением
print("I am start tap")

#Начальный экран
print("Tap")
action = TouchAction(driver).tap(None, 720, 2600, 1).perform()
time.sleep(10)

# Запуск окна кастомизации
# Проверка работы кнопок Влево Вправо
# Проверка переходов между экранами кастомизации [Внешний вид -> Прическа -> Одежда]
user_generator=0
for user_generator in range (0,3,1):

    tapOnScreen(1380,1300,5) # Тап на правой кнопке
    tapOnScreen(60,1300,5)   # Тап на левой кнопке
    tapOnScreen(720,2600,2)
    user_generator=user_generator+1

#Подтверждение внешнего вида персонажа
tapOnScreen(720,1800,1)

#Подтверждение имени персонажа
print("Confirm name tap")
tapOnScreen(720,1500,1)

#Диалог
tapOnScreen()

#Выбор 1 варианта ответа в диалоге
tapOnScreen(720,1800,1)

#Диалог
tapOnScreen()








