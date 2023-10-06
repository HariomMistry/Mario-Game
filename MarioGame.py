import SimpleGUICS2Pygame.simpleguics2pygame  as simplegui
height=500
width=700
baseh=410
enemy_pos=[350,410]
position=[350,baseh]
enemy_vel=2
velocity=[0,1]
acc=4.5
image1='p1.png'
image2='p3.png'
stage_x=100
stage_y=120.5
stage_position=[stage_x,stage_y]
stage_image=simplegui._load_local_image('stage1.png')
mario_image=simplegui._load_local_image(image1)
enemy_image=simplegui._load_local_image('e1.png')
win_image=simplegui._load_local_image('win.png')
die_image=simplegui._load_local_image('died.png')
start_image=simplegui._load_local_image('start.png')
w2=enemy_image.get_width()
h2=enemy_image.get_height()
w=mario_image.get_width()
h=mario_image.get_height()
stop=False
die=False
sacc=1.5
oacc=4.5
gt=False
animate1=False
animate2=False
PLAYER_SIZE=20
ENEMY_SIZE=10
gametime=65
start=False
obstacle_pos1 = [600, 360]
obstacle_size1 = [100, 70]

obstacle_pos2 = [600, 330]
obstacle_size2 = [103, 100]

obstacle_pos3 = [600, 302]
obstacle_size3 = [100, 125]

obstacle_pos4 = [600, 302]
obstacle_size4 = [100, 125]

obstacle_pos5 = [600, 360]
obstacle_size5 = [100, 70]

obstacle_pos6 = [600, 360]
obstacle_size6 = [100, 70]

obstacle_pos7 = [600, 420]
obstacle_size7 = [110, 70]

obstacle_pos8 = [600, 420]
obstacle_size8 = [175, 70]

obstacle_pos9 = [600, 420]
obstacle_size9 = [110, 70]

obstacle_pos10 = [600, 150]
obstacle_size10 = [10, 300]

enemy_pos1 = [700, 410]
enemy_size1 = [20, 110]

enemy_pos2 = [700, 410]
enemy_size2 = [20, 110]

enemy_pos3 = [700, 410]
enemy_size3 = [20, 110]
eacc=3.5
win=False
def reset():
    global height,start,gt,die,die_image,gametime,start_image,width,baseh,eacc,position,win,PLAYER_SIZE,ENEMY_SIZE,w2,h2,velocity,acc,image1,image1,stage_x,stage_y,stage_position,stage_image,mario_image,w,h,stop,sacc,oacc,animate1,animate2,obstacle_pos1,obstacle_pos2,obstacle_pos3,obstacle_pos4,obstacle_pos5,obstacle_pos6,obstacle_pos7,obstacle_pos8,obstacle_pos9,obstacle_pos10,enemy_pos1,enemy_pos2,enemy_pos3,obstacle_size1,obstacle_size2,obstacle_size3,obstacle_size4,obstacle_size5,obstacle_size6,obstacle_size7,obstacle_size8,obstacle_size9,obstacle_size10,enemy_size1,enemy_size2,enemy_size3
    height=500
    die=False
    start=False
    win=False
    width=700
    baseh=410
    position=[350,baseh]
    velocity=[0,1]
    acc=4.5
    gt=False
    gametime=65
    image1='p1.png'
    image2='p3.png'
    stage_x=100
    stage_y=120.5
    stage_position=[stage_x,stage_y]
    start_image=simplegui._load_local_image('start.png')
    die_image=simplegui._load_local_image('died.png')
    stage_image=simplegui._load_local_image('stage1.png')
    mario_image=simplegui._load_local_image(image1)
    enemy_image=simplegui._load_local_image('e1.png')
    win_image=simplegui._load_local_image('win.png')
    w2=enemy_image.get_width()
    h2=enemy_image.get_height()
    w=mario_image.get_width()
    h=mario_image.get_height()
    stop=False
    sacc=1.5
    oacc=4.5
    eacc=3.5
    animate1=False
    animate2=False
    PLAYER_SIZE=20
    ENEMY_SIZE=10
    obstacle_pos1 = [600, 360]
    obstacle_size1 = [100, 70]

    obstacle_pos2 = [600, 330]
    obstacle_size2 = [103, 100]

    obstacle_pos3 = [600, 302]
    obstacle_size3 = [100, 125]

    obstacle_pos4 = [600, 302]
    obstacle_size4 = [100, 125]

    obstacle_pos5 = [600, 360]
    obstacle_size5 = [100, 70]

    obstacle_pos6 = [600, 360]
    obstacle_size6 = [100, 70]
    
    obstacle_pos7 = [600, 420]
    obstacle_size7 = [110, 70]

    obstacle_pos8 = [600, 420]
    obstacle_size8 = [175, 70]
    
    obstacle_pos9 = [600, 420]
    obstacle_size9 = [110, 70]

    obstacle_pos10 = [600, 150]
    obstacle_size10 = [10, 300]
    
    enemy_pos1 = [700, 410]
    enemy_size1 = [100, 70]

    enemy_pos2 = [700, 410]
    enemy_size2 = [100, 70]

    enemy_pos3 = [700, 410]
    enemy_size3 = [100, 70]
    
def timer_handler1():
    global image1,mario_image
    if image1=='p1.png':
        image1='p2.png'
    else:
        image1='p1.png'
    mario_image=simplegui._load_local_image(image1)
def timer_handler2():
    global image2,mario_image
    if image2=='p3.png':
        image2='p4.png'
    else:
        image2='p3.png'
    mario_image=simplegui._load_local_image(image2)
def keydown(key):
    global acc,oacc,start,velocity,animate2,image1,image2,stage_x,stop,animate1
    if key==simplegui.KEY_MAP['up']:
        velocity[1]-=acc+2 
    if key==simplegui.KEY_MAP['left']:
        velocity[0]-=acc
        oacc=4.5
        animate2=not animate2
    if key==simplegui.KEY_MAP['right']:
        velocity[0]+=acc
        oacc=4.5
        stop=False
        animate1=not animate1
    if animate1:
        timer1.start()
    if animate2:
        timer2.start()
    if key==simplegui.KEY_MAP['r']:
        reset()
    if key==simplegui.KEY_MAP['s']:
        start=True
def keyup(key):
    global image,oacc,stage_x,stage_y,velocity,stop,animate1,animate2
    stop = True
    if key==simplegui.KEY_MAP['left']:
        velocity[0]=0
        oacc=0
        animate2=False
        timer2.stop()
    if key==simplegui.KEY_MAP['right']:
        velocity[0]=0
        oacc=0
        animate1=False
        timer1.stop()
    if key==simplegui.KEY_MAP['up']:
        oacc=0
def game_timer():
    global gametime
    gametime=gametime-1
def draw_handler(canvas):
    global stage_position,gametime,die,oacc,sacc,stage_x,gt,baseh,velocity,enemy_vel,win,start
    canvas.draw_image(start_image,(start_image.get_width()//2,start_image.get_height()//2),(start_image.get_width(),start_image.get_height()),(350,250),(700,500))
    canvas.draw_text('Press s to start the game',(203,350),30, "White")
    if start:
        timer3.start()
        if win==False and die==False and gt==False:
            position[1]+=velocity[1]
            position[0]+=velocity[0]
            if position[1]<=200:
                velocity[1]=-velocity[1]
            if position[1]>=410:
                velocity[1]=0
            if position[0]>=500:
                if not stop:
                    stage_position[0]+=sacc
            if position[0]>=550:
                if not stop:
                    velocity[0]=0
            if position[0]<=1:
                velocity[0]=0
            if gametime<=0:
                gt=True
                timer3.stop()
            canvas.draw_image(stage_image,stage_position,(200,240),(350,250),(700,500))
            canvas.draw_image(mario_image,(w/2,h/2),(w,h),position,(40,40))
            canvas.draw_text('Time left:'+str(gametime),(580, 40),20, "black")
            if stage_position[0]>375:
                canvas.draw_polygon([(obstacle_pos1[0], obstacle_pos1[1]),
                                 (obstacle_pos1[0] + obstacle_size1[0], obstacle_pos1[1]),
                                 (obstacle_pos1[0] + obstacle_size1[0], obstacle_pos1[1] + obstacle_size1[1]),
                                 (obstacle_pos1[0], obstacle_pos1[1] + obstacle_size1[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)")
                if (position[0] + PLAYER_SIZE > obstacle_pos1[0] and
                    position[0] < obstacle_pos1[0] + obstacle_size1[0] and
                    position[1] + PLAYER_SIZE > obstacle_pos1[1] and
                    position[1] < obstacle_pos1[1] + obstacle_size1[1]):
                    velocity[0] = 0
                    velocity[1] = 0
                    position[1] = obstacle_pos1[1] - PLAYER_SIZE
                if position[0]>=520:
                    obstacle_pos1[0] -= oacc
            if stage_position[0]>=535:
                    canvas.draw_polygon([(obstacle_pos2[0], obstacle_pos2[1]),
                                 (obstacle_pos2[0] + obstacle_size2[0], obstacle_pos2[1]),
                                 (obstacle_pos2[0] + obstacle_size2[0], obstacle_pos2[1] + obstacle_size2[1]),
                                 (obstacle_pos2[0], obstacle_pos2[1] + obstacle_size2[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos2[0] and
                        position[0] < obstacle_pos2[0] + obstacle_size2[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos2[1] and
                        position[1] < obstacle_pos2[1] + obstacle_size2[1]):
                        velocity[0] = 0
                        velocity[1] = 0
                        position[1] = obstacle_pos2[1] - PLAYER_SIZE
                    if position[0]>=520:
                        obstacle_pos2[0] -= oacc
            if stage_position[0]>=665:
                    canvas.draw_polygon([(obstacle_pos3[0], obstacle_pos3[1]),
                                 (obstacle_pos3[0] + obstacle_size3[0], obstacle_pos3[1]),
                                 (obstacle_pos3[0] + obstacle_size3[0], obstacle_pos3[1] + obstacle_size3[1]),
                                 (obstacle_pos3[0], obstacle_pos3[1] + obstacle_size3[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos3[0] and
                        position[0] < obstacle_pos3[0] + obstacle_size3[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos3[1] and
                        position[1] < obstacle_pos3[1] + obstacle_size3[1]):
                        velocity[0] = 0
                        velocity[1] = 0
                        position[1] = obstacle_pos3[1] - PLAYER_SIZE
                    if position[0]>=520:
                        obstacle_pos3[0] -= oacc
            if stage_position[0]>=840:
                    canvas.draw_polygon([(obstacle_pos4[0], obstacle_pos4[1]),
                                 (obstacle_pos4[0] + obstacle_size4[0], obstacle_pos4[1]),
                                 (obstacle_pos4[0] + obstacle_size4[0], obstacle_pos4[1] + obstacle_size4[1]),
                                 (obstacle_pos4[0], obstacle_pos4[1] + obstacle_size4[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos4[0] and
                        position[0] < obstacle_pos4[0] + obstacle_size4[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos4[1] and
                        position[1] < obstacle_pos4[1] + obstacle_size4[1]):
                        velocity[0] = 0
                        velocity[1] = 0
                        position[1] = obstacle_pos4[1] - PLAYER_SIZE
                    if position[0]>=520:
                        obstacle_pos4[0] -= oacc
            if stage_position[0]>=1030:
                    canvas.draw_polygon([(obstacle_pos7[0], obstacle_pos7[1]),
                                 (obstacle_pos7[0] + obstacle_size7[0], obstacle_pos7[1]),
                                 (obstacle_pos7[0] + obstacle_size7[0], obstacle_pos7[1] + obstacle_size7[1]),
                                 (obstacle_pos7[0], obstacle_pos7[1] + obstacle_size7[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos7[0] and
                        position[0] < obstacle_pos7[0] + obstacle_size7[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos7[1] and
                        position[1] < obstacle_pos7[1] + obstacle_size7[1]):
                        die=True
                        timer3.stop()
                    if position[0]>=520:
                        obstacle_pos7[0] -= oacc
            if stage_position[0]>1105:
                canvas.draw_image(enemy_image,(w2/2,h2/2),(w2,h2),enemy_pos2,(40,40))
                if (position[0] + ENEMY_SIZE > enemy_pos2[0] and
                    position[0] < enemy_pos2[0] + enemy_size2[0] and
                    position[1] + ENEMY_SIZE > enemy_pos2[1] and
                    position[1] < enemy_pos2[1] + enemy_size2[1]):
                    die=True
                    timer3.stop()
                if position[0]>=520:
                    enemy_pos2[0] -= eacc
            if stage_position[0]>=1300:
                    canvas.draw_polygon([(obstacle_pos8[0], obstacle_pos8[1]),
                                 (obstacle_pos8[0] + obstacle_size8[0], obstacle_pos8[1]),
                                 (obstacle_pos8[0] + obstacle_size8[0], obstacle_pos8[1] + obstacle_size8[1]),
                                 (obstacle_pos8[0], obstacle_pos8[1] + obstacle_size8[1])], 2,  "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos8[0] and
                        position[0] < obstacle_pos8[0] + obstacle_size8[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos8[1] and
                        position[1] < obstacle_pos8[1] + obstacle_size8[1]):
                        timer3.stop()
                        die=True
                    if position[0]>=520:
                        obstacle_pos8[0] -= oacc    
            if stage_position[0]>1475:
                canvas.draw_image(enemy_image,(w2/2,h2/2),(w2,h2),enemy_pos1,(40,40))
                if (position[0] + ENEMY_SIZE > enemy_pos1[0] and
                    position[0] < enemy_pos1[0] + enemy_size1[0] and
                    position[1] + ENEMY_SIZE > enemy_pos1[1] and
                    position[1] < enemy_pos1[1] + enemy_size1[1]):
                    timer3.stop()
                    die=True
                if position[0]>=520:
                    enemy_pos1[0] -= eacc
            if stage_position[0]>2005:
                canvas.draw_image(enemy_image,(w2/2,h2/2),(w2,h2),enemy_pos3,(40,40))
                if (position[0] + ENEMY_SIZE > enemy_pos3[0] and
                    position[0] < enemy_pos3[0] + enemy_size3[0] and
                    position[1] + ENEMY_SIZE > enemy_pos3[1] and
                    position[1] < enemy_pos3[1] + enemy_size3[1]):
                    timer3.stop()
                    die=True
                if position[0]>=520:
                    enemy_pos3[0] -= eacc
            if stage_position[0]>=2375:
                    canvas.draw_polygon([(obstacle_pos9[0], obstacle_pos9[1]),
                                 (obstacle_pos9[0] + obstacle_size9[0], obstacle_pos9[1]),
                                 (obstacle_pos9[0] + obstacle_size9[0], obstacle_pos9[1] + obstacle_size9[1]),
                                 (obstacle_pos9[0], obstacle_pos9[1] + obstacle_size9[1])], 2,  "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos9[0] and
                        position[0] < obstacle_pos9[0] + obstacle_size9[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos9[1] and
                        position[1] < obstacle_pos9[1] + obstacle_size9[1]):
                        timer3.stop()
                        die=True
                    if position[0]>=520:
                        obstacle_pos9[0] -= oacc 
            if stage_position[0]>=2538:
                    canvas.draw_polygon([(obstacle_pos5[0], obstacle_pos5[1]),
                                 (obstacle_pos5[0] + obstacle_size5[0], obstacle_pos5[1]),
                                 (obstacle_pos5[0] + obstacle_size5[0], obstacle_pos5[1] + obstacle_size5[1]),
                                 (obstacle_pos5[0], obstacle_pos5[1] + obstacle_size5[1])], 2,  "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos5[0] and
                        position[0] < obstacle_pos5[0] + obstacle_size5[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos5[1] and
                        position[1] < obstacle_pos5[1] + obstacle_size5[1]):
                        velocity[0] = 0
                        velocity[1] = 0
                        position[1] = obstacle_pos5[1] - PLAYER_SIZE
                    if position[0]>=520:
                        obstacle_pos5[0] -= oacc
            if stage_position[0]>=2790:
                    canvas.draw_polygon([(obstacle_pos6[0], obstacle_pos6[1]),
                                 (obstacle_pos6[0] + obstacle_size6[0], obstacle_pos6[1]),
                                 (obstacle_pos6[0] + obstacle_size6[0], obstacle_pos6[1] + obstacle_size6[1]),
                                 (obstacle_pos6[0], obstacle_pos6[1] + obstacle_size6[1])], 2, "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos6[0] and
                        position[0] < obstacle_pos6[0] + obstacle_size6[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos6[1] and
                        position[1] < obstacle_pos6[1] + obstacle_size6[1]):
                        velocity[0] = 0
                        velocity[1] = 0
                        position[1] = obstacle_pos6[1] - PLAYER_SIZE
                    if position[0]>=520:
                        obstacle_pos6[0] -= oacc
            if stage_position[0]>=3100:
                    canvas.draw_polygon([(obstacle_pos10[0], obstacle_pos10[1]),
                                 (obstacle_pos10[0] + obstacle_size10[0], obstacle_pos10[1]),
                                 (obstacle_pos10[0] + obstacle_size10[0], obstacle_pos10[1] + obstacle_size10[1]),
                                 (obstacle_pos10[0], obstacle_pos10[1] + obstacle_size10[1])], 2,  "rgba(0, 255, 0, 0.0)", "rgba(0, 255, 0, 0.0)") 
                    if (position[0] + PLAYER_SIZE > obstacle_pos10[0] and
                        position[0] < obstacle_pos10[0] + obstacle_size10[0] and
                        position[1] + PLAYER_SIZE > obstacle_pos10[1] and
                        position[1] < obstacle_pos10[1] + obstacle_size10[1]):
                        win=True
                        timer3.stop()
                    if position[0]>=520:
                        obstacle_pos10[0] -= oacc  
        elif win:
            canvas.draw_image(win_image,(win_image.get_width()//2,win_image.get_height()//2),(win_image.get_width(),win_image.get_height()),(350,250),(700,500))
            canvas.draw_text("Press r to restart the game", (230, 150),20, "White")
            timer3.stop()
        elif die:
            canvas.draw_image(die_image,(die_image.get_width()//2,die_image.get_height()//2),(die_image.get_width(),die_image.get_height()),(350,250),(700,500))
            canvas.draw_text("YOU DIED", (295, 295),20, "White")
            canvas.draw_text("Press r to restart the game", (230, 340),24, "White")
        else:
            canvas.draw_image(die_image,(die_image.get_width()//2,die_image.get_height()//2),(die_image.get_width(),die_image.get_height()),(350,250),(700,500))
            canvas.draw_text("TIMES UP!", (295, 295),20, "White")
            canvas.draw_text("Press r to restart the game", (230, 340),24, "White")
frame=simplegui.create_frame('Mario',width,height)
frame.set_draw_handler(draw_handler)
timer1=simplegui.create_timer(150,timer_handler1)
timer2=simplegui.create_timer(150,timer_handler2)
timer3=simplegui.create_timer(1000,game_timer)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()

