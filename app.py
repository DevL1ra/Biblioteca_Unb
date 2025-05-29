from flask import Flask, render_template, request, redirect, flash, url_for
import biblioteca

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        idade = request.form['idade']
        sucesso = biblioteca.cadastrar_cliente(nome, telefone, idade)
        if sucesso:
            return render_template('confirmar_cadastro.html', nome=nome)
        else:
            flash('Cliente já cadastrado.')
    return render_template('cadastro_cliente.html')

@app.route('/cadastro_livro', methods=['GET', 'POST'])
def cadastro_livro():
    if request.method == 'POST':
        nome = request.form['nome']
        autor = request.form['autor']
        sucesso = biblioteca.cadastrar_livro(nome, autor)
        if sucesso:
            return render_template('confirmar_cadastro.html', nome=nome)
        else:
            flash('Livro já cadastrado.')
    return render_template('cadastro_livro.html')

@app.route('/locacao', methods=['GET', 'POST'])
def locacao():
    clientes = biblioteca.obter_clientes()
    livros = biblioteca.obter_livros()
    if request.method == 'POST':
        cliente = request.form['cliente']
        livro = request.form['livro']
        retirada = request.form['retirada']
        entrega = request.form['entrega']
        sucesso = biblioteca.realizar_locacao(cliente, livro, retirada, entrega)
        if sucesso:
            return render_template('confirmar_locacao.html', cliente=cliente, livro=livro)
        else:
            return render_template('erro_locado.html', livro=livro)
    return render_template('locacao.html', clientes=clientes, livros=livros)

@app.route('/devolucao', methods=['GET', 'POST'])
def devolucao():
    locacoes = biblioteca.obter_locacoes_ativas()
    if request.method == 'POST':
        livro = request.form['livro']
        biblioteca.devolver_livro(livro)
        return render_template('confirmar_devolucao.html', livro=livro)
    return render_template('devolucao.html', locacoes=locacoes)

if __name__ == '__main__':
    app.run(debug=True)

