import pygame
import sys
import math
import time
#just a warning, this was a quick project so there is a lot of poor programming so everything looks right. 

#for some reason I had a hard time getting the fractal aligned right, so it believes that the window is 500 by 900
wx = 500
wy = 500

#moves the fractal left 90 pixels
xoffset=90
#how many branches down to go. 
num_iter = 12
#how long to set each branch relative to parent. 
percent_length=2/3

linecolor = (255,255,255)
screencolor = (0,0,0)
#starting branch length. 
length = 190

#setting the pygame window up. 
pygame.init()
screen = pygame.display.set_mode((700,600))
screen.fill(screencolor)

#this function is the recursive function to draw each branch. It calls itself twice each iteration. 
#the x1 and y1 are coordinates of the parent branches end point. 
def drawbranch(x1,y1,angle,length,iters):
	
	#finds the child branches end point 
	x2 = math.sin(angle)*length + x1
	y2 = math.cos(angle)*length + y1
	
	pygame.draw.lines(screen,linecolor,False,[(x1+xoffset,y1),(x2+xoffset,y2)])
	pygame.display.update()
	
	#this if statement stops it from drawing branches infinitely. 
	if iters<num_iter:
		#there are interesting possibilities in changing how much the iters go up. 
		#adding less than 1 would result in a unbalanced tree
		drawbranch(x2,y2,(angle - angle_change),length*percent_length,iters+1)
		drawbranch(x2,y2,(angle + angle_change),length*percent_length,iters+1)

	
	

#did this math so I don't have to fuck with radians
for a in range(0,360):
	screen.fill((0,0,0))
	
	#the 40 is so that it's angled right for the first branch. The 1 is the how many degrees to change the branches each frame. 
	angle_change = (40+a*1)/180*math.pi
	drawbranch(wx/2,0,math.pi*4/2,length,0)
	#after everything is drawn, save the file by screenshotting the window. 
	name = "screenshot"+str(a)+".jpg"
	pygame.image.save(screen,name)

#time.sleep(4000)
