import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np


def getSerialData(self,Samples,numData,serialConnection, lines):
    for i in range(numData):
        value  = float(serialConnection.readline().strip())  
        data[i].append(value)
        lines[i].set_data(range(Samples),data[i]) 

        
serialPort = input("COM: ") 
baudRate = 9600

try:
  serialConnection = serial.Serial(serialPort, baudRate) 
except:
  print('Cannot conect to the port')

Samples = 50  
sampleTime = 150  
numData = 7  


#Axis limit
xmin = 0
xmax = Samples
ymin = [-100, -100, -100, -180, -180, -10, 0]
ymax = [100, 100, 100, 180, 180, 40, 100]
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='blue'))
  
fig = plt.figure()
ax1 = fig.add_subplot(3, 3, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
ax1.title.set_text('AX')
ax1.add_line(lines[0])

ax2 = fig.add_subplot(3, 3, 2,xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
ax2.title.set_text('AY')
ax2.add_line(lines[1])

ax3 = fig.add_subplot(3, 3, 3,xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
ax3.title.set_text('AZ')
ax3.add_line(lines[2])

ax4 = fig.add_subplot(3, 3, 4,xlim=(xmin, xmax), ylim=(ymin[3] , ymax[3]))
ax4.title.set_text('GX')
ax4.add_line(lines[3])

ax5 = fig.add_subplot(3, 3, 5,xlim=(xmin, xmax), ylim=(ymin[4] , ymax[4]))
ax5.title.set_text('GY')
ax5.add_line(lines[4])

ax6 = fig.add_subplot(3, 3, 6,xlim=(xmin, xmax), ylim=(ymin[5] , ymax[5]))
ax6.title.set_text('Temperatura')
ax6.add_line(lines[5])

ax7 = fig.add_subplot(3, 3, 7,xlim=(xmin, xmax), ylim=(ymin[6] , ymax[6]))
ax7.title.set_text('Humedad')
ax7.add_line(lines[6])
    
anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,serialConnection,lines), interval=sampleTime)
plt.show()

serialConnection.close() # cerrar puerto serial/ close serial port
 
