# Enviar mensagem de whatsapp para chamadas abandonadas em filas do Asterisk

## Descrição

Este repositório contém um projeto que consulta chamadas abandonadas em um servidor Asterisk e automatiza o envio de mensagens via WhatsApp para retomar o contato com os clientes. O objetivo é melhorar a experiência do cliente ao oferecer uma forma rápida e eficiente de retornar chamadas perdidas.

## Funcionalidades

- Consulta periódica das chamadas abandonadas no banco de dados do Asterisk.

- Geração de uma lista de números de telefone dos clientes com chamadas abandonadas.

- Envio automático de mensagens via WhatsApp para os números identificados.

## Requisitos

- Servidor Asterisk configurado com banco de dados MySQL.

- Python 3.8+.

- Serviço do GCHAT contratado, entre no site https://gnew.com.br para mais detalhes.

### Bibliotecas Python:

- mysql-connector-python.

- requests (para chamadas à API do GCHAT).

## Instalação

O script foi homologado utilizando o Ubuntu Server 24.04 LTS.

É necessário escalar os privilégios de usuário para root para seguir o procedimento abaixo.

Acesse o diretório /usr/src/

```
cd /usr/src/
```

Clone o repositório:

```
git clone https://github.com/Gnew-Solucoes-IP-Ltda/wpp-send.git`
cd wpp-send`
```

Execute o script install.sh:

```
bash install.sh
```

## Configuração

Crie um arquivo .env no diretório `/usr/src/wpp-send/src/` com as seguintes variáveis:

```
ACCESS_TOKEN='TOKEN API GCHAT'
TEMPLATE_ID='TEMPLATE MENSAGEM WHATSAPP ID'
URL_API='https://BASE URL GCHAT'


DB_HOST='127.0.0.1'
DB_USER='asteriskuser'
DB_PASSWORD='password'
DATABASE='asterisk'
```

Certifique-se de que o banco de dados do Asterisk está corretamente configurado e acessível.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

## Contato

Para mais informações ou suporte, entre em contato pelo email:
contato@gnew.com.br