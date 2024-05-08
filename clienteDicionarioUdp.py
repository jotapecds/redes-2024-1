import socket

def main():
    host = '127.0.0.1'
    port = 12345

    palavra = input("Digite um dos seguintes termos para obter sua tradução: \n\n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n> protocolo \n\n>>> ")
    idioma = input("\nAgora escolha o idioma desejado: \n\n> (I) Inglês \n> (E) Espanhol \n\n>>> ")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cliente.sendto(palavra.encode(), (host, port))
    cliente.sendto(idioma.encode(), (host, port))

    traducao, _ = cliente.recvfrom(1024)
    print("Tradução:", traducao.decode())

    cliente.close()

if __name__ == "__main__":
    main()
