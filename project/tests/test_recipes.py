import os
import unittest

from project.factory import create_app
from project.ext import db

app = create_app()
TEST_DB = 'test.db'


class ProjectTests(unittest.TestCase):
    # execute prior to each test
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        # db.create_all()

        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        # db.session.remove()
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Kennedy Family Recipes', response.data)
        self.assertIn(b'Breakfast Recipe', response.data)
        self.assertIn(b'Lunch Recipe', response.data)
        self.assertIn(b'Dinner Recipe', response.data)
        self.assertIn(b'Dessert Recipe', response.data)
        self.assertIn(b'Add Recipe', response.data)

    def test_main_page_query_results(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertIn(b'Add Recipe', response.data)

    def test_add_recipe(self):
        response = self.app.post(
            '/add',
            data=dict(recipe_title='hamburgers',
                      recipe_description='delicious hamburger with pretzel rolls'),
            follow_redirects=True)
        self.assertIn(b'Add Recipe', response.data)

    def test_add_invalid_recipe(self):
        response = self.app.post(
            '/add',
            data=dict(recipe_title='',
                      recipe_description='Delicious hamburger with pretzel rolls'),
            follow_redirects=True)
        self.assertIn(b'ERROR! Recipe was not added.', response.data)
        self.assertIn(b'This field is required.', response.data)


if __name__ == "__main__":
    unittest.main()
