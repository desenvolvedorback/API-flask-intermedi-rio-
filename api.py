import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import requests

# Carregar as variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Carregar os tokens e chaves de API a partir das variáveis de ambiente
API_KEY_NUMVERIFY = os.getenv("API_KEY_NUMVERIFY")
API_KEY_ABUSEIPDB = os.getenv("API_KEY_ABUSEIPDB")

# Função para consultar a API NumVerify
@app.route('/consultar_numero', methods=['GET'])
def consultar_numero():
    telefone = request.args.get('telefone')
    if not telefone:
        return jsonify({'error': 'Telefone é obrigatório'}), 400

    url = f'http://apilayer.net/api/validate?access_key={API_KEY_NUMVERIFY}&number={telefone}&format=1'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Erro ao consultar número'}), 500

# Função para verificar IP no AbuseIPDB
@app.route('/verificar_ip', methods=['GET'])
def verificar_ip():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({'error': 'IP é obrigatório'}), 400

    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {'Key': API_KEY_ABUSEIPDB, 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json()['data'])
    else:
        return jsonify({'error': 'Erro ao verificar IP'}), 500

# Página inicial
@app.route('/')
def home():
    return "Bem-vindo à API de Consultas!"

if -_name__ == "__main__":
    app.run(debug=True)
