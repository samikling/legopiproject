# 4WD Lego robot car for Raspberry pi
## Fun for the whole family!
<img src="https://am3pap005files.storage.live.com/y4mWrWAkmkPhn4-j_CdEtFtz0r9ohLT8_U5rEGFzYc_0gBAV_Ym-AXDvef5ceMDGRj5nZ0gD1I7yRIcYmjRCvIOPhTqX2oTm3I_U1-HOf4wozTFDhI656YvcwuMh0XAxEQdvStUymSHBTniAt3NZgmHCjJ_pEt4JmOnUZxzcrjO8xH3oJTybGhRx_OOPaJ--s-6?width=683&height=1024&cropmode=center" width="auto" height="auto" />

### Fun way the share your love for legos with your love for coding
This poject is a great way to spend some time with your kids while introducing to the world of coding and electronics.
In this project we will build a remotely controlled Car that your kids can decorate with legos. 

This project will require some parts as follows:
###### **Raspberry pi:** `A model 3b+ or 4 - You need to be able to have a wireless lan connection.`
###### **4WD Robot car kit:** `The one used in our project was Joy-it 4WD Kit, but there are lots of alternatives around.`
###### **A breadboard**
###### **4 5V DC Motors:** `These will be included in the kit, but you could buy them separately if you don't want to buy a ready kit.`
###### **2 * l293D Motor controller:** `For controlling the motors. One controller can be used to control two DC motors or one stepper motor.`
###### **USB Powerbank** `For powering the raspberry pi.`
###### **Battery enclosure:** `You need a battery enclosure for batteries. You can use 4 AA batteries or a single 9V battery.`
###### **Soldering iron:** `This project might need some soldering, but you could try to use some electrician tape or bluetack if you don't have a soldering iron.`
###### **Legos:** `These are for the design. Our kids went with a cute little appartment on top of our robot, but I can only imagine how many different designs you could come up with. Let your imagination go wild.`

## Getting started
If your kit is anything like the one that I had, witch was Joy-It 4WD Kit you'll need to start by soldering the wires to the motors. Or you could use some bluetack or tape.

<img src="https://am3pap005files.storage.live.com/y4mtIVdPsHltCHefTMK-ss5eo1OFBaleZZx1d21ZQ1Bb8tWTB0CU7gUoGSBdqBTNBs-SNpSfsG20lRyW-2Xe5k9gKkBeRG9l9_eREtK-iPKxA0f6mu09Ai7BRRlUBgSCJ13ZKF2TFK3L_UUe1n_iDgM9qGeuFVipVbcWmo8dDnddQMPpem8eJJ_5FoQItuT8Byb?width=660&height=440&cropmode=none" width="660" height="440" />


The next step will be following the instructions that came with your kit, and install the motors to the acrylic board.

<img src="https://am3pap005files.storage.live.com/y4m6xNXzSJxIIm2aKdakJQRt4bQ6HZT-0dj7HU0jcb47goVbRmBipY24vdvzWFpZzaEjODY6J07ahmk5Pbcr_awph9JU79DLBIu9yNzKcmFj6xibzLXwUr96g6pDbuJvFtQlJG1bVo3WCpYtZfbiCYdaapLwQTekh94Nq30dsQgRGIEQrVWk045v97N4oRmyXlG?width=660&height=440&cropmode=none" width="660" height="440" />

## The wiring
The next step will be the most tedious one, wiring the breadboard. You can ask your children to help with this if you have big fingers.

![](https://i.imgur.com/NTQniFk.png)
*Note!!! There is a wire missing from the diagram. There should be a wire going from the ground pin of Raspberry Pi to the ground rail on the breadboard (For example pin number 6,14 or 20.)*

Start by plucking in the l293D Motor drivers. There is a split between the breadboard. The pins of the l293D go on each side of the gap. You need to check the orientation of the chip, this is indicated by a circular gap on the other side of the chip. Put both chips on to the breadboard so that both chips are facing upwards.
The pin numbering starts from upper left pin 1-8 and on the right side from bottom right to upper right 9-16.
Next we are going to connect the Motors to the chips. Take the red wire of one of the motors and connect it to the third pin of the chip. Now take the black wire of your motor and connect it to the sixth pin of the chip. On the other side, connect anothr motors red wire to the pin number 11 and the black to the pin number 14. 

Next we will connect the positive wire from the battery pack to the pin number 8 on the chip. The last thing to do is to connect pins 12 and 13, connect them together and connect those with the negative side of the battery pack.

Repeat the connections for the two other motors and the other chip.

Take one jumperwire and connect the ground rail of the left side with the ground of the left side.

Now that we have the battery pack connected we move on to connecting the raspberry pi with the chips.

You can follow the diagram above, I tried to use different colors so that it would be easier to tell wich wire goes where.

* 5V Goes to the positive rail on the leftside of the breadboard.
* Ground pin from Raspberry pi goes to the ground rail on the left side of the breadboard.
* Take the 5V from the rail and connect it to the pin 16 on the chip.
* `GPIO 2 -> Pin 1`, `GPIO 3 -> Pin 2`, `GPIO 4 -> Pin 7` Left side of the first chip
* `GPIO 9 -> Pin 9`, `GPIO 10 -> Pin 10`, `GPIO 11 -> Pin 15` Right side of the first chip
* `GPIO 14 -> Pin 1`, `GPIO 15 -> Pin 2`, `GPIO 12 -> Pin 7` Left side of the second chip
* `GPIO 23 -> Pin 1`, `GPIO 24 -> Pin 2`, `GPIO 25 -> Pin 7` Right side of the second chip

<img src="https://am3pap005files.storage.live.com/y4mwE6bAu0DrQqcsl5d61rE3jKXMrWXVMsM8Vi56ruFbFdjXPtTx9vooIQDIapu5RNB1HS8jzIY7c1HzvMseez1e2uBBrmDCDZCCHA6hTkZjPLTj7ggiBW77U__m46WaD9eZeiw5aPoHtwIqVr2e_gBUpdV43EcPWisbfLTm5k7ekx1RWHbAtTFMGrb5iY-DmLW?width=660&height=440&cropmode=none" width="660" height="440" />

## Testing the code

Before assemblying everything we should now test our code out and see that everything is connected right and that every motor is running.
I'm assuming that you have your Raspberry pi allready set up and running Raspberry OS. If you haven't done this yet you can refer the official raspberry foundations webpage for instructions. You should enable SSH on your Pi so that you can remotely control it.

Plug in the usb-powerbank to the Raspberry Pi and let it turn on.

Clone or copy the python code [LegoPi.py](https://github.com/samikling/legopiproject/blob/main/LegoPi.py)

Insert batteries to the batter pack.
Now run the code.

While the code is running you can test the motors with your arrow keys. Up will be forwards, down backwards and so on. After pressing a key the motors will keep running indefinetly. You can stop all movement by pressing any other key on the keyboard. I like to use the spacebar to stop. To exit the program press "q". If you have capslock on it wont work.

If everything is working allrigh, you are ready to assemble the top of the kit on and let your children decorate your robot.