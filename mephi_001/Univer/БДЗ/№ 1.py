def sort_string(input_string):
    original_string = input_string  # copy
    input_string = input_string.lower()
    case_dict = {input_string[i]: original_string[i] for i in range(len(input_string))}  # dict

    sorted_string = ''.join(sorted(input_string))  # sort
    sorted_result = ''.join(case_dict[i] for i in sorted_string)
    return sorted_result


user_input = input("Введите строку для сортировки: ")
sorted_result = sort_string(user_input)

print(f"Исходная строка: {user_input}")
print(f"Упорядоченная строка: {sorted_result}")
