### Bugs: Game over screen (with button text as "New Game" and final score) disappear too quickly
### Spacebar starts initial game and Pauses but will not resume
### Apples can spawn on snakebody
### Other than that, this is 100% functional
from tkinter import *
import random

class SnakeGUI():
    def __init__(self):
        self.snake = Tk()
        self.snake.title("Snake")
        #self.snake.minsize(600,625)
        self.canvas = Canvas(self.snake,width=600,height=600, bd = 0, relief = None, bg="green")
        self.canvas.pack()
        self.x1 = 300
        self.x2 = 320
        self.y1 = 300
        self.y2 = 320
        self.snakebody = [(self.x1,self.y1)]
        self.canvas.create_rectangle(300,300,320,320, fill = "black", tag = "critter")
        self.applex1 = random.randint(0,29) * 20
        self.appley1 = self.applex1
        self.applex2 = self.applex1 + 20
        self.appley2 = self.applex2
        self.canvas.create_oval(self.applex1,self.appley1,self.applex2, self.appley2, fill = "red", tag = "apple")
        self.start = Button(self.snake, text = "Start", bg ="red", command = self.drawsnake)
        self.start.bind(self.snake)
        self.start.pack()
        self.delay = 200
        self.snake.bind("<Down>", self.movedown)
        self.snake.bind("<Up>", self.moveup)
        self.snake.bind("<Left>", self.moveleft)
        self.snake.bind("<Right>", self.moveright)
        self.snake.bind("s", self.movedown)
        self.snake.bind("w", self.moveup)
        self.snake.bind("a", self.moveleft)
        self.snake.bind("d", self.moveright)
        self.direction = "up"
        self.snake.bind("<space>",self.drawsnake)
        self.direction = "up"
        self.lastdirection = "up"
        self.totalscore = 1
        self.total_label = Label(self.snake, text = "Score: " + str(self.totalscore))
        self.total_label.pack()
        self.gameover = Label(self.snake, text = "Game Over")
        self.snake.mainloop()

    def createapple(self):
        self.totalscore += 1
        self.total_label["text"] = "Score: " + str(self.totalscore)
        self.canvas.delete("apple")
        self.applex1 = random.randint(0,29) * 20
        self.appley1 = random.randint(0,29) * 20
        self.applex2 = self.applex1 + 20
        self.appley2 = self.appley1 + 20
        self.canvas.create_oval(self.applex1,self.appley1,self.applex2, self.appley2, fill = "red", tag = "apple")

    def drawsnake(self, event=None):
        self.gameover.destroy()
        self.snake.bind("<space>",self.pause)
        if self.direction == 'nothing':
            self.start["text"] = "Resume"
            self.start.configure(bg = "blue", command = self.resume)
        else:
            self.snakebody.append((self.x1,self.y1))
            self.start.configure(text = "Pause", bg = "yellow", command = self.pause)

            if self.x1 == self.applex1 and self.y1 == self.appley1:
                self.createapple()
                if self.delay > 4:
                    self.delay -= 4
                elif self.delay > 0 and self.delay <= 4:
                    self.delay = 1
                else:
                    self.delay = 1
            else:
                self.snakebody= self.snakebody[1:]
                
            if self.direction == "left":
                self.canvas.delete("critter")
                self.x1 -= 20       
                self.x2 -= 20
                self.createsnake()
                self.direction = "left"
            elif self.direction == "right":
                self.canvas.delete("critter")
                self.x1 += 20
                self.x2 += 20
                self.createsnake()
                self.direction = "right"
            elif self.direction == "up":
                self.canvas.delete("critter")
                self.y1 -= 20
                self.y2 -= 20
                self.createsnake()
                self.direction = "up"
            else:
                self.canvas.delete("critter")
                self.y1 += 20
                self.y2 += 20
                self.createsnake()
                self.direction = "down"

            if self.x1 <0 or self.y1 < 0 or self.x1 > 580 or self.y1 > 580:
                self.newgame()

            collision = False
            for i in range(len(self.snakebody)-1):
                if collision == False and self.snakebody[-1][0] == self.snakebody[i][0] and self.snakebody[-1][1] == self.snakebody[i][1]:
                    collision = True
                    self.newgame()

        self.canvas.after(self.delay,self.drawsnake)

    def createsnake(self):
        for i in reversed(self.snakebody):
            self.canvas.create_rectangle(i[0],i[1],i[0]+20,i[1]+20, fill = "black", tag = "critter")

    def movedown(self,event=None):
        self.direction = "down"
    def moveup(self, event=None):
        self.direction = "up"
    def moveleft(self,event=None):
        self.direction = "left"
    def moveright(self,event=None):
        self.direction = "right"
    def pause(self, event=None):
        self.start["text"] = "Resume"
        self.start.configure(bg = "blue", command = self.drawsnake)
        self.lastdirection = self.direction
        self.direction = "nothing"
        self.snake.bind("<space>",self.resume)
    def newgame(self):
        self.gameover = Label(self.snake, text = "Game Over")
        self.gameover.pack()
        self.start.configure(text = "New Game", command = self.snake)
        self.delay = 200
        self.x1 = 300
        self.x2 = 320
        self.y1 = 300
        self.y2 = 320
        self.snakebody = [(self.x1,self.y1)]
        self.total_label["text"] = "Your Score Was:" + str(self.totalscore)
        self.totalscore = 1
        self.start.configure(command = self.drawsnake)
        self.lastdirection = self.direction
        self.direction = "nothing"
        self.total_label["text"] = "Score: " + str(self.totalscore)
        self.snake.bind("<space>",self.resume)
    def resume(self, event=None):
        self.start["text"] = "Resume"
        self.direction = self.lastdirection

        
SnakeGUI()
