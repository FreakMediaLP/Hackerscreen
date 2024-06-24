import ssd1306

import machine
import random
import time


i2c = machine.I2C(-1, scl=machine.Pin(32), sda=machine.Pin(33))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
symbols = "abcdefghijklmnopqrstuvwxyz0123456789#!?%&$"

def progress_bar(progress, total, x=0, y=40, width=128, height=10):
    oled.rect(x, y, width, height, 1)
    inner_width = int((progress / total) * (width - 2))
    oled.fill_rect(x + 1, y + 1, inner_width, height - 2, 1)

def create_progress(text, offset, sleep_timer):
    oled.text(text, offset, 30)
    for progress in range(101):
        progress_bar(progress, 100)
        oled.show()
        time.sleep(sleep_timer)
    oled.fill(0)
    oled.show()

create_progress("Initiating", 24, 0)
create_progress("Reading Memory", 8, 0.05)
create_progress("Encrypting Files", 0, 0.25)
create_progress("Uploading Virus", 4, 0.1)

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
