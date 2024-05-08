import socket

# Dicionário de tradução (português -> inglês/espanhol)
traducoes = {
    "rede": {"ingles": "network", "espanhol": "red"},
    "protocolo": {"ingles": "protocol", "espanhol": "protocolo"}
    # Adicione mais palavras e suas traduções aqui
}

def traduzir_palavra(palavra, idioma):
    if palavra in traducoes:
        return traducoes[palavra].get(idioma, "Tradução não encontrada")
    else:
        return "Palavra não encontrada no dicionário"

def main():
    host = '127.0.0.1'
    port = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(1)

    print("Servidor TCP está aguardando conexões...")

    while True:
        conn, addr = servidor.accept()
        print("Conexão estabelecida com ", addr)

        palavra = conn.recv(1024).decode()
        idioma = conn.recv(1024).decode()

        traducao = traduzir_palavra(palavra, idioma)
        conn.send(traducao.encode())

        conn.close()

if __name__ == "__main__":
    main()
