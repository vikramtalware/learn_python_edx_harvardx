import requests
import sys
import json

def main():
    n = float(sys.argv[1])
    print(get_bitcoin_price(n))


def get_bitcoin_price(bitcoins):
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            result = response.json()
            price = result["bpi"]["USD"]["rate_float"] * bitcoins
            print(f"${price:,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
        except requests.RequestException:
            sys.exit("System Error")

main()
