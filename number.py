# BUIT-IN FUNCTIONS FOR WORKING WITH NUMBERS
# MORE FUNCTIONS IS IN math library

abs(-5.5)  # 5.5
round(5.5)  # 6
round(5.49, 2)  # 6.50
max()  # максимальне значення *можна передавати як digits так і list whith digits
min()  # мінімальне значення  *можна передавати як digits так і list whith digits
sorted()  # сортування
pow()  # піднесення до степені
sum()  # сума усіх чисел *працює лише з list
hex()  # переводить число в шіснадцядкову систему
oct()  # переводить число в вісімкову систему
bin()  # переводить число в бінарну систему


# CREATE COMPLEX NUMBER

num = 2 + 3j
num = complex(2, 3)

print(num.real, num.imag)
