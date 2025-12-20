from tkinter import *


class QuizInterface:
    """
    A custom UI Wrapper for the Quizzler application.
    Encapsulates Tkinter complexity into reusable methods for window,
    canvas, and button management.
    """

    def __init__(self):
        """Initializes the main window and placeholders for UI components."""
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
        """Sets up the main application window properties."""
        self.window.title(title)
        self.window.config(padx=pdx, pady=pdy, background=theme)

    def set_canvas(self, wd, ht, bg, highlight=0):
        """Creates and grids the main drawing area for questions."""
        self.canvas = Canvas(width=wd, height=ht, background=bg, highlightthickness=highlight)
        self.canvas.grid(row=1, column=0, columnspan=2)

    def set_blank(self, txt, fg, bg, fnt):
        """Adds a spacer or decorative label to the grid."""
        self.blank = Label(text=txt, fg=fg, bg=bg, font=(fnt, 10))
        self.blank.grid(row=2, column=0)

    def write_score_label(self, bg, fg, txt, font_name, font_size):
        """
        Updates the score display by destroying the old label and creating a new one.
        This ensures the UI always reflects the latest QuizBrain score.
        """
        if self.score_label is not None:
            self.score_label.destroy()

        self.score_label = Label(text=txt, bg=bg, fg=fg, font=(font_name, font_size))
        self.score_label.grid(row=0, column=1)

    def write_canvas(self, x, y, w, txt, color, fnt):
        """
        Clears the canvas and renders new text.
        Args:
            w (int): The width at which text should wrap to a new line.
        """
        self.canvas.delete("all")  # Prevents text stacking
        self.txt = self.canvas.create_text(x, y, text=txt, width=w, fill=color, font=fnt)

    def set_button(self, right_file, wrong_file, right_cmd, left_cmd, highlight=0):
        """
        Loads images and initializes the True/False buttons with their callbacks.
        Note: Images must be stored as instance variables (self) to avoid Garbage Collection.
        """
        self.right_img = PhotoImage(file=right_file)
        self.wrong_img = PhotoImage(file=wrong_file)

        self.right = Button(image=self.right_img, highlightthickness=highlight, command=right_cmd)
        self.right.grid(row=3, column=0)

        self.wrong = Button(image=self.wrong_img, highlightthickness=highlight, command=left_cmd)
        self.wrong.grid(row=3, column=1)

    def run(self):
        """Starts the Tkinter event loop to keep the window open."""
        self.window.mainloop()
