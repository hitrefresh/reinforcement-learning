"""
Defines a k-armed bandit, with the option
of making the reward distribution non-stationary
"""
import numpy as np
import random


class MultiArmedBandit:
    """
    Defines a k-armed bandit
    """
    def __init__(self, num_arms=10, initial_reward_mean=0.0,
                 initial_reward_variance=0.0, reward_draw_variance=1.0,
                 random_walk_speed=0.01):
        """
        Initialized the bandit based on parameters.

        :param num_arms: Num bandit arms
        :param initial_reward_mean: Initial mean of all rewards.
        :param initial_reward_variance: Initial variance to fix the initial means
        :param reward_draw_variance: Variance around the reward mean for draws
        :param random_walk_speed: Mean rewards change at this rate
        """
        self.num_arms = num_arms
        self.initial_reward_mean = initial_reward_mean
        self.initial_reward_variance = initial_reward_variance

        # all means will initialized to 0 by default
        self.means = np.random.normal(loc=self.initial_reward_mean,
                                      scale=self.initial_reward_variance,
                                      size=self.num_arms)

        self.reward_draw_variance = reward_draw_variance
        self.random_walk_speed = random_walk_speed

    def draw(self, arm):
        """
        Draw a reward given the arm (action chosen)
        :param arm: arm number
        :return: reward value
        """
        return np.random.normal(self.means[arm], scale=self.reward_draw_variance)

    def is_optimal_action(self, action):
        """
        Return if an action is optimal. Here action is just an
        :param action: Corresponds to arm number
        """
        optimal_action = np.argmax(self.means)
        return optimal_action == action

    def update_means_for_random_walk(self):
        """
        Update the means after sampling from reward_draw distribution
        """
        self.means += np.random.normal(loc=0, scale=self.random_walk_speed, size=self.num_arms)

    def print_vars(self):
        """
        Prints the parameters of bandit
        """
        printable_means = [round(v, 2) for v in self.means]
        print("reward means:", printable_means)
        print("reward_draw_variance:", self.reward_draw_variance)
        print("random_walk_speed:", self.random_walk_speed)
