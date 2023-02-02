#Составить генератор (yield), который преобразует все буквенные символы в
#заглавные.
def UP(crs: str):
    for ch in crs:
        yield ch.upper()

user_input = input("вводи: ")
print(''.join(user_input.upper()))
