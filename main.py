import time

message = str(input("Введите слово: "))
a = len(message)
print("Введено символов: ", a)
n = 0
while n < a:
    time.sleep(0.25)
    print(message[n])
    n += 1

