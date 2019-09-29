count = 0
for n in range(0, 100):
    if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
        continue
    else:
        count += 1
        print(n)
print(count)

