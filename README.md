# Repomix GUI

A GUI wrapper that provides a user-friendly interface for [Repomix](https://github.com/yamadashy/repomix). This is only a GUI wrapper and you must have Repomix installed to use it.

This was a 45 minute AI assisted, quick and dirty project to make AI assisted coding easier. When using AI to code something, I will often feed a Repomix file of my codebase for analysis, feed back or to have the AI model make some changes. This makes it a little easier to accomplish.

![App Screenshot](screenshots/app_preview.png)

## 📥 Download (For Most Users)

**Just want to use the app?** 
- Go to [Releases](https://github.com/yourusername/repomix-gui/releases)
- Download `repomix-gui.exe` from the latest release
- Double-click to run (requires Node.js for Repomix)

## 🛠️ For Developers

### Run from Source

It is intended to to be used by running the .exe, but you can run the .py file directly if you prefer. Simply save the repomix_gui.py file to your PC, navigate to that folder and run the following command in the terminal.

```
python repomix_gui.py
```



### Build and Customize Your Own Executable

If you want to make changes to the program, edit the repomix_gui.py file and then make the executable by running.

```
pip install pyinstaller
pyinstaller --onefile --windowed repomix_gui.py
```



## Requirements

- Node.js and npm (for Repomix)
- Python 3.6+ (if running from source)

## License
This project is licensed under CC BY-NC-SA 4.0

