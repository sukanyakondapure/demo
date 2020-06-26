from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pqrs@localhost/webel_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
