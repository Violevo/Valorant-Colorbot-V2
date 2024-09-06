<div align = "center">
    <img src="https://github.com/user-attachments/assets/1aef7388-2c7f-45e2-b448-4717304d463c" alt="logo" width="130" height="130" style = "border-radius: 25;">
</div>



<h1 align="center">Valorant Colorbot V2</h1>

<p align="center">Version 2 of my valorant colourbot (was originally detected by VGK after an anticheat update) Not really a serious cheat to be used competitively, more of an idea i am trying out, nevertheless, still should be fully undetected</p>

<hr>
## Installation

## Code

### Screengrab
![image](https://github.com/user-attachments/assets/84700e6f-c278-46f3-8a4d-9893ed09ede1)

Uses python library "dxcam" to capture images of the screen, and saves it to file

### Color Filtering
![new](https://github.com/user-attachments/assets/e14c5e33-88c8-4230-8a0f-bbacf46fa2e2)

Generate a similarity map between the image and the select color (in our case yellow)

### Mouse move

subtract the position of the topmost white pixel in the similarity map (should be where the enemys head is) from the coordinate of the centre of the screen - (540 / 2, 540 / 2) (your crosshair), to give you a resultant vector from the centre of the screen to the enemys head. (in pixels)
Unfinished -

then, it is as simple as finding a way to move the mouse the same amount as the vector (multiplied by your valorant sensitivity) in pixels, without being picked up by the anticheat (this is harder than it looks)

</br>

```
Latest Version: 2.0
Release date: 4-Sept-2024
```

### Troubleshooting - [https://github.com/Violevo/Valorant-Colourbot-V2/issues](https://github.com/Violevo/Valorant-Colourbot-V2/issues)
### Homepage - [https://github.com/Violevo/Valorant-Colourbot-V2/](https://github.com/Violevo/Valorant-Colourbot-V2/)

---

<p align="center">Educational Purposes Only 📚</p>
