# Input 5 names

def input_names():
    student_names = []

    for i in range(0, 5):
        name = input("Enter a name")
        student_names.append(name)

    return student_names



def display_names(student_names):
    print("Here's the 5 names you entered:")
    for i in range(0, 5):
        print(student_names[i], "postion", i)


stu_list = input_names()
display_names(stu_list)




