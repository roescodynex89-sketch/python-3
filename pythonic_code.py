# numbers = [1, 2, 3, 4, 5]
# squares = []

# for x in numbers:
#     squares.append(x ** 2)

# print(squares) 



# [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares) 


numbers = [1, 2, 3, 4, 5]

#  'Even'  'Odd'
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result) 


# ['Odd', 'Even', 'Odd', 'Even', 'Odd']



