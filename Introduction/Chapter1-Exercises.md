### Exercises on Tic-tac-toe example

- **Exercise 1.1: Self-Play Suppose, instead of playing against a random opponent, the
reinforcement learning algorithm described above played against itself, with both sides
learning. What do you think would happen in this case? Would it learn a different policy
for selecting moves?**
  - The agent will learn the global optimal policy for the game. In case of self play,
    the value function over the states is shared between the two sides, and
    it will converge to the true probabilities of winning from a state.
    In case of a random opponent, the agent's policy might be tuned to exploiting the mistakes
    of his opponent, and won't be same as the best policy.

- **Exercise 1.2: Symmetries Many tic-tac-toe positions appear different but are really
the same because of symmetries. How might we amend the learning process described
above to take advantage of this? In what ways would this change improve the learning
process? Now think again. Suppose the opponent did not take advantage of symmetries.
In that case, should we? Is it true, then, that symmetrically equivalent positions should
necessarily have the same value?**
  - When we update the value for a state, we can also update it for the states which are symmetrically
    equivalent to the current state, this can make the learning faster and lead to faster convergence.
  - No, because opponent's behavior can be different and in some cases suboptimal, in some of the
    symmetrically equivalent states, and we should take advantage of that. No, the symmetrically
    equivalent positions can have different values based on the opponent and policy.

- **Exercise 1.3: Greedy Play Suppose the reinforcement learning player was greedy, that
is, it always played the move that brought it to the position that it rated the best. Might
it learn to play better, or worse, than a nongreedy player? What problems might occur?**
  - It will be worse than a non-greedy player because it won't be able to explore and take
    actions which can lead to rewards in the long term. Exploration also helps improve/correct 
    value estimates of states which would not have been visited otherwise. It is analogous to exploration vs
    exploitation tradeoff in RL, and both the extremes (only exploitation and only explorations)
    are worse than a combination.

- **Exercise 1.4: Learning from Exploration Suppose learning updates occurred after all
moves, including exploratory moves. If the step-size parameter is appropriately reduced
over time (but not the tendency to explore), then the state values would converge to a
set of probabilities. What are the two sets of probabilities computed when we do, and
when we do not, learn from exploratory moves? Assuming that we do continue to make
exploratory moves, which set of probabilities might be better to learn? Which would
result in more wins?**
  * Firstly it is clear that the values (which can to be interpreted as probabilities here) will converge over time if the step
size is appropriately reduced.
  * We think that if we do'nt learn from the exploratory moves, we will end up computing the values for the optimal policy. That is because even
  though exploratory moves are being made, they are only helping us refine our estimates under the curreny policy for all states without starving
  the updates for states with low values. However if we learn from exploratory moves, depending on the rate of exploration we'll learn the values
  for an exploratory policy - where we only play optimally sometimes and randomly the rest of the times. It should probably also hold that the values
  for every state under the optimal policy is bigger than or equal to corresponding values under the exploratory policy. 
  
  * Assuming that we still make exploratory moves, it is still better to learn the values of the optimal policy. As an example, let's say that we
  make only one exploratory move in the game. Consider 2 scenarios: In scenario 1, we assign the values of the exploratory policy
  to our states. In scenario 2 we assign the values of the optimal policy. Let's firther assume the random move is played on the first move (i.e, from
  the start state). In this case it is easy to see that sceario 2 is better because we will follow better value paths after the 1st move. It feels like
  this idea should be extensible to more general cases in some kind of recursive manner.
   

- **Exercise 1.5: Other Improvements Can you think of other ways to improve the re-
inforcement learning player? Can you think of any better way to solve the tic-tac-toe
problem as posed?**
  * Apart from exploiting symmetries while finding the optimal strategies, and incporating value feedback from opponent under self play mode, I would try modifying the rewards function to further encourage certain kinds of play. For example, I'd check if setting the reward to negative on a loss might improve convergence.

  ### General observations while training the tic tac toe player:
  * We often found that the player learnt through slef play was beating the random player ~ 99% of the time when playing first, and ~ 86% of the time while playing second. In the second case the random player also won a few games (~3-4%) which we think happened because of incomplete convergence of values in our training.
  In any case, this seems very bizzare as accoring to several sources we could find on the internet, an optimal player beats a random player ~98% while playing first
  and ~80% while playing second (example, check https://blog.ostermiller.org/tic-tac-toe-strategy). Our stats seem better than the optimal player against a random opponent. We can't get our head around it.
