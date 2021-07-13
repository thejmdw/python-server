CUSTOMERS = [
    {
      "id": 1,
      "name": "Jimmy Baker",
      "address": "123 Anywhere",
      "email": "jimmy@baker.com"
    },
    {
      "id": 2,
      "name": "Fran Baker",
      "address": "321 Somewhere",
      "email": "fran@baker.com"
    },
    {
      "id": 3,
      "name": "Baker Jimmy",
      "address": "321 Anywhere",
      "email": "baker@jimmy.com"
    },
    {
      "id": 4,
      "name": "James Smith",
      "address": "423 Somewhere",
      "email": "james@smith.com"
    }
]

def get_all_customers():
    """gets a list of customers
    """
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """gets a single customer
    """
    # Variable to hold the found employee, if it exists
    requested_customer = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """creates a new customer
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
