import json

def getId(name, data):
    """Give the id of an item from its name"""    
    for i in data.items():
        if i[1]["en"] == name:
            #print("Id of ", name, " : ", i[0])
            return i[0]

def getName(id, data):
    """Give the name of an id"""    
    for i in data.keys():
        if int(i) == id:
            #print("Name of ", id, " ID : ", data[i]["en"])
            return  data[i]["en"]

def createListRecipe(dataRecipes):
    """Create a list of ids and amounts needed for crafting an item"""
    listRecipe = []
    for x in range(3, 25):
        listRecipe.append(dataRecipes[str(x)])
    return listRecipe

def findRecipe(id, dataRecipes):
    """Find the corresponding recipe of an id given"""
    for i in range(3, len(dataRecipes)):
        #print(dataRecipes[i][str(3)])
        if id == int(dataRecipes[i][str(3)]):
            return createListRecipe(dataRecipes[i])
        
def listIdToName(listId, dataItems):
    """Change ids items to items names"""
    listName = []
    for x in range(0, len(listId)):
        if x%2 == 0 and listId[x] > 0:
            listName.append(getName(listId[x], dataItems))
        elif listId[x] >0 :
            listName.append(listId[x])
    return listName

def multipleCraft(listRecipe, howMany=1):
    """"""
    multipleCraftList = []
    for x in range(0, len(listRecipe)):
        if x%2 != 0:
            multipleCraftList.append(listRecipe[x]*howMany)
        else:
            multipleCraftList.append(listRecipe[x])
    return multipleCraftList

def recipeFromName(name, howMany=1):
    with open('Data/items.json', encoding='utf-8')as f:
        dataId= json.load(f)

    with open('Data/recipes.json', encoding='utf-8')as f:
        dataRecipes= json.load(f)
    id = int(getId(name, dataId))
    return multipleCraft(listIdToName(findRecipe(id, dataRecipes), dataId),howMany)

def recipeFromId(id, howMany=1):
    with open('items.json', encoding='utf-8')as f:
        dataId= json.load(f)
    with open('recipes.json', encoding='utf-8')as f:
        dataRecipes= json.load(f)
    return multipleCraft(listIdToName(findRecipe(id, dataRecipes), dataId),howMany)

def affichage(name, howMany=1):
    recipePrint=recipeFromName(name, howMany)
    print("Ingredient(s) for ", howMany, "craft(s) of : ", name)
    print("================================================================")
    for x in range(2,len(recipePrint),2):
        print(recipePrint[x], " : ", recipePrint[x+1] )
    print("================================================================")
    print("You'll get : ",recipePrint[1]," of ", recipePrint[0])

#print("\n")
#affichage("Grade 8 Tincture of Intelligence")
#print("\n")

