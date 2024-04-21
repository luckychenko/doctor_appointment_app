

import re
from fastapi import HTTPException


class Helpers:

    @staticmethod
    def check_phone_number(cls, v):
        # Custom validation to ensure phone number format is valid
        if not re.match(r'^0\d{10}$', v):
            raise HTTPException(detail='Invalid phone number format', status_code=400)
        return v