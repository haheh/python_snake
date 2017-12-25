# -*- coding:utf-8 -*-
# __author__ = 'wj'
from Tkinter import *
import random
from time import *
import thread
import sys
sys.setrecursionlimit(sys.maxint)

def callback1():  # difficulty
    global diff
    diff = difficulty(0)

def callback11():  # difficulty
    global diff
    diff = difficulty(1)

def callback12():  # difficulty
    global diff
    diff = difficulty(2)

def callback2():  # start
    start()

def callback3():  # exit
    root.destroy()

def callback4(event):  # up
    m.append(0)

def callback5(event):  # down
    m.append(1)

def callback6(event):  # left
    m.append(2)

def callback7(event):  # right
    m.append(3)

def difficulty(x=2):
    if x == 0:
        return 0.5
    if x == 1:
        return 0.3
    if x == 2:
        return 0.1

def createfood():
    x = random.randint(0, 39)
    y = random.randint(0, 29)
    return (x, y)

def pan(now):
    for i in range(len(l)):
        if lx[i] == now[0] * 20 and ly[i] == now[1] * 20:
            return False

def food():
    now = createfood()
    while pan(now):
        now = createfood()
    r = f.create_rectangle(now[0] * 20, now[1] * 20, now[0] * 20 + 20, now[1] * 20 + 20, fill='red')
    f.update()
    z.append(r)
    lxf.append(now[0] * 20)
    lyf.append(now[1] * 20)

def gameover():
    if lx[-1] > 780 or lx[-1] < 0 or ly[-1] > 580 or ly[-1] < 0:
        try:
            f.create_text(400, 250, text='Game Over', font=('Fixdsys', 40), fill='red', justify=CENTER)
            f.create_text(400, 330, text='Ur Score : ' + str(len(l) - 3), font=('Fixdsys', 40), fill='blue', justify=CENTER)
            f.create_text(400, 400, text='please click exit', fill='black',font=('Fixdsys', 20))
        except:
            print 'Game Over'
            f.create_text(400,400,text='please click exit',fill='black',font=('Fixdsys', 20))
            sleep(100)
    for i in range(len(l) - 1):
        if lx[i] == lx[-1] and ly[i] == ly[-1]:
            try:
                f.create_text(400, 250, text='Game Over', font=('Fixdsys', 40), fill='red', justify=CENTER)
                f.create_text(400, 330, text='Ur Score : ' + str(len(l) - 3), font=('Fixdsys', 40), fill='blue',justify=CENTER)
                f.create_text(400, 400, text='please click exit', fill='black',font=('Fixdsys', 20))
            except:
                print 'Game Over'
                f.create_text(400, 400, text='please click exit', fill='black',font=('Fixdsys', 20))
                sleep(100)

#控制移动函数
def move():
    if m[-1] == 0:
        up_move1()
        m.pop(0)
    elif m[-1] == 1:
        down_move1()
        m.pop(0)
    elif m[-1] == 2:
        left_move1()
        m.pop(0)
    elif m[-1] == 3:
        right_move1()
        m.pop(0)

def crash():
    for i in range(len(l) - 1):
        if lx[i] == lx[-1] and ly[i] == ly[-1]:
            return True

#自动移动
def up_move():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1], ly[-1] - 20, lx[-1] + 20, ly[-1], fill='white')
        l.append(r)
        lx.append(lx[-1])
        ly.append(ly[-1] - 20)
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()
        if len(m) != 0:
            thread.start_new_thread(move, ())
        sleep(diff)
        move_straight()

#自动移动
def down_move():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1], ly[-1] + 20, lx[-1] + 20, ly[-1] + 40, fill='white')
        f.update()
        l.append(r)
        lx.append(lx[-1])
        ly.append(ly[-1] + 20)
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()
        if len(m) != 0:
            thread.start_new_thread(move, ())
        sleep(diff)
        move_straight()

#自动移动
def left_move():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1] - 20, ly[-1], lx[-1], ly[-1] + 20, fill='white')
        f.update()
        l.append(r)
        lx.append(lx[-1] - 20)
        ly.append(ly[-1])
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()
        if len(m) != 0:
            thread.start_new_thread(move, ())
        sleep(diff)
        move_straight()

#自动移动
def right_move():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1] + 20, ly[-1], lx[-1] + 40, ly[-1] + 20, fill='white')
        l.append(r)
        lx.append(lx[-1] + 20)
        ly.append(ly[-1])
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            f.update()
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()
        if len(m) != 0:
            thread.start_new_thread(move, ())
        sleep(diff)
        move_straight()

#自动移动
def move_straight():  # 坐标比较 然后调用四个方向移动的函数
    if lx[-1] == lx[-2] and ly[-1] > ly[-2]:
        down_move()
    if lx[-1] == lx[-2] and ly[-1] < ly[-2]:
        up_move()
    if lx[-1] > lx[-2] and ly[-1] == ly[-2]:
        right_move()
    if lx[-1] < lx[-2] and ly[-1] == ly[-2]:
        left_move()

#控制移动函数
def up_move1():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    r = f.create_rectangle(lx[-1], ly[-1] - 20, lx[-1] + 20, ly[-1], fill='white')
    l.append(r)
    lx.append(lx[-1])
    ly.append(ly[-1] - 20)
    gameover()
    if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
        f.delete(l[0])
        l.pop(0)
        lx.pop(0)
        ly.pop(0)
    else:  # 碰到了
        f.delete(z[-1])
        food()
    f.update()

#控制移动函数
def down_move1():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1], ly[-1] + 20, lx[-1] + 20, ly[-1] + 40, fill='white')
        f.update()
        l.append(r)
        lx.append(lx[-1])
        ly.append(ly[-1] + 20)
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()

#控制移动函数
def left_move1():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1] - 20, ly[-1], lx[-1], ly[-1] + 20, fill='white')
        f.update()
        l.append(r)
        lx.append(lx[-1] - 20)
        ly.append(ly[-1])
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()

#控制移动函数
def right_move1():
    if lx[-1] < 0 or lx[-1]>780 or ly[-1]<0 or ly[-1]>580:
        pass
    elif crash():
        pass
    else:
        r = f.create_rectangle(lx[-1] + 20, ly[-1], lx[-1] + 20 + 20, ly[-1] + 20, fill='white')
        l.append(r)
        lx.append(lx[-1] + 20)
        ly.append(ly[-1])
        gameover()
        if lx[-1] != lxf[-1] or ly[-1] != lyf[-1]:  # 没碰到
            f.delete(l[0])
            f.update()
            l.pop(0)
            lx.pop(0)
            ly.pop(0)
        else:  # 碰到了
            f.delete(z[-1])
            food()
        f.update()

def start():
    global r1
    global r2
    l.append(r1)
    l.append(r2)
    lx.append(0)
    lx.append(20)
    ly.append(0)
    ly.append(0)
    food()
    move_straight()

root = Tk()
root.title('snake')
root.geometry('800x600')
m = Menu(root)
root.config(menu=m)
m.add_command(label='Start', command=callback2)
difmenu = Menu(m)
m.add_cascade(label='Difficulty', menu=difmenu)
difmenu.add_command(label='Easy', command=callback1)
difmenu.add_separator()
difmenu.add_command(label='Normal', command=callback11)
difmenu.add_separator()
difmenu.add_command(label='Difficult', command=callback12)
paumenu = Menu(m)
m.add_cascade(label='Pause', menu=paumenu)
m.add_command(label='Exit', command=callback3)
f = Canvas(root, width=800, height=600, bg='white')
f.bind('<Up>', callback4)
f.bind('<Down>', callback5)
f.bind('<Left>', callback6)
f.bind('<Right>', callback7)
f.focus_set()
f.pack()
pic = PhotoImage(file='D:\wj\GitHub\\python_snake')
f.create_image(400, 300, image=pic)

for i in range(20 - 1, 600 - 1, 20):
    f.create_line(0, i, 800, i, smooth=0, fill='white')

for i in range(20 - 1, 800 - 1, 20):
    f.create_line(i, 0, i, 600, smooth=0, fill='white')

l = []
lx = []
ly = []
lxf = []
lyf = []
z = []
m = []
r1 = f.create_rectangle(0, 0, 20, 20, fill='white')
r2 = f.create_rectangle(20, 0, 40, 20, fill='white')
diff = difficulty()
root.mainloop()
