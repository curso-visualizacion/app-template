from dash import Dash, html
from flask import Flask

server = Flask(__name__)
app = Dash(__name__, server=server)

app.layout = html.Div(children="Hello World")


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
