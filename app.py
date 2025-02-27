from flask import Flask, jsonify, request

app = Flask(__name__) # Inicia a aplicação. Os endpoints são definidos por essa variável

livros = [
    {
        'id': 1,
        'título': 'O Silmarillion',
        'ano': 1977,
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'título': 'O Cavaleiro dos Sete Reinos',
        'ano': 2014,
        'autor': 'George R. R. Martin'
    },    
    {
        'id': 3,
        'título': 'E Não Sobrou Nenhum',
        'ano': 1939,
        'autor': 'Agatha Christie'
    },
    {
        'id': 4,
        'título': 'Carrie',
        'ano': 1974,        
        'autor': 'Stephen King'
    },    
    {
        'id': 5,
        'título': 'Conan O Bárbaro',
        'ano': 2024 ,
        'autor':'L. Sprague De Camp, Lin Carter'
    },

]

# Fazendo os métodos (verbos)

#GET ALL
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#GET BY ID
@app.route('/livros/<int:id>',methods=['GET'])
def obter_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#EDIT BY ID
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_por_id(id):
    livro_alt = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alt)
            return jsonify(livros[indice]) 

#CREATE NEW
@app.route('/livros',methods=['POST'])
def criar_livro():
    livro_novo = request.get_json()
    livros.append(livro_novo)
    return jsonify(livros)

#DELETE
@app.route('/livros/<int:id>',methods=['DELETE'])
def deletar_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
   


app.run(port=5000,host='localhost',debug=True)