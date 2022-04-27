while True:
    try:
        time_sec = int(input("Введите значение в секундах: "))
        if time_sec < 1:
            break
        days = time_sec // 86400
        time_hours = time_sec % 86400
        hours = time_hours // 3600
        time_minutes = time_hours % 3600
        minutes = time_minutes // 60
        seconds = time_minutes % 60

        if days > 0:
            print(days, "дн", end=" ")

        if hours > 0:
            print(hours, "час", end=" ")

        if minutes > 0:
            print(minutes, "мин", end=" ")

        if seconds > 0:
            print(seconds, "сек")

    except ValueError:
        print("Введено неверное значение!")