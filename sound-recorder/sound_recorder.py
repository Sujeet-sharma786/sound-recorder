import datetime
import sounddevice
import shutil
from scipy.io.wavfile import write
now = datetime.datetime.now()

fs=44100 #sample_rate
# second=int(input("Enter the time duration in second: ")) #enter your required time..
print("Recording for 30 sec....\n")
record_voice=sounddevice.rec(int(30 * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
filename = now.strftime("%Y%m%d_%H%M%S") + ".wav"
source = "out.wav"
shutil.copyfile(source,filename)
print("Finished...\nPlease Check it...") 
