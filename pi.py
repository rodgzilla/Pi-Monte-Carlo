import random

if __name__ == '__main__':
    inside = 0
    total = 1
    while True:
        if total % 50000 == 0:
            print(total, (4 * inside) / total)
        x, y = random.random(), random.random()
        inside += 1 if x * x + y * y <= 1 else 0
        total += 1

