
# Crowd Control with YouTube Chat in Minecraft
### Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Additional Documentation](#additional-documentation)
- [License](#license)
- [Issues and Improvements](#issues-and-improvements)
- [Known Bugs](#known-bugs)
- [Contribution](#contribution)

## Overview
**Crowd Control** is a Python script that integrates live chat commands from YouTube with Minecraft gameplay. Viewers can control the player's actions in Minecraft through messages sent in the YouTube live chat. Commands such as `!screenshot` and `!move` trigger actions like taking screenshots or moving the character within Minecraft.

This project requires the `pytchat`, `pyautogui`, and `minescript` libraries, allowing real-time interaction between the YouTube chat and Minecraft's game environment.

## Features
- **Real-time YouTube Chat Integration**: Viewers' chat messages directly influence Minecraft gameplay.
- **Customizable Command Mapping**: You can easily modify commands to fit different actions.
- **Echo Feedback**: The script provides real-time feedback in the Minecraft chat to let players know when a command has been executed.

## Installation Guide
Before you begin, ensure you have the following installed:
- **Python 3.7** or higher.
- Libraries:
  - `pyautogui`
  - `pytchat`
  - `minescript`

1. Install missing libraries using `pip`:

`pip install puautogui pytchat minescript`

2. Replace the default **YouTube video ID** in the script with your live stream video ID:

`video_id = "your_video_id_here"`

- **Note**: Your video ID is found in the URL: youtube.com/live/**WRb7TC2k1cQ**

3. Download and install [Minescript](https://modrinth.com/mod/minescript) in your Minecraft modpack.

## Usage
1. Ensure your Minecraft has the Minescript mod installed and has at least run once to generate the mod folders.

2. Download and place the `control.py` script in the newly generated **minescript** folder.

3. Start Minecraft, open the chat window, and type the following command to run the script: `\control`

4. It should then say **"Starting Crowd Control..."** and you'll be able to start seeing YouTube live chat messages in Minecraft.

## Additional Documentation
**Libraries Used:**
- pyautogui: https://pyautogui.readthedocs.io/en/latest/#
- pytchat: https://github.com/taizan-hokuto/pytchat
- minescript: https://minescript.net/docs/

**Watch me code it live!**
If you'd like to see how I developed this, check out my [live coding session](https://www.youtube.com/watch?v=WRb7TC2k1cQ&t=1s).

## License
This project is licensed under the Creative Commons Attribution 4.0 International License.

**You are free to:**
- Share — copy and redistribute the material in any medium or format.
- Adapt — remix, transform, and build upon the material.

**Under the following terms:**
- Attribution — You must give appropriate credit and indicate if changes were made.

See the LICENSE file for more details.

## Issues and Improvements
If you encounter any issues or have suggestions for improvements, please feel free to submit an issue using the **issues tab** above.

To see a list of planned improvements and future updates, please review the **Roadmap**.

## Known Bugs
- `!drop-all` command sometimes has hiccups and skips some items. Only reliable when standing still.
- `!scramble` command sometimes stutters when scrambling.
- Sometimes, when closing a world, it gets stuck on 'Saving World" screen
- Sometimes, all entities and blocks are non-interactive and non-responsive. Not sure if it's the code or my computer causing it. It happened during stream several times and did not crash OBS. A simple restart of Minecraft happened to fixed the issue but still randomly occured

## Contribution
Thank you for visiting this repository! Contributions are optional but always appreciated.  You can help by:
- Reporting bugs or issues
- Suggesting features or improvements
- Submitting pull requests
- Star the repository to show your support

Donations are also welcome to support the project. 

**Support Options:**
- Send a donation via [Cash App](https://cash.app/$MisterZen01)
- Become a YouTube Member starting @ $0.99/mo
- Donate through YouTube Super Chat

Your involvement means a lot—thank you!

### Thank you for using Control.py!
