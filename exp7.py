#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"
import gymnasium as gym
import numpy as np
import random

# create the Taxi environment
env = gym.make("Taxi-v4")

# Q-table: one row per state, one column per action
Q = np.zeros((env.observation_space.n, env.action_space.n))

alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.1    # exploration chance

# TRAIN
for episode in range(5000):
    state, _ = env.reset()
    done = False

    while not done:
        if random.random() < epsilon:
            action = env.action_space.sample()   # explore
        else:
            action = np.argmax(Q[state])         # exploit

        next_state, reward, terminated, truncated, _ = env.step(action)

        if terminated:
            future = 0                           # trip finished, no next state
        else:
            future = np.max(Q[next_state])

        Q[state, action] += alpha * (
            reward + gamma * future - Q[state, action]
        )

        state = next_state
        done = terminated or truncated

# TEST: play one game using the learned Q-table
state, _ = env.reset()
total = 0
done = False

while not done:
    state, reward, terminated, truncated, _ = env.step(
        np.argmax(Q[state])
    )
    total += reward
    done = terminated or truncated

print("Total reward:", total)

env.close()
