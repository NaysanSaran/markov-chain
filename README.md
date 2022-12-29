# Markov Chain Transition Diagrams in Python

Simple Markov Chain visualization module in Python. Only requires **matplotlib** and **numpy** to work.

## Description

Thanks to updates made by [@yagoduppel](https://github.com/yagoduppel), the code can now support more than four states.
Examples below. [@SHaf373](https://github.com/SHaf373) has also added a gui-version for two-state Markov Chains.

## Getting Started

### Dependencies

* matplotlib
* numpy
* Tkinter standard GUI library for Python

### Installation

Copy the files src/node.py and src/markovchain.py in your script directory. Then

```
from markovchain import MarkovChain
```

#### 2 X 2 Matrix

**Script-based**

```
P = np.array([[0.8, 0.2], [0.1, 0.9]]) # Transition matrix
mc = MarkovChain(P, ['1', '2'])
mc.draw("../img/markov-chain-two-states.png")
```

![Two-state Markov-Chain](https://github.com/NaysanSaran/markov-chain/blob/master/img/markov-chain-two-states.png)

**Dynamic Random Entery by the user**

For GUI-based version use <code>src/2X2.py</code>.


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

![Three-state Markov-Chain](https://github.com/NaysanSaran/markov-chain/blob/master/img/markov-chain-three-states.png)


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


#### 5-state Markov chain demo

```
P = np.array([
    [0.8, 0.1, 0.1, 0.0, 0.0], 
    [0.1, 0.6, 0.0, 0.2, 0.1],
    [0.1, 0.0, 0.7, 0.2, 0.0],
    [0.1, 0.0, 0.4, 0.2, 0.3],
    [0.6, 0.1, 0.1, 0.0, 0.2], 
])
mc = MarkovChain(P, ['1', '2', '3', '4', '5'])
mc.draw("../img/markov-chain-five-states.png")
```



## Author

Credit: [Naysan Saran](naysan.ca)
Modification: [M Shaf Khattak].(https://github.com/SHaf373)

Link to my [blog](https://naysan.ca/2020/07/08/drawing-state-transition-diagrams-in-python/).

## License

This project is licensed under the GPL V3 licence.

