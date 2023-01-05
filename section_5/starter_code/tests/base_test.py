from unittest import TestCase

from section_5.starter_code.app import app
from section_5.starter_code.db import db


class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app.context():
            db.init_app()
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
