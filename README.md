Criei essa aplicação após assistir esse vídeo do canal do YouTube Dev Aprender.
Link vídeo: https://www.youtube.com/watch?v=FBLAV1SbJFk&list=PLmxNjDka04TuMmTWZFhdNhACLFg8YSzj7&index=8

Insights sobre a aula:

1. Primeira coisa é preciso entender o que você quer fazer com uma API. Nesse caso, será criado uma API para consulta de livros, cadastro de livros, pesquisa por um livro específico (id), alteração de um livro específico
ou deletar um livro. Para isso é usado o VS Code, bibliotecas FLASK, JSONIFY e REQUEST e o POSTMAN.

2. A URL base será localhost, ou seja, será criado um ambiente na própria máquina apenas.

3. Endpoint basicamente são os verbos que a sua API irá utilizar, no caso GET, POST, PUT e DELETE.

4. Esses endpoints serão usados através do POSTMAN, uma ferramenta para fazer REQUISIÇÕES a uma API.

5. Tive que fazer a instalação do Flask no próprio terminal do VS Code, com o código aberto:

    - pip install Flask

6. app = Flask(__name__) 

	  - Inicia a aplicação. Os endpoints são definidos por essa variável (exemplo mais abaixo)
  
 7. - A fonte de dados será criada no próprio código. Obviamente isso não é recomendado, pois o ideal seria utilizar um arquivo, ou banco de dados, mas como essa é uma aplicação simples, será feito assim

8. Método consultar todos os livros:

 - #GET ALL
	@app.route('/livros',methods=['GET'])
	def obter_livros():
      return jsonify(livros)

- @app.route... é a rota para acessar esse endpoint

- app.run(port=5000,host='localhost',debug=True)

   - Fica no final do código, definindo a rota
 
- No Postman: http://localhost:5000/livros

9. Método alterar por ID:

- @app.route('/livros/<int:id>',methods=['PUT'])
   def editar_por_id(id):
  	    livro_alt = request.get_json()
  	    for indice, livro in enumerate(livros):
      	    if livro.get('id') == id:
          	    livros[indice].update(livro_alt)
                return jsonify(livros[indice])

 -  Passado um ID no endpoint , é salvo a informação (formato JSON) na variável livro_alt

 - O ENUMERATE é usado para deixar explicito que cada livro (dado cadastrado) tem um índice, começando com 0

 - livro.get('id') compara com a id que foi passada no endpoint. Quando TRUE, o livro é atualizado usando o indice no FOR

 - A atualização é feita no POSTMAN, selecionando o verbo PUT, depois BODY, RAW e JSON. Deve-se passar no formato igual está dos outros livros, para
	não bagunçar o formato dos dados. O uso desse método é ideal no caso de um cadastro estar com o ano errado ou título, por exemplo.
	Assim usa-se esse método para atualizar a informação.  





