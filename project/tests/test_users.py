import unittest
from project import app


class ProjectTest(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        pass

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Future site for logging into Kennedy Family Recipes!', response.data)


if __name__ == "__main__":
    unittest.main()
