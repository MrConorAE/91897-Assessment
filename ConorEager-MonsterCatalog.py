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

    def __init__(self, nme: str, str: int, spe: int, ste: int, cun: int):
        """Initialise a new Monster.

        Args:
            nme (String): Name of the monster.
            str (Integer): Strength of the monster.
            spe (Integer): Speed of the monster.
            ste (Integer): Stealth of the monster.
            cun (Integer): Cunning of the monster.
        """
        # Error checking for monster fields.
        # Blank name check:
        if (nme.strip() == ""):
            raise ValueError("Monsters must have names.")
        else:
            self.name = nme

        # Integer check:
        try:
            str = int(str)
            spe = int(spe)
            ste = int(ste)
            cun = int(cun)
        except ValueError:
            raise ValueError("Monster statistics must be non-blank numbers.")

        # Range checks:
        if (str > 25 or str < 0):
            raise ValueError(
                "Monster statistics must be between 0 and 20.")
        else:
            self.strength = str
        if (spe > 25 or spe < 0):
            raise ValueError(
                "Monster statistics must be between 0 and 20.")
        else:
            self.speed = spe
        if (ste > 25 or ste < 0):
            raise ValueError(
                "Monster statistics must be between 0 and 20.")
        else:
            self.stealth = ste
        if (cun > 25 or cun < 0):
            raise ValueError(
                "Monster statistics must be between 0 and 20.")
        else:
            self.cunning = cun


# This is the list in which Monster objects are stored.
#   Monster(Name,           Str,Spd,Ste,Cun)
monsters = [
    Monster("Stoneling",    7,  1,  25, 15),
    Monster("Vexscream",    1,  6,  21, 19),
    Monster("Dawnmirage",   5,  15, 18, 22),
    Monster("Blazegolem",   15, 20, 23, 6),
    Monster("Websnake",     7,  15, 10, 5),
    Monster("Moldvine",     21, 18, 14, 5),
    Monster("Vortexwing",   19, 13, 19, 2),
    Monster("Rotthing",     16, 7,  4,  12),
    Monster("Froststep",    14, 14, 17, 4),
    Monster("Wispghoul",    17, 19, 3,  2)
]


def displayMonster(monster: Monster) -> str:
    message = f"Monster '{monster.name}':\nStrength:\t{monster.strength}\nSpeed:\t{monster.speed}\nStealth:\t{monster.stealth}\nCunning:\t{monster.cunning}"
    return message

def createMonster() -> Monster:
    """Create a new Monster. Allows the user to enter all the necessary data, and handles errors.

    Returns:
        Monster: The created monster.
    """
    fields = ["Monster Name:", "Strength:", "Speed:", "Stealth:", "Cunning:"]
    data = ["", "", "", ""]
    while True:
        data = eg.multenterbox("Please enter the data for your new monster and press OK to save, or press Cancel to abort.",
                               "New Monster - Monster Catalog", fields, data)
        if (data == None):
            # Cancel was pressed, so abort without saving.
            return None
        else:
            try:
                newmonster = Monster(
                    data[0], data[1], data[2], data[3], data[4])
                break
            except ValueError as error:
                eg.msgbox(f"Error: {error}",
                          "New Monster - Monster Catalog", "Try again")
    return newmonster


def chooseMonster(source: list, action: str) -> int:
    """This function allows the user to select a monster to do something with.

    Args:
        source (list): The list from which a monster should be selected. Must contain Monster objects.
        action (str): The action to be performed to the monster, to help the user (e.g. "delete", "edit")

    Returns:
        int: The index of the monster chosen in the source.
    """
    if (len(source) == 0):
        # If there are no items to display, notify and exit.
        eg.msgbox(f"There are no monsters to {action}.\nTry adding one by clicking 'Add Monster' on the main menu.",
                  "Select Monster - Monster Catalog", "Back to Menu")
        return None
    else:
        # Otherwise, get a list of names to display.
        # In this case, I'm using a list comprehension to get the names of all the monsters.
        names = [i.name for i in source]
        # Display the list
        choice = eg.choicebox(f"Please select a monster to {action} and press OK, or press Cancel to abort.",
                              "Select Monster - Monster Catalog", names)
        if (choice == None):
            # They pressed Cancel, so abort.
            return None
        else:
            # They chose an item, so return it's index.
            return names.index(choice)


def deleteMonster(source: list, index: int) -> list:
    """This function allows the user to delete a monster from a list.

    Args:
        source (list): The source list to delete the monster from.
        index (int): The index of the monster to delete.

    Returns:
        list: A copy of the source list with the monster removed (if deleted), or an identical copy of the source list (if not deleted).
    """
    monster = source[index]
    yes = f"Yes, permanently delete {monster.name}."
    no = f"No, do not delete {monster.name}."
    confirmation = eg.buttonbox(f"Are you sure you want to permanently delete {monster.name}?\nThis cannot be undone!",
                                "Delete Monster - Monster Catalog", [yes, no])
    if (confirmation == yes):
        source.pop(index)
        eg.msgbox(f"The monster {monster.name} was deleted successfully.",
                  "Delete Monster - Monster Catalog", "Back to List")
    else:
        eg.msgbox(f"The monster {monster.name} was not deleted.",
                  "Delete Monster - Monster Catalog", "Back to List")
    return source


# MAIN MENU
# This loop is the main menu of the program, which allows the user to select what they want to do.
while True:
    # Define the list of choices. This is a dictionary of format "button text": "internal name".
    choices = {"Add Monster": "add", "Edit Monster": "edit", "Delete Monster": "delete",
               "View All Monsters": "view", "Help & About": "help", "Quit": "quit"}
    # Get the user's choice.
    choice = choices[eg.buttonbox("Welcome to Monster Manager. Select an option to get started!",
                                  "Main Menu - Monster Manager", list(choices.keys()))]
    if (choice == "add"):
        # Add a monster.
        result = createMonster()
        if (result == None):
            # Do nothing, it was cancelled.
            pass
        else:
            # Otherwise, save the result to the Monsters array.
            monsters.append(result)
    elif (choice == "edit"):
        # Edit a monster.
        pass
    elif (choice == "delete"):
        # Delete a monster.
        choice = chooseMonster(monsters, "delete")
        if (choice == None):
            # Do nothing, it was cancelled.
            pass
        else:
            # Otherwise, save the new list to the Monsters array.
            monsters = deleteMonster(monsters, choice)
    elif (choice == "view"):
        # View all monsters.
        pass
    elif (choice == "help"):
        # View help.
        pass
    elif (choice == "quit"):
        # Quit the program.
        pass
