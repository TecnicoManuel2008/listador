from flask import Flask, render_template, url_for, request, redirect
from models import Tasks, Session

app = Flask(__name__)

"""Criando a rota principal ou main """
@app.route('/', methods=["GET"])
def main():
    with Session() as session:
        dados = session.query(Tasks).all()
        
    return render_template('index.html', tarefas=dados)
    
""" Criando a rota : /create que cria """
@app.route('/create', methods=["POST"])
def criar():
    # se o método for POST
    if request.method == "POST":
       with Session() as session:
           # Pixar à tarefa do html
           tarefa = request.form.get("task")
           # criar uma nova task na tabela
           task = Tasks(description=tarefa)
           # adicionar a task no banco
           session.add(task)
           session.commit()
           
       print(" << Adicionado com sucesso >>")
       return redirect(url_for('main'))
       
""" Criando a rota que delrta dados """
@app.route("/delete", methods=["GET", "POST"])
def deleta():
    with Session() as session:
         # puxar o valor do html
         task_id = request.form.get("del")
         # fazer o select
         dados = session.query(Tasks).filter(Tasks.id==task_id).first()
         # apaga a task
         session.delete(dados)
         session.commit()
         
         return redirect(url_for('main'))
    
""" """
 
if __name__ == "__main__":
    app.run(debug=False)
    
    