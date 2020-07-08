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


## Author

[Naysan Saran](naysan.ca)

## License

This project is licensed under the GPL V3 licence.

