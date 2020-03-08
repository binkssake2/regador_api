import os
import requests
import json
from flask import Flask, render_template, request, redirect


def createeventoshtml(eventos):
    html = "<h1>Todos os eventos</h1>"
    for idx, evento in enumerate(eventos):
        eventohtml = f'<h3>Evento {idx}'
        iniciohtml = f'<ul><li>Hora de início: {evento[0][0]}:{evento[0][1]}</li>'
        durhtml = f'<li>Duração: {evento[1][0]}:{evento[1][1]}</li>'
        removehtml = f'<li><a href="/deletar/{idx}">Deletar</a></li></ul>'
        closehtml = "</h3>"
        html += (eventohtml + iniciohtml + durhtml + removehtml + closehtml)
    htmlcriar = '<a href="/criar">Criar novo evento</a>'
    html += htmlcriar
    return html


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Escreva /criar/evento para cria-lo e /deletar/evento para deletar, o evento é da forma t00:00d05 onde se tem o inicio e sua duracao em minutos (botar o 0 quando na tiver nos minutos) e para ver tudo /eventos</hi>"


@app.route('/deletar/<int:eventID>')
def deletar(eventID):
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()
    infos.pop(eventID)
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/'
    headers = {'Content-Type': 'application/json','secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    requests.put(url, json=infos, headers=headers)
    return redirect("/eventos", code=302)

@app.route('/criar')
def criar():
    return """
    <form action="/handlecriar">
      <label for="hora">Hora de inicio:</label><br>
      <input type="text" id="hora" name="hora" value="23:30"><br>
      <label for="dur">Duração:</label><br>
      <input type="text" id="dur" name="dur" value="00:30"><br><br>
      <input type="submit" value="Criar">
    </form>
    """

@app.route('/handlecriar')
def handlecriar():
    hora = request.args.get('hora').split(':')
    dur = request.args.get('dur').split(':')
    evento = [
        [
            int(hora[0]), 
            int(hora[1])
        ],
        [
            int(dur[0]), 
            int(dur[1])
        ]
    ]

    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    db = req.json()

    db.append(evento)

    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/'
    headers = {'Content-Type': 'application/json','secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    requests.put(url, json=db, headers=headers)
    return redirect("/eventos", code=302)

@app.route('/eventos')
def eventos():
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()
    return createeventoshtml(infos)

@app.route('/db')
def dbview():
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()
    return json.dumps(infos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    
