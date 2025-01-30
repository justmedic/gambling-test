from tronpy import Tron
from tronpy.providers import HTTPProvider


class TronClient:
    def __init__(self):
        self.client = Tron(HTTPProvider(endpoint_uri="https://api.trongrid.io"))

    def get_account_info(self, address: str):
        try:
            account = self.client.get_account(address)
            account_resource = self.client.get_account_resource(address)

            return {
                "balance": self.client.from_sun(account["balance"]),
                "bandwidth": account_resource.get("free_net_limit", 0)
                - account_resource.get("free_net_used", 0),
                "energy": account_resource.get("energy_limit", 0)
                - account_resource.get("energy_used", 0),
            }
        except Exception as e:
            raise ValueError(f"Error fetching data: {str(e)}")
