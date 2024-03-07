import requests

def get_amount(address):
    url = 'https://hibxjljwpk.execute-api.us-east-1.amazonaws.com/serverless_lambda_stage/proof'
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://www.enjoy.tech',
        'referer': 'https://www.enjoy.tech/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    data = {
        "address": address,
        "uuid": "f16b6742-4383-49a1-9eaa-8ec5ff89d94e"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = response.json()
        return json_response.get('amount', 'Amount not found')
    else:
        return 'Error: {}'.format(response.status_code)

def main():
    # Load addresses from wallets.txt
    with open('wallets.txt', 'r') as file:
        addresses = file.read().splitlines()

    # Iterate over addresses and print results
    for address in addresses:
        result = get_amount(address)
        print(f"{address} {result}")

if __name__ == "__main__":
    main()
