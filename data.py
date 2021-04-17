atm_data = {
    "value": 1000,
    "withdraw_value": 300,
    "pack1": (1000, 500, 500),
    "pack2": (2000, 600, 1400),
    "pack3": (3000, -500, None)
}

results = {
    "result": 700,
    "pin_length": 4
}

contributions = [
                     {
                        "startsOn":"2000-01-01",
                        "value":{
                           "currency":"GBP",
                           "amount": 100
                        },
                        "frequency":"Single",
                        "type":"LumpSum"
                     },
                     {
                        "startsOn":"2000-01-01",
                        "value":{
                           "currency": "GBP",
                           "amount": 200
                        },
                        "frequency":"Monthly",
                        "type":"Regular"
                     },
                     {
                        "startsOn":"2000-01-01",
                        "value":{
                           "currency":"GBP",
                           "amount": 300
                        },
                        "frequency":"Single",
                        "type":"Transfer"
                     }
                  ]