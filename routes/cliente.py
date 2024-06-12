from flask import Blueprint,render_template
from database.cliente import VIAGENS

cliente_route = Blueprint('cliente', __name__)

"""
    Rotas das Viagens
    
    - /clientes/ (GET) - Listar as viagens
    - /clientes/ (POST) - Inserir as viagens
    - /clientes/new (GET) - Mostrar um formulário para CRIAR uma viagem
    - /clientes/<id> (GET) - Obter os dados de uma viagem
    - /clientes/<id>/edit (GET)- Mostrar um formulário para editar os dados de uma viagem
    - /clientes/<id>/update (PUT) - atualizar os dados de uma viagem
    - /clientes/<id>/delete (DELETE) - Deletar uma viagem

"""
@cliente_route.route('/login')
def login():
    return render_template('login.html')

@cliente_route.route('/registro')
def registro():
    return render_template('registro.html')

@cliente_route.route('/lista_viagens')
def lista_viagens():
    #pagina padrao
    return render_template('lista_viagens.html', viagens=VIAGENS)

#Igual o de cima, mas serve para inserir na tabela
@cliente_route.route('/', methods=['POST'])
def inserir_viagem():
    #inserir/mostrar a nova viagem
    pass


@cliente_route.route('/new')
def form_viagem():
    #formulario para cadastrar uma viagem 
    return render_template('form_viagem.html')
    


@cliente_route.route('/<int:viagem_id>')
def detalhe_viagem(viagem_id):
    #exibir detalhes da viagem 
    render_template('detalhe_viagem.html')

@cliente_route.route('/<int:viagem_id>/edit')
def form_edit_viagem(viagem_id):
    #formulario para editar dados de uma viagem 
    return render_template('form_edit_viagem.html')

@cliente_route.route('/<int:viagem_id>/update', methods=['PUT'])
def update_viagem(viagem_id):
    #atualizar dados de uma viagem
    pass

@cliente_route.route('/<int:viagem_id>/deletet', methods=['DELETE'])
def delete_viagem(viagem_id):
    #deletar dados de uma viagem
    pass