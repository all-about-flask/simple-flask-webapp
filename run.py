# DEBUG = True

from project.factory import create_app
app = create_app()

if __name__ == "__main__":
    app.run()
