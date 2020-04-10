import pygame
import sys


pygame.init()

display_width=900
display_height=600

display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('BBall')
icon = pygame.image.load('images/icon.jpg')

pygame.display.set_icon(icon)
clock=pygame.time.Clock()


class hp_bar:
	def __init__(self,
		x,y, 
		firts_img=pygame.image.load("images/health_bar/Full.jpg"), 
		second_img=pygame.image.load("images/health_bar/075.jpg"), 
		third_img=pygame.image.load("images/health_bar/05.jpg"), 
		fourth_img=pygame.image.load("images/health_bar/025.jpg"), 
		fifth_img=pygame.image.load("images/health_bar/0.jpg"),
		count=4 ):
		self.firts_img=firts_img
		self.second_img=second_img
		self.third_img=third_img
		self.fourth_img=fourth_img
		self.fifth_img=fifth_img
		self.count=count
		self.x=x
		self.y=y

	def draw(self):
		if self.count==4:
			display.blit(self.firts_img,(self.x,self.y))
		if self.count==3:
			display.blit(self.second_img,(self.x,self.y))
		if self.count==2:
			display.blit(self.third_img,(self.x,self.y))
		if self.count==1:
			display.blit(self.fourth_img,(self.x,self.y))
		if self.count==0:
			display.blit(self.fifth_img,(self.x,self.y))					

class hero:
	def __init__(self, x, y, width, height, speed, image, 
		image2, image_isc, image_isc2, image_hand_fight,image_hand_fight_isc,
		check_right, check_pos, press_atack,health_bar, clock_check=5, 
		make_jump=False, jump_counter=20, pos_counter=5, count_atack=0, atack_available=True, check_collision=False):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.speed=speed
		self.make_jump=make_jump
		self.jump_counter=jump_counter
		self.image=image
		self.image2=image2
		self.image_isc=image_isc
		self.check_right=check_right
		self.image_isc2=image_isc2
		self.check_pos=check_pos
		self.pos_counter=pos_counter
		self.image_hand_fight=image_hand_fight
		self.image_hand_fight_isc=image_hand_fight_isc
		self.press_atack=press_atack
		self.clock_check=clock_check
		self.count_atack=count_atack
		self.atack_available=atack_available
		self.check_collision=check_collision
		self.health_bar=health_bar

	def hand_atack(self):
		if self.atack_available:
			self.press_atack=True
			self.atack_available=False


	def atack_couldown(self):
		if self.count_atack==20:
			self.atack_available=True
			self.count_atack=0

		if self.atack_available==False:
			self.count_atack+=1


	def timer_atack(self):
		self.clock_check-=1
		if self.clock_check<=0:
			self.press_atack=False
			self.clock_check=5 


	def move_right(self):
		if self.x>900:
			self.x=0

		self.check_right=True
		if self.check_collision==False:
			self.x+=self.speed
		self.pos_counter-=1
		if self.pos_counter<=0:
			if self.check_pos:
				self.check_pos=False
			else:
				self.check_pos=True
			self.pos_counter=5

	def move_left(self):
		if self.x<0:	
			self.x=display_width

		self.check_right=False
		if self.check_collision==False:
			self.x-=self.speed

		self.pos_counter-=1
		if self.pos_counter<=0:
			if self.check_pos:
				self.check_pos=False
			else:
				self.check_pos=True
			self.pos_counter=5


	def draw(self):
		self.health_bar.draw()
		if self.check_right:
			if self.check_pos:
				if self.press_atack:
					display.blit(self.image_hand_fight,(self.x,self.y))
				else:	
					display.blit(self.image,(self.x,self.y))
			else:
				if self.press_atack:
					display.blit(self.image_hand_fight,(self.x,self.y))
				else:
					display.blit(self.image2,(self.x,self.y))
		else:
			if self.check_pos:
				if self.press_atack:

					display.blit(self.image_hand_fight_isc,(self.x,self.y))

				else:

					display.blit(self.image_isc,(self.x,self.y))
			else:
				if self.press_atack:

					display.blit(self.image_hand_fight_isc,(self.x,self.y))

				else:
					display.blit(self.image_isc2,(self.x,self.y))
						
		  ##pygame.draw.rect(display,(247,240,22),(self.x,self.y,self.width,self.height))

	def jump(self):
		
		if self.jump_counter>=-20:
			self.y+=-self.jump_counter
			self.jump_counter-=1
		else:
			self.jump_counter=20
			self.make_jump=False


		

def run_game():
    global make_jump
   
    game = True

    
    vlad=hero(300,300,60,100,4,
    	image=pygame.image.load('images/vlad/hero_walk1.jpg'),
    	image2=pygame.image.load('images/vlad/hero_walk2.jpg'),
    	image_isc=pygame.image.load('images/vlad/hero_walk_isc1.jpg'),
    	image_isc2=pygame.image.load('images/vlad/hero_walk_isc2.jpg') ,
    	image_hand_fight=pygame.image.load('images/vlad/image_press_atack.jpg'),
    	image_hand_fight_isc=pygame.image.load('images/vlad/image_press_atack_isc.jpg'),
    	health_bar=hp_bar(0,0),
    	check_right=True,check_pos=True,press_atack=False)


    artem=hero(450,300,60,100,4,
    	image=pygame.image.load('images/artem/hero_walk1.jpg'),
    	image2=pygame.image.load('images/artem/hero_walk2.jpg'),
    	image_isc=pygame.image.load('images/artem/hero_walk_isc1.jpg'),
    	image_isc2=pygame.image.load('images/artem/hero_walk_isc2.jpg') ,
    	image_hand_fight=pygame.image.load('images/artem/image_press_atack.jpg'),
    	image_hand_fight_isc=pygame.image.load('images/artem/image_press_atack_isc.jpg'),
    	health_bar=hp_bar(780,0),
    	check_right=False,check_pos=True,press_atack=False)

    ground=pygame.image.load("images/background.jpg")
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()        
        keys = pygame.key.get_pressed()

        if vlad.press_atack==True:
        	vlad.timer_atack()
        vlad.atack_couldown()
        if artem.press_atack==True:

        	artem.timer_atack()
        artem.atack_couldown()

        if keys[pygame.K_w]:
        	vlad.make_jump=True

        if vlad.make_jump:
        	vlad.jump()

        if keys[pygame.K_d]:
        	if artem.x>vlad.x and artem.x-vlad.x<=20:
        		vlad.check_collision=True
        	else:
        		vlad.check_collision=False	
        	vlad.move_right()

        if keys[pygame.K_a]:
        	if artem.x<vlad.x and vlad.x-artem.x<=20:
        		vlad.check_collision=True
        	else:
        		vlad.check_collision=False
        	vlad.move_left()

        if keys[pygame.K_x]:
        	vlad.hand_atack()

        if keys[pygame.K_m]:
        	artem.hand_atack()	

       	if keys[pygame.K_UP]:
        	artem.make_jump=True

        if artem.make_jump:
        	artem.jump()

        if keys[pygame.K_RIGHT]:
        	if vlad.x>artem.x and vlad.x-artem.x<=20:
        		artem.check_collision=True
        	else:
        		artem.check_collision=False		
        	artem.move_right()

        if keys[pygame.K_LEFT]:
        	if vlad.x<artem.x and artem.x-vlad.x<=20:
        		artem.check_collision=True
        	else:
        		artem.check_collision=False		
        	artem.move_left()
        if vlad.check_right and vlad.press_atack and vlad.clock_check==5 and vlad.x<artem.x and artem.x-vlad.x<=80:
        	artem.x+=8
        	artem.health_bar.count-=1
        if vlad.check_right==False and vlad.press_atack and vlad.clock_check==5 and vlad.x>artem.x and vlad.x-artem.x<=60:
        	artem.x-=8
        	artem.health_bar.count-=1	
        if artem.check_right and artem.press_atack and artem.clock_check==5 and artem.x<vlad.x and vlad.x-artem.x<=80:
        	vlad.x+=8
        	vlad.health_bar.count-=1
        if artem.check_right==False and artem.press_atack and artem.clock_check==5 and artem.x>vlad.x and artem.x-vlad.x<=60:
        	vlad.x-=8
        	vlad.health_bar.count-=1	
        	
        display.blit(ground,(0,0))
      
        vlad.draw()
        artem.draw()
        

        pygame.display.update()   
        clock.tick(60)     



run_game()
