import os
import serial
import readchar
import msvcrt # Windows only, for now
ser = serial.Serial("COM3",9600)
isRecording = False
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def recordingCheck():
    global isRecording
    if msvcrt.kbhit():
        if str(msvcrt.getch()) == "b's'":
            isRecording = not isRecording;
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
while True:
    # print('\033[?25l', end="")
    line = ser.readline()
    recordingCheck()
    if line:
        line = line.decode("utf-8").rstrip("\r\n");
        values = line.split(',');
        print(values)
        print(f"{CLEAR}Sensor One:{values[0]}", end='\n')
        print(f"{CLEAR}Sensor Two:{values[1]}", end='\n')
        print(f"{CLEAR}Sensor Three:{values[2]}", end='\n')
        print(f"{CLEAR}Sensor Four:{values[3]}", end='\n')
        print(f"{CLEAR}Sensor Five:{values[4]}", end='\n')
        if not isRecording:
            print(f"{CLEAR}{GREEN}[s]tart recording{RESET}", end='\n')
        else:
            print(f"{CLEAR}{RED}[s]top recording{RESET}", end='\n')
        print(LINE_UP*8, end='')
