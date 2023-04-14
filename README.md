# Raspberry Pi Christmas Tree

This repository contains code for controlling a 3D RGB Christmas tree using a Raspberry Pi. The tree used in this project is available [here](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi).

## Installation

To use the code in this repository, you'll need to have a Raspberry Pi connected to the 3D RGB Christmas tree. You'll also need to install the RGBTree Python library, which provides a simple interface for controlling the lights on the tree. You can install the library by running the following command in your terminal:

`sudo pip install rgbtree`


Once you have the RGBTree library installed, you can download the code in this repository by running the following command in your terminal:

`git clone https://github.com/JelleWierenga/Raspberry-pi-christmas-tree.git`


## Usage

The repository contains several Python scripts for controlling the lights on the Christmas tree. Here's a brief overview of each script:

- `Blinking Lights.py`: Makes the lights on the tree blink on and off.
- `Fading Lights.py`: Gradually fades the lights on the tree in and out.
- `Random Lights 3-6.py`: Randomly changes the colors of 3 to 6 lights on the tree at a time.
- `Rainbow Lights.py`: Displays a rainbow pattern on the tree.
- `Rotate Lights.py`: Rotates a single light around the tree.
- `Wave Lights.py`: Creates a wave effect on the tree.

To run any of these scripts, navigate to the `Raspberry-pi-christmas-tree` directory in your terminal and run the script using Python. For example, to run the `Blinking Lights.py` script, you would run:

`python Blinking Lights.py`


## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.
