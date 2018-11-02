# PROM_keypad

![Cleaner wiring in final implementation](/clean_wiring.jpg)

During our first year at the University of York, we were put into groups of three and assigned the challenge of designing, and implementing, a Raspberry Pi based system to control the locking and unlocking of a digital lock.
We were told that, users should be able to interface with the system through a membrane matrix keypad. However, we were posed the challenge of not using any interrupt based techniques to detect key presses, so our implementation polled the pi's input pins to discover which keys were pressed by the user.

In our solution, the user initially entered a 4-digit passcode to gain access to the system. We also included an LED to indicate whether or not the entered passcode was correct (Red for incorrect, Green for correct). As well as this, when the system detected an incorrect guess, a delay would initiate preventing the user from entering another passcode for another few seconds (to prevent brute force attacks).

Once the user had gained access to the system, they were presented with a text based user interface through which they could lock/unlock the lock and adjust a few settings of the system. (Also, having found extra time after implementing the basic system we also added a sound system, consisting of a single piezoelectric buzzer, that played a series of predefined short songs once the user gained access to the lock. The songs include: The Star Wars theme song, Careless Whisper by George Micheals, The Super Mario Bros theme song and The Super Mario Bros 2 theme song).

We also included software designed to automatically "lock-pick" our own design by generating electrical signals mimicking key presses.

Find below a video demonstrating a test of our system, which displays most of the features of the final implementation (note that the wiring of the system had not yet been tidied up yet).
[![Video demonstrating implementation](http://img.youtube.com/vi/nL3srjRjIdc/0.jpg)](http://www.youtube.com/watch?v=nL3srjRjIdc)

Following completion of the project, we were approached by a university lecturer (Mike Freeman) to display our system on open days at the university.
