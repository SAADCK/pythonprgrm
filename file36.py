# from javax.swing import JFrame,JLabel,JButton,JTextField
# from java.awt import FlowLayout

# frame = JFrame("Hello")
# frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
# frame.setLocation(100,100)
# frame.setSize(200,200)
# frame.setLayout(FlowLayout())

# label=JLabel("Welcom to Jython Swing")
# txt=JTextField(30)
# btn=JButton("ok")

# frame.add(label)
# frame.add(txt)
# frame.add(btn)
# frame.setVisible(True)


from javax.swing import JFrame,JButton
from java.awt import GridLayout
frame = JFrame("Hello")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(400,400)
frame.setLayout(GridLayout(4,4))
k=0
for i in range(1,5):
          for j in range (1,5):
                    k=k+1
                    frame.add(JButton(str(k)))
frame.setVisible(True)