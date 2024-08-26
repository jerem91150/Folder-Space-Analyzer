# Folder-Space-Analyzer
This project is a simple Python script that analyzes the disk space usage of a selected folder. It allows the user to choose a folder through a graphical interface and then calculates and displays the sizes of the subfolders in that folder. The results are printed to the console.

Features
Folder Selection: The user can select a folder to analyze using a graphical dialog box (via easygui).
Disk Space Analysis: The script recursively calculates the size of each subfolder within the selected folder.
Result Display: The results are printed in the terminal, showing the subfolder names and their respective sizes in gigabytes (GB).
Pause on Completion: After displaying the results, the program waits for the user to press Enter before closing, ensuring that the results can be viewed before the program terminates.
Prerequisites
Before running the script, make sure you have Python installed and the required dependencies:

Dependencies
Python 3.x
easygui (for the graphical folder selection dialog)
To install the required libraries, run:

bash
Copier le code
pip install easygui
How to Use
Running the Script
You can run the script directly using Python or as a standalone executable.

1. Running with Python
Clone or download this repository to your local machine.
Navigate to the directory where the script is located.
Run the script with Python:
bash
Copier le code
python analyse_dossier.py
2. Running as an Executable
If you have compiled the script into an executable (e.g., using PyInstaller), you can run the executable directly by double-clicking it in your file explorer. The program will launch and allow you to select a folder for analysis.

Steps:
Launch the program.
A dialog box will appear prompting you to select a folder.
Once a folder is selected, the program will analyze the space usage of each subfolder.
The results will be printed to the console.
The program will pause and wait for you to press "Enter" before closing.
Creating an Executable (Optional)
If you want to convert this script into an executable, you can use PyInstaller. Here's how:

Install PyInstaller if you haven't already:
bash
Copier le code
pip install pyinstaller
Generate the executable:
bash
Copier le code
pyinstaller --onefile analyse_dossier.py
The executable will be created in the dist/ folder. You can now run the program by double-clicking the executable file.
License
This project is open-source and available under the MIT License.
