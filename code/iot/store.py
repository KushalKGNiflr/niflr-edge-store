global STORE_STATUS

# Store Modes

CUSTOMER_MODE = 'CUSTOMER_MODE'
REFILLMENT_MODE = 'REFILLMENT_MODE'
MAINTENANCE_MODE = 'MAINTENANCE_MODE'

DEFAULT_STORE_STATUS = MAINTENANCE_MODE


VALID_STATUS = [
    CUSTOMER_MODE,
    REFILLMENT_MODE,
    MAINTENANCE_MODE
]


def get_store_status():
    global STORE_STATUS
    return STORE_STATUS


def update_store_status(status):
    global STORE_STATUS
    if status not in VALID_STATUS:
        return False
    else:
        STORE_STATUS = status
        return True

# Weight Change Types

PICK = "PICKED"
PLACE = "PLACED"

# Ticket Status

REVIEW_PENDING = "TO_BE_REVIEWED"

# USER SESSION TYPE

ENTRY = "ENTRY_AUTHENTICATED"
EXIT = "EXIT_AUTHENTICATED"