Names = ['Иванов', 'Петров', 'Яблочкин', 'Грушин', 'Ласточкин']
Algebra = [3, 4, 5, 5, 4]
Phisic = [2, 4, 4, 5, 3]
Russian = [2, 5, 5, 5, 2]
Class = ['10a', '10b', '10a', '10b', '10v']


def mark_more_then(subject, number):
    id_of_students = []
    counter = 0
    for i in subject:
        if i > number:
            id_of_students.append(counter)
            counter += 1
        else:
            counter += 1
    return id_of_students


def get_count_of_mark_by_id(user_id, mark, *subjects):
    mark_count = 0
    for subj in subjects:
        if subj[user_id] == mark:
            mark_count += 1
    return mark_count


def print_names_by_id(names, ids):
    for i in ids:
        print(names[i])


# Check
print('Хорошисты по алгебре:')
print_names_by_id(Names, mark_more_then(Algebra, 3))
print('Хорошисты по физике:')
print_names_by_id(Names, mark_more_then(Phisic, 3))
print('Хорошисты по русскому языку:')
print_names_by_id(Names, mark_more_then(Russian, 3))

# печать сколько 2 у конткретного ученика
print(get_count_of_mark_by_id(0, 2, Algebra, Phisic, Russian))
