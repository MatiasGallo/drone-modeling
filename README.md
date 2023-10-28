# VoloDrone Challenge

The new VoloDrone can be controlled remotely and is optimized for indoor use. It has several sensors and a
connection to the controller. When the drone boots, its sensors will receive the dimensions of the room as well as the
location of the room and sends you the 3D coordinates in centimeters. The drone is only millimeters in size and
doesn't take up notable space.

## Planning

1. Create constants
    - Commands   : to set valid set of commands
    - Dimensions : to set minimum values for a room/world

2. Create basic models
    - Coordinate: position for drone/obstacles
    - Drone     : main movable object of the simulation
    - Command   : order to move dron
    - World     : limits of the simulation

    - Test: Creation

3. Create drone moving
    - Drone
        - Create move method
            - Test: Moving drone
    - World
        - Calculate potential destination
            - Test: Create a destination, given a command create a destination for a drone
        - Calculate if destination is valid
            - Test: Given a destination for a drone, check if it's valid or not
        - Bonus: Correct course
            - Test: Given an invalid destination, correct course

4. Bonus: More output
    - Add the total distance flown to the output

5. Create user input
    - Simple input to assign commands

## Future Work

1. Create obstacles and out of service areas
    - Create abstract obstacle and different obstacles
        - Stop before colission
2. Create out of service(OOS) area
    - Dron should return if ending in one
3. Adapts OOS and World to implement polygons as shapes instead of rectangles/squares
4. Adapt Commands to use vectors. 
    Eg: move dron from (0,4,2) to (1,2,7) with vector (1,-2,5)