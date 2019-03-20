import gym

env = gym.make('CarRacing-v0')
env.reset()

for _ in range(2000):
    env.render()
    env.step(env.action_space.sample())

env.close()
