def pairCount(List_of_Integer, Given_Number):
    Integer_Frequency = {}
    pairCount = 0

    # Iterate Over every Integer and Capture Frequency
    for Integer_Number in List_of_Integer:
        try:
            Integer_Frequency[Integer_Number] += 1
        except:
            Integer_Frequency[Integer_Number] = 1

    # Again Iterate Over every Integer and Capture
    # if Given_Number-Integer_Number exist in Keys
    # Keep on adding those Frequency
    for Integer_Number in List_of_Integer:
        Differenece = Given_Number-Integer_Number
        if Differenece in Integer_Frequency.keys():
            if Differenece != Integer_Number: # Not the same number itself
                pairCount += Integer_Frequency[Differenece]
            else:
                if Integer_Frequency[Differenece] > 1:
                    pairCount += Integer_Frequency[Differenece]-1

    # Return Half count
    # As it will search both (5,2) and (2,5)
    return int(pairCount/2)

List_of_Integer = [5, 4, 2, 2 , 3, 4, 4, 4]
Given_Number = 8
print(pairCount(List_of_Integer, Given_Number))
