# node-status

- Pyhton 2.7.1

### Description
This is a console application that takes in an input file with status notifications that a monitoring system receives from a number of nodes on a network.

#### Example Input
```
 1508405807340 1508405807350 luke HELLO
 1508405807378 1508405807387 luke LOST vader
 1508405807467 1508405807479 luke FOUND r2d2
 1508405807468 1508405807480 luke LOST leia
 1508405807512 1508405807400 vader LOST luke
 1508405807560 1508405807504 vader HELLO
```

#### How to run
```
python main.py input.txt
```

#### Assumptions
- if a node finds or loses another node then the former is assumed to be ALIVE
- if a node is found without first saying HELLO it is assumed to be ALIVE
- if a node is lost without first saying HELLO it is assumed to be DEAD
- Nodes are synced to within less than 50 milliseconds of each other
- Monitor time is not synced to Node time
- If more than one notifications, which have a less than 50 millisecond difference (node time), are received by the monitor, it means the status of the node is UNKNOWN
- If the node is in an UNKNOWN state and then a notification is received by the monitor with a timestamp (node time) that marks 50 milliseconds later than the first notification that caused the UNKNOWN state the state is set to what this new notification shows the node to be
