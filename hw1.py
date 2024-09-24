numbers: list[int] = []
for i in range(0, 101):
    numbers.append(i)
print(numbers[0])
print(numbers[-1])
print('len', len(numbers))
print('numbers[3: 12]-->', numbers[3: 12])
print('numbers[80 ::]-->', numbers[80::])
print('numbers[: 17]-->', numbers[: 17])
print('numbers[:: -1]-->', numbers[:: -1])
print('numbers[0:100:2]-->', numbers[0:101:2])
print('numbers[:: 3]-->', numbers[:: 3])
print('numbers[:: 7]-->', numbers[:: 7])
print('numbers[0:100:10]-->', numbers[0:101:10])
print('numbers[99:63:-3]-->', numbers[99:63:-3])

print(numbers.pop(-1))

middle_index = len(numbers) // 2
numbers.insert(middle_index, 999)
print("Add element 999 :", f"{numbers} ")

print(numbers.insert(len(numbers // 2, 999)))



