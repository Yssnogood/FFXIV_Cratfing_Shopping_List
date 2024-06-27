#Time To Code

def howMuchMatForACraft():
    '''
    Define all the Mats require for one craft
    '''
    mats=["A","B","C","D","E","F"]
    print("How many mats ?")
    craft ={mats[x] : 0 for x in range(0,int(input()))}
    for i, v in craft.items():
        print ("How much "+ str(i) + " is needed ? ")
        craft[i] = int(input())

    print("How much mats crafted are needed ?")
    howMuchMatsCrafted = int(input())
    if howMuchMatsCrafted != 0: 
        matsCrafted=[]
        for i in range(0, howMuchMatsCrafted):
            print("Wich mats is crafted ? And how many mats are needed ? ")
            matCrafted=[input(),int(input())]
            matHowMany=[]
            for j in range(0, matCrafted[1]):
                print("Mat needed for " + str(matCrafted[0]) + mats[j])
                matHowMany=[str(matCrafted[0])+ str(mats[j]), int(input())]
                craft[matHowMany[0]] = matHowMany[1]
    print(craft)
    return craft

def howManyCraft(craft):
    print("How many craft do you want ?")
    manyCraft=int(input())
    for cle, valeur in craft.items():
        print("Mats : ", cle, " | Needed : ", valeur*manyCraft)


#howManyCraft(howMuchMatForACraft())
    
