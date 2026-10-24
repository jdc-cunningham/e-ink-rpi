# this file references the structure of epd_2in13_V2_test.py

import sys
import os
from pathlib import Path
import logging
from datetime import date
from PIL import Image,ImageDraw,ImageFont

base_path = str(Path.cwd())
picdir = base_path + "/e-Paper/pic"
libdir = base_path + "/e-Paper/lib"

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V2

logging.basicConfig(level=logging.DEBUG)

# google AI code
def get_days_left():
    move_in_date = date(2026, 12, 1)
    today = date.today()
    days_left = move_in_date - today
    return days_left.days

def display_text(epd, x_offset, y_offset, text):
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.text((x_offset, y_offset), text, font = font24, fill = 0)
    epd.display(epd.getbuffer(image))

try:
  epd = epd2in13_V2.EPD()
  days_left = get_days_left()
  text = f"days to move in: {days_left}"
  display_text(epd, 10, 10, text)
except Exception as e:
    print(f"An error occurred: {e}")
