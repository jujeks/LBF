#pip3 install pynput pyserial

import serial
from pynput.keyboard import Key, Controller
import sys
import glob


ser = serial.Serial(
    port='COM3',    # Numer portu szeregowego (zmień na odpowiedni dla Twojego systemu)
    baudrate=9600,  # Prędkość transmisji danych
    timeout=1       # Czas oczekiwania na odczyt danych
)




print("OK, działa - czekam na dane z COM1 - 9600")
print("Program pobiera wagę ignorując [] i jednostkę, kropkę zamienia na przecinek")
print("Naciśnij ctrl + c aby wyjść z programu")

keyboard = Controller()

try:
    while(ser.is_open):

        if(ser.in_waiting>0):
            
            rxLine=ser.readline().decode("ascii").strip()
            # w celu usunięcia z wyników nawiasów [] i jednostki miary trzeba użyć poniższych funkcji
            rxLine = rxLine.split(" ")[0].replace("[", "").replace("]", "").replace(".", ",")
            keyboard.type(rxLine)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
except:
    print("Koniec pracy programu")