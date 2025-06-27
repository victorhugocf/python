# Crie um sistema para cadastrar alunos e suas notas.

# Use um dicionário principal onde as chaves são os nomes dos alunos (string) e os valores são listas de notas (float).

# Permita ao usuário adicionar novos alunos e adicionar notas a alunos existentes.

# Implemente uma função que calcule e exiba a média das notas de um aluno específico.

# Exiba a média de todos os alunos e o aluno com a maior média.

def is_name_valid(name):
    if not name.strip():
        return False
    return all(letter.isalpha() or letter.isspace() for letter in name)

def insert_student(hash):
    grades = []
    
    try:
        for i in range(1, 4):
            grade = float(input(f'Insira a {i}ª nota do aluno: '))
            grades.append(grade)
        return hash.update({student: grades})
    except ValueError:
        print('Você digitou uma nota inválida, tente novamente.')
        print()

def student_average_grade(hash, student):
        try:
            grades = hash[student]
            total = 0

            for grade in grades:
                total += grade

            average = total / len(grades)

            return average
        except KeyError:
            print('Esse nome não está na classe, insira o nome do aluno e suas notas e tente novamente.')
            print()
            return False

def average_of_class(hash):
    students_avarage = 0
    highest_avarage = 0

    for student in hash.keys():
        average = student_average_grade(hash, student)
        students_avarage += average

        if average >= highest_avarage:
            highest_avarage = average
            highest_avarage_student = student

    class_average = students_avarage / len(hash.keys())

    return class_average, highest_avarage,highest_avarage_student
    

students = {
    "Ana Silva": [8.5, 7.0, 9.0],
    "Bruno Costa": [6.0, 5.5, 7.0],
    "Carla Dias": [9.5, 8.0, 10.0],
    "Daniel Rocha": [7.0, 7.5, 6.5],
    "Eduarda Lima": [5.0, 6.0, 5.5]
}

verify_loop = True

while verify_loop:
    print('GERENCIADOR DE CLASSE:')
    print('-------------------')
    print()

    print('1. Inserir aluno na lista da classe')
    print('2. Calcular média de aluno')
    print('3. Calcular média da classe')
    print('4. Listar alunos')
    print('5. Sair do programa')
    print()

    choice = input('Qual a operação desejada: ')
    print()

    if choice == '1':
        student = input('Digite o nome do aluno: ')
        verify = is_name_valid(student)
        if verify:
            insert_student(students)
            print()
        else:
            print('Você digitou um nome inválido, tente novamente.')
            print()

    if choice == '2':
        student = input('Qual o aluno a média devera ser calculada? ')
        verify = is_name_valid(student)

        if verify:
            average = student_average_grade(students, student)
            if average:
                print(f'A média de {student} é {average:.1f}')
                print()
        else:
            print('Digite um nome válido.')
            print()

    if choice == '3':
        class_average, highest_avarage,highest_avarage_student = average_of_class(students)
        print(f'A média da classe é {class_average:.1f}')
        print(f'O aluno com a maior média foi {highest_avarage_student} e sua média foi {highest_avarage}')
        print()

    if choice == '4':
        if students:
            for student, grades in students.items():
                print(f'{student} / {grades}')
                print()
        else:
            print('A lista de alunos ainda não foi preenchida.')
            print()

    if choice == 5:
        verify_loop = False