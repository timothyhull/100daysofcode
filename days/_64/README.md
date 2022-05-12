# :calendar: Day 64: 5/9/2022-5/11/2022

---

## Topics

:clipboard: Sending Emails With `smtplib`

---

## Resources

:star: [Create a Google app-specific password](https://support.google.com/accounts/answer/185833)

---

## Tasks

:white_check_mark: Watch videos 1-4

:white_check_mark: Watch video 5

:white_large_square: Watch videos 6-8

---

## Notes

### :notebook: 5/9/22

- Watched videos 1-4.
- Verified the existence of an existing Google app-specific password intended for use with Python.
- The required Python modules are `smtplib` and `email.mime`, and are part of the Python Standard Library.
- Created two blank Python files to support sending emails:
    - [./blob/main/days/_64/emailer_app/emailer.py](./blob/main/days/_64/emailer_app/emailer.py).
    - [./blob/main/days/_64/emailer_app/emailer_mime.py](./blob/main/days/_64/emailer_app/emailer_mime.py).

---

### :notebook: 5/10/22

- Watched video 5.
- Added basic functional code to [./blob/main/days/_64/emailer_app/emailer.py](./blob/main/days/_64/emailer_app/emailer.py).
    - Refactored code with a `send_email` function, and added `print` statements at each steps for a better interactive experience.

---

### :notebook: 5/11/22

- Refactored [./blob/main/days/_64/emailer_app/emailer.py](./blob/main/days/_64/emailer_app/emailer.py) with additional constants.

- Watched video 6
    - MIME stands for **Multipurpose Internet Mail Extensions**.
    - MIME extends email functionality, by allowing multiple parts within an email message (header, subject, body, etc.).
    - The message body can be **plain text** or **HTML**.

- Added basic functional code to [./blob/main/days/_64/emailer_app/emailer_mime.py](./blob/main/days/_64/emailer_app/emailer_mime.py).
    - Ported over the imports, `namedtuple` objects, and constants from [./blob/main/days/_64/emailer_app/emailer.py](./blob/main/days/_64/emailer_app/emailer.py):
        - Modified the `EmailObject` `namedtuple` object to include a field for an email subject.
    - Created the function `create_mime_message` to construct a MIME message using the `email.mime.multipart.MIMEMultipart` method.
        - Use the `email.mime.text.MIMEText` method to create a plain text email body.
            - Also supports creating an HTML-based body.
        - Returns a `email.mime.multipart.MIMEMultipart` object (`mime_message`) that contains an email header, subject, and body.
    - Ported over the majority of the `send_email` function from [./blob/main/days/_64/emailer_app/emailer.py](./blob/main/days/_64/emailer_app/emailer.py):
        - Added the **kwarg** `mime_message` to support including the return value from the `create_mime_message` function.
