import json
import requests

# Example: Fetch from an API or modify existing list
def update_token_list():
    # For this example, let’s assume we fetch from the HydraChain API
    api_url = "https://skynet.hydrachain.org/api/v2/tokens?type=ERC-20%2CERC-721%2CERC-1155"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        tokens = response.json()
        # Convert to the desired format
        token_list = [
            {
                "address": token["address"].lower(),
                "symbol": token["symbol"],
                "decimals": token.get("decimals", 18)
            } for token in tokens
        ]
    except Exception as e:
        print(f"Error fetching tokens: {e}")
        # Fallback: Load existing file and modify it
        with open("Hydra-Token-list.json", "r") as f:
            token_list = json.load(f)
        # Example modification: Add a dummy token
        token_list.append({"address": "0xdeadbeef", "symbol": "DUMMY", "decimals": 18})

    # Write updated list back to tokens.json
    with open("Hydra-Token-list.json", "w") as f:
        json.dump(token_list, f, indent=2)

if __name__ == "__main__":
    update_token_list()
