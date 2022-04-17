def reverseString(string_value):
    # In Python String is immutable
    string_value_List = list(string_value)

    start_index = 0
    end_index = -1
    while start_index < len(string_value_List)/2:
        string_value_List[start_index], string_value_List[end_index] = string_value_List[end_index], string_value_List[start_index] # Swap two values
        start_index += 1
        end_index -= 1

    return "".join(string_value_List)

def reverseStringInOneLine(string_value):
    return "".join(list(string_value)[::-1])

print(reverseString("abcde"))
print(reverseStringInOneLine("abcde"))