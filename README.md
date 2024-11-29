# AWS DeepRacer - Reward Function (First Iteration)
This repository contains the reward function for optimizing AWS DeepRacer's performance on a specific track. The first iteration encourages staying on track, following the centerline, and maintaining speed while penalizing excessive steering.

# Hyperparameters
Min Speed: 1.5 m/s
Max Speed: 2.5 m/s
Learning Rate: 1e-4
Discount Factor (Gamma): 0.95
Clipping Epsilon: 0.2
Batch Size: 64

# Training Strategy
Initial Testing (20 mins): Verify model stability.
Main Training (80 mins): Focus on speed and track adherence.
Evaluation (30 mins): Final performance check for lap completion and consistency.
