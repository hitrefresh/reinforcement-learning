### Exercises on Tic-tac-toe example

- **Exercise 2.1 In ε-greedy action selection, for the case of two actions and ε = 0.5, what is
the probability that the greedy action is selected?**

- **Exercise 2.2: Exercise 2.2: Bandit example Consider a k-armed bandit problem with k = 4 actions,
denoted 1, 2, 3, and 4. Consider applying to this problem a bandit algorithm using
ε-greedy action selection, sample-average action-value estimates, and initial estimates
of Q1(a) = 0, for all a. Suppose the initial sequence of actions and rewards is A1 = 1,
R1 = 1, A2 = 2, R2 = 1, A3 = 2, R3 = 2, A4 = 2, R4 = 2, A5 = 3, R5 = 0. On some
of these time steps the ε case may have occurred, causing an action to be selected at
random. On which time steps did this definitely occur? On which time steps could this
possibly have occurred?**


- **Exercise 2.3 In the comparison shown in Figure 2.2, which method will perform best in
the long run in terms of cumulative reward and probability of selecting the best action?
How much better will it be? Express your answer quantitatively.**


- **Exercise 2.4 If the step-size parameters, αn, are not constant, then the estimate Qn is
a weighted average of previously received rewards with a weighting different from that
given by (2.6). What is the weighting on each prior reward for the general case, analogous
to (2.6), in terms of the sequence of step-size parameters?**

   

- **Exercise 2.5 (programming) Design and conduct an experiment to demonstrate the
difficulties that sample-average methods have for nonstationary problems. Use a modified
version of the 10-armed testbed in which all the q∗(a) start out equal and then take
independent random walks (say by adding a normally distributed increment with mean
zero and standard deviation 0.01 to all the q∗(a) on each step). Prepare plots like
Figure 2.2 for an action-value method using sample averages, incrementally computed,
and another action-value method using a constant step-size parameter, α = 0.1. Use
ε = 0.1 and longer runs, say of 10,000 steps.**


- **Exercise 2.7: Unbiased Constant-Step-Size Trick In most of this chapter we have used
sample averages to estimate action values because sample averages do not produce the
initial bias that constant step sizes do (see the analysis in (2.6)). However, sample
averages are not a completely satisfactory solution because they may perform poorly
on nonstationary problems. Is it possible to avoid the bias of constant step sizes while
retaining their advantages on nonstationary problems? One way is to use a step size of
βt .= α/o¯t, (2.8)
where α > 0 is a conventional constant step size, and o¯t is a trace of one that starts at 0:
o¯t+1
.= ¯ot + α(1 − o¯t), for t ≥ 1, with ¯o1
.= α. (2.9)
Carry out an analysis like that in (2.6) to show that βt is an exponential recency-weighted
average without initial bias.
**

- **Exercise 2.8: UCB Spikes In Figure 2.4 the UCB algorithm shows a distinct spike
in performance on the 11th step. Why is this? Note that for your answer to be fully
satisfactory it must explain both why the reward increases on the 11th step and why it
decreases on the subsequent steps. Hint: if c = 1, then the spike is less prominent.**


- **Exercise 2.9 Show that in the case of two actions, the soft-max distribution is the same
as that given by the logistic, or sigmoid, function often used in statistics and artificial
neural networks.**

- **Exercise 2.10 Suppose you face a 2-armed bandit task whose true action values change
randomly from time step to time step. Specifically, suppose that, for any time step, the
true values of actions 1 and 2 are respectively 0.1 and 0.2 with probability 0.5 (case A),
and 0.9 and 0.8 with probability 0.5 (case B). If you are not able to tell which case you
face at any step, what is the best expectation of success you can achieve and how should
you behave to achieve it? Now suppose that on each step you are told whether you are
facing case A or case B (although you still don’t know the true action values). This is an
associative search task. What is the best expectation of success you can achieve in this
task, and how should you behave to achieve it?**

- **Exercise 2.11 (programming) Make a figure analogous to Figure 2.6 for the nonstationary
case outlined in Exercise 2.5. Include the constant-step-size ε-greedy algorithm with
α= 0.1. Use runs of 200,000 steps and, as a performance measure for each algorithm and
parameter setting, use the average reward over the last 100,000 steps.**