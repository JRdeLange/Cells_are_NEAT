# General idea

Several for-fun experiments using NeuroEvolution of Augmenting Topologies (https://ieeexplore.ieee.org/abstract/document/6790655).

Attempt 1 (in the _\_gradient\_cells_ folder) tried to get small cells to move around and follow a gradient, which did not work properly

Attempt 2 (in the _\_herbivores_ folder) was more succesful. Here cells were tasked with moving around in order to grab pieces of food floating in the world. This worked very well, as can be seen here:

![Example image 1](images/1.png)
![Example image 2](images/2.png)

The plan is to, once I am done with my thesis, extend the library used for NEAT to support mutiple chromosomes, allowing for evolution of both cell behavior and cell properties at once.
