import os
import smtplib
import ssl
import sys

from dejavu import Dejavu


class HiddenPrints:
    """Simple class just to hidden polluted outputs from dejavu"""

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def get_dejavu(db_host, db_user, db_password, db_name):
    db_config = {
        "database_type": "mysql",
        "fingerprint_limit": 1,
        "database": {
            "host": db_host,
            "user": db_user,
            "passwd": db_password,
            "db": db_name,
        },
    }
    return Dejavu(db_config)


def check_modem_connection(connection):
    """Checks if connection with modem is healthy"""
    connection.write(b"AT\r")
    answer = connection.read_until(b"\r\nOK\r\n")
    return b"OK" in answer


def perform_call_to_contest(connection):
    """Performs call to contest phone number (210304321)"""
    connection.write(b"ATD210304321;\r")
    answer = connection.read_until(b"\r\nOK\r\n")
    return b"OK" in answer


def send_alert_email():
    try:
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
        service.login("EMAIL", "PASSWORD")

        subject = "Bomba was detected"
        body = (
            f"Bomba was detected and call performed at {str(datetime.datetime.now())}"
        )

        email_text = """Subject: %s\n
        %s
        """ % (
            subject,
            body,
        )

        for to in ["DESTINATION_EMAIL"]:
            service.sendmail("SOURCE_EMAIL", to, email_text)

        service.quit()
    except Exception as e:
        print(f"Something went wrong while sending the email {e}")
