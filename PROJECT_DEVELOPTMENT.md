# 9CT Task 1 - Mechatronics
### By Fraser Maple

## Requirements outline

### Purpose

I need to design a program for the EV3 MINDSTORM robot that will allow it to collect red and yellow LEGO blocks and bring them to a designated area, while avoiding all other LEGO blocks. I must use at least two sensors in my design for navigation and object detection.

### Key actions

- Use colour sensor to detect edges of the map to ensure it does not leave.
- Use ultrasonic sensor to detect obstacles.
- Avoid obstacles if they aren't the correct colour.
- Move the correct blocks to the designated area.

### Functional requirements
- Edge of map detection - The colour sensor points down to detect the edge of the map. When the edge of the map is detected, the robot will stop moving, rotate, and begin moving again.
- Obstacle detection - The ultrasonic sensor is used to detect when an obstacle is within 5 cm of the robot. When an obstacle is nearby, a motor will rotate the colour sensor to determite the colour of the block.
- Obstacle evasion - If the colour of the block is bad, the robot will rotate and then continue to move forward.
- Block transportation - If the colour of the block is good, it will be collected and taken to the designated area.

### Use cases

1. Edge of map detection
- Scenario: The robot is moving forward and the robot reaches the edge of the map.
- Inputs: The colour sensor detects the black border of the map.
- Action: The robot stops and turns, before moving again.
- Expected outcome: The robot avoids the edge of the map and continues moving forward.

2. Obstacle detection
- Scenario: The robot is moving forward and encounters an obstacle.
- Inputs: The ultrasonic sensor detects an object within 5 cm.
- Action: The robot stops and rotates the colour sensor to detect the colour of the block.
- Expected outcome: The robot detects the colour of the block.

3. Obstacle evasion
- Scenario: The block is not supposed to be collected.
- Inputs: The colour sensor detects an the colour of the object.
- Action: The robot stops and turns, before moving again.
- Expected outcome: The robot avoids the block and continues moving.

4. Block transportation
- Scenario: The block is supposed to be collected.
- Inputs: The colour sensor detects an the colour of the object.
- Action: The robot uses a spear to collect the block and bring it back to the starting area.
- Expected outcome: The block is in its designated area.

### Test cases
|Test Case|Input|Expected output|
|-|-|-
|Avoids leaving map|Colour sensor detects black line|Robot stops, turns and continues moving|
|Detects obstacle|Ultrasonic sensor detects <5 cm|Robot rotates colour sensor and detects colour of the block.|
|Avoids obstacle|Colour sensor detects block is green/blue|Robot stops, turns and continues moving|
|Transports block|Colour sensor detects block is red/yellow|Robot collects block and moves it to the starting area.|

### Non-functional requirements

- Efficiency - The robot should be efficient and not waste time doing pointless things.
- Response Time - The robot should be quick to react input from sensors.
- Accuracy - The robot should be accurate in it's detection and measurements using the sensors.

## Design

### Mainline routine

### Subroutine

### Subroutine

## Development and Integration


## Testing and Debugging


## Evaluation

- Scenario: The robot is navigating a path and encounters an obstacle.
- Inputs: The ultrasonic sensor detects an object within 10 cm.
- Action: The robot stops and turns 90° to avoid the obstacle.
- Expected Outcome: The robot avoids the obstacle and continues its path.