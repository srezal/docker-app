from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from models.User import User

admin = Admin(app)
admin.add_view(ModelView(User, db.session))