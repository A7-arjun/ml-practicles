#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"
import numpy as np
import random

# Create an empty Tic-Tac-Toe board
def create_board():
    return [0] * 9

# Check whether a player has won
def check_winner(b):

    # All possible winning combinations
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    # Check every winning combination
    for a, b1, c in wins:
        if b[a] == b[b1] == b[c] != 0:
            return b[a]

    return 0

# Find all empty positions on the board
def available(b):
    return [i for i in range(9) if b[i] == 0]


# Q-learning settings
Q = {}                 # Stores learned values
alpha = 0.1            # Learning rate
gamma = 0.9            # Future reward importance
epsilon = 0.1          # Random action chance


# TRAINING THE AGENT
for episode in range(10000):

    board = create_board()   # Start a new game
    done = False

    while not done:

        state = tuple(board)       # Current board state
        actions = available(board) # Empty positions

        # Choose a random move or the best learned move
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            values = Q.get(state, [0] * 9)
            action = max(actions, key=lambda x: values[x])

        # Agent (1) makes its move
        board[action] = 1

        winner = check_winner(board)

        # Check whether the agent has won
        if winner == 1:
            reward, done = 1, True

        # Check whether the game is a draw
        elif not available(board):
            reward, done = 0, True

        else:
            # Opponent (-1) makes a random move
            opponent = random.choice(available(board))
            board[opponent] = -1

            winner = check_winner(board)

            # Check whether opponent has won
            if winner == -1:
                reward, done = -1, True

            # Check whether the game is a draw
            elif not available(board):
                reward, done = 0, True

            else:
                reward = 0

        # Get the board after both players' moves
        next_state = tuple(board)

        # Find the best future value
        future = 0 if done else max(
            Q.get(next_state, [0] * 9)[a] for a in available(board)
        )

        # Update the Q-value of the selected move
        old = Q.setdefault(state, [0] * 9)[action]

        Q[state][action] = old + alpha * (
            reward + gamma * future - old
        )

    # Slowly reduce random moves during training
    epsilon = max(0.01, epsilon * 0.999)

print("Training completed!")


# TESTING THE TRAINED AGENT
wins = draws = losses = 0

for game in range(1000):

    board = create_board()  # Start a new game

    while True:

        state = tuple(board)
        actions = available(board)
        values = Q.get(state, [0] * 9)

        # Agent chooses its best learned move
        action = max(actions, key=lambda x: values[x])
        board[action] = 1

        winner = check_winner(board)

        if winner == 1:
            wins += 1
            break

        if not available(board):
            draws += 1
            break

        # Opponent chooses a random move
        opponent = random.choice(available(board))
        board[opponent] = -1

        winner = check_winner(board)

        if winner == -1:
            losses += 1
            break

        if not available(board):
            draws += 1
            break

# Display final results
print("Wins:", wins)
print("Draws:", draws)
print("Losses:", losses)
