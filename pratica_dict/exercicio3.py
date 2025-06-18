# Dado um dicionário onde as chaves são nomes de alunos e os valores são suas notas (de 0 a 10), crie uma função que retorne apenas os alunos com nota maior ou igual a 7.

def verify_student(dict):
    next_grade = []

    for student, grade in dict.items():
        if grade >= 7:
            next_grade.append(student)

    return next_grade

students_grades = {
    'victor' : 8.5,
    'marcia' : 5.5,
    'clara' : 10,
    'eliza' : 6.5,
    'rita' : 7
}

next_grade = verify_student(students_grades)

print(next_grade)