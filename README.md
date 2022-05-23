# Markov Chain Transition Diagrams in Python

Simple Markov Chain visualization module in Python. Only requires **matplotlib** and **numpy** to work.

## Description

The current version works with 2 to 4 states. 

## Getting Started

### Dependencies

* matplotlib
* numpy
* TK enter

### Installation

Copy the files src/node.py and src/markovchain.py in your script directory. Then

```
from markovchain import MarkovChain
```

#### 2 X 2 Matrix

Dynamic Random Entery by the user:


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

## Author

Credit: [Naysan Saran](naysan.ca)
Modification: M Shaf Khattak

Link to my [blog](https://naysan.ca/2020/07/08/drawing-state-transition-diagrams-in-python/).

## License

This project is licensed under the GPL V3 licence.

