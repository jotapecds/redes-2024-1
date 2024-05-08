import socket

def main():
    host = '127.0.0.1'
    port = 12345

    palavra = input("Digite a palavra a ser traduzida: ")
    idioma = input("Digite o idioma desejado (inglês ou espanhol): ")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    cliente.send(palavra.encode())
    cliente.send(idioma.encode())

    traducao = cliente.recv(1024).decode()
    print("Tradução:", traducao)

    cliente.close()

if __name__ == "__main__":
    main()
