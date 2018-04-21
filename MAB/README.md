## Multi-armed Bandits

### Goals

- Learn about the k-armed bandit problem and various approaches used to tackle it.
- Building a k-armed testbed and evaluating the approaches.

### Summary

- Discussion on different settings:
    - Non-associative setting: actions are taken in only one situation. e.x. k-armed bandit
    - Associative setting: actions are taken in more than one situation
    - Reinforcement learning: actions affect the next situation as well as the reward.
- Description and comparison of various bandit algorithms. 
    - Action value methods (estimate action values and use those estimates to select actions)
      and various heuristics to improve them.
    - Gradient bandit algorithms, in which welearn a numerical preference for each action.
    - Use a 10-armed testbed and parameter study to compare various bandit algorithms

### Lectures & Readings

- Reinforcement Learning: An Introduction - Chapter 2: Multi-armed Bandits

### Exercises

- [Chapter 2 Exercises](Chapter2-Exercises.md)

