for i in range (1, 101):
    if (10 < i < 20) or (i % 10 in [0, 5, 6, 7, 8, 9]):
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    else:
        print(i, "процента")