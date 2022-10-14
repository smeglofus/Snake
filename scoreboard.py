import re
import json
from tkinter import *
from collections import OrderedDict


top_10 = []
with open('score.json') as f:
    hraci = json.load(f)
    sort = OrderedDict(sorted(hraci.items(), key=lambda i: i[1]["Body"],reverse=True))
    print(sort)
    for polozka in sort:
         if len(top_10) < 11:
             top_10.append(sort[polozka])
             print(len(top_10))


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
