Late 20th century and early 21st century: the advent of machine learning
=================================

The technological advancements of the late 20th century paved the way for large scale data processing units capable of running multiple tasks in parallel.
Compute paralellization led to the adoption of new techniques for data analysis developed throughout the second half of the 20th century, the most prominent of which was the introduction of the multi-layer perceptron.
The perceptron was inspired by the function of the neuron as the fundamental processing unit in the human brain, where each node or "neuron" in a network can be thought of as executing some transformation of its input data before passing the signal forward to its neighbors.
Nowadays we see extremely complex AI architectures that emulate many components of biological cognition, (e.g. attention, memory, etc.), however, the core component of these networks is still a relatively simple neuron architecture that simply takes in an input and performs a transformation to it before passing it along.

.. image:: media/perceptron.png
   :width: 600

The above `figure https://stackoverflow.com/questions/47527080/how-many-neurons-does-a-perceptron-have`_ shows the structure and function of a single perceptron, with input data coming in from the left, weighted by some parameter w (just a multiplication operation), summed over, and scaled with the so called "activation function", which in this case is just a step function, meaning the output of this particular neuron will be one of two numbers (usually -1 and 1 or 0 and 1). Other activation functions can be used, the output does not have to be binary.
By stacking many of these neurons together, we can form a "neural network" which can learn representations of high dimensional data. Neural networks are currently ubiquitous in data science thanks to their ability to learn complex representations from vast amounts of data. In physics, neural networks are particularly helpful in particle physics, in which experiments such as ATLAS produce vast amounts of data that cannot be parsed by a single team of scientists.
In the following notebook, we'll explore one such application of neural networks in particle physics.