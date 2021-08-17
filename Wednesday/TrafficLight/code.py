# Write your code here :-)
from adafruit_clue import clue
from adafruit_slideshow import SlideShow, PlayBackDirection
import board
slideshow = SlideShow(
    board.DISPLAY,
    None,
    folder="/1/",
    loop=False,
    order = 0,
    dwell=0,
    fade_effect = False,
)
while True:
    if clue.proximity > 25 and clue.proximity < 75:
        slideshow = SlideShow(
        board.DISPLAY,
        None,
        folder="/2/",
        loop=False,
        order = 0,
        dwell=0,
        fade_effect = False,)
    elif clue.proximity >= 75:
        slideshow = SlideShow(
        board.DISPLAY,
        None,
        folder="/3/",
        loop=False,
        order = 0,
        dwell=0,
        fade_effect = False,)
    else:
        slideshow = SlideShow(
        board.DISPLAY,
        None,
        folder="/1/",
        loop=False,
        order = 0,
        dwell=0,
        fade_effect = False,)
