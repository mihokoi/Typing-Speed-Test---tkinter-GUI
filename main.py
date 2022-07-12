from tkinter import *



counter = 60
timer_id = None
word_list = ['this', 'is', 'to', 'prove', 'program', 'is', 'working']
input_word = ''
cpm = 0
accuracy = 0


def count(env=None):
    global counter, timer_id
    if counter > 0:
        text.unbind('<Button-1>')
        counter -= 1
        n_time_left.config(text=str(counter))
        timer_id = time_left_label.after(1000, count)
    elif counter == 0:
        game()

def game(*args):
    calculate_cpm()
    calculate_accuracy()


def calculate_cpm():
    global cpm, input_word
    written = text.get("1.0", 'end-1c')
    written = written.replace(" ", "")
    input_word = written
    cpm = len(written)
    n_cpm_label.config(text=cpm)

def calculate_wpm():
    global wpm
    wpm = len(input_word)*60/(5*60)

def calculate_accuracy():
    global accuracy
    num = 0
    word_list_str = ""
    word_list_str = word_list_str.join(word_list)
    for i, c in enumerate(word_list_str):
        try:
            if input_word[i] == c:
                num += 1
        except:
            pass
    accuracy = num/len(word_list_str)*100
    n_accuracy.config(text=f'{int(accuracy)}%')

def reset(label):
    global counter
    counter = 60
    if timer_id:
        n_time_left.after_cancel(timer_id)
    text.bind('<Button-1>', count)
    n_time_left.config(text=str(counter))

root = Tk()
root.title("Hello")
root.columnconfigure(1, weight=6)


canvas_top = Canvas(root)
canvas_top.grid(column=0, row=0)

corrected_cpm_label = Label(canvas_top, text='CPM:')
corrected_cpm_label.grid(column=0, row=0)

n_cpm_label = Label(canvas_top)
n_cpm_label.grid(column=1, row=0)

accuracy_label = Label(canvas_top, text='Accuracy:')
accuracy_label.grid(column=2, row=0)

n_accuracy = Label(canvas_top)
n_accuracy.grid(column=3, row=0)

time_left_label = Label(canvas_top, text='Time left:')
time_left_label.grid(column=4, row=0)

n_time_left = Label(canvas_top, text='60')
n_time_left.grid(column=5, row=0)

canvas_mid = Canvas(root)
canvas_mid.grid(column=0, row=1)

word_entry = Text(canvas_mid, height=10, width=90)
word_entry.grid()
word_entry.insert(INSERT, [word for word in word_list])

button = Button(root, text="Hit me to reset", command=lambda: reset(time_left_label))
button.grid()

text = Text(root, height=5, width=20, padx=20)
text.grid()
text.bind("<Return>", game)
text.bind('<Button-1>', count)

start_index = 0
end_index = 0



root.mainloop()