# AWS DeepRacer - Reward Function (First Iteration)
This repository contains the reward function for optimizing AWS DeepRacer's performance on a specific track. The first iteration encourages staying on track, following the centerline, and maintaining speed while penalizing excessive steering.

# Hyperparameters
Gradient descent batch size
64
Entropy
0.01
Discount factor
0.95
Loss type
Huber
Learning rate
0.0003
Number of experience episodes between each policy-updating iteration
20
Number of epochs
10

# Setup
Action space type
Continuous
Action space
Speed: [ 1.2 : 2 ] m/s
Steering angle: [ -30 : 30 ] °
Framework
Tensorflow
Reinforcement learning algorithm
PPO

# Training Strategy
Initial Testing (20 mins): Verify model stability.
Main Training (80 mins): Focus on speed and track adherence.
Evaluation (30 mins): Final performance check for lap completion and consistency.
