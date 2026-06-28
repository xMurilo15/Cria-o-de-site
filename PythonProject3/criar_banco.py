from fakePInterest import database,app
from fakePInterest.models import Usuario,Foto

with app.app_context():
    database.create_all()