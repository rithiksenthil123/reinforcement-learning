from QLearning import QLearning

class MyQLearning(QLearning):
    def update_q(self, prev_state, action_taken, r_observed, new_state, possible_actions, alpha, gamma):
        Q_old = self.get_q(prev_state, action_taken)
        Q_max = max(self.get_action_values(new_state, possible_actions))
        Q_new = Q_old + alpha * (r_observed + gamma * Q_max - Q_old)
        self.set_q(prev_state, action_taken, Q_new)
