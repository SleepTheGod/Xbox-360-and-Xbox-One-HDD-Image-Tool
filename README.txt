The first script, xbox_hard_drive_explorer.py, is a Python GUI application built using PyQt5 for exploring the contents of Xbox One and Xbox 360 hard drives. 
The script presents a graphical interface with a file tree view that allows users to navigate and view all files and directories on the Xbox hard drive. 
When a file is selected, the script displays its path and provides previews for supported image and video file formats.
 The application also includes a menu option to open the Xbox hard drive directory, enabling users to select the appropriate drive for exploration. 
It's designed to run both as a standalone GUI application and from the command line, offering flexibility for different usage scenarios. Additionally, the script's requirements are listed in the requirements.txt file, which includes PyQt5 as the only dependency for the graphical interface.
extract_files.py is a Python utility designed to extract files from Xbox One and Xbox 360 hard drives.
 It utilizes the standard library modules os and shutil to recursively traverse the source directory (representing the Xbox hard drive) and copy all files to a specified destination directory while preserving their metadata.
 The script is executed from the command line, where users provide the source directory containing Xbox hard drive files and the destination directory where extracted files will be copied. This utility simplifies the process of extracting files from Xbox hard drives, 
facilitating forensic analysis or data management tasks. Additionally, since the script relies solely on standard Python modules, there are no external dependencies to include in the requirements.txt file.





