import os
import numpy as np
import serial
import tensorflow as tf
from tensorflow import keras
import msvcrt # Windows only, for now
import time
import pyfiglet

GESTURES = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]

ser = serial.Serial("COM4",9600)
print(tf.version.VERSION)

print("Loading model...")
model = tf.keras.models.load_model("my_model.h5")
print("Model loaded!")
arr = np.zeros((1,1000))

while True:
    print("Waiting for keypress...")
    ser.readline()
    msvcrt.getch()
    print("Keypress detected!")
    ser.reset_input_buffer()
    for i in range(100):
        line = ser.readline()
        if not line:
            break
        line = line.decode("utf-8").rstrip("\r\n");
        values = line.split(',');
        values = list(map(int, values))
        # print(values)
        #ax, ay, az, gx, gy, gz, r1, r2, r3, r4 from arduino
        arr[0][i*10+0] = (values[0]/8192+4) / 8
        arr[0][i*10+1] = (values[1]/8192+4) / 8
        arr[0][i*10+2] = (values[2]/8192+4) / 8
        arr[0][i*10+3] =  (values[3] /16.384+2000) / 4000
        arr[0][i*10+4] =  (values[4] /16.384+2000) / 4000
        arr[0][i*10+5] =  (values[5] /16.384+2000) / 4000
        arr[0][i*10+6] = values[6] / 1023
        arr[0][i*10+7] = values[7] / 1023
        arr[0][i*10+8] = values[8] / 1023
        arr[0][i*10+9] = values[9] / 1023
        # for j in range(10):  # Assuming values has 10 elements
        #     arr[0, i*10+j] = values[j]
    # print(np.round(arr, 2))
    result = model.predict(arr)
    # print(result)
    letter = GESTURES[np.argmax(result)]
    print(pyfiglet.figlet_format(letter))
    ser.write(letter.encode())

