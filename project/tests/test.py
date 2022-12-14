import unittest

# import self as self

from project import app


class ProjectTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] =True
        app.config['DEBUG']= False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the Kennedy Family Recipe App!', response.data)
        self.assertIn(b'This site describes our favorite family recipes!', response.data)
        self.assertIn(b'Breakfast Recipes', response.data)
        self.assertIn(b'Lunch Recipes', response.data)
        self.assertIn(b'Dinner Recipes', response.data)
        self.assertIn(b'Dessert Recipes', response.data)

    if __name__ == "__main__":
        unittest.main()