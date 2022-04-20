import pandas as pd
import turtle as t
import time

BG = r'C:\Users\montv\python_work\100_days_of_code\day_25\us_states_game\blank_states_img.gif'
BG_WIDTH = 730
BG_HEIGHT = 491
STATE_DATA = r'c:\users\montv\python_work\100_days_of_code\day_25\us_states_game\50_states.csv'
TO_LEARN = r'c:\users\montv\python_work\100_days_of_code\day_25\us_states_game\states_to_learn.csv'
ALIGN = 'left'
FONT = ('Courier', 6, 'bold')
SLEEP = 0.30
MAX_SCORE = 50


def get_state(guessed_state):
    """Returns True if guessed state exists in data set, else returns False."""
    return guessed_state.title() in states_df['state'].values


def get_state_coordinates(guessed_state):
    """Returns a tuple containing the coordinates of the guessed state."""
    x_cor = states_df[states_df['state'] == f'{guessed_state.title()}'].x
    y_cor = states_df[states_df['state'] == f'{guessed_state.title()}'].y
    return x_cor.iloc[0], y_cor.iloc[0]


def show_answer(guessed_state):
    """Creates a python Turtle object and places it at the coordinates of the state."""
    answer = t.Turtle()
    answer.hideturtle()
    answer.penup()
    answer.goto(get_state_coordinates(guess))
    answer.write(f'{guessed_state.title()}', align=ALIGN, font=FONT)


screen = t.Screen()
screen.setup(width=BG_WIDTH, height=BG_HEIGHT)
screen.tracer(0)
screen.addshape(BG)
screen_background = t.Turtle(shape=BG)

states_df = pd.read_csv(STATE_DATA)

score = 0
guessed_states = []
while score < MAX_SCORE:
    screen.update()
    time.sleep(SLEEP)

    guess = t.textinput(title=f'States Game - {score}/{MAX_SCORE}', prompt='Name a US state.')

    if get_state(guess):
        show_answer(guess)
        guessed_states.append(guess.title())
        score += 1

    if guess == 'exit':
        missed_states = [state for state in states_df.state.values if state not in guessed_states]

        missed_states_sr = pd.Series(missed_states)
        missed_states_sr.to_csv(TO_LEARN, index_label='States to Learn')

        print("Thanks for playing!\nSee generated CSV for which states that you still need to learn.")

        t.bye()
        break

if score == MAX_SCORE:
    print("Congratulations, you have guessed every state!")
    t.bye()
