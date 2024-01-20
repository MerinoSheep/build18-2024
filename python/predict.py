import os
import numpy as np
import serial
import tensorflow as tf
from tensorflow import keras
import msvcrt # Windows only, for now

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

model = tf.keras.models.load_model("my_model.h5")

arr = np.zeros.rand(1,1000)

while True:
    msvcrt.getch()
    for i in range(100):
        line = ser.readline()
        line = line.decode("utf-8").rstrip("\r\n");
        values = line.split(',');
        arr[i+0] = values[0]
        arr[i+1] = values[1]
        arr[i+2] = values[2]
        arr[i+3] = values[3]
        arr[i+4] = values[4]
        arr[i+5] = values[5]
        arr[i+6] = values[6]
        arr[i+7] = values[7]
        arr[i+8] = values[8]
        arr[i+9] = values[9]

    result = model.predict(arr)