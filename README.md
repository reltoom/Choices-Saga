# Choices Saga

![Load screen of Choices Saga, after pressing Run Program](/readmeimages/screenonload.png)

Visit the deployed site here: [Choices Saga](https://choices-saga-20bfad436228.herokuapp.com/)

Choices Saga is a Python command line interface (CLI) application that runs the player through an adventure story. Before starting, the player answers a few questions which will make the story a touch more personal and even effect the outcome. Throughout Choices Saga, the player will need to make choices of what to do. Making a wrong choice will end your story while a right choice will drive the story forward. Before being able to complete chapter 1 the player will be challenged by a puzzle. Completing the puzzle will have a more favorable outcome then giving up on the puzzle.


## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Planning Process](#planning-process)
  * [Design](#design)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Future Implementations](#future-implementations)
* [Features](#features)
    * [The Home Page](#the-home-page)
    * [The Thank You Page](#the-thank-you-page)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Websites & Programs](#websites-programs)
* [Deployment](#deployment)
* [Testing](#testing)
   * [Validator Test](#validator-test)
   * [Bugs](#bugs)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgments](#acknowledgments)

- - -
## User Experience (UX)

### User Stories

#### Visitor Goals

* To play an interactive story game.
* Have an engaging experience, where your choices matter.
* Interesting story and something to challenge you.
* Easy to differentiate between story text, input text and error text.


#### Returning Visitor Goals

* Choosing a different story path 
* Seeing how different answers and choices effect what you do.

## Planning Process

For Choices Saga, I knew I wanted an adventure story with choices at certain points, a 'player' character with different values/items that could effect the story and atleast one puzzle for the user to solve.

* First, I created a player dictonary with some keys and blank values. To fill this in, I added an 'intro' function that asks several questions and fills in the player character by writing to the player dict.
* Second, I thought of a possible puzzle and created the code for it. I encapsulated it into one function so I could call it when needed. For the puzzle, I made sure I could solve it myself first and then worked on creating the code for it. I wanted this puzzle to be the 'high point or climax' of the story, something to challenge the user after making it through most of the story.
* Third, I came up with a basic story idea. Since this would be a whole lot of text, I decide to create a text file for the actual story and read it from my python file. Once I started writing the story, whenever I reached a possible 'choice' point, I would write keywords for the options but contine writing only 1 path until I reached the end of the story. 
* Forth, I went back to all of the 'empty' choice key words and filled in a new story arc, possibly creating new keywords/choices. I did this until there were no empty keywords/choices.
* Last, I created the functions(for each choice) in Python to read the story text(only certain lines) and then tied them together so that the right function would run after each user choice.

## Design

Visually there was not too much to design with Choices Saga as it is a command line application, although choosing different colors for the text was included, for better user expeirnce.

### Color Scheme

By importing the 'colorama' package, I was able to incorporate different colors for each type of text.
* <span style="color:green;">Green</span> was chosen for only the title 'CHOICES SAGA' so it would stand out more.
* <span style="color:yellow;">Yellow</span> is used as the story text. To understand what is happening with the story, one will have to read the yellow text. Yellow is also used in the puzzle and the spheres glow a warm light.
* <span style="color:white;">White</span> is used for all input choices the user will need to make. In order for a user to know what choices to make, read the white text.
* <span style="color:cyan;">Cyan</span> is used for all keywords that the user will need to type, creating an easy visual for the user to understand.
* <span style="color:red;">Red</span> is used for error messages. If the user types wrong input, a red message appears telling the user what they need to do to fix it. Red is also used in the puzzle to clearly show with 'spheres'(X), is not turned on.
* <span style="color:royalblue;">Blue</span> text is used to signify restarting of the game or restarting of the Intro section.
* <span style="color:magenta;">Magenta</span> was only used once and it is to clearly mark the user ending Choices Saga, exiting program.

Image showing most of the color choices:

  ![Choices Saga](readmeimages/colorchoices.png)

### Typography

I kept the original text style from the command line interface, as I like the retro look.

### Future Implementations

1. Add a moves counter to see how many 'turns' it takes to win.
2. Adding a timer to see how long it takes to win a game.
3. Different pictures for the 'cards' and even bigger game area.
4. Get kids to send in their own drawings for Kidz Memo art.

- - -

## Features

Kidz Memo has a 'home' page, 'easy mode' page and 'hard mode' page.

The whole site is responsive and works just as well on mobile phones as desktop screens.

* The word 'Memo'is writen in font-style and color scheme used for the site as the favicon.

  ![favicon](assets/readmeimages/faviconreadme.png)

* The Header section includes the title: 'Kidz Memo' as well as links to the game modes  and Sound On/Off button.
    ![Sound Button On](assets/readmeimages/soundon.png)
    ![Sound Button Off](assets/readmeimages/soundoff.png)

* The Main area holds the rules, descriptions of game modes and the game areas.

* When a player complete a game by matching all the pairs, a win message will pop up. This can be closed by clicking anywhere on the message.
![Win Message On The Completion Of A Game](assets/readmeimages/winmessage.png)

#### The Home Page

The home page of 'Kidz Memo' has the main header and then game rules and descriptions.
![Main Header](assets/readmeimages/header1.png)
![Home Page Image](assets/readmeimages/rules.png)
![Home Page Image](assets/readmeimages/gamemodes.png)


- - -

## Technologies 

### Languages 

Python was used in the making of Choices Saga

###  Websites & Programs 

* [Github](https://github.com/) - Created repository and stored files here after commits.
* [Microsoft Visual Studio](https://visualstudio.microsoft.com/) - Wrote code and did commits to Github from here.
* [W3 School](https://www.w3schools.com/) Read and used as a guide for some code.


- - -

## Deployment 

Kidz Memo is deployed from Heroku - [Choices Saga](https://choices-saga-20bfad436228.herokuapp.com/).

To Deploy the site from GitHub Pages:

1. Go to the repository for this project and choose 'Settings'
2. From left side selection, go to 'Pages'.
3. Under 'Build and Deployment' from Source - choose 'Deploy from a branch'.
4. Under 'Branch', choose 'Main' from the first dropdown menu.
5. From the second dropdown menu, with the image of a folder, choose 'root', then save.

![Deployment Steps](assets/readmeimages/deploy.png)

#### How to Fork

If you want to fork this repository:

1. Go to the repository for this project, [Kidz Memo](https://github.com/reltoom/Memo).
2. In the upper right hand area of the screen, click the 'Fork' button.
3. Then when the menu drops down, click 'Create New Fork'. (If you are the owner of a repository, you cannot fork.) 

#### How to Clone

If you want to clone this repository:

1. Go to the repository for this project [Kidz Memo](https://github.com/reltoom/Memo).
3. Click on the green 'Code' button and then select how you would like to clone: HTTPS, SSH or GitHub CLI (under the 'local' tab). 
4. Either copy the desired code or click to open with another program from the list below the code.
4. Open your code editor and go to 'Clone Repository' usually under 'File'.
5. Paste if your code and then 'Clone'.

- - -

## Testing

Kidz Memo has been tested on: Chrome, Microsoft Edge and Safari(Reset button does not cover full bottom of page).

With Dev Tools all standard screen sizes were tested to make sure the site looks good and is still readable. 

I had a couple of friends, my brothers, and my daughter test the game and check user error possiblities.

Links in the main menu take the user to correct game modes. Sound On/Off works correctly. Reset Button works correctly by reshuffling the whole game board.

Win message pops up on player completion of a game mode and can be closed.

## Validator Test

* HTML
    * Using the [W3C Validator](https://validator.w3.org/#validate_by_input), code was checked for each webpage of Kidz Memo to see if there were any errors. There were no errors.
    ![W3C HTML Test](assets/readmeimages/htmlvalidator.png)
* CSS
    * Using the [W3C Validator](https://jigsaw.w3.org/css-validator/) the code for CSS was checked for errors, there were none.
    ![W3C CSS Test](assets/readmeimages/cssvalidator.png)
* Javascript
    * Using the [JShint Validator](https://jshint.com/) we analyzed the Javascript code. There are no errors but 17 warnings, most of which are :'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
* Accessibility 
    * Using the Lighthouse dev tool from Chrome; accessibitly, performace, best practices and SEO were tested for each page.
    
![Validator Test Home Page](assets/readmeimages/lighthouse1.png)
![Validator Test Easy Mode](assets/readmeimages/lighthouse2.png)
![Validator Test Hard Mode](assets/readmeimages/lighthouse3.png)

### Bugs

Here are some, but not all, of the bugs that were fixed during development. 

| Bug | Fix |
| :--- | :--- |
| Boxes for the game areas not aligning properly | Commented out lines of CSS code and reapplied them one by one. |
| Sound Button not working | Googled javascript code for muting, read several sites and put it into code. Trial and error until it worked. |
| Not being able to close the pop up win message | Googled ways to close a modal pop up and tested several varients.
| Boxes not flipping when clicked | Doubled checked CSS and javascript function to make sure right elements were selected for flipping|

There was alot of back and forth with the writing of several lines of code, saving, running and re-writing. For some functions to work, all 3 elements had to be right, HTML, CSS and Javascript. Rereading course material and Googling that same material to better grasp the concepts was needed. 

There are no unsolved errors.

- - -

## Credits

### Code Used

Most of the code I wrote myself with a lot of trial and error, saving and viewing on web browser. 

For the structure of the functions for the game I followed [Paddy Walshes Project](https://github.com/paddyw11/Paddy-walsh-project-2b).

For the modal pop up I followed code from [W3School](https://www.w3schools.com/howto/howto_css_modals.asp).

Structure for the README file is from my project [Ways to Relax](https://github.com/reltoom/Project-1-Relax) adjusted to fit Kidz Memo.

### Media

Audio clip is from [Free Sound](https://freesound.org/).

Images for the Memo game are drawn by my daughter.

### Acknowledgments

Thank you to my daughter and wife for helping support me through my studies.

Thank you to the Swedish Slack channel for keeping my spirits high.

Thank you to my mentor from CI, Precious, for giving me advice and guidelines on the project.
