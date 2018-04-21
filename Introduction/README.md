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
- David Silver's RL Course Lecture 1 - Introduction to Reinforcement Learning
 ([video](https://www.youtube.com/watch?v=2pWv7GOvuf0),
  [slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf))
<!---
- [OpenAI Gym Tutorial](https://gym.openai.com/docs)
-->

### Exercises

- [Chapter 1 Exercises](Chapter1-Exercises.md)
<!---
- [Work through the OpenAI Gym Tutorial](https://gym.openai.com/docs)
-->

 ### General observations while training the tic tac toe player:
- Random player vs random player. Player 1 wins: 58%, Player 2 wins: 30%. 
- RL player (learnt with self play) vs random player. 
    - Player 1 (RL) wins: 99%, (should be ~98%)
    - Player 1 (Random) wins: 4% (should be ~0), Player 2 (RL) wins: 86% (should be ~80%)
    - The errors might be due to the statistical nature of experiments and not achieving a total convergence of values,
  but the observations were bizarre  in the sense that an optimal player is able to beat a random opponent
  more times than as suggested by the statistics.
  
    [Source: Tic Tac Toe Statistics](https://blog.ostermiller.org/tic-tac-toe-strategy)

