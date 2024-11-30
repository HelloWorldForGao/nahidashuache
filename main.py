import pgzrun
import random as r
from tkinter import messagebox
WIDTH = 801
HEIGHT = 639

lingche = Actor("lingche2.png",(400,550))
all_huapin = []
all_flower = []
all_pailie = [[1,1,1],[1,2,1],[2,1,2],[0,1,0],[1,2,0]]
counter = 0
counter_update_time = 25
speed = 75 / counter_update_time
live = 4
max_live = 4
score = 0

def update_speed():
    global counter_update_time,speed
    speed = 75 / counter_update_time
def spawn_huapin(a):
    global all_huapin
    #a = r.choice([0,1,2])
    if a == 0:
        all_huapin.append(Actor("huapin",(300,0)))
    elif a == 1:
        all_huapin.append(Actor("huapin",(400,0)))
    else:
        all_huapin.append(Actor("huapin",(500,0)))
def spawn_flower(a):
    global all_flower
    #a = r.choice([0,1,2])
    if a == 0:
        all_flower.append(Actor("flower",(300,0)))
    elif a == 1:
        all_flower.append(Actor("flower",(400,0)))
    else:
        all_flower.append(Actor("flower",(500,0)))
def spawn_one(thing,where):
    if thing == 1:
        if r.choice([0,1]) == 0:
            #print("spawned " + "flower" + " " + str(where))
            spawn_flower(where)
    elif thing == 2:
        if r.choice([0,1,2]) == 0:
            #print("spawned " + "huapin" + " " + str(where))
            spawn_huapin(where)
    else:
        pass
def spawn():
    a = r.choice(all_pailie)
    for i in range(len(a)):
        #print("spawned " + str(a[i]) + " " + str(i))
        spawn_one(a[i],i)
def zuoyouqiehuan(fangxiang):
    if fangxiang == 0:
        if lingche.x == 300:
            pass
        else:
            lingche.x -= 100
    elif fangxiang == 1:
        if lingche.x == 500:
            pass
        else:
            lingche.x += 100
    else:
        pass
def update():
    global all_flower
    global all_huapin
    global counter,counter_update_time,speed,lingche
    global live,score,max_live
    counter += 1
    #print(counter)
    if counter % counter_update_time == 0:
        spawn()
        #counter = 0
        #print("==========")
    for i in all_flower:
        i.y += speed
        if i.top >= 639:
            i.image = "none"
        if i.colliderect(lingche):
            i.image = "none"
            i.top = lingche.bottom + 10
            if live < max_live:
                live += 1
            else:
                score += 5
            print("纳西妲表示：真香，现在纳西妲还剩" + str(live) + "点血，还剩" + str(score) + "点分数")
    for i in all_huapin:
        i.y += speed
        if i.top >= 639:
            i.image = "none"
        if i.colliderect(lingche):
            i.image = "none"
            i.top = lingche.bottom + 10
            live -= 1
            print("纳西妲表示：阿米诺斯，现在纳西妲还剩" + str(live) + "点血，还剩" + str(score) + "点分数")
    if live == 0:
        messagebox.showinfo("游戏结束","纳西妲蛋黄被摇匀了，你失败了！")
        exit()
        
def on_mouse_up(pos,button):
    global counter_update_time,max_live
    if button == 1:
        zuoyouqiehuan(0)
    elif button == 3:
        zuoyouqiehuan(1)
    elif button == 4:
        if counter_update_time - 5 <= 0:
            print("纳西妲表示：阿米诺斯，再加快我要被颠飞了")
        else:
            max_live += 1
            counter_update_time -= 5
            update_speed()
    elif button == 5:
        counter_update_time += 5
        update_speed()
        max_live -= 1

def draw():
    global live,score,max_live
    screen.blit("background.png",(0,0))
    lingche.draw()
    for i in all_flower:
        i.draw()
    for i in all_huapin:
        i.draw()
    screen.draw.text(str(live) + "/" + str(max_live),(10,10),color='black',fontname='main')
    screen.draw.text(str(score),(450,10),color='black',fontname='main')

pgzrun.go()