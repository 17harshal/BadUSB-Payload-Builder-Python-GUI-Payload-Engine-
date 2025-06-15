Overview
Created a Python-based GUI that lets you:
* Type your payload commands (like keystrokes)
* Set delays between actions
* Convert them into HID-compatible binary codes
* Automatically deploy the script via /dev/hidg0 on the Raspberry Pi

Tools/Technologies
* Python 3
* Tkinter (for GUI)
* Custom HID keycode mapper
* Optional: Save/load payloads from .txt files

File Structure
badusb_builder/
├── main.py
├── keycodes.py
├── payload_sender.py
├── payloads/
│   └── example.txt
