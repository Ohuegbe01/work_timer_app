import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
    tick_label.config(bg=YELLOW, fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# TODO.8 create a count down

# TODO.9 modify the count down with the timer_text and count


def count_down(count):

    # to achieve this format: "00:00"...
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark=''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✔️'
            tick_label.config(text=mark)
# TODO 10. create a start_timer function that will work with the count down function
#  and correspond with the button function


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if its the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, 'bold') )
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
    else:
        count_down(work_sec)
        label.config(text='Work Now', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))

# ---------------------------- UI SETUP ------------------------------- #
# TODO.1 Create UI setup, window display


window = Tk()
window.title('Pomodoro')
# TODO.3 creating background color
window.config(padx=100, pady=50, bg=YELLOW)
# TODO.9 call the function 'count down'


# TODO.6 create a label
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
label.grid(column=1, row=0)

tick_label = Label(bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=3)

# TODO.2 Learn to put images into our program using Canvas widget
# TODO.4 changing the canvas background color
# TODO.5 TO remove canvas border: use(highlightthickness=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)
# count_down(5)

# TODO.7 add button
start_button = Button(text='Start', bg='white', highlightthickness=0, command=start_timer)
reset_button = Button(text='Reset', bg='white', highlightthickness=0, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)




window.mainloop()
