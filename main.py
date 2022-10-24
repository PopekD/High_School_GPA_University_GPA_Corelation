import numpy as np


def main():
    # Creating the students
    students = []
    student_Number = int(input("Enter number of students: "))
    for i in range(student_Number):
        print(f"Type the data for Student{i + 1}")
        student = dict()
        hs_GPA = float(input("Enter a HS_GPA: "))
        student["HS_GPA"] = hs_GPA
        uni_GPA = float(input("Enter a Uni_GPA: "))
        student["Uni_GPA"] = uni_GPA
        students.append(student)

    # Calculations
    list_of_x = []
    list_of_y = []
    for data in students:
        list_of_x.append(float(data["HS_GPA"]))
        list_of_y.append(float(data["Uni_GPA"]))

    sum_of_x = sum(list_of_x)
    sum_of_y = sum(list_of_y)
    x_bar = sum_of_x / student_Number
    y_bar = sum_of_y / student_Number

    list_minus_x = []
    list_minus_x_pow = []
    for i in list_of_x:
        minus_x = i - x_bar
        list_minus_x.append(minus_x)
        minus_x_pow = np.power(minus_x, 2)
        list_minus_x_pow.append(minus_x_pow)

    list_minus_y = []
    list_minus_y_pow = []
    for i in list_of_y:
        minus_y = i - y_bar
        list_minus_y.append(minus_y)
        minus_y_pow = np.power(minus_y, 2)
        list_minus_y_pow.append(minus_y_pow)

    sum_of_minus_x_pow = sum(list_minus_x_pow)
    sum_of_minus_y_pow = sum(list_minus_y_pow)

    S_x_x = np.sqrt(sum_of_minus_x_pow / (student_Number - 1))
    S_y_y = np.sqrt(sum_of_minus_y_pow / (student_Number - 1))

    list_x_y = []
    for i in range(student_Number):
        x = list_minus_x[i]
        y = list_minus_y[i]
        x_y = x * y
        list_x_y.append(x_y)

    S_x_y = (sum(list_x_y) / (student_Number - 1))
    r = S_x_y / (S_x_x * S_y_y)

    if r > 0.9:
        print(f"Strong positive correlatrion: p = {r}")
    elif r < -0.9:
        print(f"Strong negative correlation: p = {r}")
    elif r > -0.1:
        print(f"No correlation: p = {r}")


if __name__ == '__main__':
    main()
