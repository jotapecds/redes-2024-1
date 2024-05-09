import socket

def main():
    HOST = '127.0.0.1'
    PORT = 2319

    termo = input("Digite um dos seguintes termos para obter sua tradução: \n\n> protocolo \n> roteador \n> firewall \n> gateway \n> protocolo de internet (IP) \n> rede de área local (LAN) \n> rede privada virtual (VPN) \n> switch \n> sistema de nomes de domínio (DNS) \n> subnet \n\n>>> ")
    idioma = input("\nAgora escolha o idioma desejado: \n\n> (I) Inglês \n> (E) Espanhol \n\n>>> ")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cliente.sendto(termo.encode(), (HOST, PORT))
    cliente.sendto(idioma.encode(), (HOST, PORT))

    traducao, _ = cliente.recvfrom(1024)
    print("Tradução:", traducao.decode())

    cliente.close()

if __name__ == "__main__":
    main()
