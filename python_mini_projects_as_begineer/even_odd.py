
# question 6:Even or odd filter

def even_odd_filter(num_list,type):
    even=[]
    odd=[]
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if type == "even":
        return even
    elif type == "odd":
        return odd
    else:
        return "Invalid type. Please choose 'even' or 'odd'."
    

print(even_odd_filter([1, 2, 3, 4, 5, 6], "even"))