from operator import index
import os
import numpy
import serial
import pandas as pd
import msvcrt # Windows only, for now
import csv
import string
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
            isRecording = True
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
letter_check = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for c in letter_check:
    letter_check_file_path = os.path.join('data', f'{c}.csv')
    if not os.path.exists(letter_check_file_path):
        with open(letter_check_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ', 'r1', 'r2', 'r3', 'r4'])
SAMPLES = 100
curr = 0

arr = numpy.zeros((100,10))
while True:
    ser.readline()
    keypress_check()
    print(f"{CLEAR}{GREEN}[1] start recording{RESET}", end='')
    print(f"\t\tCurrent Letter:{YELLOW}{letter}{RESET}", end = "\n")
    print(LINE_UP,end='')
    if isRecording:
        print(f"{CLEAR}{RED}recording...{RESET}", end='')
        print(f"\t\tCurrent Letter:{YELLOW}{letter}{RESET}", end = "\n")
        print(LINE_UP,end='')
        for i in range(100):
            values = ser.readline().decode("utf-8").rstrip("\r\n").split(',');
            # print(f"{CLEAR}aX:{values[0]}", end='\n')
            # print(f"{CLEAR}aY:{values[1]}", end='\n')
            # print(f"{CLEAR}aZ:{values[2]}", end='\n')
            # print(f"{CLEAR}gX:{values[3]}", end='\n')
            # print(f"{CLEAR}gY:{values[4]}", end='\n')
            # print(f"{CLEAR}gZ:{values[5]}", end='\n')
            # print(f"{CLEAR}R1:{values[6]}", end='\n')
            # print(f"{CLEAR}R2:{values[7]}", end='\n')
            # print(f"{CLEAR}R3:{values[8]}", end='\n')
            # print(f"{CLEAR}R4:{values[9]}", end='\n')
            arr[curr] = values
        isRecording = False
        df = pd.DataFrame(arr,index=None)
        df.to_csv(os.path.join('data', f'{letter}.csv'), mode='a', header=False,index=False)
    print(LINE_UP,end='')