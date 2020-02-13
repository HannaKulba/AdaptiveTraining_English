def student_average(list):
    sum = 0

    for i in range(1, len(list)):
        sum += int(list[i])

    average = sum / (len(list) - 1)
    return average


def average_subject(matrix):
    math = 0
    physics = 0
    English = 0

    for list in matrix:
        math += int(list[1])
        physics += int(list[2])
        English += int(list[3])

    average_math = math / len(matrix)
    average_physics = physics / len(matrix)
    average_English = English / len(matrix)
    return average_math, average_physics, average_English


with open('dataset_28253_1.txt') as file:
    students_data = []

    for line in file:
        results = line.split(';')
        students_data.append(results)

    for student in students_data:
        print(student_average(student))

    print(average_subject(students_data))
