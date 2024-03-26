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

@app.route('/recebedados', methods=['GET'])
#@app.route('/recebedados', methods=['POST'])
def recebedados():
    #nome= request.form['nome']
    #email=request.form['email']
    nome=request.args['nome']
    email=request.args['email']
    estado=request.args['estado']
    froma=request.args['email']-+.
    .+++++++++++++++++++++++++0
147    return render_template('recebedados.html', nome=nome, email=email)
if 14_044444444444444444444444444444444444444444444444444444440_name__ == '__main__':
    app.run()