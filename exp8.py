
import numpy as np
import random

# Create Tic-Tac-Toe board
def create_board():
    return [0] * 9

# Check winner
def check_winner(b):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b1, c in wins:
        if b[a] == b[b1] == b[c] != 0:
            return b[a]
    return 0

# Get empty positions
def available(b):
    return [i for i in range(9) if b[i] == 0]

# Q-learning parameters
Q = {}
alpha = 0.1
gamma = 0.9
epsilon = 0.1

# Training
for episode in range(10000):
    board = create_board()
    done = False

    while not done:
        state = tuple(board)
        actions = available(board)

        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            values = Q.get(state, [0] * 9)
            action = max(actions, key=lambda x: values[x])

        board[action] = 1
        winner = check_winner(board)

        if winner == 1:
            reward, done = 1, True
        elif not available(board):
            reward, done = 0, True
        else:
            opponent = random.choice(available(board))
            board[opponent] = -1
            winner = check_winner(board)

            if winner == -1:
                reward, done = -1, True
            elif not available(board):
                reward, done = 0, True
            else:
                reward = 0

        next_state = tuple(board)
        future = 0 if done else max(
            Q.get(next_state, [0] * 9)[a] for a in available(board)
        )

        old = Q.setdefault(state, [0] * 9)[action]
        Q[state][action] = old + alpha * (
            reward + gamma * future - old
        )

    epsilon = max(0.01, epsilon * 0.999)

print("Training completed!")

# Testing
wins = draws = losses = 0

for game in range(1000):
    board = create_board()

    while True:
        state = tuple(board)
        actions = available(board)
        values = Q.get(state, [0] * 9)

        action = max(actions, key=lambda x: values[x])
        board[action] = 1

        winner = check_winner(board)

        if winner == 1:
            wins += 1
            break
        if not available(board):
            draws += 1
            break

        opponent = random.choice(available(board))
        board[opponent] = -1
        winner = check_winner(board)

        if winner == -1:
            losses += 1
            break
        if not available(board):
            draws += 1
            break

print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)
