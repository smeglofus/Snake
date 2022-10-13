from tkinter import *

jmeno = ""
class Player(Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Player_score')
    self.geometry('300x300')


    self.label = Label(self, text='Get your name: ')
    self.label.pack()

    self.inputtxt = Text(height=2,
                    width=20,
                    bg="light yellow")
    self.inputtxt.pack()

    self.display = Button(height=2,
                     width=20,
                     text="Show",
                     command=self.button_clicked)
    self.display.pack()

  def button_clicked(self):
      INPUT = self.inputtxt.get("1.0", "end-1c")
      global jmeno
      jmeno = INPUT
      with open("player_name.txt", "w") as name:
          name.write(f"{jmeno}")
      self.destroy()


if __name__ == "__main__":
  app = Player()
  app.mainloop()
