import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        self.label0 = tk.Label(self.master, text="Count Down Timer", font=("Arial", 28))
        self.label0.pack(pady=10)

        self.label = tk.Label(self.master, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer, width=10, height=2)
        self.start_button.pack(pady=9)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer, width=10, height=2)
        self.pause_button.pack(pady=9)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer, width=10, height=2)
        self.reset_button.pack(pady=9)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_application, width=10, height=2)
        self.exit_button.pack(pady=9)

        self.time_remaining = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            minutes, seconds = divmod(self.time_remaining, 60)
            hours, minutes = divmod(minutes, 60)
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.label.config(text=time_string)
            self.time_remaining += 1
            self.master.after(1000, self.update_timer)

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_remaining = 0
        self.label.config(text="00:00:00")

    def exit_application(self):
        if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
            self.master.destroy()

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
