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
        "rede privada virtual (VPN):": {
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
    PORT = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))

    print("Servidor UDP está aguardando conexões...")

    while True:
        data, addr = servidor.recvfrom(1024)
        palavra = data.decode()
        
        data, addr = servidor.recvfrom(1024)
        idioma = data.decode()

        traducao = getTraducao(palavra, idioma)
        servidor.sendto(traducao.encode(), addr)

if __name__ == "__main__":
    main()
