import os
from connexion import FlaskApp

app = FlaskApp(__name__)
app.add_api('mymathserver.yml')

@app.route('/')
def index():
    return 'Welcome to My Math Server'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", "5001"))  # default 5001
    app.run(host='0.0.0.0', port=port)
