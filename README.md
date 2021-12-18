# Mathmatical-Foundation-of-Data-Science

# A Crossing the Desert


Team Members：[Ronnie](https://github.com/mahfuztbt)
[Apel](https://github.com/apel2021)
[Zulker](https://github.com/ZulkRS) 
[Prince](https://github.com/awprince69) 
[Hasan](https://github.com/hasan120328) 
[Hasib](https://github.com/hasib-mmu007)

School of software, Sotware Engineering



## content

- [Problem introduction] ($Experience introduction)
  - [Resource allocation problem]
    - Problem introduction
    - Solving ideas
  - [Optimal Decision-Making Problem Solving]
    - Problem introduction
    - Solving ideas
  - [Dynamic Game Problem] 
    - Problem introduction
    - Solving ideas
- [Experience introduction] 


## Resource allocation problem

### Problem introduction

The first and second levels are similar. Both players make decisions when the weather is certain. There is an optimal strategy. After simplifying the model, we can establish a state transition equation and solve the optimal strategy through dynamic programming.




### Solution ideas

Establish state transition equation and stage profit and loss function, then dynamic programming can be solved.

Since there are different supply strategies at the starting point (day 0), these strategies will affect the initial state, and then the decision sequence and final result during the game. Therefore, a multiple search algorithm is used to consider the replenishment of water and food on the 0th day, and search all replenishment strategies on the 0th day. Each replenishment strategy corresponds to an initial state. After determining the initial state, the dynamic programming model is used to calculate the optimal strategy corresponding to each initial state. Finally, the optimal strategy is selected from the optimal strategies corresponding to all the initial states, which is the global optimal strategy of the level.

In maps with villages, too many village replenishment strategies greatly increase the computational complexity. Therefore, the algorithm is optimized using the strategy of "use first and then bookkeeping": Allow resource gaps, and each time you pass through the village or reach the destination, if there is a gap in resources, check whether the gap can be met the last time you pass through the village. If it can be met, the gap will be filled and the funds will be deducted to ensure the minimum replenishment; if it cannot be met (exceeding the weight or insufficient funds when passing through the village last time), pruning will be carried out and the recurrence of this state will be stopped. In addition, considering that the solution direction of the model and the direction of the state transition function are both positive, the classical dynamic programming algorithm is improved by combining the memory search algorithm in the solution process. 
![image](https://user-images.githubusercontent.com/67628125/146635840-0d39998a-946a-4d18-a25e-3745639adcf9.png)
![image](https://user-images.githubusercontent.com/67628125/146635849-111b4dbf-1e35-4fbe-ac33-dc9d96a7311b.png)


## Optimal decision problem

### Problem introduction

The third and fourth hurdles are all uncertain decision-making problems. Because all the weather is uncertain, the decision-making problems are more complicated. We need to simplify the decision-making path, analyze the benefits of choosing different strategies in different weather, and finally make a decision.



### Solving process

First, establish the entire decision-making process and constraint equations. Players have a total of several options, choose to go directly to the end point, or go to the mine/village and then go to the end point; in the whole process, a certain constraint equation needs to be met.
![image](https://user-images.githubusercontent.com/67628125/146635903-31f5b49d-321c-4381-93d4-5d17e10479b4.png)
![image](https://user-images.githubusercontent.com/67628125/146636056-86b252dd-a68e-4f57-8d0c-a1f9ef938228.png)


Based on the above decision-making process, analyzing the termination conditions and mining conditions of each decision analysis, we can find that the food and water purchased at the initial point can be profited by mining, while the mining profit of the materials purchased in the village is negative. . At the same time, further considering the initial purchase, it is necessary to maximize the number of days that can eventually be mined. However, due to the uncertainty of the weather, it may cause an imbalance of water and food, but it can be obtained by calculation. No matter how the imbalance is, go to the village to buy resources. Re-mining is not cost-effective, and the following results can be obtained in the end:

![image](https://user-images.githubusercontent.com/67628125/146636075-4effe964-d631-4016-b0a8-50e07c4293df.png)


The third level is similar. According to a certain purchase strategy, when the weather is all sunny, it happens to be able to mine one more time, and the best answer is the only one.

## Dynamic game problem

### Problem introduction

The fifth and sixth levels are all about multi-player participation. The weather in the fifth level is determined, and the weather in the sixth level is uncertain. The complexity of the problem lies in the fact that there is no communication between players and there is a game relationship. If the decisions are the same, the comprehensive income will be low. Considering that in the actual game process, the players are all risky, so we can treat the players The risk propensity of the system is defined, and then the Markov state transition process and Monte Carlo simulation are used to simulate, so as to obtain the final analysis.



### Solving process

Set risk preferences and establish state transition equations for different risk preferences, as follows

![image](https://user-images.githubusercontent.com/67628125/146636193-6ec6e0a6-a3d5-45b6-ab23-5c3c0040ed83.png)

The Monte Carlo simulation method is used to construct a simulation program to simulate the Markov decision process of players with different risk acceptance levels, and then to explore the impact of risk acceptance on the pros and cons of players' decision-making.

In each simulation, all players have exactly the same initial conditions except for the degree of risk acceptance (state transition probability), and the degree of risk acceptance of each player is randomly specified by the program. At each stage, the player considers whether there is a conflict between the possible action directions of other players and the optimal sub-strategy from the current position to the end of the player. If there is a conflict, the decision to go to the conflict point or detour is made according to the degree of risk acceptance. The solution method of the optimal sub-strategy in the simulation process is the same as the solution method of dynamic programming in problem one. After each simulation, record the decision path of each player and the final remaining funds. If the player fails to reach the end (game failure) due to insufficient resources or funds, the final remaining funds will be 0. 

Analysis of the simulation results shows that among the players with the most remaining funds, the proportion of players with the highest risk acceptance among the three players in the government game is about 40% (the highest proportion), and most of these players are risk-appreciative. And risk averse. However, the simulation results also show that too many conflicts brought about by too high risk acceptance will consume too many resources and cause the game to fail. In order to explore the appropriate risk acceptance level, the risk acceptance level of all game failed players is counted, and a histogram can be drawn and kernel density estimation can be performed. The result is shown in Figure 14.

![image](https://user-images.githubusercontent.com/67628125/146636214-d59fead3-37ec-43fb-9f02-53e7a164a191.png)

## Summary of experience

**Team situation**: All the seniors in the senior year

**Pre-match preparation**: The three students have insufficient experience in participating, and have not prepared in advance or read any information. However, there are some prerequisite courses such as decision simulation, algorithm analysis and design, operations research, game theory, optimization methods, etc. Some projects have been done in the class, and some projects on resource optimization and decision-making problems have been done. I have read a lot of materials in this area. The two students in the group are basically preparing for direct Ph.

**Question selection**: After seeing the question that night, the threshold of question C is too low, question A is not very familiar, question B is completely in our area of ​​expertise, and we will simply discuss the consequences and choose question B.



**Schedule**: Our schedule is relatively calm. We didn’t do anything on Thursday. The first and second questions started on Friday and we basically finished it at noon on Saturday. We did not stay up late. WeChat and Zoom communicated new findings. And the progress, the third question encountered some problems, probably finished at noon on Sunday, and the second question was added and revised at noon and afternoon on Sunday, and then submitted after finishing on Sunday afternoon.

**Summary**: Judging from our team's experience in the game, because this country one is relatively easy to take, and we didn't stay up late and check the information. Although frankly speaking, we are not so satisfied. The essence In the mathematical modeling competition, mathematical tools are used to solve real-world problems. Therefore, theoretically speaking, it is most important to have a better ability to solve mathematical problems encountered through code, data processing and modeling. Winning should only be natural.

