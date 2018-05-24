"""
Creates a player for a k-armed bandit
"""
import numpy as np


class Player:
    def __init__(self, bandit,
                 epsilon=0.0,
                 alpha_css=0.0,
                 q_0=0.0,
                 c=0.0,
                 alpha_gb=0.0):
        """
        :param bandit: Instance of MultiArmedBandit class
        :param epsilon: Probability for exploration in epsilon-greedy algorithm
        :param alpha_css: Constant step-size parameter.
        :param q_0: Initial estimate for the values
        :param c: UCB param
        :param alpha_gb: step size for gradient bandit
        """
        self.bandit = bandit  # A player can play with only 1 bandit.
        self.epsilon = epsilon
        self.alpha_css = alpha_css
        self.q_0 = q_0
        self.c = c
        self.alpha_gb = alpha_gb

        self.pref_estimates = np.zeros(self.bandit.num_arms)

        self.value_estimates = q_0 * np.ones(self.bandit.num_arms)
        self.num_samples = np.zeros(self.bandit.num_arms)
        self.curr_step = 0

    def update_estimates(self, arm, val):
        num_samples = self.num_samples[arm]

        if self.alpha_css > 0:
            self.value_estimates[arm] = (1 - self.alpha_css) * self.value_estimates[arm] + self.alpha_css * val
            self.num_samples[arm] += 1.0
            return

        if self.alpha_gb > 0:
            scores = np.exp(self.pref_estimates)
            prob = scores / np.sum(scores)

            self.pref_estimates -= self.alpha_gb * (val - self.value_estimates) * prob
            self.pref_estimates[arm] += self.alpha_gb * (val - self.value_estimates[arm])

        self.value_estimates[arm] = (num_samples * self.value_estimates[arm] + val) / (num_samples + 1.0)

        self.num_samples[arm] += 1.0

    def get_action(self):
        #explore
        if self.epsilon > 0:
            if (np.random.binomial(1, self.epsilon)) == 1:
                return np.random.randint(0, self.bandit.num_arms)

        #exploit
        estimates = None
        if self.c > 0:
            estimates = np.zeros(self.bandit.num_arms)
            for i in range(self.bandit.num_arms):
                if self.num_samples[i] == 0:
                    estimates[i] = float('inf')
                else:
                    estimates[i] = self.value_estimates[i] + \
                                   self.c * np.sqrt(np.log(self.curr_step) / (self.num_samples[i]))

        if self.alpha_gb > 0:
            scores = np.exp(self.pref_estimates)
            estimates = scores / np.sum(scores)  # action probabilities

        if estimates is None:
            estimates = self.value_estimates

        arm = np.random.choice(np.flatnonzero(
            estimates == estimates.max()))

        return arm

    def draw(self):
        """
        With (1-epsilon) prob, draws the greedy arm; Otherwise, draws a random arm
        In either case, updates the estimated value for the action.
        :return: The drawn amount, action as well as whether the selected option was optimal.
        """
        self.curr_step += 1

        arm = self.get_action()
        val = self.bandit.draw(arm)

        self.update_estimates(arm, val)

        # Player class does not need to know if an action is optimal
        # we have just done it for simplicity.
        is_optimal = self.bandit.is_optimal_action(arm)

        self.bandit.update_means_for_random_walk()

        return val, arm, is_optimal

