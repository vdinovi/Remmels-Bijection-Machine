
# Find the minimum disease from a given list for a given lambda
def diagnose(patient, diseases):
    for ndx, dis in enumerate(diseases):
        dup = patient
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
            return ndx
    # If patient is clean, return None
    return None