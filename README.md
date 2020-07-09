# Project Title

Simple Markov Chain visualization module in Python. Only requires **matplotlib** and **numpy** to work.

## Description

The current version works with 2 to 4 states. 

## Getting Started

### Dependencies

* matplotlib
* numpy

### Installation

Copy the files src/node.py and src/markovchain.py in your script directory. Then

```
from markovchain import MarkovChain
```

#### 2-state Markov chain demo

```
P = np.array([[0.8, 0.2], [0.1, 0.9]]) # Transition matrix
mc = MarkovChain(P, ['1', '2'])
mc.draw("../img/markov-chain-two-states.png")
```

![two state markov chain transition diagram python](https://github.com/NaysanSaran/markov-chain/blob/master/img/markov-chain-two-states.png)


#### 3-state Markov chain demo

```
P = np.array([
    [0.8, 0.1, 0.1],
    [0.1, 0.7, 0.2],
    [0.1, 0.7, 0.2],
])
mc = MarkovChain(P, ['A', 'B', 'C'])
mc.draw("../img/markov-chain-three-states.png")
```

![three state markov chain transition diagram python](https://github.com/NaysanSaran/markov-chain/blob/master/img/markov-chain-three-states.png)


#### 4-state Markov chain demo

```
P = np.array([
    [0.8, 0.1, 0.1, 0.0],
    [0.1, 0.7, 0.0, 0.2],
    [0.1, 0.0, 0.7, 0.2],
    [0.1, 0.0, 0.7, 0.2]
])
mc = MarkovChain(P, ['1', '2', '3', '4'])
mc.draw("../img/markov-chain-four-states.png")
```

![four state markov chain transition diagram python](https://github.com/NaysanSaran/markov-chain/blob/master/img/markov-chain-four-states.png)


## Author

[Naysan Saran](naysan.ca)

## License

This project is licensed under the GPL V3 licence.

