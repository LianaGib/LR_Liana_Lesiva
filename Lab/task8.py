# TODO Напишите функцию find_common_participants
def find_common_participants(first_group: str, second_group: str, sep=","):
    first_group = set(first_group.split(sep=sep))
    second_group = set(second_group.split(sep=sep))
    return sorted(list(first_group.intersection(second_group)))


participants_first_group = "Иванов|Петров|Сидоров|"
participants_second_group = "Петров|Сидоров|Смирнов|"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group[:-1], participants_second_group[:-1], sep="|"))
