#Write a function square_list(numbers) that takes a list and returns a new list with squares of each element

def square_list(numbers):
    sq = []
    for n in numbers:
        sq.append(n ** 2)
    return sq

numbers = [1, 2, 3, 4]
result = square_list(numbers)
print(result)
