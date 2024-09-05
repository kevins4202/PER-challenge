# PER-challenge
Part 1:
How to run the code:
0. Requirements: Have [git](https://git-scm.com), and [Python3](https://www.python.org/downloads/) installed
1. Clone the repository using 
```sh
  git clone https://github.com/kevins4202/PER-challenge.git
```
2. Run the program using 
```sh
  python3 partA.py
```
Results
Min speed:  0.18995884 MPH
Justification: I decided to use the smallest non-zero speed (since the car will always have to go to zero speed). To Calculate the speed, I took the average of the four wheel speeds. I was thinking about taking an average for each side (front left, back left and front right, back right) and calculating some kind of angle that would give a better measurement of speed, but I could not figure out a formula. The minimum speed is basically the smallest non-zero average of the four wheel speeds.
Max speed:  49.681338499999995 MPH
Justification: This is similar to the calculation for minimum speed, except I used the max function instead of min. I used the same method to calculate the speed.  
Avg speed:  20.961331817332038 MPH
Justification: Since the average is the total/time, I added the speeds at each time interval. I assumed that if at a specific time, the speeds of the wheels were not provided, that the car would maintain relatively the same speed (so I did not update the variables). Even when the speed was 0, after it started moving for the first time I accounted for every speed at every time. For the denominator, I chose to start keeping track of time when the car started moving to the end. I could have ended time when the car stopped, but I was struggling to think of a method and also believed that the excess time would have minimal impact over such a long time frame. 
Total energy:  4.160638179398205 kWh
Justification: Using the formula P = I * V, I added up the power at every interval to get the Riemann sum for Energy. It did non matter when the car started moving since everything factors into total energy, whether the car is in motion or not. I then had to convert to kW by multiplying by 0.001 (the multiplier variable), then converting hours by multiplying by 1 / 3600000. 

Overall, I think I should have checked more for edge cases such as zeros or infinities, but I think I handled them well and they would have minimal impact over such a long time period.

Part 2

