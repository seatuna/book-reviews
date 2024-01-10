import os
from . import create_app  # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def hello():
    return "Hello World!"


# Applications Routes
from api import urls

# ----------------------------------------------- #

if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000

    app.run()
