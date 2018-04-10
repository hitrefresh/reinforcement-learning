## Introduction

### Goals

- Learn about the definition of Reinforcement Learning (RL) problem and its key elements.
- Early history of RL and how the field evolved over time.

### Summary

- RL is learning from interactions, how to map situations to actions, to maximize rewards.
- Key distinguishing features from supervised learning:
  - No supervised labels, only rewards which are delayed
  - Sequential, time really matters
  - Interaction with environment, agent's action determine the subsequent data it receives.
- An agent: interacts with environment via: sensation ( which state I am in), actions, goal (maximize rewards).
- Elements of RL: agent and environment, subelements: policy, reward, value function, model of environment.

### Lectures & Readings

- Reinforcement Learning: An Introduction - Chapter 1: Introduction
- David Silver's RL Course Lecture 1 - Introduction to Reinforcement Learning ([video](https://www.youtube.com/watch?v=2pWv7GOvuf0), [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf))
<!---
- [OpenAI Gym Tutorial](https://gym.openai.com/docs)
-->

### Exercises

- [Chapter 1 Exercises](Chapter1-Exercises.md)
<!---
- [Work through the OpenAI Gym Tutorial](https://gym.openai.com/docs)
-->

 ### General observations while training the tic tac toe player:
  * We often found that the player learnt through slef play was beating the random player ~ 99% of the time when playing first, and ~ 86% of the time while playing second. In the second case the random player also won a few games (~3-4%) which we think happened because of incomplete convergence of values in our training.
  In any case, this seems very bizzare as accoring to several sources we could find on the internet, an optimal player beats a random player ~98% while playing first
  and ~80% while playing second (example, check https://blog.ostermiller.org/tic-tac-toe-strategy). Our stats seem better than the optimal player against a random opponent. We can't get our head around it.
