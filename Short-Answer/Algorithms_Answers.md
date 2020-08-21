#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - in this algorithm, n must be some number which is just multiplying with it self three time and comparing with a. and just looping once meaning just n time there fore it is O(n)


b) O(n^2) - there is one loop nested inside another loop which wis n * n resulting n^2. therefore O(n^2)


c) O(n) - its a recursive algorithm and has called itself once there fore it is O(n), if it has called twice it would be O(2^n)

## Exercise II

if flores are already sorted from lowest to highest.
We should implement a binary search to find the floor.

So, first step would be going to the middle floor then drop egg
        - if egg breaks we know it is f or more than f floor
                - then we should move to the bottom half of the floor
                        - then find the middle of the bottom half and check if egg breaks until we find the floor f where egg does not break
        similarly
        - if egg does not break we know that floor f is in the upper half of the floors.
                - now need to go to the middle of the upper half floor and check if egg breaks.
                        -if breaks need to go to the middle of the lower half of upper half and check if egg breaks 
                                - if breaks means f floor must be in the bottom half of upper original half. and need to keep checking if egg breaks until we find floor f           


------ Runtime Complexity = O(log n)
