###############################################################
##                                                           ##
##     PIXMOD Console by Sean Yem & The PIXMOD Community     ##
##         https://github.com/sean1983/PIXMOD-Console        ##
##                                                           ##
##   With special thanks to:                                 ##
##         Dani Weidman: https://github.com/danielweidman    ##
##          Zach Resmer: https://github.com/zacharesmer      ##
##           James Wang: https://github.com/jamesw343        ##
##                 cra0: https://github.com/cra0             ##
##                                                           ##
## >>> JOIN OUR DISCORD: https://discord.gg/UYqTjC7xp3   <<< ##
##                                                           ##
###############################################################
##                                                           ##
##    ****   MAKE SURE TO INSTALL REQUIRE LIBRARYS   ****    ##
##    ***      pip install -r ./requirements.txt      ***    ##
##    **                                               **    ##
##    *   Please configure Serial Port in 'config.py'   *    ##
##                                                           ##
###############################################################

# Ver & GUI Settings
APP_TITLE = "PIXMOD Console"
APP_VERSION = "v.0.1.7"
FULL_TITLE = f"{APP_TITLE} {APP_VERSION}"
dropdown_width = 20
window_background_color = "#331166"  # Dark Purple

# Import required Libs
import config as cfg
import libs.pixmob_ir_protocol as pmir
from libs.pixmob_ir_protocol import Chance, Time
from libs.pixmob_conversion_funcs import bits_to_arduino_string
import PySimpleGUI as sg
import pyperclip
import serial
import time

# Mapping Labels to values in pixmob_ir_protocol
chance_options = {
    "100%": Chance.CHANCE_100_PCT,
     "88%": Chance.CHANCE_88_PCT,
     "67%": Chance.CHANCE_67_PCT,
     "50%": Chance.CHANCE_50_PCT,
     "32%": Chance.CHANCE_32_PCT,
     "16%": Chance.CHANCE_16_PCT,
     "10%": Chance.CHANCE_10_PCT,
      "4%": Chance.CHANCE_4_PCT,
}

time_options = {
       "0 ms": Time.TIME_0_MS,
      "32 ms": Time.TIME_32_MS,
      "96 ms": Time.TIME_96_MS,
     "192 ms": Time.TIME_192_MS,
     "480 ms": Time.TIME_480_MS,
     "960 ms": Time.TIME_960_MS,
    "2400 ms": Time.TIME_2400_MS,
    "3840 ms": Time.TIME_3840_MS,
}

# GUI Theme & Layout
layout = [
    [sg.Text(FULL_TITLE, size=(20, 1), font=("Helvetica", 16), justification="left", background_color=window_background_color)],
    [
        sg.Column([
            [sg.Text("Red", size=(10, 1), justification='left', background_color=window_background_color)],
            [sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=128, key='-RED-', enable_events=True),
             sg.Input(default_text='128', size=(5, 1), key='-IN-RED-', enable_events=True)],
            [sg.Text("Green", size=(10, 1), justification='left', background_color=window_background_color)],
            [sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=128, key='-GREEN-', enable_events=True),
             sg.Input(default_text='128', size=(5, 1), key='-IN-GREEN-', enable_events=True)],
            [sg.Text("Blue", size=(10, 1), justification='left', background_color=window_background_color)],
            [sg.Slider(range=(0, 255), orientation='h', size=(20, 15), default_value=128, key='-BLUE-', enable_events=True),
             sg.Input(default_text='128', size=(5, 1), key='-IN-BLUE-', enable_events=True)]
        ], background_color=window_background_color),
        sg.Canvas(size=(150, 240), background_color='black', key='-COLOR_PREVIEW-'),
        sg.Column([
            [sg.Text("Probability", size=(15, 1), justification='right', background_color=window_background_color),
             sg.Combo(list(chance_options.keys()), default_value=list(chance_options.keys())[0], key='-CHANCE-', size=(dropdown_width, 1), readonly=True, enable_events=True)],
            [sg.Text("Fade In", size=(15, 1), justification='right', background_color=window_background_color),
             sg.Combo(list(time_options.keys()), default_value=list(time_options.keys())[0], key='-ATTACK-', size=(dropdown_width, 1), readonly=True, enable_events=True)],
            [sg.Text("Sustain", size=(15, 1), justification='right', background_color=window_background_color),
             sg.Combo(list(time_options.keys()), default_value=list(time_options.keys())[0], key='-SUSTAIN-', size=(dropdown_width, 1), readonly=True, enable_events=True)],
            [sg.Text("Fade Out", size=(15, 1), justification='right', background_color=window_background_color),
             sg.Combo(list(time_options.keys()), default_value=list(time_options.keys())[0], key='-RELEASE-', size=(dropdown_width, 1), readonly=True, enable_events=True)],
        ], background_color=window_background_color)
    ],
    [
        sg.Push(background_color=window_background_color),  
        sg.Button("Reset", button_color=('white', '#8B0000')),  
        sg.Button("Generate IR", button_color=('white', '#006400'), visible=False),  # Hidden for now as using Auto.
        sg.Button("Copy Code", button_color=('white', '#404040'), disabled=True),
        sg.Button("Send IR", button_color=('white', '#006400'), disabled=True) 
    ],
    [sg.InputText(size=(145, 1), key='-OUTPUT-', font=('Helvetica', 7), background_color='white')]
]

# Launch GUI
window = sg.Window(FULL_TITLE, layout, finalize=True, background_color=window_background_color)

def update_color_preview(window, red, green, blue):
    color_hex = f'#{int(red):02x}{int(green):02x}{int(blue):02x}'
    window['-COLOR_PREVIEW-'].TKCanvas.configure(background=color_hex)

def reset_values(window):
    window['-RED-'].update(128)
    window['-IN-RED-'].update('128')
    window['-GREEN-'].update(128)
    window['-IN-GREEN-'].update('128')
    window['-BLUE-'].update(128)
    window['-IN-BLUE-'].update('128')
    window['-CHANCE-'].update(list(chance_options.keys())[0])
    window['-ATTACK-'].update(list(time_options.keys())[0])
    window['-SUSTAIN-'].update(list(time_options.keys())[0])
    window['-RELEASE-'].update(list(time_options.keys())[0])
    window['-OUTPUT-'].update('')
    update_color_preview(window, 128, 128, 128)
    window['Copy Code'].update(disabled=True)
    window['Send IR'].update(disabled=True)

def generate_ir(window, values):
    try:
        # Check used params
        ##print(f"Selected chance: {values['-CHANCE-']}")
        chance = chance_options[values['-CHANCE-']]  
        command = pmir.CommandSingleColorExt(
            red=int(float(values['-IN-RED-'])), 
            green=int(float(values['-IN-GREEN-'])), 
            blue=int(float(values['-IN-BLUE-'])),
            chance=chance,
            attack=time_options[values['-ATTACK-']],
            sustain=time_options[values['-SUSTAIN-']],
            release=time_options[values['-RELEASE-']],
        )
        encoded_command = command.encode()
        window['-OUTPUT-'].update(f"{encoded_command}")

# Enable Copy and Send IR buttons on valid output is generated
        window['Copy Code'].update(disabled=False)
        window['Send IR'].update(disabled=False)
    except KeyError as e:
        print(f"Error: {e} not found in chance_options dictionary")

# Initial color preview update
update_color_preview(window, 128, 128, 128)

# Start loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Debug: Print debug values
    #print("Debug:", values['-CHANCE-'], values['-ATTACK-'], values['-SUSTAIN-'], values['-RELEASE-'])

    # Update color preview and sync on slider move
    if event in ['-RED-', '-GREEN-', '-BLUE-']:
        input_key = f'-IN-{event[1:]}' 
        window[input_key].update(int(values[event])) 
        update_color_preview(window, int(values['-RED-']), int(values['-GREEN-']), int(values['-BLUE-']))
        generate_ir(window, values)  # Automatically generate IR

    # Update slider value when any input changes
    elif event in ['-IN-RED-', '-IN-GREEN-', '-IN-BLUE-']:
        try:
            value = int(float(values[event])) 
            if 0 <= value <= 255:
                slider_key = event.replace('-IN-', '-')
                window[slider_key].update(value)
                update_color_preview(window, int(values['-IN-RED-']), int(values['-IN-GREEN-']), int(values['-IN-BLUE-']))
                generate_ir(window, values)  # Automatically generate IR
        except ValueError:
            window[event].update(int(values[event.replace('-IN-', '-')]))  # Reset on invalid

    # Generate IR when values change
    elif event in ['-CHANCE-', '-ATTACK-', '-SUSTAIN-', '-RELEASE-']:
        generate_ir(window, values)

    if event == "Reset":
        reset_values(window)

    if event == "Copy Code":
        pyperclip.copy(values['-OUTPUT-'])

    if event == "Send IR":
        try:
            effect_bits = list(map(int, values['-OUTPUT-'].strip('[]').split(',')))
            arduino_string = bits_to_arduino_string(effect_bits)
            
            # Setup serial connection
            arduino = serial.Serial(port=cfg.ARDUINO_SERIAL_PORT, baudrate=cfg.ARDUINO_BAUD_RATE, timeout=.1)
            if cfg.WAIT_BEFORE_SEND:
                time.sleep(1)

            arduino.write(bytes(arduino_string, 'utf-8'))
            time.sleep(0.1)  # Give time for the data to be sent
            arduino.close()

        except Exception as e:
            sg.popup_error(f"Failed to send IR: {e}")

window.close()
