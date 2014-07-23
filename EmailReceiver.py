import sys
import imaplib
import getpass
import email
import datetime
import re

EMAIL_ADDRESS = "whereis.dimagi001@gmail.com"


def receive_emails():
    """
    Collect emails from account
    """
    # Retrieve auth info
    auth_info_file = open("PRIVATE")
    username = auth_info_file.readline()
    password = auth_info_file.readline()

    # Connect to imap server
    imap_connection = imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        imap_connection.login(username, password)
    except imaplib.IMAP4.error:
        print("Email Authentication Error")
        return

    # Retrieve all unread emails
    result, _ = imap_connection.select("INBOX")
    if result != "OK":
        print("Unable to select INBOX")
        return
    result, email_ids = imap_connection.search(None, "(UNSEEN)")

    # Are there new emails?
    if not email_ids[0]:
        return

    # Parse them
    for email_id in email_ids[0].split():
        ret, email_string = imap_connection.fetch(str(email_id), '(RFC822)')
        email_contents = email.message_from_string(email_string[0][1])
        body_text = email_contents.get_payload()[ 0 ].get_payload()




if __name__ == "__main__":
    receive_emails()