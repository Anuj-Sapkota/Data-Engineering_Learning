# Tuples are immutable sequences of values, meaning once created the values inside tuples cannot be modified.
tuple1 = tuple(('Anuj', 2, 'sapkota'))
tuple2 = (1,2,3, 5, 6)
print(tuple1)
print(tuple2)

# unpacking
( one, *two, three) = tuple2
print(one)
print(two)
print(three)

# counting
t = (1,1,2,2,2,2,2)
print(t.count(2))