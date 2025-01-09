from settings import (
    COUNTRY_CODE,
    AREA_CODE,
    LENGTH_MIN_VALID_PHONE,
    LENGTH_MIN_VALID_PHONE_WITHOUT_COUNTRY_CODE,
    LENGTH_MIN_VALID_PHONE_WITHOUT_AREA_CODE
)


class PhoneInvalidException(Exception):

    def __init__(self, message: str):
        self.message = message


class Phone:

    def __init__(self, number: str) -> None:
        self.number = self._conversion_pattern_e164(number)

    @property
    def eh_mobile(self) -> bool:
        return bool(self.number[4] == '9')

    def _conversion_pattern_e164(self, number: str) -> str:

        if len(number) < LENGTH_MIN_VALID_PHONE:
            raise PhoneInvalidException('ERROR LENGTH MIN!')

        elif len(number) in LENGTH_MIN_VALID_PHONE_WITHOUT_COUNTRY_CODE:
            return f'{COUNTRY_CODE}{number}'

        elif len(number) in LENGTH_MIN_VALID_PHONE_WITHOUT_AREA_CODE:
            return f'{COUNTRY_CODE}{AREA_CODE}{number}'

        return number