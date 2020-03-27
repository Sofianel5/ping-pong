## Basic Organization

* We have a number of students
* We have a number of classes 
* Students want to take certain classes
* For each student, we have a list of classes that they WANT to take, 
and a list of classes that they HAVE to take
* We indicate preference using a point system
* For each class, a maximum of N students can be assigned
* We want to program students in the best way possible

## How do we apply RL to this?

* We give each student a buying and selling agent that acts on the students behalf

### Buying Agent
* Observation: the period the class is in, number of points assigned to that class, all the point values of the student's current schedule
* Action: A single number

### Selling Agent
* Observation: all the point values of the student's current schedule, 
  current highest bid period, current highest bid point value
* Action: A single number
