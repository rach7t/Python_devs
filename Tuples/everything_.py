#tuple comparison
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 < t2)  # True, because 3 < 4
print(t1 == t2)  # False
print(t1 > t2)  # False


#tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6)


#tuple repetition
t1 = (1, 2, 3)
t3 = t1 * 3
print(t3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)