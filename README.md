# archeryMontyCarlo

If you run monty.py, it will run a monty carlo simulation of an archery game (assuming no skill), and result in an example, such as seen in 'Figure_Uniform' or 'Figure_Radial' below:

Uniform:

![](Figure_Uniform.png)

5 zone Scoring: AVG ~3.32
10 zone Scoring: AVG ~3.73

Radial:

![](Figure_Radial.png)

5 zone Scoring: AVG ~5.02
10 zone Scoring: AVG ~5.57

The average across the two scoring styles, the Radial method averages out at a higher average, and is closer to he representation of a skilled archer. 


## Analysis
- data and what


## Evaluation

The two models simulate different aspects of archery. 

The Radial model simulates aiming and stability. 

The Uniform model simulates a basic propensity to miss, and variation in the shot. 


In terms of the accuracy of such a simulation, it is more accurate to run it radially, since Archers aim towards the centre, however because archers are not perfect, there is a slight bias against this and archers on occasion miss, so you can use the two models together to roughly estimate the expected score you would have if an archer was shooting without much skill. 

However simply averaging out the two models fails to meaningfully measure people in terms of skill. 
As Archers improve, their propensity to miss decreases, and so the uniform model becomes less and less accurate at measuring an archer. 

Thus propensity to miss would be a factor that would be desirable.
The propensity to miss never truly reaches zero, however it can get very low, to the point of being unnoticeable on most days. 

Archers aim to hit the gold, and so when skill increases they will reach a point where they will stop hitting other colours entirely, outside of the rare occasion where they might miss. 
Thus, the actual radius of their accuracy is something that would ideally be measured. 

And finally, because archers are human, their skills vary. Each of these factors that model skill you would want some variance for. 

Thus an improved model would include these 4 variables as factors: 
Propensity to miss, propensity variance, radius, and radius variance. 


There still lies a limitation in such a model however. 
When aiming, the arrows will go to a specific location. And it is the grouping, the radius of the circle the arrows land in that is important. 

But you can have a good grouping in a location outside of the gold. The grouping is the actual measure used to demonstrate skill. 
Adjusting the location of the grouping is largely trivial, although there are psychological issues that occur sometimes and get in the way. 


## Conclusion 

Nuances to take into consideration: 

1. What these models are, is a way to measure if you are doing better than random luck. 

They are two different aspects in what it means to shoot an arrow. 


2. What these models are not, is a way to measure skill. These models cannot quantify accuracy, nor skill. 

Skill, the ability to hit the point that you want to hit. Note that this is separate from the ability to hit the point you are aiming at. 

Accuracy, determined by the consistency of shot and the proportion of shots where point of aim = point you want to hit. This is a basic definition.

Golds, a measure that in Target archery is used as a proxy of skill. 


There is no way of calculating accuracy using these models. Accuracy involved a human's desired; same for skill. 


Skill and Golds can be assumed to be correlated to one another. A skilled archer will have a lot of golds. An archer with a lot of golds is likely to be skilled. 

Within the context of Target archery, it is undeniable to also assume accuracy and golds are correlated, because golds is used as a proxy for accuracy, archers naturally self select and aim to increase golds. 

However outside of this context, a scoring system based on what colours you hit, accuracy and golds are not strongly correlated. 


This correlation comes out through the sport and people desiring to perform well. The selection for hitting golds comes about from the points system. 
If you ignore the points, 

Secondly you can shoot at 


There is a correlation between skill and accuracy, however it does not have an intrinsic correlation. It is one that comes out of the sport through the people; and their desire to perform well. It is not one intrinsic to the act of shooting a bow. It is a natural consequence in the sport within the context of the 5 and 10 zone scoring methods, and outside of this context there is no correlation -- this is wrong, it assumes accuracy is hitting the gold, which is true within the context of target archery

People can choose to aim at something other than the gold to hit it accurately. 





Skill is slightly unrelated to accuracy. There is a correlation, however even if you are skilled, you can shoot badly with small samples or unusual conditions, or shoot dramatically better than either of the two models. 

Thus, higher levels of skill live within being able to counteract this multitude of forces to be able to be accurate. 


The two models I have are a Radially distributed model, and a more Uniformly distributed model. I call these, but you could argue that both are uniformly distributed against a corresponding parameter, since the radial model is uniformly distributed based on the radius, with a roughly equal number of points within each ring. However, because a circle's outer rings are bigger, this causes them to naturally have a much lower density of points than the inner most rings. 
The uniform model is uniformly distributed amongst the x and y axes. 

The current representation in figure 1 doesn't create random points radially, but alone the two axes. It's not a large change, just using a radius from a centre point and an angle. Realistically the angle doesn't matter for the distribution but makes it more apparent seeing it around the centre instead of one line going in one direction. If I ever get back to this project, I shall implement this functionality. 


Interesting websites / sources:
- https://stackoverflow.com/questions/28567166/uniformly-distribute-x-points-inside-a-circle
- https://www.ncasarchery.org.uk/tournaments_events/scoring-rounds/metric-scoring-rounds/





