'''student_ids = {123, 456, 789, 123}
numbers=[1, 2, 3, 4, 456, 5, 6, 7, 8, 9] 

print(student_ids)

student_ids.add(000)

print(student_ids)

student_ids.update(numbers)

print(student_ids)

student_ids.discard(789)

print(student_ids)
'''

set_a={1, 2, 3, 4, 5}
set_b={4, 5, 6, 7, 8, 9}


print(set_a.union(set_b)) 

print(set_a.intersection(set_b))

print(set_a.symmetric_difference(set_b))

print(set_b - set_a)