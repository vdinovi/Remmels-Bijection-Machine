import pdb
from bijection_machine import *

"""
partition = [5, 5, 1, 1, 1, 1]
cond1 = [x for x in range(1, 32) if (x % 6 != 1) and (x % 6 != 1)]
cond2 = [[x/2, x/2] if (x % 2 == 0) else [x] for x in cond1]
result = bijection_machine(partition, cond1, cond2)
"""

patient = [[5, 5, 1, 1, 1, 1], []]
A = [ [2], [3], [4], [6], [8], [9], [10], [12], [14], [15], [16] ]

B = [ [1, 1], [3], [2, 2], [6], [4, 4], [9], [5, 5], [11], [6, 6], [13],
      [7, 7], [15], [8, 8] ]
i = 0
while (i< 20):
    #pdb.set_trace()
    print(str(patient))
    swap_diseases(patient, A, B)
    print("   "+str(patient))
    toggle_min_disease(patient, B)
    if (len(patient[1]) == 0):
        print("DONE: "+str(patient))
        break
    print("      "+str(patient))
    swap_diseases(patient, B, A)
    print("         "+str(patient))
    toggle_min_disease(patient, A)
    print("\n")
    i += 1

