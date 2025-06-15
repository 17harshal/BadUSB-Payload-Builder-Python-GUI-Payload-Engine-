# payload_sender.py

import time
from keycodes import key_map

def send_char(char):
    code = key_map.get(char.lower())
    if code is None:
        return
    with open('/dev/hidg0', 'wb') as f:
        f.write(bytes([0x00, 0x00, code, 0x00, 0x00, 0x00, 0x00, 0x00]))
        time.sleep(0.05)
        f.write(bytes(8))  # release

def send_string(text):
    for c in text:
        if c == ' ':
            send_char('SPACE')
        elif c == '\n':
            send_char('ENTER')
        else:
            send_char(c)

def run_payload(lines):
    for line in lines:
        if line.startswith("DELAY"):
            time.sleep(int(line.split()[1]) / 1000)
        elif line.startswith("STRING"):
            send_string(line[7:])
        elif line.startswith("ENTER"):
            send_char('ENTER')
        elif line.startswith("TAB"):
            send_char('TAB')
