# PIXMOD Console

The PIXMOB Console allows Generating IR Sequence's and also allowing sending them via Infrared to Pixmob Wristbands and LED Devices.

Big thanks to:
*Dani Weidman[@danielweidman](https://github.com/danielweidman)

*Zach Resmer[@zacharesmer](https://github.com/zacharesmer)

*James Lyphiard[@Lyphiard](https://github.com/Lyphiard

For the time and enough of all the initial research, many hours dedicated to the reverse engineering, research, discoveries and the time programming, But most of all to the the code used in this project.

Also not forgetting all the work, input and research done by the loyal members of our Discord community.

*Come join our PIXMOD Discord server! You can learn more, chat about your Pixmob Projects or MOD's, get help with our scripts or tools, and even ask for assistance with reactivating your wristband. It's just a few clicks away!
[JOIN DISCORD](https://discord.gg/UYqTjC7xp3)

You will need:

1. An Arduino-compatible microcontroller.
2. A 940nm IR emitter for the Arduino. You could set up a raw IR led or use a board like the transmitter piece of [this](https://www.amazon.com/Digital-Receiver-Transmitter-Arduino-Compatible/dp/B01E20VQD8/).

You can find the Arduino Sender Sketch on Dani's Github here: [@danielweidman - PixMob IR (and RF!) Reverse Engineering Project](https://github.com/danielweidman/pixmob-ir-reverse-engineering/tree/main/arduino_sender).

Basically, the steps are:
1. Connect an IR LED/transmitter to the Arduino board.

2. Connect the MCU to a computer by USB.

3. Upload the sketch from &quot;[here](https://github.com/danielweidman/pixmob-ir-reverse-engineering/tree/main/arduino_sender)&quot;to the MCU. 
*You may need to install the IRremote or IRremoteESP8266 library first.*

**Make sure to set the IR tranmitter data pin variable and note down the port/device address (COM port on Windows, /dev/\<something\> on Linux and macOS) of the MCU.**

4. Set the `ARDUINO_SERIAL_PORT` in "config.py". 

*If using a lower-power Arduino device like an Arduino Nano, also set `WAIT_BEFORE_SEND` to True.*

5. Run the PiXMoD Console Python Script.



## Requirements:
Arduino, ESP32 or Simlar MCU that uses the Arduino IDE.

#A 940nm Infrared LED and a 200Ω Resistor or Prebuilt Emitter

#A computer to upload the Arduino Sketch to the MCU & also to run the PIXMOD Console.

#Software and Libraries

#Arduino IDE

IRremote &/or IRremoteESP8266

#Python 3.11+

PySimpleGUI, 
pyperclip, 
serial, 
time, 
enum, 
sys, 
