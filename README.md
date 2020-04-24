# SearchSortExperiment

This repository contains implementations of classic search and sort algorithms 
in Python to help students empirically determine growth of worst case running 
time.

`usage: python searchsort_runner.py <algorithm> <listSize> <reps>`

`algorithm` One of `linear binary` searches or  `bubble merge insertion radix` sorts.

`listSize` An integer from 10 to 10,000,000 representing the size of the
list.

`reps` An integer from 1 to 10 representing how many times to run the algorithm.

Example: `python searchsort_runner.py binary 10000 10` performs a binary search on a 
list of 10,000 elements 10 times.

The application will print out the number of milliseconds it took the algorithm to 
run on the given list size.