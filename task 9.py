sum of all multipl of 3 and 5 blow 1000
def find_sum():
sum = 0
for number range(1,1000):
if number %3 == 0:
sum += number
elif number % 5== 0:
sum += number
elif number% 9 == 0:
sum += number
else:
pass
print(sum)
