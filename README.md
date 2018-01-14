# Social-Network-Analysis


The application of the proposed algorithm is marketing i.e. in case of a promotional event, fiding the minimum number of people and also who all to give th information about the event so that they cover maximum people in a community. 
Consider a promotional event for triathlon which requires you to pick few people to give a free pass so that event is publicized in the networks. So picking people whose specific interests are cycling or running or swimming would ensure us more coverage for the event rather than picking people who are only interested in running. By picking people with diversified interests,one can reach to neighborhood of a diversified committee.

The goal is to find cognitive coverage by choosing some number of nodes(x) with the constraints of having k attributes.

Getting Started

1. Provide link to the data to be analysed in "creatingGraph.py" file.
2. Run BruteForce.py to judge the time it will take to pick people from brute force and also the most optimized solution.
3. Run DiverseCoverage.py(contining the proposed algorithm) to fetch the solution in polynomial time.

P.S.: config.json maintains the config details about the number of clients and ports to be used for the application.


Prerequisites

Python 2.7

Application Components:

Social Network Marketing is always seeking to reach maximum nodes(people) in the network with the least cost. This problem is NP Hard and hence, the proposed algorithm gives an approximates solution to the problem .


Authors

Ishani Gupta
Sai Nikhil 



Acknowledgments

Thanks to Prof. Ambuj Singh, Computer Science Department, UCSB for his constant guidance.

Data:
Joseph J. Pfeiffer III and Sebastian Moreno and Timothy La Fond and Jennifer Neville and Brian Gallagher, Attributed Graph Models: Modeling network structure with correlated attributes.
https://www.cs.purdue.edu/homes/jpfeiff/agm/agm.html

