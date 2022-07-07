import random
import tkinter
from tkinter import messagebox

run = True
score = 0
with open('./random_words.txt', 'r') as file:
    words = file.read().split()
    guessed_word = random.choice(words)
    hidden_word = guessed_word


def entry(x):
    widget_text = x.widget['text']
    text.set(widget_text)


while run:
    with open('./random_words.txt', 'r') as file:
        words = file.read().split()
        guessed_word = random.choice(words)
        hidden_word = guessed_word
    lives = len(guessed_word)
    win_count = 0
    window = tkinter.Tk()
    window.title("Hangman Game")
    window.geometry('330x235')
    window.resizable(width=False, height=False)
    window.configure(background='#b5b5b5')
    window.update()
    text = tkinter.StringVar(value='')
    dashboard_box = tkinter.Entry(window, relief="groove", state='readonly', textvar=text)
    dashboard_box.grid(row=8, column=1, columnspan=3, sticky='news')
    x = 0
    for i in range(0, len(guessed_word)):
        x += 20  # aj, dzax
        exec('d{}=tkinter.Label(window, background="#b5b5b5", justify="center", text="-",font=("arial",15))'.format(i))
        exec('d{}.place(x={}, y={}, anchor="center")'.format(i, x, 220))  # tivy verev nerqevna

    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
    button = [['A', 'a', 2, 0], ['B', 'b', 2, 1], ['C', 'c', 2, 2], ['D', 'd', 2, 3], ['E', 'e', 2, 4], ['F', 'f', 3, 0],
              ['G', 'g', 3, 1], ['H', 'h', 3, 2], ['I', 'i', 3, 3], ['J', 'j', 3, 4], ['K', 'k', 4, 0], ['L', 'l', 4, 1],
              ['M', 'm', 4, 2], ['N', 'n', 4, 3], ['O', 'o', 4, 4], ['P', 'p', 5, 0], ['Q', 'q', 5, 1], ['R', 'r', 5, 2],
              ['S', 's', 5, 3], ['T', 't', 5, 4], ['U', 'u', 6, 0], ['V', 'v', 6, 1], ['W', 'w', 6, 2], ['X', 'x', 6, 3],
              ['Y', 'y', 6, 4], ['Z', 'z', 7, 2]]

    for q in button:
        exec('{}=tkinter.Button(window, text="{}", relief="groove", command=lambda:main("{}","{}"), height=1, width=8)'
             ''.format(q[0], q[0], q[1], q[0]))
        exec('{}.grid(row={},column={})'.format(q[0], q[2], q[3]))
        exec('{}.bind("<Button-1>", entry)'.format(q[0]))

    def close():
        global run
        answer = messagebox.askyesno('ALERT', 'YOU WANT TO EXIT THE GAME?')
        if answer:
            run = False
            window.destroy()

    ex = tkinter.Button(window, text='Exit', relief='groove', command=close, height=1, width=8)
    ex.grid(row=0, column=4)
    s2 = 'Score:' + str(score)
    s1 = tkinter.Label(window, text=s2, bg="#b5b5b5", font=("arial", 10))
    s1.grid(row=0, column=0)


    def main(letter, button):
        global lives, win_count, run, score
        exec('{}.destroy()'.format(button))
        if letter in guessed_word:
            for i in range(0, len(guessed_word)):
                if guessed_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i, letter.upper()))
            if win_count == len(guessed_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER', f'YOU WON!\nTHE WORD IS: {guessed_word.upper()}\nWANT TO PLAY '
                                                          f'AGAIN?')
                if answer:
                    run = True
                    window.destroy()
                else:
                    run = False
                    window.destroy()
        else:
            lives -= 1
            l2 = 'Lives:' + str(lives)
            l1 = tkinter.Label(window, text=l2, bg="#b5b5b5", font=("arial", 10))
            l1.grid(row=0, column=2)
            if lives == 0:
                answer = messagebox.askyesno('GAME OVER', f'YOU LOST!\nTHE WORD IS: {guessed_word.upper()}\nWANT TO PLAY'
                                                          f' AGAIN?')
                if answer:
                    run = True
                    window.destroy()
                else:
                    run = False
                    window.destroy()

    window.mainloop()
