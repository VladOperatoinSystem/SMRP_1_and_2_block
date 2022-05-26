dict_friend = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person in dict_friend:
        dict_friend[name_of_person] = dict_friend[name_of_person] + list_of_friends
    else:
        dict_friend[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    print(name_of_person2 in dict_friend[name_of_person1])


def print_friends(name_of_person):
    print(*sorted(dict_friend[name_of_person]))


add_friends("Алла", ["Марина", "Иван"])
are_friends("Алла", "Мария")
add_friends("Алла", ["Мария"])
are_friends("Алла", "Мария")
print_friends("Алла")

