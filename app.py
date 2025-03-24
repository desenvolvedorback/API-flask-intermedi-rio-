from flask import Flask, jsonify, request
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

# Pegue o token criptografado da variável de ambiente
API_KEY = os.getenv('API_KEY')  # Chave criptografada da API real

# Função para descriptografar o token
def decrypt_token(encrypted_token):
    cipher = Fernet(os.getenv('SECRET_KEY'))  # A chave secreta para criptografar e descriptografar
    return cipher.decrypt(encrypted_token.encode()).decode()

@app.route('/consulta_numero', methods=['GET'])
def consulta_numero():
    telefone = request.args.get('telefone')
    
    if not telefone:
        return jsonify({"error": "Número de telefone é necessário!"}), 400
    
    # Decriptografando o token armazenado
    decrypted_token = decrypt_token(API_KEY)
    
    # Simulação de consulta à API real usando o token descriptografado
    response = {
        "numero": telefone,
        "status": "validado",
        "token_usado": decrypted_token
    }
    
    return jsonify(response)

if -_name__ == '__main__':
    app.run(debug=True)
