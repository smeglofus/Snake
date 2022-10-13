import re
import json
from tkinter import *

top_10 = []

with open('score.json', 'r') as file:
    data = file.read()

with open('score.json') as f:
    hraci = json.load(f)
    for i in range(100,0,-1):
        try:
            if hraci[str(i)]:
                top_10.append((hraci[str(i)], f"Body: {i}"))
        except:
            pass
#print(top_10)


high_score = '\n'.join(str(x) for x in top_10).strip("(){}','")
high_score = re.sub("[(){}<>'',]","", high_score)

print(high_score)

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
    self.scores = Label(self, text=f"{high_score}")
    self.scores.pack()


if __name__ == "__main__":
  app = Scoreboard()
  app.mainloop()
