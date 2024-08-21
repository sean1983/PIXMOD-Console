# PIXMOD Console

## Overview
The PIXMOD Console let's you   generate and transmit Infrared  sequences, enabling control of Pixmob wristbands and other pixmob device's.

## Acknowledgments
Special thanks to:
- Dani Weidman [@danielweidman](https://github.com/danielweidman)
- Zach Resmer  [@zacharesmer](https://github.com/zacharesmer)
- James Wang   [@jamesw343](https://github.com/jamesw343)
- Cra0         [@cra0](https://github.com/cra0)

For their extensive initial research, dedication to reverse engineering, and contributions to the programming and code used in this project. Also, a shoutout to our loyal Discord community members for their invaluable work, input, and research.

## Join Our Community
Come join our PIXMOD Discord server! Engage in discussions about Pixmob projects or MODs, receive help with our scripts or tools, and request assistance with reactivating your wristband.
[JOIN DISCORD](https://discord.gg/UYqTjC7xp3)

## Hardware Requirements
1. An Arduino, ESP8266, ESP32 or simlar compatible (MCU) microcontroller.
2. A 940nm Infrared LED and a 200Ω Resistor or Prebuilt Emitter.
3. Computer running Windows, Linux or OSX, For uploading Arduino Sketch and running PIXMOD Console.

## Getting Started
You'll first need the Arduino Sender Sketch on Dani's Github here:<br />
[PixMob IR (and RF!) Reverse Engineering Project](https://github.com/danielweidman/pixmob-ir-reverse-engineering/tree/main/arduino_sender)

### Steps
Follow these steps to set up your DIY Infrared Transmitter:

1. Connect an IR LED/transmitter to the MCU board.

2. Connect the MCU to a computer via USB.

3. Upload the sketch from [here](https://github.com/danielweidman/pixmob-ir-reverse-engineering/tree/main/arduino_sender) to the MCU.

  #### Examples
- *Note the serial port/device address of the MCU*
  - **Window:** COM***x***
  - **Linux:** /dev/ttyUSB***x***
  - **OSX:** /dev/tty.usb***x***
  
4. Set the serial port using  *ARDUINO_SERIAL_PORT* in **config.py**.
*If using a low-power Arduino device like an Arduino Nano, also set `WAIT_BEFORE_SEND` to True.*

5. Install the Python Libraries using:
    ``` pip install -r ./requirements.txt ```

6. Run the PIXMOD Console.

## Software Requirements
- Arduino IDE with the following libraries:
  - IRremote *(Use for Arduinio UNO & Mega)*
  - IRremoteESP8266 *(Use for ESP8266 & ESP32)*
    - ***Version 2.0.17*** *(Version 3+ has issues)*

- Python 3.11 or later with the following libraries:
  - pyperclip==1.9.0
  - pyserial==3.5
  - PySimpleGUI==5.0.6
  - PySimpleGUI==5.0.6
  - config==0.5.1

## Contributing
Contributions to the PIXMOD Console are welcome! Whether it's refining the code, adding new features, or improving documentation, we appreciate your help in making this project better.
