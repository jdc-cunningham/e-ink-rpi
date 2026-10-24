# this file references the structure of epd_2in13_V2_test.py

import sys
import os
from pathlib import Path
import logging
from datetime import date
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)
base_path = str(Path.cwd())

# check exec path for CRON
if base_path == "/home/pi":
    base_path = "/home/pi/e-ink-rpi/code"

picdir = base_path + "/e-Paper/pic"
libdir = base_path + "/e-Paper/lib"

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V2

# double-click file to see available sizes in Windows
font_18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
font_24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font_36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)
font_72 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 72)

# google AI code
def get_days_left():
    move_in_date = date(2026, 12, 1)
    today = date.today()
    days_left = move_in_date - today
    return days_left.days

def clear_screen(epd):
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

def write_text(image, epd, x_offset, y_offset, text, font):
    draw = ImageDraw.Draw(image)
    draw.text((x_offset, y_offset), text, font = font, fill = 0)

def render_scene(epd):
    epd.display(epd.getbuffer(image))

try:
  epd = epd2in13_V2.EPD()
  days_left = get_days_left()
  title_text = "days till move in:"
  clear_screen(epd)
  image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
  write_text(image, epd, 10, 10, title_text, font_24)
  write_text(image, epd, 100, 40, str(days_left), font_72)
  render_scene(epd)
except Exception as e:
    print(f"An error occurred: {e}")
