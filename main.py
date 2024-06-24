import ssd1306

import machine
import random
import time


i2c = machine.I2C(-1, scl=machine.Pin(32), sda=machine.Pin(33))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

symbols = "abcdefghijklmnopqrstuvwxyz0123456789#!?%&$"
while True:
    columns = []
    while len(columns) < 16:
        temp = random.randint(0, 15)
        if not temp in columns:
            columns.append(temp)
    
    for column in columns:
        for line in range(random.randint(1, 6)):
            oled.text(str(random.choice(symbols)), column * 8, line * 10)
            oled.show()
    oled.fill(0)
    oled.show()
    time.sleep(0.05)
