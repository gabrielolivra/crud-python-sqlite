import sqlite3

def get_books():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    for id, nome, autor, data in books :
        print(f'ID: {id} TITULO: {nome} AUTOR: {autor} ANO: {data}')


def cadastro_books():
    titulo = input('Digite o nome do titulo do livro: ')
    autor = input('Digite o autor do livro: ')
    ano = int(input('Digite o ano do livro: '))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
              (titulo, autor, ano))
    print('Cadastro realizado com sucesso!')
    conn.commit()
    conn.close()

def remover_book():
    get_books()
    valor = int(input("Digite o id do livro que deseja remover: "))
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id = ?",(valor,))
    conn.commit()
    conn.close()
    get_books()
    print('1 - PARA EXCLUIR OUTRO LIVRO')
    print('2 - PARA FINALIZAR EXCLUSÃO')
    num = int(input())
    if num == 1:
        remover_book()
    elif num == 2:
        iniciar()
        
def iniciar():
    print('--- CRUD DE LIVROS ----')
    print('')
    print('1 - CADASTRO DE LIVROS')
    print('2 - LISTA DE LIVROS ')
    print('3 - EXCLUIR LIVRO')
    while True:
        valor = int(input('Digite aqui: '))
        if valor == 1:
            cadastro_books()
            print('1 - PARA CADASTRAR NOVO LIVRO')
            print('2 - PARA FINALIZAR CADASTRO')
            voltar = int(input())
            if voltar == 1:
                cadastro_books()
            elif voltar == 2:
                iniciar()
        elif valor == 2:
            print('')
            get_books()
            print('')
            print('1 - PARA VOLTAR AO MENU')
            print('2 - PARA FINALIZAR O APP')
            sair = int(input())
            if sair == 1:
                iniciar()
            elif sair == 2:
                break
        elif valor == 3:
            remover_book()
        else:
            break
iniciar()
