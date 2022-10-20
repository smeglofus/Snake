from tkinter import *

class Player(Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Player_score')
    self.geometry('200x100')


    self.label = Label(self, text='Get your name: ')
    self.label.pack()

    self.inputtxt = Text(height=2,
                    width=20,
                    bg="light yellow")
    self.inputtxt.pack()

    self.display = Button(height=2,
                     width=20,
                     text="OK",
                     command=self.button_clicked)
    self.display.pack()

  def button_clicked(self):
      input = self.inputtxt.get("1.0", "end-1c")
      with open("player_name.txt", "w") as name:
          name.write(f"{input}")
      self.destroy()


if __name__ == "__main__":
  app = Player()
  app.mainloop()
