#!/usr/src/wpp-send/venv/bin/python

import logging
from time import sleep
from repositories.call_repository import CallRepository
from services.whatsapp import WhatsappService


logger = logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S',
    filename='wpp-send.log',
    level=logging.INFO
)


if __name__ == '__main__':
    whatsapp_service = WhatsappService()
    call_repository = CallRepository()

    try:

        while True:

            for phone_number in call_repository.get_abandon_callers():
                whatsapp_service.send_template_message(phone_number)
            
            sleep(60)
    
    except KeyboardInterrupt:
        print('Exec end')