# Robot Supermarket Navigation with Q-learning

This repository contains a project that focuses on helping a robot learn an optimal route in a labyrinth-like supermarket maze through rewards. The objective is to train the robot to navigate from a fixed starting point to a rewarded target location by leveraging Reinforcement Learning (RL) techniques, specifically Q-learning.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

The Robot Supermarket Navigation project aims to enable a robot to learn an efficient route in a maze-like supermarket environment. The robot learns this route through multiple rounds of exploration and reinforcement. The supermarket maze is represented as a labyrinth, where the target location yields a reward. Q-learning, a model-free off-policy RL algorithm, is utilized to train the robot.

The key components of the project include:

- **Q-learning**: Q-learning is a reinforcement learning technique that uses a tabular representation to determine the optimal actions for each state in the maze. A Q-table, represented as a matrix with two dimensions (S, A), stores the Q-values, representing the value of an action in a particular state. The Q-value update rule implemented in this project is:

  Q(s, a)_new = Q(s, a)_old + α(r + γ * Q(s', a_max) - Q(s, a)_old)

  where Q(s', a_max) is the Q-value of the best action in the next state s', r is the reward received, α is the learning rate, and γ is the discount factor.

- **ϵ-Greedy Exploration**: To control the exploration-exploitation trade-off, the ϵ-Greedy method is implemented for action selection. The robot takes a random action with a probability of ϵ (exploration) or selects the action with the highest predicted value so far (greedy action) with a probability of 1-ϵ (exploitation). By varying the ϵ value, the level of exploration can be controlled.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Install any required dependencies specified in the project's requirements.

## Usage

Follow these steps to use the Robot Supermarket Navigation project:

1. Set up the labyrinth-like supermarket maze, including the starting point and the target location that yields a reward.

2. Configure the Q-learning parameters, such as the learning rate (α), discount factor (γ), and exploration rate (ϵ).

3. Run the Q-learning algorithm to train the robot on the maze environment. The robot will explore different paths, receive rewards, and update the Q-values accordingly using the Q-value update rule.

4. Analyze the Q-values or the learned policy to determine the optimal route from the starting point to the rewarded target location.

Feel free to modify the code, experiment with different parameters, and enhance the project to suit your specific requirements.

## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name for your feature or bug fix.

3. Implement your changes, documenting and testing them as necessary.

4. Submit a pull request, providing a clear explanation of your modifications and their benefits.

---

Train your robot to navigate efficiently through a labyrinth-like supermarket maze using Q-learning and the ϵ-Greedy exploration method. Explore the repository, experiment with different configurations, and help your robot find the optimal route to the rewarded target location.

Happy navigating!
