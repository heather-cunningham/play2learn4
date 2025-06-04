# Play2learn4
This last Play2Learn project was started with this GitHub template: django-vue-play2learn-template, 
created by my Webucator instructors, for the Final for the Full Stack Dev program at 
North Shore Community College in MA.

## Project Instructions
For this project, create the backend for the Play2Learn website with Django and Python. The website should allow users to log in to the site, play games, track their progress, see leaderboards, manage their account, and leave reviews. Administrators may run reports and manage users. Any visitor to the site may fill out a Contact-Us form or write a review. The reviews should rotate in a slideshow on the homepage. 

Add tracking history for both games, which stores the time the user finished the game, the game's name, 
game settings (e.g., operation: multiplication and max number: 20, or word-length: 5), and the 
final score for each game.  Also, add leaderboards for both games. These leaderboards should look similar to the game tracking, but they should display scores for all users.

## Tech stack for this Final
* Python - Written by me
* Django -  Written by me
* Postgresql - For the database
* -- See file: `./play2learn/fixtures/fixture_play2learn4.json` for the data dump.
* Node.js - Written by my instructors in the GitHub template
* Vue.js - Part of the GitHub template written by my instructors with bug fixes by me
* JavaScript - Some written by me, some from the template written by my instructors
* Bootstrap.js - For style, some written by me, some from the template written by my instructors
* HTML & CSS - Written by me
* Honcho - For process management to run the Python Django server and the Vue server at the same time
* Venv - For Python virtual environment, see requirements.txt for dependencies
* Npm - For Vue and Node, see package.json for dependencies   
    
## How to run this project?
1. Open a terminal or console at the project root.
2. Run `honcho start`.
3. Open a browser (a modern browser is best, e.g. Chrome, Edge, Firefox) and navigate to:
http://127.0.0.1:8000/

## How to run this project w/o Honcho?
1. Open a terminal or console at the project root and run `python manage.py runserver`.
2. Open a terminal or console at the root directory of the games: `vue-games` and run `npm run serve`.
3. Open a browser (a modern browser is best, e.g. Chrome, Edge, Firefox) and navigate to:
http://127.0.0.1:8000/
