from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#982176"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#CECE5A"
FONT_NAME = "Courier"
VERE_GREEN = "#1A5D1A"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_label.config(text="")
    time_label.config(text="Timer")
    canvas.itemconfig(text_canvas, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1

    if reps % 2 == 1:
        time_label.config(text="Work", fg=VERE_GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        time_label.config(text="Long break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        time_label.config(text="Short break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(counter):
    mine = math.floor(counter / 60)
    if mine < 9:
        mine = f"0{mine}"
    sec = counter % 60
    if sec < 9:
        sec = f"0{sec}"
    canvas.itemconfig(text_canvas, text=f"{mine}:{sec}")
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter-1)
    else:
        global marks
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(1, work_sessions+1):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pmomdoro")
window.config(padx=200, pady=120, bg=GREEN)

canvas = Canvas(width=200, height=223, bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=img)
text_canvas = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

time_label = Label(text="Timer", font=(FONT_NAME, 21, "bold"), bg=GREEN)
time_label.grid(row=0, column=1)

check_label = Label(font=(FONT_NAME, 18), bg=GREEN, fg=VERE_GREEN)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", bg=YELLOW, command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, command=reset)
reset_button.grid(row=2, column=2)

window.mainloop()
