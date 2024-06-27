import requests
import json

from Classes.Item import Item
from Classes.ShoppingList import ShoppingList

from Helpers.Recipes import *



with open('Data/items.json', encoding='utf-8')as f:
    data= json.load(f)

print("###### Welcome to Alta's Shopping List ! ######")     
#itemName=str(input("Enter item's name :",))
itemName="Marble Alcove Bed" 
itemId = int(getId(itemName, data))

baseItem = Item(itemId, itemName)
baseShoppingList = ShoppingList(baseItem)
print("\n")
print("===== Recipe List from Local ========")
print("\n")

print(recipeFromName(itemName))



print("\n")
print("===== Recipe List from Sandbag ========")
print("\n")

baseShoppingList.printItemListWithoutCrystal()

print("\n")



#print("############################################################")
#shoppingList.setItemShoppingList()
#shoppingList.printItemListWithoutCrystal()
#print("\n")
#print("############################################################")
#print("#### Price of ", itemName, " on ",shoppingList.getItem()["home_server"], " ####" )
#print(shoppingList.printItemMarketPrice())

#print("#### Shopping List for ", itemName, " ended ! ####")