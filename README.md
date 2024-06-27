# FFXIV_Crafting_Shopping_List

# Project Overview

<b> /!\ I'm currently not working on this project and the api from Sandbag isn't up to date. This project also only work for A Realm Reborn to EndWalker crafts. /!\ </b>

This project is a Python application designed to generate a crafting list of required materials for crafting an item and to display the cost of each material on the market board. It uses several modules to handle item data, create shopping lists, and manage recipes.

## Directory Structure
````
FFXIV_Crafting_Shopping_List/
│
├── Data/
│   ├── items.json
│   └── recipes.json
│
├── Classes/
│   ├── Item.py
│   └── ShoppingList.py
│
├── Helpers/
│   ├── Recipes.py
│   └── Craft.py
│
├── Main.py
└── README.md
````

## Files and Their Purposes

<b>- Data/items.json:</b> Contains item data used for looking up item IDs and names.

<b>- Data/recipes.json:</b> Contains recipe data used for crafting calculations.

<b>- Classes/Item.py:</b> Defines the Item class, which represents an item and its details.

<b>- Classes/ShoppingList.py:</b> Defines the ShoppingList class, which handles the creation and management of shopping lists.

<b>- Helpers/Recipes.py:</b> Contains helper functions for managing recipes and crafting calculations.

<b>- Main.py:</b> The main entry point of the application that ties everything together.

## Set up Instructions

### Prerequisites 

    Python 3.x installed on your machine

    Internet connection (for API requests)

### 1. Clone the Repository

    git clone https://github.com/Yssnogood/FFXIV_Cratfing_Shopping_List

### 2. Install Required Librairies

    pip install requests

### 3. Run the Application 

    python main.py

The application isn't finish. You'll need to run the main inside a terminal or an idle.