![infected and recovered](https://github.com/mkhalai/Disease-Spread/blob/master/model.png)
# Disease-Spread
An animated visualization of how infections diseases spread over time using matplotlib.animation and numpy.

## Usage
The model has 3 adjustable model paramaters and 3 initial conditions:
### infection_radius (default = 0.6)
All uninfected people that enter within the given radius of a contagious person becomes infected.
### recovery_rate (default = 0.01)
By the end of each step, each infected person on the stage has the above probability of recovery. Once recovered, this person is granted permanent immunity.
### stage_dimension (default = 20)
Sets an M x M stage with (0,0) as the stage centre. Changing the stage are will have the effect of increasing or decreasing the number of interactions any given person will have.
### initial conditions
population size (default = 100), initial infected (2), initial removed (0)






