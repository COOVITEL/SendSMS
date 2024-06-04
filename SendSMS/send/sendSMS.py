import requests

def soap_sms(num, turn, city):
    soap_body = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://coovitel.niyaraky.com.co/webService">
        <soapenv:Header>
            <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                <wsse:UsernameToken>
                    <wsse:Username>desarrollador2@coovitel.coop</wsse:Username>
                    <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">sha1(52a0e5757660949482bab52763e055f3a41f97ee)</wsse:Password>
                    <wsse:Nonce>nonce_value</wsse:Nonce>
                    <wsu:Created xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">timestamp</wsu:Created>
                </wsse:UsernameToken>
            </wsse:Security>
        </soapenv:Header>
        <soapenv:Body>
            <web:RegistrarMensajeSMS>
                <web:idUsuario>desarrollador2@coovitel.coop</web:idUsuario>
                <web:Texto>Bienvenido a Coovitel {city}, tu turno es {turn}, por favor espera tu llamado en sala.\nRecuerda calificar nuestro servicio al finalizar.</web:Texto>
                <web:Celular>{num}</web:Celular>
                <web:Flash>true</web:Flash>
                <web:Certificado>false</web:Certificado>
            </web:RegistrarMensajeSMS>
            <!-- Aquí va el cuerpo de la solicitud específica del servicio web -->
        </soapenv:Body>
    </soapenv:Envelope>
    """

    url = 'https://coovitel.niyaraky.com.co/webService.php?WSDL'
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(url, data=soap_body, headers=headers)
    
    if response.status_code == 200:
        return f"Mensaje exitoso! {response.text}"
    else:
        raise Exception(f"Error al enviar el mensaje SMS: {response.status_code}")