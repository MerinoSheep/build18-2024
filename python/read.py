import os
import serial
import readchar
import msvcrt # Windows only, for now
ser = serial.Serial("COM3",9600)
isRecording = False
letter = '?'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def keypress_check():
    global isRecording
    global letter
    if msvcrt.kbhit():
        if bytes.decode(msvcrt.getch()) == '1':
            isRecording = not isRecording;
        if bytes.decode(msvcrt.getch()).isalpha():
            letter = bytes.decode(msvcrt.getch()).upper()
# Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m' # reset to the default color

LINE_UP = '\033[1A'
CLEAR = "\033[K"

if not os.path.exists('data'):
    os.makedirs('data')

while True:
    # print('\033[?25l', end="")
    line = ser.readline()
    keypress_check()
    if line:
        line = line.decode("utf-8").rstrip("\r\n");
        values = line.split(',');
        print(values)
        print(f"{CLEAR}Sensor One:{values[0]}", end='\n')
        print(f"{CLEAR}Sensor Two:{values[1]}", end='\n')
        print(f"{CLEAR}Sensor Three:{values[2]}", end='\n')
        print(f"{CLEAR}Sensor Four:{values[3]}", end='\n')
        print(f"{CLEAR}Sensor Five:{values[4]}", end='\n')
        print(f"{CLEAR}Sensor Six:{values[5]}", end='\n')
        print(f"{CLEAR}Sensor Seven:{values[6]}", end='\n')
        print(f"{CLEAR}Sensor Eight:{values[7]}", end='\n')
        print(f"{CLEAR}Sensor Nine:{values[8]}", end='\n')
        print(f"{CLEAR}Sensor Ten:{values[9]}", end='\n')
        print(f"{CLEAR}Sensor Eleven:{values[10]}", end='\n')
        if not isRecording:
            print(f"{CLEAR}{GREEN}[1] start recording{RESET}", end='')
        else:
            print(f"{CLEAR}{RED}[1] stop recording{RESET}", end='')
        print(f"\t\tCurrent Letter:{BLUE}{letter}{RESET}", end = "\n")

        print(LINE_UP*8, end='')
