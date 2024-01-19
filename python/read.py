import os
import serial
import readchar
import msvcrt # Windows only, for now
import csv
ser = serial.Serial("COM4",9600)
isRecording = False
letter = '='
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
if not os.path.exists('data'):
    os.makedirs('data')
def keypress_check():
    global isRecording
    global letter
    if msvcrt.kbhit():
        c = bytes.decode(msvcrt.getch())
        if  c == '1':
            isRecording = not isRecording;
        elif c.isalpha():
            letter = c.upper()

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


SAMPLES = 100
curr = 0
while True:
    # print('\033[?25l', end="")
    line = ser.readline()
    keypress_check()
    letter_file_path = os.path.join('data', f'{letter}.csv')
    if not os.path.exists(letter_file_path):
        with open(letter_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ', 'r1', 'r2', 'r3', 'r4'])
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
        # print(f"{CLEAR}Sensor Eleven:{values[10]}", end='\n')
        if curr == SAMPLES:
            curr = 0
            isRecording = False
        if not isRecording:
            print(f"{CLEAR}{GREEN}[1] start recording{RESET}", end='')
        else:
            print(f"{CLEAR}{RED}[1] stop recording{RESET}", end='')
            curr += 1
            with open(letter_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(values)


        print(f"\t\tCurrent Letter:{YELLOW}{letter}{RESET}", end = "\n")

        print(LINE_UP*13, end='')
