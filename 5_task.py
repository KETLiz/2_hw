# 5'. Реализуйте алгоритм перемешивания списка
import random
test_list = [1, 4, 5, 6, 3]
print (f'Исходный список: {str(test_list)}')
for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    test_list[i], test_list[j] = test_list[j], test_list[i]
     
print (f'Перемешанный список: {str(test_list)}')