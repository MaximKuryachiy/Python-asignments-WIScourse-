import tkinter as tk

def start_game():
    print('The game started!')




app = tk.Tk()
app.geometry('640x240')
app.title('Number Guesser Game')



entrance_label = tk.Label(
    app,
    text = 'Welcome to the Number Guesser!',
)
entrance_label.pack()
entrance_label.config(font=("gisha", 25, 'bold'))
entrance_label.config(fg="#00CCCC")
entrance_label.config(bg='lightblue')

start_button = tk.Button(app,
    text='Start the game',
    width=25,
    command=start_game,
    bg='lightblue',
)
start_button.pack()


close_button = tk.Button(app,
    text = 'Close',
    fg = 'red',
    width = 25,
    command = app.destroy,
    bg = 'White'
)
close_button.pack()
app.mainloop()