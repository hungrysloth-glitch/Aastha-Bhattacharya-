# Sharky Dodger
Sharky Dodger is a simple 2D obstacle-dodging game made with Python and Pygame. Play as Blobby and dodge the incoming Sharkys for as long as possible!

The game features custom-made sprites and backgrounds, a portrait-style game window, keyboard controls, randomly spawning obstacles, collision detection, and a survival-time counter displayed after the game ends.

## How to Play
* Press **SPACE** to start the game.
* Use **W A S D** to move Blobby.
* Dodge the Sharkys falling from the top of the screen.
* Survive for as long as possible.
* If you collide with a Sharky, the game ends.
* Your survival time is displayed on the Game Over screen.
* Press **SPACE** to restart.
* Press **X** to quit.

## Tools Used

* **Python** - Programming language
* **Pygame** - Game development, graphics, input handling, collision detection and timing
* **Visual Studio Code** - Code editor and development environment

## How to Run

### 1. Install Python
Make sure Python is installed on your computer.

### 2. Install Pygame
Open a terminal in the project folder and run:

```bash
pip install pygame
```

### 3. Clone the repository
```bash
git clone https://github.com/hungrysloth-glitch/Aastha-Bhattacharya-.git
```
Then open the project folder in VS Code.

### 4. Check the image paths
The game uses custom image assets, so make sure `blobby.PNG`, `sharky.png`, and `background.PNG` are included in the project folder.

### 5. Run the game
From the project folder:

```bash
python main.py
```

## Current Features

* Custom Blobby player sprite
* Custom Sharky obstacle sprites
* Custom background
* WASD movement
* Portrait game window
* Random Sharky spawning
* Increasing obstacle challenge through fast obstacle movement
* Collision detection with adjusted hitboxes
* Start menu
* Game Over menu
* Restart functionality
* Quit functionality
* Survival-time tracking
