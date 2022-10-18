import unittest

from project.factory import create_app

app = create_app()


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
        self.assertIn(b'Kennedy Family Recipes', response.data)
        self.assertIn(b'Breakfast Recipe', response.data)
        self.assertIn(b'Lunch Recipe', response.data)
        self.assertIn(b'Dinner Recipe', response.data)
        self.assertIn(b'Dessert Recipe', response.data)


if __name__ == "__main__":
    unittest.main()
