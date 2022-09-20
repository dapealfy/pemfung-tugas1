def pangkat(angka, pangkatnya):
    total = 0
    for i in range(1, pangkatnya + 1):
        total += angka * angka
    return total

print(pangkat(3,2))