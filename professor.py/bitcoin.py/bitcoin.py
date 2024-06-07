import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a valid number")
        sys.exit(1)
else:
    print("Missing or incorrect command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r.raise_for_status()  # Check if the request was successful
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_value = bitcoin * value
    print(f"${total_value:,.4f}")
except requests.RequestException as e:
    print(f"RequestException: {e}")
    sys.exit(1)
