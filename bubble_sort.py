numbers = [7, 4, 5, 2]
print(numbers)
def bubble_sort(numbers):
    N = len(numbers)
    for k in range(N - 1):
        for i in range(N - k - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    print(numbers)
bubble_sort(numbers)


