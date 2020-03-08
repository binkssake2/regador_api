import os
import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Escreva /criar/evento para cria-lo e /deletar/evento para deletar, o evento é da forma t00:00d05 onde se tem o inicio e sua duracao em minutos (botar o 0 quando na tiver nos minutos) e para ver tudo /eventos</hi>"


@app.route('/deletar/<string:evento>')
def deletar(evento):
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()["infos"]
    infos = infos.replace(evento,"")
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/'
    headers = {'Content-Type': 'application/json','secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    data = {"infos":infos}
    requests.put(url, json=data, headers=headers)
    return "<h1>Evento deletado<hi>"

@app.route('/criar/<string:evento>')
def criar(evento):
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()["infos"]
    infos = infos + evento
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/'
    headers = {'Content-Type': 'application/json','secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    data = {"infos":infos}
    requests.put(url, json=data, headers=headers)
    return "<h1>Evento criado<hi>"

@app.route('/eventos')
def eventos():
    url = 'https://api.jsonbin.io/b/5e61133074ed8a66ce71e657/latest'
    headers = {'secret-key': '$2b$10$ZYd/uxhp./Hfer6e/nPFW.iAhykkM2rGWMSbO2St8K2YEh7NUc8Z2'}
    req = requests.get(url, headers=headers)
    infos = req.json()["infos"]
    return str(infos)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    
