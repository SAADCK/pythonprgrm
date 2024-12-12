from gtts import gTTS
import os 
mytext=open('demo.txt','r').read()
myjobj=gTTS(text=mytext,lang='en',slow=False)
myjobj.save("myfile.mp3")
os.system('start myfile.mp3')


# from gtts import gTTS
# import os 
# mytext=open('demo.txt','r').read()
# myobj=gTTS(text=mytext,lang='en',slow=False)
# myobj.save("myfile.mp4")
# os.system('start mylife.mp4')
