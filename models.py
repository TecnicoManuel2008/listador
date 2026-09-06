from sqlalchemy import create_engine
import sqlalchemy as db

from sqlalchemy.orm import (

   declarative_base,
   sessionmaker
)

# CONFUGURAÇÕES DO MOTOR E SESSOES
Engine = create_engine("sqlite:///tarefas.db")
Base = declarative_base()
Session = sessionmaker(bind=Engine)

""" Criando a table Tasks """
class Tasks(Base):
    __tablename__ = "Tasks"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Tarefas: [{self.description}] "
        

""" Criar a tabela """
Base.metadata.create_all(Engine)
