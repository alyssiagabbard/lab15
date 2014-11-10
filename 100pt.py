#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
tx1,ty1,tx2,ty2 = drawpad.coords(target)
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=0)
		self.up.bind("<Button-1>", self.moveUp)
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Down", background="red")
		self.button2.grid(row=0,column=1)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Right", background="purple")
		self.button3.grid(row=0,column=2)
		self.button3.bind("<Button-1>", self.button3Click)
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Left", background="yellow")
		self.button4.grid(row=0,column=3)
		self.button4.bind("<Button-1>", self.button4Click)											
                

		drawpad.pack()
		self.animate()
		
		
	def moveUp(self, event):   
		global player
		global drawpad
		global tx1,ty1,tx2,ty2
                drawpad.move(player,0,-20)
               
                
        def button2Click(self,event):
            global player
            global tx1,ty1,tx2,ty2
            drawpad.move(player,0,20)
           
            
        def button3Click(self,event):
            global player
            global tx1,ty1,tx2,ty2
            drawpad.move(player,20,0)
        
            
        def button4Click(self,event):
            global player
            global tx1,ty1,tx2,ty2
            drawpad.move(player,-20,0)
  
	def animate(self):
	    global target
	    global direction
	    global player
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)   
	    drawpad.move(target,direction,0)
	    if tx2>drawpad.winfo_width():
	        direction = -4
	    if tx1<0:
	        direction = 4
            didWeHit = self.collisionDetect() 
            if didWeHit == True:
                drawpad.move(target,0,0)
                drawpad.itemconfig(target, fill="red")
            else:
                drawpad.itemconfig(target, fill="blue")
                drawpad.after(10,self.animate)
                

                                
	def collisionDetect(self):
                global target
		global drawpad
                global player
                tx1,ty1,tx2,ty2 = drawpad.coords(target) 
                px1,py1,px2,py2 = drawpad.coords(player)
                if px1>=tx1 and px2<=tx2 and py1>ty1 and py2<ty2:
                        return True
                else:
                    return False     
		
myapp = MyApp(root)

root.mainloop()