from tkinter import *
from tkinter import ttk, messagebox

class TimerDemo:
    def __init__(self,app):
        self.root = app
        self.app_layout()

    def app_layout(self): 
        self.EnterTime = ttk.Label(app, text="Enter time in seconds: ")
        self.EnterTime.pack()

        self.TimeBox = ttk.Entry(app, width=20)
        self.TimeBox.pack()

        self.EnterText = ttk.Label(app, text="Enter message: ")
        self.EnterText.pack()

        self.TextBox = ttk.Entry(app, width=20)
        self.TextBox.pack()
        
        self.label = ttk.Label(app, font=('Helvetica', 35))
        self.label.pack(pady=20)

        self.startbutton = ttk.Button(app, text="Start Timer", command=self.start_timer)
        self.startbutton.pack(side=LEFT, expand = True, fill = BOTH)

        self.stopbutton = ttk.Button(app, text="Stop Timer", command=self.stop_timer)
        self.stopbutton.pack(side=LEFT, expand = True, fill = BOTH)

    def countdown(self, count):
            if self.running:
                self.label['text'] = count
                if count > 0:
                    self.root.after(1000, self.countdown, count-1)
                elif count == 0:
                    MessageText = self.TextBox.get()
                    messagebox.showinfo("Time's Up", MessageText)

    def start_timer(self):
        self.running = True
        timeinsecs = int(self.TimeBox.get())
        self.countdown(timeinsecs)

    def stop_timer(self):
        self.running = False

if __name__ == "__main__":
    app = Tk()
    app.title("Timer")
    app.resizable(False,False)
    app.geometry("230x205")
    app2 = TimerDemo(app)
    app.mainloop()
