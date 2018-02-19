import matplotlib.pyplot as plt
import numpy as np
from WIB_args import init_parser

args = init_parser().parse_args()

FEMB = args.FEMB
f = args.input
outputdir = args.output

#files = ['rce_stream0.txt', 'rce_stream1.txt']
samps = []
for z in range(0,10000):
  z = z*.0000005
  samps.append(z)
print len(samps)

fin = open(f,"read")
content = fin.readlines()
a = 0
for line in content:
  wf = line.strip('\n').split()    
  
  wf = map(int, wf)

  mean = sum(wf)/10000

  rms = 0.
  for val in wf:
    rms = rms + float(val - mean)*float(val - mean)
  rms = np.sqrt(rms/10000)
  print "Mean: ", mean, "RMS: ", rms

  plt.plot(samps,wf)
  plt.xlabel('Time')
  plt.ylabel('ADC Count')
  plt.title('FEMB: ' + str(FEMB) + ' Channel: ' + str(a) + ', RMS: ' + '{0:.2f}'.format(rms))
  plt.savefig(outputdir + "wf_outputs/stream_"+str(FEMB) + "_wf_" + str(a)+".png")
  plt.clf()

  fft = np.abs(np.fft.rfft(wf))/10000
  fft = fft[range(1, 5001)]
  fd = np.fft.rfftfreq(10000,.0005)
  fd = fd[1:5001]
  m = max(fft)
  spot = 0
  for val in fft:
    if val == m:
      break
    spot = spot + 1 
  max_pos = fd[spot]
  print len(fd)
  plt.plot(fd,fft)
  plt.xlabel('Freq (kHz)')
  plt.title('FEMB: ' + str(FEMB) + ' Channel: ' + str(a) + ', Peak: ' + '{0:.2f}'.format(max_pos) +" kHz")
  plt.savefig(outputdir + "fft/fft_"+str(FEMB)+"_"+str(a) + ".png")
   #plt.show()
  plt.clf()

  a = a + 1
