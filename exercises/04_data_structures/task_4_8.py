# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = "192.168.3.1"
work_ip = ip.split('.')
ip = '''
 {0:<10} {1:<10} {2:<10} {3:<10}
 {0:09b}  {1:09b}  {2:09b}  {3:09b}
 '''
okt1 = int(work_ip[0])
okt2 = int(work_ip[1])
okt3 = int(work_ip[2])
okt4 = int(work_ip[3])
print(ip.format(okt1, okt2, okt3, okt4))