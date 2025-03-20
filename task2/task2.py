import sys

def calculate_point_position(circle_file, points_file):

    try:
        with open(circle_file, 'r') as f:
            center_x, center_y = map(float, f.readline().split())
            radius = float(f.readline())

        with open(points_file, 'r') as f:
            points = []
            for line in f:
                x, y = map(float, line.split())
                points.append((x, y))

    except FileNotFoundError:
        print(" Один или оба файла не найдены.")
        return
    except ValueError:
        print("Некорректные данные во входных файлах")
        return
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return
    
    if not 1 <= len(points) <= 100:
        print("Ошибка: Количество точек выходит за допустимый диапазон (1-100).")
        return

    for point_x, point_y in points:
        distance = ((point_x - center_x)**2 + (point_y - center_y)**2)**0.5

        if abs(distance - radius) < 1e-6:
            print(0)
        elif distance < radius:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python script.py <circle_file> <points_file>")
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]
        calculate_point_position(circle_file, points_file)
