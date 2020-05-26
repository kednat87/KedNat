import turtle
import random
import time

turtlelist = []
player1_score = 0
player2_score = 0
reset = 'N'

sc = turtle.Screen()
sc.setup(height=700, width=1400)
sc.bgcolor('Dark Green')
sc.title("Car Racing !!")


def create_turtles():
    for i in range(5):
        if reset == 'N':
            turtlelist.append(turtle.Turtle())
        t = turtlelist[i]
        t.penup()
        t.shape('square')
        t.color('Red')
        t.name = i
        t.setpos((-600 + i * 300), -330)
        if reset == 'N':
            t.left(90)


def scoring(pl, wn):
    s_dict = {11: 30, 10: 15, 21: 20, 20: 10, 31: 10, 30: 5}
    score = 0
    for i in range(3):
        if pl[i] == wn[i]:
            e = (i + 1) * 10 + 1
            score += s_dict[e]
        elif pl[i] in wn[:3]:
            e = (i + 1) * 10 + 0
            score += s_dict[e]
    return score


def winner():
    if scoring(p1, wlist) > scoring(p2, wlist):
        win = 'Player 1'
    elif scoring(p2, wlist) > scoring(p1, wlist):
        win = 'Player 2'
    else:
        win = 'Its a Tie'
    return win


while True:
    p1 = []
    p2 = []
    p1_score = 0
    p2_score = 0
    wlist = []
    cnt = 0

    create_turtles()
    score = turtle.Turtle()
    score.color('White')
    score.penup()
    score.setpos(-600, 150)
    style = ('Courier', 14, 'bold')

    display = ''' Predict the 1st , 2nd and 3rd winners.  Eg : Inputs should be numeric from 1 - 5 '''
    score.write(display, font=style)
    time.sleep(2)
    score.clear()

    p1.append(int(input('Player 1 : Predict the First winner : ')))
    p1.append(int(input('Player 1 : Predict the Second winner : ')))
    p1.append(int(input('Player 1 : Predict the Third winner : ')))
    p2.append(int(input('Player 2 : Predict the First winner : ')))
    p2.append(int(input('Player 2 : Predict the Second winner : ')))
    p2.append(int(input('Player 2 : Predict the Third winner : ')))

    time.sleep(2)

    while True:
        sc.update()
        ch = random.choice(turtlelist)
        if cnt == 5:
            break
        if ch.ycor() >= 330:
            if ch.name not in wlist:
                wlist.append(ch.name)
                cnt += 1
            continue
        ch.forward(10)

    p1_score = scoring(p1, wlist)
    p2_score = scoring(p2, wlist)
    player1_score = player1_score + p1_score
    player2_score = player2_score + p2_score

    win = winner()
    display = '''
                 1st Car: {}
                 2nd Car: {}
                 3rd Car: {}

                 Player 1 Scores : {}
                 Player 2 Scores : {}
                 Winner is : {}
                '''.format(wlist[0], wlist[1], wlist[2], player1_score, player2_score, win)
    score.write(display, font=style)
    time.sleep(3)

    score.clear()

    display = '''Do you want to Continue(C) , Reset(R) or Quit(Q) ?: '''
    time.sleep(3)
    reset = input('Do you want to Continue(C) , Reset(R) or Quit(Q) ?: ')
    if reset == 'C':
        continue
    elif reset == 'R':
        player1_score = 0
        player2_score = 0
        continue
    elif reset == 'Q':
        sc.bye()
        break