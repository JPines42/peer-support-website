# Import module
from website import create_app

# App creation
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
