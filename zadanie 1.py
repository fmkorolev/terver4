# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

def main():
    start = 200
    end = 800
    avg = (start + end) / 2
    var = (start - end) ** 2 / 12
    print(f"среднее: {avg}")
    print(f"дисперсия: {var}")



if __name__ == '__main__':
    main()