# from java.awt import Dimension
# from javax.swing import JButton,JFrame,JPanel,BoxLayout,Box

# frame = JFrame()
# frame.setTitle("button")
# frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
# frame.setSize(300,150)

# panel = JPanel()
# panel.setLayout(BoxLayout(panel,BoxLayout.Y_AXIS))
# frame.add(panel)

# top =JPanel()
# top.setLayout(BoxLayout(top,BoxLayout.X_AXIS))
# b1=JButton("OK")
# b2=JButton("CLOSE")
# top.add(Box.createVerticalGlue())
# top.add(b1)
# top.add(Box.createRigidArea(Dimension(25,0)))
# top.add(b2)


# bottom =JPanel()
# bottom.setLayout(BoxLayout(bottom,BoxLayout.X_AXIS))
# b3=JButton("OPEN")
# b4=JButton("SAVE")
# bottom.add(Box.createVerticalGlue())
# bottom.add(b3)
# bottom.add(Box.createRigidArea(Dimension(25,0)))
# bottom.add(b4)


# panel.add(top)
# panel.add(bottom)

# frame.setVisible(True)

from javax.swing import JButton,JFrame,JPanel,GroupLayout
frame = JFrame()
panel = JPanel()
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
layout=GroupLayout(panel)
panel.setLayout(layout)
buttonD=JButton("D")
buttonR=JButton("R")
buttonY=JButton("Y")
buttonO=JButton("O")
buttonT=JButton("T")
leftToRight=layout.createSequentialGroup()
leftToRight.addComponent(buttonD)
columnMiddle=layout.createParallelGroup()
columnMiddle.addComponent(buttonR)
columnMiddle.addComponent(buttonO)
columnMiddle.addComponent(buttonT)
leftToRight.addGroup(columnMiddle)
leftToRight.addComponent(buttonY)

topToBottom=layout.createSequentialGroup()
rowTop=layout.createParallelGroup()
rowTop.addComponent(buttonD)
rowTop.addComponent(buttonR)
rowTop.addComponent(buttonY)
topToBottom.addGroup(rowTop)
topToBottom.addComponent(buttonO)
topToBottom.addComponent(buttonT)

layout.setHorizontalGroup(leftToRight)
layout.setV










erticalGroup(topToBottom)

frame.add(panel)
frame.pack()
frame.setVisible(True)