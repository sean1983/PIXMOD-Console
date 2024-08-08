# PIXMOD Console

The PIXMOB Console allows Generating IR Sequence's and also allowing sending them via Infrared to Pixmob Wristbands and LED Devices.

Big thanks for Dani [@danielweidman](https://github.com/danielweidman) & James [@Lyphiard](https://github.com/Lyphiard) for the code used in this project.

You can come find out more, get assistance or help with our projects by joining us on our PIXMOD Discord server! 
https://discord.gg/UYqTjC7xp3

You will need:

1. An Arduino-compatible microcontroller.
2. A 940nm IR emitter for the Arduino. You could set up a raw IR led or use a board like the transmitter piece of [this](https://www.amazon.com/Digital-Receiver-Transmitter-Arduino-Compatible/dp/B01E20VQD8/).

You can find the Arduino Sketch on @danielweidman repo, [here](https://github.com/danielweidman/pixmob-ir-reverse-engineering/tree/main/arduino_sender).

Basically, the steps are:
1. Connect an IR LED/transmitter to the Arduino board.
2. Connect the Arduino to a computer by USB.
3. Upload the sketch from &quot;arduino\_sender&quot; to the Arduino. You may need to install the IRremote or IRremoteESP8266 library first. Make sure to set the IR tranmitter data pin variable and note down the port/device address (COM port on Windows, /dev/\<something\> on Linux and macOS) of the Arduino.
4. Set the `ARDUINO_SERIAL_PORT` in "config.py". If using a lower-power Arduino device like an Arduino Nano, also set `WAIT_BEFORE_SEND` to True.
5. Run the PiXMoD Console Python Script.



## Requirements:
Python 3.11+

with Libs:
PySimpleGUI
pyperclip
serial
time
enum
sys
