# Gerenciamento de Tarefas Simples
# Crie um programa que permita ao usuário adicionar, listar e marcar como concluída tarefas.

# Use uma lista para armazenar as tarefas. Cada tarefa pode ser um dicionário com chaves como "descrição" (string) e "concluída" (booleano).
# Use um loop while para manter o menu do programa ativo até que o usuário decida sair.
# Use condicionais (if/elif/else) para lidar com as diferentes opções do menu.

def insert_task(task_list):
    task = input('**Digite a descrição da tarefa a ser incluída na lista: ').upper()
    print()
    stage = False
    tasks_list.update({task: stage})

def list_tasks(tasks_list):
    if tasks_list:
        print('Itens da lista:')
        for key, item in tasks_list.items():
            if item:
                print(f'*{key} --- CONCLUÍDO')
            else:
                print(f'*{key} --- A CONCLUIR')
    else:
        print('**A lista de tarefas está vazia')
    print()

def mark_task(tasks_list):
    completed_task = input('Qual a tarefa deseja marcar como condluída: ').upper()
    tasks_list[completed_task] = True
    print()

def verify_option(option, tasks_list):
    if option == '1':
        insert_task(tasks_list)
        verify = True
        return verify
    
    elif option == '2':
        list_tasks(tasks_list)
        verify = True
        return verify
    
    elif option == '3':
        mark_task(tasks_list)
        verify = True
        return verify
    
    elif option == '4':
        verify = False
        return verify
    
    else:
        print('Opção selecionada incorreta, tente novamente')
        print()
        verify = True
        return verify
    
tasks_list = {}

verify = True

while verify:
    print('LISTA DE TAREFAS')
    print('------------------')
    print('1. INSERIR ITENS')
    print('2. LISTAR ITENS')
    print('3. MARCAR ITEM COMO CONLUÍDO')
    print('4. SAIR DO PROGRAMA')
    print('------------------')
    print()

    option = input('Insira a opção desejada: ')
    print()

    verify = verify_option(option, tasks_list)
