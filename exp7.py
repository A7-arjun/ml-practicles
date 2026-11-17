#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"
import gymnasium as gym #taxi environment
import numpy as np #to manage q tables
import random #choose random acton agent choose

# create the Taxi environment
env = gym.make("Taxi-v4")

# Q-table: one row per state, one column per action
Q = np.zeros((env.observation_space.n, env.action_space.n))

alpha = 0.1      # learning rate--how new info changes Q-level
gamma = 0.9      # discount factor--importance given to future reward
epsilon = 0.1    # exploration chance--random action choose chance--10%

# TRAIN
for episode in range(5000):
    state, _ = env.reset() #start new episode
    done = False #task not finished yet

    while not done:
        if random.random() < epsilon: #genrate no. between 0-1
            action = env.action_space.sample()   # explore between 6 actions
        else:
            action = np.argmax(Q[state])         # exploit

        next_state, reward, terminated, truncated, _ = env.step(action)
#new state,reward,naturally fineshed task ,or due to limit
        if terminated:
            future = 0                           # trip finished, no next state
        else:
            future = np.max(Q[next_state])

        Q[state, action] += alpha * ( #update q table formula
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
        np.argmax(Q[state]) #taxi choose reward of highest q value
    )
    total += reward
    done = terminated or truncated

print("Total reward:", total)

env.close()
