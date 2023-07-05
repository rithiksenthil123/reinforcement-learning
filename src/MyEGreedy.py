import random


class MyEGreedy:
    def __init__(self):
        pass

    def get_random_action(self, agent, maze):
        valid_action_list = maze.get_valid_actions(agent)
        random_idx = random.randrange(0, len(valid_action_list))
        return valid_action_list[random_idx]

    def get_best_action(self, agent, maze, q_learning):
        valid_action_list = maze.get_valid_actions(agent)
        action_values = q_learning.get_action_values(agent.get_state(maze), valid_action_list)
        max_indeces = [i for i in range(len(action_values)) if action_values[i] == max(action_values)]
        return valid_action_list[random.choice(max_indeces)]

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        rand_num = random.uniform(0, 1)
        if rand_num <= epsilon:
            return self.get_random_action(agent, maze)
        else:
            return self.get_best_action(agent, maze, q_learning)
