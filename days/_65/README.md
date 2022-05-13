# :calendar: Day 65: 5/12/2022

---

## Topics

:clipboard: Sending Emails With `smtplib`

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Watch videos 7-8

---

## Notes

### :notebook: 5/12/22

- Watched videos 7-8.
- MIME does not honor the BCC field as a message element, by design.
    - All parts of the MIME header part will be displayed
    - Adding a BCC field to an `email.mime.multipart.MIMEMultipart` object will effectively create a non-blind CC message element:

        ```python
        from email.mime.multipart import MIMEMultipart

        # Create a MIMEMultipart object
        mime_message = MIMEMultipart()

        # Create From and Subject message parts
        mime_message['From'] = 'user1@email.local'
        mime_message['Subject'] = 'Test email'

        # Creating a BCC field in this manner will NOT create a 'blind' CC list
        mime_message['Bcc'] = 'user2@email.local'
        ```

- The workaround for this situation is to create a list object with all email addresses for the BCC field, and pass that list to the `to_addrs` parameter of the `smtplib.SMTP.sendmail` object:

    ```python
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Create a MIMEMultipart object
    mime_message = MIMEMultipart()

    # Create From and Subject message parts
    mime_message['From'] = 'user1@email.local'
    mime_message['Subject'] = 'Test email' 

    # Create a message body
    body = 'This is the email body'
    mime_messsage.attach(
        payload=MIMEText(
            _text=body,
            _subtype='plain'
        )
    )

    # Create a BCC list
    bcc_list = [
        'user1@email.local',
        'user2@email.local',
        'user3@email.local'
    ]

    # Create an smtplib.SMTP object
    with smtplib.SMTP(
        host='smtp_server',
        port=587
    ) as smtp_object:

        # Setup the SMTP connection
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.login(
            user='user_name',
            password='app_password'
        )

        # Send the SMTP message
        smtp_object.sendmail(
            from_addr='from_address',
            # Enclose the to address in a list, and concatenate with the bcc_list 
            to_addrs=['to_address'] + bcc_list'
            msg=mime_message.as_string()
        )
    ```

- Created [./blob/main/days/_64/emailer_app/emailer_mime_bcc.py](./blob/main/days/_64/emailer_app/emailer_mime_bcc.py) to send emails to a BCC recipients list.
