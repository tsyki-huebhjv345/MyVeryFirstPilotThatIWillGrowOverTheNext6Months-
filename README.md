# MyVeryFirstPilotThatIWillGrowOverTheNext6Months-
hello hello there, I have a dream and I shall achieve it. this primitive node code project will grow overtime into something extraordinary in just 6 months. this first demo is really similar to my previous 3.py code, but it is slightly changed to fit my plan better. 


Now all the buzzwords aside - this project is my Passion Project. It will attempt to connect the nonlinear logic of electrical circuits with the very much linear logic of quantum computing. The final goal of this project is the creation of a code that will solve an NP-hard problem:
Based on the post-CPLU conditions, the program will use QAOA algorithm to quickly rerout large amounts of electricity through wires without melting them down in harsh real world conditions. This program would have to solve AC Optimal Power Flow Equations through a quantum system that I will work hard to develop.

I hope that this code, upon its completion, could be used for greater and practical good.

Welcome aboard!

This readme file will serve as a diary that documents my: progress, questions, observations and ideas
regarding this project.

29.10.2026

Questions: 

1. Why exactly are physical qubits unstable?

What are proposed materials to shield qubits against decoherence? Why did they fail?

3. Why can't quantum scientists just stick up together a couple hundred thousands of qubits together to just create a big grid?

30.10.2026

1. Physical qubits suffer from decoherence, gate infidelity, readout errors and crosstalk (influence of neighbouring qubits due to electromagnetic coupling
Crosstalk becomes more severe in dense arrays, contributing to logical errors and limiting qubit scalability!). different kinds of qubits (superconducting, topological, trapped, spin, photonic
) suffer from different kinds of
behavioral instabilities to varying degrees, where one pro always comes at a cost of one con.

3. Because of crosstalk!

03.11.2026

Update!
I created a new file where the quantum operations would be more heavily used! Using the concepts I learned today on 
quiskit (Compositions of probabilistic operations, Quantum state vectors
Examples of qubit states
Quantum states of other systems
Measuring quantum states
Unitary operations), I will make a simple code, trying to put as much in it as I can!

note: just added a new rep with calculations implementing a fraction of stuff I learned
math wise. but a fraction is not a zero, so it counts!


05.11.2026

Update
Today I will extend the map that is in the 3_the_starter: 
1- adding 9 nodes (16 in the end) (done)
2- assigning each node a + or - value (showing whether the node is on or off) (done)
3- taking 4 linked together nodes and assigning to each of the nodes a corresponding
quantum bit and a quantum vector (done)
4- checking if the quantum vector is correct (the euclidean norm check) (done)
5- making all 3 nodes depend on the 4th node (that is, if 4th node is +, other nodes are able to change
if the 4th node is -, then the other 3 are turned off) (done)

6- taking other 4 nodes, where only 3 are linked together, and the fourth one is just an extension
of one of the 3 previous ones (done)
7- make the 3 linked nodes equal (apply the fair lottery vector), and check how the 
extended 4th node reacts (done)
8- measure the quantum states and check whether the euclidean norm is fullfilled (done)
9- perform a unitary operation on these 3 nodes (done)
10- measure the before and the after of the quantum state vectors, are they equal? (done)

note: did not finish, just added 9 nodes. going to come back tomorrow


07.11.2026

1- Distance the first "Island" - "Vit; F; G; H"
2- finish the yesterdays work load (all the done in parethesis were done today, 07.11, 3am, not 05.11, 11pm)
3- upgraded version on plus-minus rep.

09.11.2026

Update!
1-implement 2 new quantum concepts onto the code!
2- so the updates are the 2 pauli operations, the x (NOT operation, flipping the sign) and the y (the phase
and the bit flip - used for error correction and bit flips)


1. https://www.researchgate.net/publication/393449400_Behavioural_Limitations_of_Qubits_A_Review_of_Stability_and_Reliability_Challenges_in_Quantum_Systems