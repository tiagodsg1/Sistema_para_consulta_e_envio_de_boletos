import requests
from recuperar_boleto import recuperar_boleto

def emitir_boleto():
    request_body = "client_id=4e032da3-504b-49e8-973b-514b988088a9&client_secret=fc708758-7aec-4b60-b8c6-c2203b073c6b&scope=boleto-cobranca.read boleto-cobranca.write&grant_type=client_credentials"
        
    response = requests.post("https://cdpj.partners.bancointer.com.br/oauth/v2/token", 
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    cert=('Certificados/Inter API_Certificado.crt','Certificados/Inter API_Chave.key'),
    data=request_body)

    response.raise_for_status()

    token=response.json().get("access_token") 

    dados_boleto ={
    "seuNumero": "00001",
    "valorNominal": 100,
    "dataVencimento": "2023-10-24",
    "numDiasAgenda": 30,
    "pagador": {
        "cpfCnpj": "71375781448",
        "nome": "Nome do Pagador",
        "email": "",
        "telefone": "",
        "cep": "99999999",
        "numero": "00",
        "complemento": "",
        "bairro": "Bairro do Pagador",
        "cidade": "Cidade do Pagador",
        "uf": "MG",
        "endereco": "Endereço do Pagador",
        "ddd": "",
        "tipoPessoa": "FISICA"
        }
    }

    response = requests.post("https://cdpj.partners.bancointer.com.br/cobranca/v2/boletos", 
        headers={"Authorization": "Bearer " + token}, 
        cert=('Certificados/Inter API_Certificado.crt','Certificados/Inter API_Chave.key'),
        json=dados_boleto
    )

    response.raise_for_status()

    nosso_numero=response.json().get("nossoNumero")
    codigo_barras=response.json().get("codigoBarras")
    print(codigo_barras)
    print(nosso_numero)
    recuperar_boleto(nosso_numero)


if __name__ == "__main__":
    emitir_boleto()
    