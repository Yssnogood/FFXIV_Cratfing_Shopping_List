import requests

class ShoppingList():


    def __init__(self,item) -> None:
        self.item = item
        self.itemShoppingListRequest = requests.post("http://api.saddlebagexchange.com/api/v2/shoppinglist", json=self.item.details)
        self.itemShoppingList = self.itemShoppingListRequest.json()["data"]
        self.itemShoppingListTotalCost = self.itemShoppingListRequest.json()["total_cost"]
        self.itemShoppingListAverageCost = self.itemShoppingListRequest.json()["average_cost_per_craft"]

    def printItemListWithoutCrystal(self):
        self.itemWithout = [{"total_cost":0}]
        for i in self.itemShoppingList:
            if i['name'] not in self.item.cristalData:
                self.itemWithout.append(i)
                self.itemWithout[0]["total_cost"] += i['pricePerUnit']*i['quantity']
                print(i)
        print("Total cost : ",self.itemWithout[0]["total_cost"], "For : ", self.item.details["shopping_list"][0]["craft_amount"]," ",self.item.details["shopping_list"][0]["name"], " crafted")

    def printItemList(self):
        for i in self.itemShoppingList:
            print(i)
     ##Getter and Setter##
            
    def printItemMarketPrice(self):
        itemMarketPrices = self.itemMarketPrice.json()["listings"]
        if len(itemMarketPrices) <6:            
            for i in itemMarketPrices :
                print("Price per Unit : ",i["pricePerUnit"], " Quantity : ", i["quantity"], "Hq :", i["hq"], " Total Price : ", i["total"])
        else:
            j=0
            for i in itemMarketPrices:
                if j<6:
                    j+=1
                    print("Price per Unit : ",i["pricePerUnit"], " Quantity : ", i["quantity"], "Hq :", i["hq"], " Total Price : ", i["total"])
                else : break
