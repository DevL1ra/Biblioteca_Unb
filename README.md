
# 📚 Sistema de Biblioteca

Este é um sistema completo de gerenciamento de biblioteca desenvolvido em **Python (Flask)** com interface web em **HTML/CSS**. O sistema permite:

- Cadastro de clientes
- Cadastro de livros
- Locação e devolução de livros
- Validação para evitar duplicações
- Armazenamento dos dados em arquivos `.json`
- Geração de executável `.exe` para uso offline

---

## 🚀 Funcionalidades

✅ **Clientes**
- Nome, telefone e idade
- Impede cadastros duplicados (mesmo nome e telefone)

✅ **Livros**
- Nome e autor
- Impede duplicação de livros já cadastrados

✅ **Locação**
- Seleciona cliente e livro
- Define data de retirada e devolução
- Impede que o mesmo livro seja locado mais de uma vez

✅ **Devolução**
- Seleciona livro para devolver
- Confirma devolução e remove do sistema

---

## 🖥️ Tecnologias

- **Python 3.11+**
- **Flask**
- **HTML5 / CSS3**
- **JSON** para armazenamento local
- **Font Awesome** ou imagens `.png` como ícones
- Compatível com `.exe` via PyInstaller

---

## 📂 Estrutura de Pastas

```
biblioteca/
├── app.py                   # Arquivo principal Flask
├── biblioteca.py            # Lógica e manipulação de dados
├── clientes.json            # Armazena os dados dos clientes
├── livros.json              # Armazena os dados dos livros
├── locacoes.json            # Armazena os dados das locações
├── templates/
│   ├── index.html
│   ├── cadastro_cliente.html
│   ├── cadastro_livro.html
│   ├── locacao.html
│   ├── devolucao.html
│   ├── confirmar_locacao.html
│   ├── confirmar_devolucao.html
│   └── erro_livro_locado.html
├── static/
│   ├── style.css
│   └── imagens/
│       ├── novo_cliente.png
│       ├── novo_cliente.png
│       ├── livros.png
│       ├── locacao.png
│       └── devolucao.png
```

---

## ⚙️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca.git
   cd sistema-biblioteca
   ```

2. Instale o Flask:
   ```bash
   pip install flask
   ```

3. Execute o app:
   ```bash
   python app.py
   ```

4. Acesse no navegador:
   ```
   http://localhost:5000
   ```

---

## 🧊 Como gerar o executável `.exe`

Se quiser transformar o projeto em um programa que roda com duplo clique:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

Isso gerará o executável em `dist/app.exe`.

---

## 📌 Requisitos

- Python 3.10 ou superior
- Navegador moderno (Chrome, Firefox, Edge...)
- Biblioteca Flask instalada

---

## 📃 Licença

Este projeto é de uso livre para fins educativos e pessoais. Você pode modificá-lo conforme necessário.

---

## 🙋‍♂️ Autor

Desenvolvido por [Renan Figueiredo]  
Contato: [renanf.l@hotmail.com]
