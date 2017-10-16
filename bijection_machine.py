import pdb

# Find the minimum disease from a given list for a given patient
def toggle_min_disease(patient, diseases):
    for idx, dis in enumerate(diseases):
        dup = patient[0][:]
        valid = True
        # Check for disease symptom by symptom
        for symptom in dis:
            if symptom in dup:
                dup.remove(symptom)
            # When a symptom is not found in the patient,
            #   invalidate disease and end search
            else:
                valid = False
                break
        if (valid):
            if (idx in patient[1]):
                patient[1].remove(idx)
            else:
                patient[1].insert(0, idx)
                sorted(patient[1])
            return

# Patient: Doctor... why are you doing this...
# Doctor:  Quiet! You will be cured -- eventually...
#
# Replace existing diseases with diseases in new set
def swap_diseases(patient, old_diseases, new_diseases):
    # Iterate over old diseases
    for _, idx in enumerate(patient[1]):
        dup = patient[0][:]
        valid = True
        old_dis = old_diseases[idx]
        new_dis = new_diseases[idx]
        # Replace with new disease
        for symptom in old_dis:
            if (symptom in dup):
                dup.remove(symptom)
            else:
                valid = False
                break
        if (valid):
            dup.extend(new_dis)
            patient[0] = sorted(dup, reverse=True)

# lambda: an integer partition of n
#       (list of weakly decr. integers that sum to n)
# A & B: Pairwise disjoin lists of 'diseases'.
#       Sum(el in A_i) == Sum(el in B_i) for all i.
#
def bijection_machine(partition, A, B):
    patient = [partition, []]
    iterations = 1
    while (True):
        swap_diseases(patient, A, B)
        toggle_min_disease(patient, B)
        if (len(patient[1]) == 0):
            print("Solved ({} iterations): ".format(iterations) + str(patient))
            break
        swap_diseases(patient, B, A)
        toggle_min_disease(patient, A)
        iterations += 1

"""
Sample Code
A = [ [2], [3], [4], [6], [8], [9], [10], [12], [14], [15], [16] ]

B = [ [1, 1], [3], [2, 2], [6], [4, 4], [9], [5, 5], [11], [6, 6], [13],
      [7, 7], [15], [8, 8] ]

partition = [5, 5, 1, 1, 1, 1]
bijection_machine(partition, A, B)

partition = [10, 4]
bijection_machine(partition, B, A)
"""