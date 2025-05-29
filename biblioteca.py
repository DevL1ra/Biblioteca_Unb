import json
import os

CAMINHO = 'dados.json'

def carregar_dados():
    if not os.path.exists(CAMINHO):
        with open(CAMINHO, 'w') as f:
            json.dump({'clientes': [], 'livros': [], 'locacoes': []}, f)
    with open(CAMINHO, 'r') as f:
        return json.load(f)

def salvar_dados(dados):
    with open(CAMINHO, 'w') as f:
        json.dump(dados, f, indent=4)

def cadastrar_cliente(nome, telefone, idade):
    dados = carregar_dados()
    for cliente in dados['clientes']:
        if cliente['nome'] == nome and cliente['telefone'] == telefone:
            return False
    dados['clientes'].append({'nome': nome, 'telefone': telefone, 'idade': idade})
    salvar_dados(dados)
    return True

def cadastrar_livro(nome, autor):
    dados = carregar_dados()
    for livro in dados['livros']:
        if livro['nome'] == nome:
            return False
    dados['livros'].append({'nome': nome, 'autor': autor})
    salvar_dados(dados)
    return True

def realizar_locacao(cliente, livro, retirada, entrega):
    dados = carregar_dados()
    for loc in dados['locacoes']:
        if loc['livro'] == livro and not loc.get('devolvido', False):
            return False
    dados['locacoes'].append({
        'cliente': cliente,
        'livro': livro,
        'retirada': retirada,
        'entrega': entrega,
        'devolvido': False
    })
    salvar_dados(dados)
    return True

def obter_clientes():
    dados = carregar_dados()
    return dados['clientes']

def obter_livros():
    dados = carregar_dados()
    return dados['livros']

def obter_locacoes_ativas():
    dados = carregar_dados()
    return [loc for loc in dados['locacoes'] if not loc.get('devolvido', False)]

def devolver_livro(nome_livro):
    dados = carregar_dados()
    for loc in dados['locacoes']:
        if loc['livro'] == nome_livro and not loc.get('devolvido', False):
            loc['devolvido'] = True
            break
    salvar_dados(dados)
