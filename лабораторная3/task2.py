# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(str1, str2, sep=','):
    participants1 = str1.split(sep)
    participants2 = str2.split(sep)
    res = [i for i in participants1 if i in participants2]
    return res
# TODO Провеьте работу функции с разделителем отличным от запятой


print(find_common_participants(participants_first_group, participants_second_group, '|'))