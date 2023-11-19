# CSF_CAP3_TestCase

1/Player and Enemy Movement Tests

*TestPlayerInitialization: Ensures that the player is correctly initialized with the expected attributes and values.
*TestPlayerMovement: Tests different aspects of player movement, including turning, keyboard and mouse inputs, and overall movement.
*TestEnemyMovement: Tests various functionalities related to enemy movement, including checking if the enemy is alive, roaming, hunting the player, calculating vector distances, animating, checking player collision, drawing enemy health, and updating.

2/CSV Layout Import Test

*TestImportCSVLayout: Tests the import of a CSV layout for the game level. A temporary CSV file is created for testing purposes.

3/End Screen Display Test

*TestEndScreenDisplay: Tests the display of the end screen under different conditions (game over and beating the game). The tests simulate the conditions, call the display_end_screen function, and check if specific text is present in the expected output.

4/Resource Used

*Pygame: The tests utilize the Pygame library for game development. Pygame provides functionalities for creating games, handling events, and rendering graphics.
*unittest Framework: The unittest module is used for writing and running unit tests in Python. It provides a test discovery mechanism, test fixtures, and assertions for validating expected behaviors.
*CSV File: A temporary CSV file is used to test the import of a game layout.

The test cases are organized using the unittest framework. Each test class inherits from unittest.TestCase, and each test method within a class is a separate test case. The setUp and tearDown methods are used to set up and clean up resources before and after each test, respectively.
