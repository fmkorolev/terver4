# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

def main():
    start = 178
    end = 190
    var = 25
    answer =(end-start)/var**0.5
    print(f"отклонение на {answer} сигм")


if __name__ == '__main__':
    main()