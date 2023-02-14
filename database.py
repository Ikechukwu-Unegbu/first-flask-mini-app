# from project import create_app, db
from project import create_app, db
from project.models import User


app = create_app()

with app.app_context():
    db.create_all()
