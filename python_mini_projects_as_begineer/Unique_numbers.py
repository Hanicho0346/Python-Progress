
# question 12:unique_number of list
def unique_number(num_list):
    unique_numbers = set(num_list)
    return list(unique_numbers)
print(unique_number([1, 2, 3, 2, 4, 1, 5]))

# another method
def unique_number(num_list):
    unique_numbers = []
    for num in num_list:
      if num not in unique_numbers:
        unique_numbers.append(num)
    return unique_numbers
print(unique_number([1, 2, 3, 2, 4, 1, 5]))

# here is another method
def unique_number(num_list):
    seen = set()
    unique_numbers = []
    for num in num_list:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    return unique_numbers
print(unique_number([1, 2, 3, 2, 4, 1, 5]))

