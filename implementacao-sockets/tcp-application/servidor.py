import socket

def getTraducao(termo, idioma):
    dicionario = {
        "protocolo": {
            "I": "protocol",
            "E": "protocolo"
        },
        "roteador": {
            "I": "router", 
            "E": "enrutador"
        },
        "firewall": {
            "I": "firewall",
            "E": "cortafuegos"
        },
        "gateway": {
            "I": "gateway",
            "E": "puerta de enlace"
        },
        "protocolo de internet (IP)": {
            "I": "internet protocol (IP)", 
            "E": "protocolo de internet (IP)"
        },
        "rede de área local (LAN)": {
            "I": "local area network (LAN)",
            "E": "red de área local (LAN)"
        },
        "rede privada virtual (VPN)": {
            "I": "virtual private network (VPN)", 
            "E": "red privada virtual(VPN)"
        },
        "switch": {
            "I": "switch", 
            "E": "conmutador"
        },
        "sistema de nomes de domínio (DNS)": {
            "I": "domain name system (DNS)", 
            "E": "sistema de nombres de dominio (DNS)"
        },
        "subnet": {
            "I": "subnet", 
            "E": "subred"
        }
    }

    if termo in dicionario: return dicionario[termo].get(idioma.upper(), "Idioma inválido.")
    else: return "Termo não encontrado."

def main():
    HOST = '127.0.0.1'
    PORT = 2319

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)

    print("O servidor TCP já está escutando na porta", PORT)

    while True:
        conn, addr = servidor.accept()
        print("Conexão estabelecida com ", addr)

        termo = conn.recv(1024).decode()
        idioma = conn.recv(1024).decode()

        traducao = getTraducao(termo, idioma)
        conn.send(traducao.encode())

        conn.close()

if __name__ == "__main__":
    main()
