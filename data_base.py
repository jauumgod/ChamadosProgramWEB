from flask_sqlalchemy import SQLalchemy

class User(db.Model):
  def usuarios(self):
    __tablename__ = 'usuarios'
    add = usuarios()
    add.id = db.column(db.Integer, primary_key=True)
    add.name = db.column(db.String(84), nullable=False)
    add.email = db.column(db.String(84), nullable=False, unique=True)
    add.password = db.column(db.String(255), nullable=False)
    
    def __str__(self):
      return self.name
    
    
      
