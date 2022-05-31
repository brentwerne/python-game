import pygame
import sys
import random
pygame.init()


def set_level(score, enemy_speed):
	enemy_speed = (score / 20 + 3)  / reducer
	return enemy_speed

def drop_enemies(enemy_list, score):
	delay = random.random()
	if len(enemy_list) < score/10 + 5 and delay < 0.1:
		x_pos = random.randint(0, width- enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, blue, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def draw_balls(shooting_balls):
	for i in range(len(shooting_balls)):
		pygame.draw.circle(screen, blue, (int(shooting_balls[i][0]), int(shooting_balls[i][1])), ball_length)

def detect_collision(player_pos,  enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x <= (p_x +player_size)) or ((e_x + enemy_size) >= p_x and (e_x +enemy_size <= (p_x + player_size))):
		if (e_y >= p_y and e_y <= (p_y + player_size)) or ((e_y + enemy_size )>= p_y and (e_y + enemy_size )<= (p_y + player_size)):
			enemy_pos[1] = height * 2
			return True

	return False


def update_enemy_positions(enemy_list, score, enemy_speed):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < height:
			enemy_pos[1] += enemy_speed
		else: 
			enemy_list.pop(idx)
			score += 1

	return score		

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(player_pos, enemy_pos) :
			return True	
	return False



def power_up_drop(power_up_pos, enemy_speed):
	if power_up_pos[1] >= 0 and power_up_pos[1] < height:
		power_up_pos[1] += enemy_speed
	elif power_up_pos[1] >= 600:
		power_up_pos[1] = 0
		return False
	return True
			

def power_up_collision(power_up_pos, player_pos, enemy_list, power_up):  #give power up a function // yellow square
	if((power_up_pos[0] >= player_pos[0] and power_up_pos[0] <= player_pos[0] + player_size) or (power_up_pos[0] + player_size >= player_pos[0] and power_up_pos[0] + player_size<= player_pos[0] + player_size)):
		if((power_up_pos[1] >= player_pos[1] and power_up_pos[1] <= player_pos[1] + player_size) or (power_up_pos[1] + player_size >= player_pos[1] and power_up_pos[1] + player_size<= player_pos[1] + player_size)):
			for enemy_pos in enemy_list:
				enemy_pos[1] = height + 100
			power_up_pos[1] = height *2

def power_up_shooting(power_up_pos, player_pos):  #give power up a function // orange square
	if((power_up_pos[0] >= player_pos[0] and power_up_pos[0] <= player_pos[0] + player_size) or (power_up_pos[0] + player_size >= player_pos[0] and power_up_pos[0] + player_size<= player_pos[0] + player_size)):
		if((power_up_pos[1] >= player_pos[1] and power_up_pos[1] <= player_pos[1] + player_size) or (power_up_pos[1] + player_size >= player_pos[1] and power_up_pos[1] + player_size<= player_pos[1] + player_size)):
			return True

def in_shooting(power_up_pos, player_pos, enemy_list, shooting_balls, shooter_counter):		
	if (shooter_counter % 6 == 0):
		left_ball = [player_pos[0], player_pos[1]]
		right_ball = [player_pos[0]+50, player_pos[1]]
		shooting_balls.append(left_ball)
		shooting_balls.append(right_ball)

def shooting(power_up_pos, player_pos, enemy_list, shooting_balls):
	if(len(shooting_balls) > 1):
		for m in range(len(shooting_balls)):
			if(m > len(shooting_balls)):
				if(shooting_balls[m][1] < 0 or shooting_balls[m][1] > 600):
					shooting_balls.remove(shooting_balls[m])

	for i in range(len(shooting_balls)):
		shooting_balls[i][1] = shooting_balls[i][1]- 25
	for j in range(len(shooting_balls)):
		for k in range(len(enemy_list)):
			if((shooting_balls[j][0] >= enemy_list[k][0] and shooting_balls[j][0] <= enemy_list[k][0] + player_size) or (shooting_balls[j][0]+ ball_length >= enemy_list[k][0] and shooting_balls[j][0] + ball_length <= enemy_list[k][0]+enemy_size)):
				if((shooting_balls[j][1] >= enemy_list[k][1] and shooting_balls[j][1] <= enemy_list[k][1] + enemy_size) or (shooting_balls[j][1]+ ball_length >= enemy_list[k][1] and shooting_balls[j][1] + ball_length <= enemy_list[k][1]+enemy_size)):
					enemy_list[k][1] = height + 100


width = 800
height = 600

screen = pygame.display.set_mode((width, height))

myFont = pygame.font.SysFont("monospace", 35)

black = (0,0,0)
orange = (255,165,0)
game_over = False
player_size = 50
red = (255,0,0)
blue = (0, 0, 255)
background = (40,238,207)
player_pos = [width/2, height-2*player_size]
enemy_size = 50
enemy_pos = [random.randint(0,width-enemy_size), 0]
clock = pygame.time.Clock()
enemy_speed = 3
enemy_list = [enemy_pos]
score = 0 
yellow = (255, 255, 0)
min_speed = 5
power_up_pos = [random.randint(0, width-enemy_size), 0]
green = (0,255, 0)
pink = (255,182,193)
reducer = 1
reduction = False
reducer_pos = [random.randint(0,width-enemy_size), 0]
r_multiply = False
extra_life_pos = [random.randint(0, width-enemy_size), 0]
shooting_pos = [random.randint(0, width-enemy_size), 0]
extra_life = 0
power_up = False
add_life = False
pink_block = False
orange_block = False
ball_length = 5

left_ball = [player_pos[0], player_pos[1]*-2]
right_ball = [player_pos[0]+50, player_pos[1]*-2]

shooting_balls = [left_ball, right_ball]

s = False
num = 0

while not game_over:
	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_pos[0] -= 50
			elif event.key == pygame.K_RIGHT:	
				player_pos[0] += 50
			
 			
	


	
	score = update_enemy_positions(enemy_list, score, enemy_speed)
	text = "Score: " + str(score)
	label = myFont.render(text, 1, black)
	if player_pos[0] >= width:
		player_pos[0] -= width 
	if player_pos[0] <= -25:
		player_pos[0] += width 
	

	screen.fill(background)
	

	if score % 50 == 43:
		pygame.draw.rect(screen, orange_block, (shooting_pos[0], shooting_pos[1], enemy_size, enemy_size))
		orange_block = True

	if orange_block:
		pygame.draw.rect(screen, orange, (shooting_pos[0], shooting_pos[1], enemy_size, enemy_size))
		orange_block = power_up_drop(shooting_pos, min_speed)

	if score % 149 == 78:
		pygame.draw.rect(screen, green, (reducer_pos[0], reducer_pos[1], enemy_size, enemy_size))
		reduction = True

	if r_multiply:
		reducer = reducer *1.2


	if score % 77== 5:
		pygame.draw.rect(screen, pink, (extra_life_pos[0], extra_life_pos[1], enemy_size, enemy_size))
		pink_block = True

	if pink_block:
		pygame.draw.rect(screen, pink, (extra_life_pos[0], extra_life_pos[1], enemy_size, enemy_size))
		pink_block = power_up_drop(extra_life_pos, min_speed)
	
	
	if reduction:
		pygame.draw.rect(screen, green, (reducer_pos[0], reducer_pos[1], enemy_size, enemy_size))
		reduction = power_up_drop(reducer_pos, min_speed)

	add_life = detect_collision(player_pos,  extra_life_pos)
	shoot = detect_collision(player_pos, shooting_pos)
	r_multiply =  detect_collision(player_pos,  reducer_pos)

	if shoot:
		s = True
		shooter_counter = 0


	if s:
		if(num < 360):
			in_shooting(power_up_pos, player_pos, enemy_list, shooting_balls, shooter_counter)
			num = num +	1
			shooter_counter += 1
		else:
			num = 0
			shooter_counter = 0
			s = False

	shooting(power_up_pos, player_pos, enemy_list, shooting_balls)

	if add_life and extra_life < 3:
		extra_life += 1
		add_life = False

	game_over = collision_check(enemy_list, player_pos)
	power_up_collision(power_up_pos, player_pos, enemy_list, power_up)
	if(game_over == True) and extra_life >= 1:
		game_over = False
		extra_life -= 1


	
		
	if((score % 51) == 50):
		pygame.draw.rect(screen, yellow,(power_up_pos[0] ,power_up_pos[1] , enemy_size, enemy_size))
		power_up = True
	
	if power_up == True:
		pygame.draw.rect(screen, yellow,(power_up_pos[0] ,power_up_pos[1] , enemy_size, enemy_size))
		power_up = power_up_drop(power_up_pos, min_speed)

	
	life_info = "Extra Lives = " + str(extra_life)
	label_2 = myFont.render(life_info, 1, black)
	screen.blit(label_2, (50, height -50))
	screen.blit(label, (width-300, height-50))
	enemy_speed = set_level(score, enemy_speed)
	drop_enemies(enemy_list, score)
	draw_enemies(enemy_list)
	draw_balls(shooting_balls)

	pygame.draw.rect(screen, red,(player_pos[0], player_pos[1], player_size, player_size ) )
	pygame.display.update()
	clock.tick(30)



print(f"Score: {score}")
if score > 40:
	print("good job")

