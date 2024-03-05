import datetime

import serial
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

from utils import *

# Config
DB_HOST = "127.0.0.1"
DB_USER = "dejavu_user"
DB_PASSWORD = "dejavu_password"
DB_NAME = "dejavu"
MODEM_CHANNEL = "/dev/ttyUSB0"

djv = get_dejavu(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
djv.fingerprint_directory("./samples/", [".mp3"], 4)
connection = serial.Serial(
    MODEM_CHANNEL,
    115200,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=3,
    rtscts=False,
    dsrdtr=False,
)

print_animation = True
while True:
    if not check_modem_connection(connection):
        input("Something went wrong, modem is not answering")

    print("Listening... /" if print_animation else "Listening... \\", end="\r")
    print_animation = not print_animation
    with HiddenPrints():
        recognizer = djv.recognize(MicrophoneRecognizer, seconds=1)

    # Something was found with over 6 matches
    if recognizer[0] != [] and recognizer[0][0]["hashes_matched_in_input"] > 6:
        perform_call_to_contest(connection)
        print(f"Call performed at {datetime.datetime.now()}")
        # send_alert_email()
        break
