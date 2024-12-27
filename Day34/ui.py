
from tkinter import *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.canvas = None
        self.score_label = None
        self.txt = None
        self.blank = None
        self.right = None
        self.wrong = None
        self.right_img = None
        self.wrong_img = None

    def set_window(self, title, pdx, pdy, theme):
        self.window.title(title)
        self.window.config(padx=pdx, pady=pdy, background=theme)

    def set_canvas(self, wd, ht, bg, highlight=0):
        self.canvas = Canvas(width=wd, height=ht, background=bg, highlightthickness=highlight)
        self.canvas.grid(row=1, column=0, columnspan=2)

    def set_blank(self, txt, fg, bg, fnt):
        self.blank = Label(text=txt, fg=fg, bg=bg, font=(fnt, 10))
        self.blank.grid(row=2, column=0)

    def write_score_label(self, bg, fg, txt, font_name, font_size):
        if self.score_label is None:
            self.score_label = Label(text=txt, bg=bg, fg=fg, font=(font_name, font_size))
        else:
            self.score_label.destroy()
            self.score_label = Label(text=txt, bg=bg, fg=fg, font=(font_name, font_size))
        self.score_label.grid(row=0, column=1)

    def write_canvas(self, x, y, w, txt, color, fnt):
        self.canvas.delete("all")  # Clears everything on the canvas
        self.txt = self.canvas.create_text(x, y, text=txt, width=w, fill=color, font=fnt)

    def set_button(self, right_file, wrong_file, right_cmd, left_cmd, highlight=0):
        self.right_img = PhotoImage(file=right_file)  # Store as an instance variable
        self.wrong_img = PhotoImage(file=wrong_file)  # Store as an instance variable

        self.right = Button(image=self.right_img, highlightthickness=highlight, command=right_cmd)
        self.right.grid(row=3, column=0)

        self.wrong = Button(image=self.wrong_img, highlightthickness=highlight, command=left_cmd)
        self.wrong.grid(row=3, column=1)

    def run(self):
        self.window.mainloop()
