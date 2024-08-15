first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for y in first_strings for x in second_strings if len(x) == len(y)]
third_result = {x: len(y) for x in first_strings + second_strings if len(x) % 2 == 0
                for y in first_strings + second_strings if len(y) == len(x)}
print(first_result)
print(second_result)
print(third_result)
