from stable_baselines3 import PPO

model = PPO('MlpPolicy', 'CartPole-v1')
model.learn(100)