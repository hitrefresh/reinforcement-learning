### Exercises on Tic-tac-toe example

- Exercise 1.1: Self-Play Suppose, instead of playing against a random opponent, the
reinforcement learning algorithm described above played against itself, with both sides
learning. What do you think would happen in this case? Would it learn a different policy
for selecting moves?
  - The agent will learn the global optimal policy for the game. In case of self play,
    the value function over the states is shared between the two sides, and
    it will converge to the true probabilities of winning from a state.
    In case of a random opponent, the agent's policy might be tuned to exploiting the mistakes
    of his opponent, and won't be same as the best policy.

- Exercise 1.2: Symmetries Many tic-tac-toe positions appear different but are really
the same because of symmetries. How might we amend the learning process described
above to take advantage of this? In what ways would this change improve the learning
process? Now think again. Suppose the opponent did not take advantage of symmetries.
In that case, should we? Is it true, then, that symmetrically equivalent positions should
necessarily have the same value?
  - When we update the value for a state, we can also update it for the states which are symmetrically
    equivalent to the current state, this can make the learning faster and lead to faster convergence.
  - No, because opponent's behavior can be different and in some cases suboptimal, in some of the
    symmetrically equivalent states, and we should take advantage of that. No, the symmetrically
    equivalent positions can have different values based on the opponent and policy.

- Exercise 1.3: Greedy Play Suppose the reinforcement learning player was greedy, that
is, it always played the move that brought it to the position that it rated the best. Might
it learn to play better, or worse, than a nongreedy player? What problems might occur?
  - It will be worse than a non-greedy player because it won't be able to explore and take
    actions which can lead to rewards in the long term. It is analogous to exploration vs
    exploitation tradeoff in RL, and both the extremes (only exploitation and only explorations)
    are worse than a combination.

- Exercise 1.4: Learning from Exploration Suppose learning updates occurred after all
moves, including exploratory moves. If the step-size parameter is appropriately reduced
over time (but not the tendency to explore), then the state values would converge to a
set of probabilities. What are the two sets of probabilities computed when we do, and
when we do not, learn from exploratory moves? Assuming that we do continue to make
exploratory moves, which set of probabilities might be better to learn? Which would
result in more wins?

- Exercise 1.5: Other Improvements Can you think of other ways to improve the re-
inforcement learning player? Can you think of any better way to solve the tic-tac-toe
problem as posed?
