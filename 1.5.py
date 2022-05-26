def polite_input(question):
    global name
    if len(name) == 0:
        name = str(input('как вас зовут'))
    print(name, ",", question)
    buf = input()
    return buf

name = ""
age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')

