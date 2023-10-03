import time
from machine import Pin, UART, I2C, ADC
# Библиотека для работы со светодиодами WS2812
from neopixel import Neopixel
from ssd1306 import SSD1306_I2C
import framebuf,sys

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

maxJoyX= 64300
minJoyX= 1255
maxJoyY= 63485
minJoyY= 1270
centerX = 1000
centerY = 1000
mZone = 300

valuesjoyx = []
valuesjoyy = []
buttonValue = 0


uart0 = UART(0, baudrate=9600)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display



joyxA = ADC(26)
joyyA = ADC(27)
joyBut = Pin(2, Pin.IN, Pin.PULL_UP)
jdy40Set = Pin(3,Pin.OUT)




def readJoy():
    joyxr = joyxA.read_u16()
    joyyr = joyyA.read_u16()
    valuesjoyx.pop(0)
    valuesjoyx.append(joyxr)
    valuesjoyy.pop(0)
    valuesjoyy.append(joyyr)
    joyx = int(sum(valuesjoyx) / len(valuesjoyx))
    joyy = int(sum(valuesjoyy) / len(valuesjoyy))
    if 
    else:
        if joyx >= maxJoyX:
            joyx = maxJoyX
        else:
            if joyx <= minJoyX:
                joyx= minJoyX
    if joyx 
    else:
        if joyy >= maxJoyY:
            joyy = maxJoyY
        else:
            if joyy <=minJoyY:
                joyy = minJoyY


    if joyBut.value():
        joyB =0
    else:
        joyB = 1
    return joyx, joyy, joyB

def displayText(text, position=(0,0),clear_oled=True,show_text=True):
    if clear_oled:
        oled.fill(0) # Clear the oled display in case it has junk on it.
    oled.text(text,position[0],position[1]) # dispaying text
    if show_text:
        oled.show()  # Updating the display






# Создаём объект для работы со светодиодной матрицей
# Номер пина, к которому подключена матрица WS2812
led_pin = 23
# Количество светодиодов
led_count = 1
strip = Neopixel(led_count, 0, led_pin, "GRB")
colors = ((255,153,0),(51,255,0),(0,41,255))
# Создаём фиксированные цвета


# Устанавливаем яркость светодиодов
# Диапазон значений от 0 до 255
strip.brightness(35)

for _ in range(10):
    joyxr = joyxA.read_u16()
    joyyr = joyyA.read_u16()
    valuesjoyx.append(joyxr)
    valuesjoyy.append(joyyr)
    joyx = int(sum(valuesjoyx) / len(valuesjoyx))
    joyy = int(sum(valuesjoyy) / len(valuesjoyy))

while True:
    oled.fill(0)
    joyx, joyy, joyB = readJoy()
    print(joyx, joyy, joyB)
    displayText(str(joyx), (0, 0), clear_oled=False, show_text=True)
    displayText(str(joyy), (50, 0), clear_oled=False, show_text=True)
    displayText(str(joyB), (0, 10), clear_oled=False, show_text=True)
    '''for color in colors:
        # Перебираем светодиоды
            # Выставляем цвет светодиода
        strip.set_pixel(0, color)
        # Ждём 100 мс
        time.sleep(0.35)
        # Обновляем изменения
        strip.show()'''




