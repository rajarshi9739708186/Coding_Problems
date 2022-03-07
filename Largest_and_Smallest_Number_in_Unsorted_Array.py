List_Integer = [ 100, 23, 20, 300, 5, 6, 0, 176, 253]

def max_min(List_Integer):
    max_value = List_Integer[0]
    min_value = List_Integer[0]

    for value in List_Integer:
        if value > max_value:
            max_value = value

        if value < min_value:
            min_value = value

    return max_value, min_value

print(max_min(List_Integer))