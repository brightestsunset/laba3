
import tkinter as tk
import re

def check_snils(snils):
    pattern = r"\d{3}-\d{3}-\d{3} \d{2}"
    if re.match(pattern, snils):
        snils_number = snils[:11].replace('-', '')
        control_number = int(snils[-2:])

        if int(snils_number) > 1001998:
            digits = [int(digit) for digit in snils_number]
            weighted_sum = sum([(9 - i) * digits[i] for i in range(len(digits))])
            result = weighted_sum % 101

            if result == control_number or (result == 100 and control_number == 0):
                return True
        else:
            return False

    return False
def respond():
    snils_number = snils_entry.get()
    if check_snils(snils_number):
        result_label.config(text="СНИЛС введён верно.", font=('Book Antiqua', 16, 'bold'), fg = "green")
    else:
        result_label.config(text="СНИЛС введён некорректно! Попробуйте снова.", font=('Book Antiqua', 16, 'bold'), fg="red")

window = tk.Tk()
window.title("проверка снилс")

snils_label = tk.Label(window, text="Введите СНИЛС:", font=('Book Antiqua', 16, 'bold'))
snils_entry = tk.Entry(window)
validate_button = tk.Button(window, text="Проверить", font=('Book Antiqua', 16, 'bold'), command=respond)
result_label = tk.Label(window, text="")

snils_label.pack()
snils_entry.pack()
validate_button.pack()
result_label.pack()

window.mainloop()

# 087-654-303 00
# 087-654-302 00
# 123-3456-56-566