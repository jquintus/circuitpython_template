# Circuit Python Projects
Template repository for quickly creating new circuit python projects with stubs for 

* The readme.md
* The .gitignore
* boot.py (including instruction on changing the name of the board)

# Hardware and Software dependencies

* [CircuitPython](https://circuitpython.org/)

# Installing CircuitPython

1. [Install instructions from Adafruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
2. [Download CircuitPython for your board](https://circuitpython.org/)
3. Download the .uf2 file from the sie above
4. Plug the board in to your USB drive
5. Wait a second or two for it to fully boot (likely the LED will be changing colors)
6. Hold the `Boot Select` button on the end of the board down while you press and release the `Reset` button by the LED
7. The board will restart quickly
8. You will see a new drive on your computer named something like `RPI-RP2` (Names may differ depending on the board you're using)
9. Copy the .uf2 file to that drive
10. The device will reboot one more time and you will see another new drive on your computer named `CIRCUITPY`
11. Done.

# Cloning this repo directly to your board

By default, git wants to clone repositories to folders, 
so cloning directly to the root of a filesystem requires a few extra steps.

```batch
cd d:\
git init
git remote add origin https://github.com/jquintus/<repo_name>
git pull origin main
git branch --set-upstream-to=origin/main main
```

# Update the Circuit Python Bundles

1. Go to the [CircuitPython](https://circuitpython.org/libraries) Website
2. Download the latest bundle for 9.x
3. Unzip the file
4. Select the libs you need and drop them into the `CIRCUITPY/lib` folder

# Useful Tutorials and Documentation

* [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview)
