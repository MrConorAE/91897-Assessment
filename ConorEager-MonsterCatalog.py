# MONSTER CATALOG for Python
# Copyright (c) Conor Eager, 2021. All rights reserved.
# Developed as a submission for AS91897: Use advanced programming techniques to develop a computer program

# IMPORTS
# Import EasyGUI for creating a graphical interface
import easygui as eg

# DATA STRUCTURES
class Monster:
    """This class represents a monster card - it contains all the fields required for a monster (name, strength, speed, stealth and cunning).
    """
    def __init__(self, nme, str, spe, ste, cun):
        """Initialise a new Monster.

        Args:
            nme (String): Name of the monster.
            str (Integer): Strength of the monster.
            spe (Integer): Speed of the monster.
            ste (Integer): Stealth of the monster.
            cun (Integer): Cunning of the monster.
        """
        self.name = nme
        self.strength = str
        self.speed = spe
        self.stealth = ste
        self.cunning = cun
        
# This is the list in which Monster objects are stored.
monsters = []

# MAIN MENU
# This loop is the main menu of the program, which allows the user to select what they want to do.
while True:
    # Define the list of choices. This is a dictionary of format "button text": "internal name".
    choices = {"Add Monster": "add", "Edit Monster": "edit", "Delete Monster": "delete", "View All Monsters": "view", "Help & About": "help", "Quit": "quit"}
    choice = choices[eg.buttonbox("Welcome to Monster Manager. Select an option to get started!", "Main Menu - Monster Manager", list(choices.keys()))]
    if (choice == "add"):
        # Add a monster.
        pass
    elif (choice == "edit"):
        # Edit a monster.
        pass
    elif (choice == "delete"):
        # Delete a monster.
        pass
    elif (choice == "view"):
        # View all monsters.
        pass
    elif (choice == "help"):
        # View help.
        pass
    elif (choice == "quit"):
        # Quit the program.
        pass
    