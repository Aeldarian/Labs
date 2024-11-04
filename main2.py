# TODO Напишите функцию find_common_participants
def find_common_participants(string1,string2,separator=','):
    group1=set(string1.split(separator))
    group2=set(string2.split(separator))
    group=list(group1.intersection(group2))
    group.sort()
    return group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
