# Radio Comercial Bomba 💣 Detector

This repository provides an automated solution for participating in contests hosted by Portugal's national radio broadcaster, Radio Comercial. Participants are required to call in promptly after hearing a specific sound to win vouchers for fuel stations.

The sound to be detected is included in the repository and will be loaded into Dejavu upon startup for seamless operation.

## Features

* Sound Detection: Utilizes the [Dejavu library](https://github.com/worldveil/dejavu) to detect the designated sound played during the contest.
* Automated Calling: Initiates the call automatically upon detecting the specified sound.

## Requirements

* To perform the call, it requires a GSM Modem with a SIM card to be connected for making the call.
* It is recommended to connect an analog radio directly to an input jack of the device for minimal delay.

## Usage

1. Install the necessary Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the MySQL server using Docker Compose:

    ```bash
    docker-compose up -d
    ```

3. Run the script

    ```bash
    python main.py
    ```

## Additional Notes

Keep in mind that if your phone number wins the contest they will call you back shortly.
That means that you need some strategy to be able to pick up the call (forward it to another number, for example).

[Contest Info](https://radiocomercial.pt/artigo/bomba-um-deposito-de-combustivel-a-qualquer-momento-na-comercial)