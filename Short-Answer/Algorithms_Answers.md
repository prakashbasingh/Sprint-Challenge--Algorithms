#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(n)

## Exercise II

Lets assume flores are already sorted from lowest to highest.
We should implement a binary search to find the floor.
So, first step would be going to the middle floor and when egg is dropped and 
        - if egg breaks we know it is f or more than f floor
        - if egg does not break we should go to the middle of the upper half and check if egg breaks
Now, if the egg breaks, move to the bottom half of the floor and again we find the middle of the bottom half floor 
Then drop the egg again, 
        - if it breaks then find another middle floor from third half of the floors 
                            and keep going until  we find less than f floor.
        - or if it does not break then it must be in the upper half of the 1st button half of the floors
then keep performing this operation until we find f floor and when we drop the egg it does not break.


------ Runtime Complexity = O(log n)
