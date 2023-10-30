import requests
import base64
def recuperar_boleto(nosso_numero):
    request_body = "client_id={seuid}&client_secret={seuid}&scope=boleto-cobranca.read boleto-cobranca.write&grant_type=client_credentials"
        
    response = requests.post("https://cdpj.partners.bancointer.com.br/oauth/v2/token", 
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    cert=('certificado.crt','certifiado.key'),
    data=request_body)

    response.raise_for_status()

    token=response.json().get("access_token") 

    response = requests.get(f"https://cdpj.partners.bancointer.com.br/cobranca/v2/boletos/{nosso_numero}/pdf", 
        headers={"Authorization": "Bearer " + token}, 
        cert=('certificado.crt','certificado.key') 
    )

    response.raise_for_status()
    # Decodifica a string Base64 para bytes
    base64_data = response.json().get("pdf")
    pdf_data = base64.b64decode(base64_data)
    # Salva os bytes do PDF em um arquivo
    with open('Boletos/boleto.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_data)




    
