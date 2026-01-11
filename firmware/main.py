# IMPORTANT! Currently project is not finished. Only harware design is done. Sofware is under development. this code is a placeholder.

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D4, board.D2)
keyboard.row_pins = (board.D26, board.D27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D29, board.D28, None, False),) 
keyboard.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.D0,
    num_pixels=6,
    val_limit=100,
    hue_default=0,
    sat_default=255,
    val_default=50,
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.N1,    KC.N2,    KC.N3,
        KC.N4,    KC.N5,    KC.N6,
    ],
    [
        KC.F1,    KC.F2,    KC.F3,
        KC.F4,    KC.F5,    KC.F6,
    ],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), 
    ((KC.LEFT, KC.RIGHT),), 
]

if __name__ == '__main__':
    keyboard.go()
