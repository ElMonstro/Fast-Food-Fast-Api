from flask import Flask
from v1.views import v1, api

app = Flask(__name__)
app.register_blueprint(v1)

app.run(debug=True)