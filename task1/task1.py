import sys

def circular_path(n, m):

    path = ""
    current_index = 0
    visited = [False] * n
    for _ in range(n):
        if visited[current_index]:
            break
        path += str(current_index + 1)  
        visited[current_index] = True 
        current_index = (current_index + m - 1) % n 
    return path

def main(n, m):

    try:
        n = int(n)
        m = int(m)

        if n <= 0 or m <= 0:
            print("Ошибка: n и m должны быть положительными целыми числами.")
            return

        result = circular_path(n, m)
        print(result)

    except ValueError:
        print("Ошибка: Некорректный формат входных данных. n и m должны быть целыми числами.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py n m")
    else:
        n = sys.argv[1]
        m = sys.argv[2]
        main(n, m)
