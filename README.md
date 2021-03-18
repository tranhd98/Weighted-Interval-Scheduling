# Name
Weighted Interval Scheduling<br/>

A work by: Hung Tran
Dynamic programming is break up a problem into a series of overlapping sub-problems and build up solutions to larger and larger sub-problems. (Jon Kleinberg)
# Description
The project is implemented weighted-Interval-Scheduling problem using python as programming language. Using dynamic programming to choose as many with none overlapping intervals as possible to get biggest weighted in interval. My time complexity of my program is O(nlogn) where sort from python is nlogn and while compute list of p I also use bisect library which is logn to find largest index i <j such that job i is compatible with j. <br/>
Know more about bisect: <br/>
https://docs.python.org/3/library/bisect.html

# Requirements
1/ need to have file csv and with title on the first line. <br />
2/ need python to run program.

# User Manual
Once a person clones this to the computer, there are several steps to test.
1st step: Clone this
```
https://github.com/tranhd98/Weighted-Interval-Scheduling.git
```
2nd step: Run command line
```
python main.py input.csv
```
If uses other files of .csv, then:
```
python main.py type-your-name-file-here.csv
```
The link below will show instructions to run program.<br/>
https://youtu.be/YXg8qWp_GWw

