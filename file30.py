from tkinter import*
root=Tk()
from gtts import gTTS
import os
def texttospech():
          text=mytext.get()
          myobj=gTTS(text=text,lang='en',slow=False)
          myobj.save("myaudio.mp3")
          os.system('start myaudio.mp3')
          
canvas=Canvas(root,height=200,width=400)
canvas.pack()
mytext=Entry(root)
canvas.create_window(200,100,window=mytext)
convert=Button(text="Covert",command=texttospech)
canvas.create_window(200,150,window=convert)
root.mainloop()

          
