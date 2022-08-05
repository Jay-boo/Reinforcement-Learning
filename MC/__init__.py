import gym
import matplotlib.pyplot as plt
from utils import plot_state_values
env = gym.make("Blackjack-v1")
print("---------------")
print(env.action_space)
print(env.observation_space)

print("---------------")


def generate_episode_deterministic(env):
    '''
        Generate a trajectory based on a deterministic policy detailled by int(state[0] <=18)
    '''
    state = env.reset()
    episode = []
    counter=0
    while True:
        action = int(state[0] <= 18) #our policy
        next_state, reward, terminate, _ = env.step(action)
        episode.append((state, action, reward))
        state = next_state
        counter+=1
        if terminate:
            break
    return episode

def MCV(env,generate_eps,gamma,episodes):
    """
        first visited Mont Carlos
    """
    V,returns={},{}

    for episode in range(episodes):
        trajectory = generate_eps(env)
        visited_state = set()
        G,T =0,len(trajectory)

        for i in range(T-1,-1,-1):# Going back through the trajectory
            state,action,reward=trajectory[i]

            #--------------
            
            G+= gamma**i *reward
            if state not in visited_state:
                reward,visits=returns.get(state,[0,0])
                returns[state]=[reward+G,visits+1]
                visited_state.add(state)

    for state ,(sum_reward,n_visits) in returns.items():
        V[state]=sum_reward /n_visits

    return V



n_episodes =10000

V=MCV(env,generate_episode_deterministic,1,n_episodes)

plot_state_values(V,n_episodes)         



# Monte Carlo for estimating Q matrix
