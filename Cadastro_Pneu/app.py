from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["loja_pneus"]
colecao_pneus = db["pneus"]

# Página principal: lista de pneus
@app.route('/')
def index():
    pneus = list(colecao_pneus.find())
    return render_template('index.html', pneus=pneus)

# Cadastrar novo pneu
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        pneu = {
            "marca": request.form['marca'],
            "modelo": request.form['modelo'],
            "tamanho": request.form['tamanho'],
            "preco": float(request.form['preco'])
        }
        colecao_pneus.insert_one(pneu)
        return redirect('/')
    return render_template('cadastrar.html')

# Editar pneu existente
@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    pneu = colecao_pneus.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        colecao_pneus.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "marca": request.form['marca'],
                "modelo": request.form['modelo'],
                "tamanho": request.form['tamanho'],
                "preco": float(request.form['preco'])
            }}
        )
        return redirect('/')
    return render_template('editar.html', pneu=pneu)

# Apagar pneu
@app.route('/apagar/<id>')
def apagar(id):
    colecao_pneus.delete_one({"_id": ObjectId(id)})
    return redirect('/')

# Buscar pneus por marca, modelo ou tamanho
@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '').strip()
    filtro = {"$or": [
        {"marca": {"$regex": termo, "$options": "i"}},
        {"modelo": {"$regex": termo, "$options": "i"}},
        {"tamanho": {"$regex": termo, "$options": "i"}}
    ]}
    pneus = list(colecao_pneus.find(filtro))
    return render_template('index.html', pneus=pneus, termo=termo)

# Página para impressão
@app.route('/imprimir')
def imprimir():
    pneus = list(colecao_pneus.find())
    return render_template('imprimir.html', pneus=pneus)

if __name__ == '__main__':
    app.run(debug=True)
