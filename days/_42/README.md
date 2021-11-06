# :calendar: Day 42: 11/5/2021

---

## Topics

:clipboard: JSON Data in Python

---

## Resources

:star: [PyBite 16](https://codechalleng.es/challenges/16/)

:star: [Twilio API](https://www.twilio.com/docs/sms/api)

---

## Tasks

:white_check_mark: Choose a use case - send text messages with the Twilio API

:white_large_square: Complete PyBite 16

---

## Notes

### :notebook: 11/5/21

- Setup Twilio:
    - API credentials.
    - Phone number (+15034863861).
- Added `python-dotenv` and `requests-mock` to [`requirements.txt`](requirements.txt)
- Created [test_twilio_api.py](tests/test_twilio_api.py) with a `pytest` framework.
    - Temporarily bypassed TDD in order to become familiar with the Twilio API, and to re-familiarize with the `requests_mock` `pytest` fixture.
    - Need to create functional `pytest` tests and resume TDD.
- Created [twilio_api.py](pybite_16/twilio_api.py) to provide the `TwilioAPI` `class` object.
    - Created simple `__init__` method.
    - Created `send_msg` method to send an SMS message.
- Created [twilio_app.py](pybite_16/twilio_app.py) to create an instance of the `TwilioAPI` `class` object.
    - Successfully tested sending an SMS message with the following code:

    ```python
    from pybite_16.twilio_api import TwilioAPI

    twilio = TwilioAPI()

    msg = twilio.send_msg(
        account_sid=getenv('ACCOUNT_SID'),
        user_sid=getenv('USER_SID'),
        user_key=getenv('USER_KEY'),
        message_body='Python send_msg method test'
    )
    ```
