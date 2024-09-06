# Valorant Colorbot Version 2.0!
<div align = "center">
    <img src="https://github.com/user-attachments/assets/41c6624a-24a2-4f9d-b433-e7bf8f11ee23" alt="logo" width="130" height="130" style = "border-radius: 25;">
</div>

## Version 2 of my valorant colorbot (was originally detected by VGK after an anticheat update) Not really a serious cheat to be used competitively, more of an idea I am trying out, nevertheless, still should be fully undetected

How does it work?

1. Python library [Dxcam](https://pypi.org/project/dxcam-cpp/) captures an image of the screen
2. The program generates a similarity map between the image captured and the enemy outline color (in our case yellow)
3. A function is ran to find the topmost white pixel (which should be where the enemys head is) in the similarity map and save its coordinate
4. Subtract the last coordinate from the coordinate of the centre of your screen and you get a resultant vector from the centre of your screen to the enemys head
5. Multiply the vector, wich is in pixels by your Valorant sensitivity and you get the amount of pixels your mouse needs to move to lock to the players head

## Video Explanation

![GIFMaker_me](https://github.com/user-attachments/assets/5bbf509f-b2b8-4f6d-9455-db4846483bc3)

## How to install

The easiest way to see how this works is to watch the series, but here's the short version.

1. Download and unzip
2. Install [Python](https://www.python.org/downloads/) and dependencies
3. Modify `settings.py` to your liking
4. Run the `main.py file` and instructions

## Changes

Since this is more of an example project, I'd encourage you to clone and rename this project to use for your own puposes, it's a good starter boilerplate for creating your own valorant cheat.

## Find a bug?

If you found an issue or would like to submit an improvement to this project, please [Submit An Issue](https://github.com/Violevo/Valorant-Colorbot-V2/issues)

## Known issues (Work in progress)

The following bugs/features are yet to be fixed/implemented, but feel free to implement these yourself:

- Triggerbot
- RCS (recoil control system)
- Silentaim
- Flickbot / any other type of aimbots
- GUI
- Config Editor

---

<p align="center">Educational Purposes Only 📚</p>

![image](https://github.com/user-attachments/assets/84700e6f-c278-46f3-8a4d-9893ed09ede1)
![new](https://github.com/user-attachments/assets/e14c5e33-88c8-4230-8a0f-bbacf46fa2e2)
