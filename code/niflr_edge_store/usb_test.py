import usb.core
import usb.util
import requests
from user.store import *
from cryptography.fernet import Fernet
import jwt
import requests
from requests.auth import HTTPBasicAuth
from iot.models import *

# Find the USB device
dev = usb.core.find(idVendor='0x2dd6', idProduct='0x21c1') # Replace XXXX with the vendor and product IDs of your USB device

if dev is None:
    raise ValueError('USB device not found')

# Configure the USB device
dev.set_configuration()

# Loop to detect input from the USB port
while True:
    try:
        # Read the data from the USB port
        val = dev.read(1, 8) # Read 8 bytes of data from endpoint 1
        print("Input fetched: ", val)
        if get_store_status() == REFILLMENT_MODE:
            print("Oops!!! System under Refillment Mode")

        elif get_store_status() == MAINTENANCE_MODE:
            print("Oops!!! System under Maintenance Mode")

        else:
            # Fernet Secret
            encryption_key = b'kYZ-3CPIdjJxaLBZlzqzBcg8EyQKTcUigASAv2IZ8tE='
            encrypted_token = val
            encrypted_token = bytes(encrypted_token, 'utf-8')

            print(type(encrypted_token))
            fernet = Fernet(encryption_key)
            decrypted_token = fernet.decrypt(encrypted_token)

            token = decrypted_token.decode('utf-8')

            # JWT token secret
            secret_key = 'mysecretkey'
            try:
                payload_rec = jwt.decode(token, secret_key, algorithms=['HS256'])
                print(payload_rec)
            except jwt.exceptions.InvalidSignatureError:
                print('Invalid User')

            session_id = StoreSessions.objects.order_by('created_at').values_list('id', flat=True).last()
            print(session_id)

            url = "http://127.0.0.1:8000/user_session/"

            payload = {
                "user_id": payload_rec['id'],
                "phone_number": payload_rec['phoneNumber'],
                "role": payload_rec['role'],
                "status": "Entry Authenticated",
                "session_id": str(session_id)
            }
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(url, auth = HTTPBasicAuth('kushal', 'Kushal@123'), json=payload, headers=headers)

            print(response.status_code)
            print(response.json())
        

    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue