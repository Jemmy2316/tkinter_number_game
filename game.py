import tkinter
import random
from functools import reduce
from tkinter import font
from tkinter import *
import time
import os
import sys

WIDTH, HEIGHT = 480, 720

root = tkinter.Tk()
root.title("数字当てゲーム")
root.minsize(WIDTH, HEIGHT)
font1 = font.Font(family='Meiryo', size=24)
font2 = font.Font(family='Meiryo', size=16)

#ウィンドウ生成
canvas = tkinter.Canvas(bg="gray", width=WIDTH, height=HEIGHT)
canvas.place(x=0, y=0)

#テーブル生成
i = 28
for tablex in range(6):
    j = 28
    for tabley in range(6):
        cell = tkinter.Canvas(bg="lightgray", width=64, height=64)
        cell.place(x=i,y=j)
        j += 72
    i += 72

#入力格納
table = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
count = 0
cnt = 0
start = 0
stop = 0

#数字生成
def rand_nocon(a, b, k): #連続排除ランダム
    r = [random.randint(a, b)]
    while len(r) < k:
        n = random.randint(a, b)
        if r[-1] != n:
            r.append(n)
    return r

#num = random.randint(0,999999) #ノーマルランダム
#num = rand_nocon(0, 9, 6)
num = random.sample(range(9), 6) #重複なしランダム（エラー防止）
n = reduce(lambda a,b:10*a+b, num) #リストから6桁の整数に変換
fnum = str(n).zfill(6) #ゼロ埋め
#print(fnum)

#ボタン
button0 = tkinter.Button(text="        0        ")
button0.place(x=48,y=500)
button1 = tkinter.Button(text="        1        ")
button1.place(x=128,y=500)
button2 = tkinter.Button(text="        2        ")
button2.place(x=208,y=500)
button3 = tkinter.Button(text="        3        ")
button3.place(x=288,y=500)
button4 = tkinter.Button(text="        4        ")
button4.place(x=368,y=500)
button5 = tkinter.Button(text="        5        ")
button5.place(x=48,y=532)
button6 = tkinter.Button(text="        6        ")
button6.place(x=128,y=532)
button7 = tkinter.Button(text="        7        ")
button7.place(x=208,y=532)
button8 = tkinter.Button(text="        8        ")
button8.place(x=288,y=532)
button9 = tkinter.Button(text="        9        ")
button9.place(x=368,y=532)
check_button = tkinter.Button(text="             照会             ")
check_button.place(x=185,y=564)
line_reset_button = tkinter.Button(text="行リセット")
line_reset_button.place(x=126,y=564)
skip_button = tkinter.Button(text="   Skip   ")
skip_button.place(x=300,y=564)

def zero():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 0")
    if count < 6 :
        table[0][count] = 0
        cx = count * 72
        count += 1
        #print
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 0
        count += 1
        #print
        cx = cnt * 72
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 0
        count += 1
        #print
        cx = cnt * 72
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 0
        count += 1
        #print
        cx = cnt * 72
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 0
        count += 1
        #print
        cx = cnt * 72
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 0
        count += 1
        #print
        cx = cnt * 72
        table0 = tkinter.Label(root, text="0", font=font1, bg="lightgray")
        table0.place(x=50+cx ,y=396)
    else:
        pass

def one():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 1")
    if count < 6:
        table[0][count] = 1
        cx = count * 72
        count += 1
        #print
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 1
        count += 1
        #print
        cx = cnt * 72
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 1
        count += 1
        #print
        cx = cnt * 72
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 1
        count += 1
        #print
        cx = cnt * 72
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 1
        count += 1
        #print
        cx = cnt * 72
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 1
        count += 1
        #print
        cx = cnt * 72
        table1 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
        table1.place(x=50+cx ,y=396)
    else:
        pass

def two():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 2")
    if count < 6 :
        table[0][count] = 2
        cx = count * 72
        count += 1
        #print
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 2
        count += 1
        #print
        cx = cnt * 72
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 2
        count += 1
        #print
        cx = cnt * 72
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 2
        count += 1
        #print
        cx = cnt * 72
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 2
        count += 1
        #print
        cx = cnt * 72
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 2
        count += 1
        #print
        cx = cnt * 72
        table2 = tkinter.Label(root, text="2", font=font1, bg="lightgray")
        table2.place(x=50+cx ,y=396)
    else:
        pass

def three():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 3")
    if count < 6 :
        table[0][count] = 3
        cx = count * 72
        count += 1
        #print
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 3
        count += 1
        #print
        cx = cnt * 72
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 3
        count += 1
        #print
        cx = cnt * 72
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 3
        count += 1
        #print
        cx = cnt * 72
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 3
        count += 1
        #print
        cx = cnt * 72
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 3
        count += 1
        #print
        cx = cnt * 72
        table3 = tkinter.Label(root, text="3", font=font1, bg="lightgray")
        table3.place(x=50+cx ,y=396)
    else:
        pass

def four():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 4")
    if count < 6 :
        table[0][count] = 4
        cx = count * 72
        count += 1
        #print
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 4
        count += 1
        #print
        cx = cnt * 72
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 4
        count += 1
        #print
        cx = cnt * 72
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 4
        count += 1
        #print
        cx = cnt * 72
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 4
        count += 1
        #print
        cx = cnt * 72
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 4
        count += 1
        #print
        cx = cnt * 72
        table4 = tkinter.Label(root, text="4", font=font1, bg="lightgray")
        table4.place(x=50+cx ,y=396)
    else:
        pass

def five():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 5")
    if count < 6 :
        table[0][count] = 5
        cx = count * 72
        count += 1
        #print
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 5
        count += 1
        #print
        cx = cnt * 72
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 5
        count += 1
        #print
        cx = cnt * 72
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 5
        count += 1
        #print
        cx = cnt * 72
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 5
        count += 1
        #print
        cx = cnt * 72
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 5
        count += 1
        #print
        cx = cnt * 72
        table5 = tkinter.Label(root, text="5", font=font1, bg="lightgray")
        table5.place(x=50+cx ,y=396)
    else:
        pass

def six():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 6")
    if count < 6 :
        table[0][count] = 6
        cx = count * 72
        count += 1
        #print
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 6
        count += 1
        #print
        cx = cnt * 72
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 6
        count += 1
        #print
        cx = cnt * 72
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 6
        count += 1
        #print
        cx = cnt * 72
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 6
        count += 1
        #print
        cx = cnt * 72
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 6
        count += 1
        #print
        cx = cnt * 72
        table6 = tkinter.Label(root, text="6", font=font1, bg="lightgray")
        table6.place(x=50+cx ,y=396)
    else:
        pass

def seven():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 7")
    if count < 6 :
        table[0][count] = 7
        cx = count * 72
        count += 1
        #print
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 7
        count += 1
        #print
        cx = cnt * 72
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 7
        count += 1
        #print
        cx = cnt * 72
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 7
        count += 1
        #print
        cx = cnt * 72
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 7
        count += 1
        #print
        cx = cnt * 72
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 7
        count += 1
        #print
        cx = cnt * 72
        table7 = tkinter.Label(root, text="7", font=font1, bg="lightgray")
        table7.place(x=50+cx ,y=396)
    else:
        pass

def eight():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 8")
    if count < 6 :
        table[0][count] = 8
        cx = count * 72
        count += 1
        #print
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 8
        count += 1
        #print
        cx = cnt * 72
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 8
        count += 1
        #print
        cx = cnt * 72
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 8
        count += 1
        #print
        cx = cnt * 72
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 8
        count += 1
        #print
        cx = cnt * 72
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 8
        count += 1
        #print
        cx = cnt * 72
        table8 = tkinter.Label(root, text="8", font=font1, bg="lightgray")
        table8.place(x=50+cx ,y=396)
    else:
        pass

def nine():
    global count
    global start
    if count == 0:
        start = time.time()
    #print("pushed 9")
    if count < 6 :
        table[0][count] = 9
        cx = count * 72
        count += 1
        #print
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=36)
    elif count < 12:
        cnt = count - 6
        table[1][cnt] = 9
        count += 1
        #print
        cx = cnt * 72
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=108)
    elif count < 18:
        cnt = count - 12
        table[2][cnt] = 9
        count += 1
        #print
        cx = cnt * 72
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=180)
    elif count < 24:
        cnt = count - 18
        table[3][cnt] = 9
        count += 1
        #print
        cx = cnt * 72
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=252)
    elif count < 30:
        cnt = count - 24
        table[4][cnt] = 9
        count += 1
        #print
        cx = cnt * 72
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=324)
    elif count < 36:
        cnt = count -30
        table[5][cnt] = 9
        count += 1
        #print
        cx = cnt * 72
        table9 = tkinter.Label(root, text="9", font=font1, bg="lightgray")
        table9.place(x=50+cx ,y=396)
    else:
        pass

def check():
    global count
    #print("pushed check")
    if count == 6:
        for i in range(6):
            if  int(table[0][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            elif int(table[0][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            elif int(table[0][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            elif int(table[0][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            elif int(table[0][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            elif int(table[0][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    match = tkinter.Label(root, text=table[0][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=36)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=28)
                    line = tkinter.Label(root, text=table[0][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=36)
            else:
                print("event13")
    elif count == 12:
        for i in range(6):
            if  int(table[1][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            elif int(table[1][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            elif int(table[1][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            elif int(table[1][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            elif int(table[1][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            elif int(table[1][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    match = tkinter.Label(root, text=table[1][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=108)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=100)
                    line = tkinter.Label(root, text=table[1][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=108)
            else:
                print("event13")
    elif count == 18:
        for i in range(6):
            if  int(table[2][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            elif int(table[2][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            elif int(table[2][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            elif int(table[2][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            elif int(table[2][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            elif int(table[2][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    match = tkinter.Label(root, text=table[2][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=180)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=172)
                    line = tkinter.Label(root, text=table[2][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=180)
            else:
                print("event13")
    elif count == 24:
        for i in range(6):
            if  int(table[3][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            elif int(table[3][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            elif int(table[3][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            elif int(table[3][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            elif int(table[3][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            elif int(table[3][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    match = tkinter.Label(root, text=table[3][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=252)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=244)
                    line = tkinter.Label(root, text=table[3][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=252)
            else:
                print("event13")
    elif count == 30:
        for i in range(6):
            if  int(table[4][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            elif int(table[4][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            elif int(table[4][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            elif int(table[4][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            elif int(table[4][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            elif int(table[4][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    match = tkinter.Label(root, text=table[4][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=324)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=316)
                    line = tkinter.Label(root, text=table[4][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=324)
            else:
                print("event13")
    elif count == 36:
        global start
        global stop
        stop = time.time()
        timer_text = str(round(stop-start, 1))+"秒"
        timer = tkinter.Label(root, text=timer_text, font=font2, bg="white")
        timer.place(x=350,y=650)

        for i in range(6):
            if  int(table[5][i]) == int(fnum[0]):
                if i == 0:
                    print("event1")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event2")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            elif int(table[5][i]) == int(fnum[1]):
                if i == 1:
                    print("event3")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event4")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            elif int(table[5][i]) == int(fnum[2]):
                if i == 2:
                    print("event5")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event6")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            elif int(table[5][i]) == int(fnum[3]):
                if i == 3:
                    print("event7")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event8")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            elif int(table[5][i]) == int(fnum[4]):
                if i == 4:
                    print("event9")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event10")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            elif int(table[5][i]) == int(fnum[5]):
                if i == 5:
                    print("event11")
                    fcell = tkinter.Canvas(bg="cyan", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    match = tkinter.Label(root, text=table[5][i], font=font1, bg="cyan")
                    match.place(x=50+(i*72),y=396)
                else:
                    print("event12")
                    fcell = tkinter.Canvas(bg="yellow", width=64, height=64)
                    fcell.place(x=28+(i*72),y=388)
                    line = tkinter.Label(root, text=table[5][i], font=font1, bg="yellow")
                    line.place(x=50+(i*72),y=396)
            else:
                print("event13")
        answer = tkinter.Label(root, text=fnum, font=font1, bg="#00ffff")
        answer.place(x=180,y=620)
    else:
        pass

def line_reset():
    global count
    if count < 6:
        count = 0
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=28)
    elif count < 12:
        count = 6
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=100)
    elif count < 18:
        count = 12
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=172)
    elif count < 24:
        count = 18
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=244)
    elif count < 30:
        count = 24
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=316)
    elif count < 36:
        count = 30
        for i in range(6):
            delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
            delete.place(x=28+(i*72),y=388)
    else:
        pass

def skip():
    global count
    count = 36
    check()
    for i in range(6):
        delete = tkinter.Canvas(bg="lightgray", width=64, height=64)
        delete.place(x=28+(i*72),y=388)

#文字テスト
#table00 = tkinter.Label(root, text="1", font=font1, bg="lightgray")
#table00.place(x=50,y=36)

#print(num)
button0["command"] = zero
button1["command"] = one
button2["command"] = two
button3["command"] = three
button4["command"] = four
button5["command"] = five
button6["command"] = six
button7["command"] = seven
button8["command"] = eight
button9["command"] = nine
check_button["command"] = check
line_reset_button["command"] = line_reset
skip_button["command"] = skip
#print(fnum[0], fnum[1], fnum[2], fnum[3], fnum[4], fnum[5]) #check

root.mainloop()