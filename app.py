from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/compras")
def compras():
    return render_template('compras.html',item1="laranja", item2="farofa")

@app.route ('/mercados')
def mercados():
    return render_template('mercado.html') 

'''@app.route ('/gastos')
def gastos():
    mes="fevereiro"
    valor="843,00"
    return render_template('gastos.html',a=mes, b=valor)'''

@app.route ('/gastos', defaults={'mes':'janeiro', 'valor':'0'})
@app.route ('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html',a=mes, b=valor)

@app.route ("/dobro", defaults={'n':0})
@app.route ('/dobro/<int:n>')
@app.route ('/dobro/<float:n>')
def dobro(n):
    resultado=2*n
    return render_template('dobro.html', n=n, resultado=resultado)

@app.route ('/perfil/<nome>')
def perfil (nome):
    return render_template('perfil.html', nome=nome)

@app.route ('/dados')
def dados():
    return render_template('dados.html')

@app.route ('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade>=18:
        return "você é maior de idade"
    else:
        return "você é menor de idade"
    
@app.route ('/situacaofinal/<float:nota>')
def situacaofinal(nota):
    if nota>=60.0:
        return"aprovado"
    elif nota>=20.0:
        return "recuperação"
    else:
        return "reprovado"
    
@app.route ('/login')
def login():
    return render_template('login.html')

@app.route ('/verificalogin', methods=['post'])
def verificalogin():
    usuario=request.form['usuario']
    senha=request.form['senha']
    if usuario=="alba" and senha=="123":
        return render_template ('arearestrita.html')
    else:
        return "Você não tem permissão"
    
@app.route('/verificaidade2/<int:idade>')
def verificaidade2(idade):
    return render_template('verificaidade2.html', idade=idade)

@app.route('/usuario/<nome>')
def usuario (nome):
    return render_template ('usuario.html', nome=nome)