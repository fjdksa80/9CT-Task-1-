# 9CT Task 1 - Mechatronics
### By Fraser Maple

## Requirements outline

### Purpose

I need to design a program for the EV3 MINDSTORM robot that will allow it to collect red and yellow LEGO blocks and bring them to a designated area, while avoiding all other LEGO blocks. I must use at least two sensors in my design for navigation and object detection.

### Key actions

- Use colour sensor to detect edges of the map to ensure it does not leave.
- Use ultrasonic sensor to detect obstacles.
- Move forward until and object is detected or the edge of the map is reached.
- Move the correct blocks to the designated area.

### Functional requirements
- Edge of map detection - The colour sensor points down to detect the edge of the map. When the edge of the map is detected, the robot will stop moving, rotate, and begin moving again.
- Obstacle detection - The ultrasonic sensor is used to detect when an obstacle is within 5 cm of the robot. When an obstacle is nearby, a motor will rotate the colour sensor to determite the colour of the block.
- Movement - The robot will be constantly moving forward until the robot detects an obstacle or the edge of the map.
- Block transportation - If the colour of the block is good, it will be speared and taken to the designated area.

### Use cases

1. Edge of map detection
- Scenario: The robot is navigating a path and encounters an obstacle.
- Inputs: The ultrasonic sensor detects an object within 10 cm.
- Action: The robot stops and turns 90° to avoid the obstacle.
- Expected Outcome: The robot avoids the obstacle and continues its path.

## Design


## Development and Integration


## Testing and Debugging


## Evaluation