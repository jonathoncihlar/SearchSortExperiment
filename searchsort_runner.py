"""This Python file actual conducts the experiment by processing command 
line args and running the appropriate algorithm on the list.
The code is written in a non-compact way (and not always Pythonic)
to help beginning students follow the logic.

usage: python searchsort_runner.py <algorithm> <listSize> <reps>
- algorithm must be one of linear binary bubble insert merge
- listSize is an integer between 10 and 10,000,000. Default: 10
- reps is an integer representing the number of times to run the
  the algorithm. The range is 1 to 10 . Default: 5
"""

import sys
import string
import searchsort
import timeit

  # make sure there are 4 command line args
if (len(sys.argv) != 4):
  print("Wrong number of command line arguments.")
  print ("usage: python searchsort_runner.py <algorithm> <listSize> "\
         "<reps>")
  sys.exit(1)

  # make sure the algorithm passed in is valid
validAlgorithms = ["linear", "binary", "merge", "insert", "bubble"]
algorithm = sys.argv[1].lower() # translate the string to lower case
if (algorithm not in validAlgorithms):
  print("Invalid algorithm '"+sys.argv[1]+"'.")
  print("It must be one of linear, binary, merge, insert, bubble")
  sys.exit(1)
 
 # make sure list size is in bounds
listSize = int(sys.argv[2])
if (listSize < 10 or listSize > 10000000):
  print("List size "+sys.argv[2]+" is not an integer from 10 "\
        "to 10000000.")
  print("Defaulting to 10.")
  listSize = 10
  
listSize = str(listSize) # use the string representation

 # make sure reps are in bounds
reps = int(sys.argv[3])
if (reps < 1 or reps > 10):
  print("Number of reps "+sys.argv[2]+" is not an integer from"\
        "1 to 10.")
  print("Defaulting to 5.")
  reps = 5
  
  # setup a dictionary/hash where the primary key is the algoritm name.
  # The value is another hash with keys "setup" and "test" which point
  # to strings that actually contain the code and a key "description", 
  # points to a description of the algorithm.
  # the code strings are passed to the timeit object
  
  # there are two setup code templates to use 
setup = """import searchsort
list = searchsort.buildList("""+listSize+""")
"""
setupReversed = """import searchsort
list = searchsort.buildList("""+listSize+""", True)
"""

code = {
  "linear" : 
   {"description" : "linear search",
    "setup" : setup,
    "test" : "searchsort.linearSearch(list, 0)"
   },
  
  "binary" : 
   {"description" : "binary search",
    "setup" : setup,
    "test" : "searchsort.binarySearch(list, 0)"
   },
  
  "merge" : 
   {"description" : "merge sort",
    "setup" : setupReversed,
    "test" : "searchsort.mergeSort(list)"
   },
  
  "bubble" : 
   {"description" : "bubble sort",
    "setup" : setupReversed,
    "test" : "searchsort.bubbleSort(list)"
   },
  
   "insert" : 
   {"description" : "insertion sort",
    "setup" : setupReversed,
    "test" : "searchsort.bubbleSort(list)"
   }
}

print("Running "+ code[algorithm]["description"] + "on a list of "+\
      listSize + " elements " + str(reps) + " times.")
  # run the code and 
times = timeit.repeat(
  setup = code[algorithm]["setup"], 
  stmt = code[algorithm]["test"], 
  repeat = reps, 
  number = 1) # use the repeat function to get a brand new list

print("--Time in ms--")
for i in range(0, len(times)):
  print(str(round(times[i]*1000, 5)))