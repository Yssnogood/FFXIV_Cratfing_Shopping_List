import requests

class Item:
    def __init__(self, itemID=17606, name="Axe of the Fiend", craft_amount=1, home_server="Moogle", hq=True, job=0):

        self.cristalData = [
                            "Wind Shard","Wind Crystal", "Wind Cluster",
                            "Fire Shard", "Fire Crystal", "Fire Cluster",
                            "Ice Shard","Ice Crystal","Ice Cluster", 
                            "Earth Shard", "Earth Crystal", "Earth Cluster",
                            "Lightning Shard","Lightning Crystal","Lightning Cluster",
                            "Water Shard","Water Crystal","Water Cluster",
                            ]

        self.details = {
          "home_server": home_server,
          "shopping_list": [
            {
              "itemID": itemID,
              "name": name,
              "craft_amount": craft_amount,
              "hq": hq,
              "job": job
            }
          ],
          "region_wide": True
        }

        self.itemMarketPrice = requests.get("https://universalis.app/api/v2/" + str(self.details["home_server"]) + "/" + str(self.details["shopping_list"][0]["itemID"]))