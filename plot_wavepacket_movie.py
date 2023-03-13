#6.15
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, pi
from matplotlib.animation import FuncAnimation


distance = np.linspace(-6, 6, 250)
times = np.linspace(-1,1, 250)
amplitude = exp(-(distance-3*times)**2) * sin(3*pi*((distance-3*times)))

fig = plt.figure()
lines = plt.plot(distance, times)
plt.axis([distance[0], distance[-1], -1,1])
plt.xlabel('Linear Distance')
plt.ylabel('Amplitude')


def frame(time):
  y = exp(-(distance-3*time)**2) * sin(3*pi*((distance-3*time)))
  lines[0].set_ydata(y)
  return lines


anim = FuncAnimation(fig, frame, frames = times*5, interval = 50)
anim.save("wave.gif","imagemagick")


def wave_packet(x, t):
   return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))

 
xlist = np.linspace(-4, 4, 1001)
time_list = [-0.85, 0, 0.85]
for time in time_list:
   ylist = wave_packet(xlist, time)
   plt.plot(xlist, ylist)
   plt.xlabel('x')
   plt.ylabel('Amplitude')
   plt.title('One dimensional wave packet: t = %.2f s' % time)
   plt.savefig('wavepacket_report-t=%.2f.png' % t)
   plt.close()
 
