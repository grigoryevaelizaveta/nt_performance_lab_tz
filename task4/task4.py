import sys

def min_moves_to_equalize(nums):

    nums.sort()
    median = nums[len(nums) // 2] 
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves

def main(filename):

    try:
        with open(filename, 'r') as f:
            nums = []
            for line in f:
                try:
                    num = int(line.strip())  
                    nums.append(num)
                except ValueError:
                    print(f"Некорректное целое число '{line.strip()}'")
                    return  
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return

    if not nums:
        print("Файл пуст")
        return


    result = min_moves_to_equalize(nums)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python script.py <filename>")
    else:
        filename = sys.argv[1]
        main(filename)
