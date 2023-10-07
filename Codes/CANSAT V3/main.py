from sense_hat import SenseHat
from os import system
from openpyxl import Workbook
from time import sleep
import threading

imgnum = 0
vidnum = 0

book = Workbook()
sheet = book.active

sense = SenseHat()
sense.set_imu_config(True, True, True)  # accelerometer, magnetometer , gyroscope
sense.clear()
sense.low_light = True
    
def Exel():
    sheet['A1'] = "Temperatura"
    sheet['B1'] = "Humedad"
    sheet['C1'] = "Presion"
    sheet['D1'] = "Accel X"
    sheet['E1'] = "Accel Y"
    sheet['F1'] = "Accel Z"
    sheet['G1'] = "Ang X"
    sheet['H1'] = "Ang Y"
    sheet['I1'] = "Ang Z"
    sheet['J1'] = "Mag X"
    sheet['K1'] = "Mag Y"
    sheet['L1'] = "Mag Z"

    for i in range(2,450):
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_orientation()
        mag = sense.get_compass_raw()
        
        sheet[f'A{i}'] = round(sense.get_temperature(),2)
        sheet[f'B{i}'] = round(sense.get_humidity(),2)
        sheet[f'C{i}'] = round(sense.get_pressure(),2)
        sheet[f'D{i}'] = round(accel['x'],3)
        sheet[f'E{i}'] = round(accel['y'],3)
        sheet[f'F{i}'] = round(accel['z'],3)
        sheet[f'G{i}'] = round(gyro['pitch'],2)
        sheet[f'H{i}'] = round(gyro['roll'],2)
        sheet[f'I{i}'] = round(gyro['yaw'],2)
        sheet[f'J{i}'] = round(mag['x'],2)
        sheet[f'K{i}'] = round(mag['y'],2)
        sheet[f'L{i}'] = round(mag['z'],2)
        
        values = [{"Temp":round(sense.get_temperature(),2)}, 
        {"Hum":round(sense.get_humidity(),2)}, 
        {"Pres":round(sense.get_pressure(),2)}, 
        {"Accel":sense.get_accelerometer_raw()}, 
        {"Gyro":sense.get_orientation()}, 
        {"Mag":sense.get_compass_raw()}] 
        
        print(values)
        book.save('/home/ipet66/Desktop/Balsat/Muestras.xlsx')
        sleep(1)

def Images():
    global imgnum
    
    while True:
        system(f"fswebcam -r 1280x720 -q 80 --skip 5 /home/ipet66/Desktop/Balsat/images/img{imgnum}.jpg")
        imgnum = imgnum+1
        print(f"Total images: {imgnum}")
        sleep(1)   

#def Videos():
    system(f"ffmpeg -t 300 -f video4linux2 -i /dev/video1 -vf scale=1280x720 ./videos/grabacion.avi -y")

t1 = threading.Thread(target=Exel)
t2 = threading.Thread(target=Images)
t3 = threading.Thread(target=Videos)

t1.start()
t2.start()
t3.start()