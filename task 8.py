convert any number into hours minutes

n = 24
hours = 0
minutes = 0

while n > 59:
n = n-60
hours = hours + 60

if n <= 60:
minutes = n
hours = hours/60
