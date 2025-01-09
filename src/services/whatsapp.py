import logging
from entities.contact import Contact
from entities.phone import PhoneInvalidException
from providers.chatbot import ChatBotProvider
from settings import BASE_URL, ACCESS_TOKEN, TEMPLATE_ID


class WhatsappService:

    def __init__(self):
        base_url = BASE_URL
        access_token = ACCESS_TOKEN
        self.template_id = TEMPLATE_ID
        self.provider = ChatBotProvider(base_url, access_token)

    def send_template_message(self, phone_number: str):

        try:
            contact = Contact.create(phone_number)
            phone_number = contact.get_phone_number()
            response = self.provider.send_template(phone_number, self.template_id)
            logging.info(f'Send message for phone number {phone_number}')

        except PhoneInvalidException as error:
            logging.error(f'{error.message} phone number: {phone_number}')