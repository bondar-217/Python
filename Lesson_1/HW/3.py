ticket_number = input("Введите номер билета: ")

if len(ticket_number) != 6:
    print("Некорректный номер билета.")
else:
    first_half = sum(int(digit) for digit in ticket_number[:3])
    second_half = sum(int(digit) for digit in ticket_number[3:])

    if first_half == second_half:
        print("Счастливый билет!")
    else:
        print("Обычный билет.")
