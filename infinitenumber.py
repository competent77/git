n = 123456789

digits = []
total_sum = 0

while n > 0:
    digit = n % 10
    digits.append(digit)
    total_sum += digit
    n = n // 10

digits.reverse()
print("Digits", digits)
print("Sum", total_sum)

