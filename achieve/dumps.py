""""
Boilerplate project by Andrew Li
Description: 
"""
import json


def main():

    text = {

        'title': "\r\n    |||||     |||||    |||||   ||     |||\r\n    ||  ||   |     |  |     |  ||||  ||||\r\n    ||   ||  |     |  |     |  || |||| ||\r\n    ||   ||  |     |  |     |  ||  ||  ||\r\n    ||  ||   |     |  |     |  ||      ||\r\n    |||||     |||||    |||||   ||      ||\r\n\r\n\r\n             |||||     ||||\r\n            |     |   |   ||\r\n            |     |   | |||\r\n            |     |   |||\r\n            |     |   | ||\r\n             |||||    |  ||\r\n\r\n\r\n|||||  ||      |||||    |||||   ||     |||\r\n||  || ||     |     |  |     |  ||||  ||||\r\n|||||  ||     |     |  |     |  || |||| ||\r\n||  || ||     |     |  |     |  ||  ||  ||\r\n||  || ||     |     |  |     |  ||      ||\r\n|||||  ||||||  |||||    |||||   ||      ||\r\n",

        'help': "\r\n    To start this game, enter \"new game\", \"new\", or \"n\".\r\n    If you have previously played this game,\r\n    you should see load game that can be activated if \r\n    \"load game\", \"load\", or \"l\" is entered.\r\n\r\n    WARNING: if you start a new game, the saved game will be overwritten!\r\n\r\n    If you want to report a bug, go to the following url:\r\n    https:\/\/github.com\/Zeyu-Li\/text_game\/issues\r\n\r\n    Suggestions will also be accepted and feel free to fork this project\r\n    ** remember this is licensed with the MIT license\r\n\r\n    To continue, press the enter key\r\n\r\n",
        
    'about': "\r\n    This is a text-based Python game made for a class project.\r\n\r\n    If you wish to modify it, please read license,\r\n    other than that, please enjoy the game ;)\r\n\r\n    To continue, press the enter key\r\n\r\n",

    'Ev1': "\r\n    2019: You fall into a nuclear dump site\r\n\r\n    Yearning for sunlight to photosynthesize,\r\n    you venture with your newly mutated roots\r\n    in hopes of reaching fresh air and sunlight\r\n\r\n    As you wonder around on your studded roots,\r\n    you find a small hole\r\n\r\n    With limited time on your non-exist hands, what do you do?\r\n",

    'Ev2': "You climb out of the hole and observe a few groundhogs but something doesn't seem right.\r\nUpon closer inspection, you see most of the groundhogs as deformed!\r\n\r\nHowever, you seem to have gotten too close, so the groundhogs are rush towards you.\r\nYou hope to dodge them",


    }

    with open('text.json', 'w') as f:
        json.dump(text, f)
    return 0

# system calls main
if __name__ == "__main__":
    main()