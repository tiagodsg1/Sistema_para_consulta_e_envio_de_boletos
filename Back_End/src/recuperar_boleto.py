import requests
import base64
def recuperar_boleto(nosso_numero):
    request_body = "client_id=4e032da3-504b-49e8-973b-514b988088a9&client_secret=fc708758-7aec-4b60-b8c6-c2203b073c6b&scope=boleto-cobranca.read boleto-cobranca.write&grant_type=client_credentials"
        
    response = requests.post("https://cdpj.partners.bancointer.com.br/oauth/v2/token", 
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    cert=('Certificados/Inter API_Certificado.crt','Certificados/Inter API_Chave.key'),
    data=request_body)

    response.raise_for_status()

    token=response.json().get("access_token") 

    response = requests.get(f"https://cdpj.partners.bancointer.com.br/cobranca/v2/boletos/{nosso_numero}/pdf", 
        headers={"Authorization": "Bearer " + token}, 
        cert=('Certificados/Inter API_Certificado.crt','Certificados/Inter API_Chave.key') 
    )

    response.raise_for_status()
    # Decodifica a string Base64 para bytes
    base64_data = response.json().get("pdf")
    pdf_data = base64.b64decode(base64_data)
    # Salva os bytes do PDF em um arquivo
    with open('Boletos/boleto.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_data)




    