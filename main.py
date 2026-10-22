from random import randint

arr = [i for i in range(1,1000)]
target = randint(434, 1500)


def two_pointers(arr, target):
    left, right = 0, len(arr) - 1

    print("target = ", target)

    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            print(f"{arr[left]} + {arr[right]} = {target}")
            print(f"left = {left}, right = {right}")
            return True
    return False


def main():
    arr = []
    target = 0
    target_n = 0
    n = randint(50, 100)
    k = 324

    while len(arr) < n:
        if randint(0, 10) == 7:
            arr.append(k)
            if randint(0, 20) == 7 and target_n < 2:
                target += k
                target_n += 1
                if target_n == 2:
                    print("Target - получен")
        k += 1

    print(two_pointers(arr, target))



if __name__ == "__main__":
    while True:
        input("Введите enter для старта...")
        main()