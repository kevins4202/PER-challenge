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
Results\
Min speed:  0.18995884 MPH\
Justification: I decided to use the smallest non-zero speed (since the car will always have to go to zero speed). To Calculate the speed, I took the average of the four wheel speeds. I was thinking about taking an average for each side (front left, back left and front right, back right) and calculating some kind of angle that would give a better measurement of speed, but I could not figure out a formula. The minimum speed is basically the smallest non-zero average of the four wheel speeds.\
Max speed:  49.681338499999995 MPH\
Justification: This is similar to the calculation for minimum speed, except I used the max function instead of min. I used the same method to calculate the speed.\
Avg speed:  20.961331817332038 MPH\
Justification: Since the average is the total/time, I added the speeds at each time interval. I assumed that if at a specific time, the speeds of the wheels were not provided, that the car would maintain relatively the same speed (so I did not update the variables). Even when the speed was 0, after it started moving for the first time I accounted for every speed at every time. For the denominator, I chose to start keeping track of time when the car started moving to the end. I could have ended time when the car stopped, but I was struggling to think of a method and also believed that the excess time would have minimal impact over such a long time frame. 
Total energy:  4.160638179398205 kWh\
Justification: Using the formula P = I * V, I added up the power at every interval to get the Riemann sum for Energy. It did not matter when the car started moving since everything factors into total energy, whether the car is in motion or not. I then had to convert to kW by multiplying by 0.001 (the multiplier variable), then converting hours by multiplying by 1 / 3600000. \\

Overall, I think I should have checked more for edge cases such as zeros or infinities, but I think I handled them well and they would have minimal impact over such a long time period.\\

Part 2\
Run the program using 
```sh
  python3 partB.py
```
Make sure to have the .txt file in the same directory as partB.py\
Results\
Min speed:  0.6621164017326994 MPHH\
Justification: Like part A, I decided to use the smallest non-zero speed. I used the average of the left and right wheel speeds. To deal with faulty data, I noticed some of the values were more than 700 miles per hour, or negative which is obviously not possible. Usually this occured with one side seeming to have a normal speed and the other being much greater. I decided to solve this problem by only updating the speed when the difference is less than 50 MPH and the speed was positive. I think I could have analyzed the data deeper, but I could not think of a way to detect when data was corrupt. \
Max speed:  67.67033311454048 MPH\
Justification: My method of using the absolute difference seemed to produce a reasonable max speed, but I do not know if this is right. \
Average speed:  29.02550708230085 MPH\
Justification: I added the speeds at each time interval, multiplied by delta time. I assumed that the time values were not corrupt but this could have been possible and easy to check by comparing the current one to the previous/next one.
Total energy:  6.267346850672142 kWhh\
Justification: I used a similar method as before, except that I did not count negative values. I looked at the max/min voltage and current and they seemed reasonable at 200-300 volts or amps, so I did not filter out any positive values. \

I am sure I missed some cases and that my values have some error, but comparing them to the first part they were similar. \
\
Part 3:
Encode the .csv file using 
```sh
  python3 encode.py
```
Decode the .bin file using
Run the program using 
```sh
  python3 decode.py
```
The decoded file will appear in the parent directory of the repository since it is large.\
Extensibility\
My data format is self-explanatory because there is no external file required. It is like the csv but with spaces and colons as separators. I chose this because it would be easy to both encode and decode, as well as understand\
2. Space efficiency: I chose to encode the files in binary since that is very space efficient. I tried hex at first but that was not as efficient as binary. I also compressed it using the zlib library but had some issues with decompression (the code does not work and I am getting blank lines when reading the file).\
3. Maintainability\
I think the code is easy to understand because it is in two main sections: the first has all the value descriptions and indicies, the second has all of the data. I do not use any complex libraries and only use simple string and binary encoding operations.
4. Portability\
My code could be converted into other languages since it is easy to understand, but I also use a library to compress/encode it that could be problematic for other languages. I tried to work with a specific endianness at first with hex but the result was too large of a file so I switched to binary instead, which could create problems with endianness.\
5. Corruption\
I was considering using huffman encoding for the words, but I did not have enough time and the algorithm was fairly complex.
