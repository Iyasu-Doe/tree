import pygame
import sys
import math
import time

wx = 500
wy = 500
xoffset=90
num_iter = 12
percent_length=2/3
linecolor = (255,255,255)
screencolor = (0,0,0)
length = 190

pygame.init()

screen = pygame.display.set_mode((700,600))

screen.fill(screencolor)


def drawbranch(x1,y1,angle,length,iters):
	
	x2 = math.sin(angle)*length + x1
	y2 = math.cos(angle)*length + y1
	
	pygame.draw.lines(screen,linecolor,False,[(x1+xoffset,y1),(x2+xoffset,y2)])
	pygame.display.update()
	
	if iters<num_iter:
		drawbranch(x2,y2,(angle - angle_change),length*percent_length,iters+1)
		drawbranch(x2,y2,(angle + angle_change),length*percent_length,iters+1)

	
	

#did this math so I don't have to fuck with radians
for a in range(0,360):
	screen.fill((0,0,0))
	#*3 is the multiplier for degrees
	angle_change = (40+a*1)/180*math.pi
	drawbranch(wx/2,0,math.pi*4/2,length,0)
	name = "screenshot"+str(a)+".jpg"
	pygame.image.save(screen,name)

#time.sleep(4000)
