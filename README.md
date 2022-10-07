# ape-escape
A tool that will compile nfts into wallpapers for those who like ever changing wallpapers

First, download the images by heading into the PNGs folder and running "python3 apeget.py"
After that finishes, head back to the to the root directory. 
To generate a lot of backgrounds real quick, run "./init-monkeybone".
This script will automatically pass on 4 to the bgtool.py script and output backgrounds timestamped to "BGs/".
running the program manually like "python3 bgtool.py [columns] [optional argument for output png location]" will generate a single image using the images in the PNGs directory with an optional argument of where to outout it. Will default to "out.png".
