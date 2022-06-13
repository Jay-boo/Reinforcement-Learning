import gym
import matplotlib.pyplot as plt
import numpy as np

#---------------------
# Initialisation
env=gym.make("FrozenLake-v1")
transition_probs=env.P
env.reset(return_info=True)
