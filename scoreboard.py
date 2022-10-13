

from tkinter import *

with open('score.txt', 'r') as file:
    data = file.read()

class Scoreboard(Tk):
  def __init__(self):
    super().__init__()
    self.title('High Scores')
    self.geometry('300x300')


    self.label = Label(self, text='High Scores')
    self.label.pack()

    self.display = Button(height=2,
                     width=20,
                     text="exit",
                     command=self.destroy)
    self.display.pack()
    self.scores = Label(self, text=f"{data}")
    self.scores.pack()


if __name__ == "__main__":
  app = Scoreboard()
  app.mainloop()
