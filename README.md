# PROM_keypad

During our first year at the University of York, we were put into groups of three and assigned the challenge of designing, and implementing, a Raspberry Pi based system to control the locking and unlocking of a digital lock.

Our implementation involved the use of a keypad to allow the user to input a password, our system also displays to the user whether or not the inputed password was correct through the blinking of an LED (Red for incorrect, Green for correct).

(Not only this, but after finding extra time after implementing the basic system we also added a sound system that played a series of predefined short songs once the user gained access to the lock).

We also included software designed to autoamtically "lock-pick" our design by generating electrical signals mimicking key presses.

Additionally, we were posed the challenge of not using any interrupt based techniques to detect key presses, so our implementation polls input channels to discover which keys were pressed by the user.

Find below a video demonstrating a test of our system, which displays most of the features of the final implementation.
[![Video demonstrating implementation](http://img.youtube.com/vi/nL3srjRjIdc/0.jpg)](http://www.youtube.com/watch?v=nL3srjRjIdc)

Below we have provided an image of the final, neater, hardware configuration of the system.
![Cleaner wiring in final implementation](/clean_wiring.jpg)

Following completion of the project, we were approached by a university lecturer (Mike Freeman) to display our system on open days at the University.
