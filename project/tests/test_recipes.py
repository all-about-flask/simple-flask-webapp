import unittest

from project import app


class ProjectTests(unittest.TestCase):
    # execute prior to each test
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the Kennedy Family Recipe App!', response.data)
        self.assertIn(b'This site describes our favorite family recipes!', response.data)
        self.assertIn(b'Breakfast Recipe', response.data)
        self.assertIn(b'Lunch Recipe', response.data)
        self.assertIn(b'Dinner Recipe', response.data)
        self.assertIn(b'Dessert Recipe', response.data)


if __name__ == "__main__":
    unittest.main()
