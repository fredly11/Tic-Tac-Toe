# Overview

## Building a Networked Tic-Tac-Toe Game

In order to develop my skills in computer networking, I developed a networked Tic-Tac-Toe game. This project aimed to create a functional, real-time multiplayer experience, providing a practical application of socket programming and GUI development.

This software allows two players to engage in a Tic-Tac-Toe game over a local network. To start a game, one player hosts a server, and the other player must connect to that server using the host's IP address.

**How to use:**

1.  **Host (Player X):**
    * Run `main.py`.
    * When prompted, enter 'y' to host the game.
    * The game window will appear, and the program will wait for the opponent to connect.
2.  **Client (Player O):**
    * Run `main.py`.
    * When prompted, enter 'n' to join a game.
    * Enter the IP address of the host player.
    * The game window will appear, and the game will begin.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This software utilizes a **client/server** architecture. One player acts as the server, hosting the game, and the other player connects as a client, though the same code is used for both players.

**TCP** is used for the connection between client and server. The server listens on port **5555**, and the client connects to the server on port **5555**. The client uses port **5556** to connect to the server.

Messages sent between the client and server consist of a single integer, representing the index of the Tic-Tac-Toe board cell that the player has selected.

# Development Environment

The software was developed using **Python 3.2**.

**Tools:**

* **Python:** The language used for the code
* **VS Code:** For code editing and debugging.
* **Command Prompt/Terminal:** For running the Python scripts.

**Libraries:**

* **`socket`:** For network communication.
* **`tkinter`:** For the graphical user interface.
* **`threading`:** For handling network operations.

# Useful Websites

* [Python Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
* [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
* [Real Python - Socket Programming in Python](https://realpython.com/python-sockets/)

# Future Work

* Implement error handling for invalid IP addresses and connection failures.
* Add a feature to allow players to choose their symbols (X or O) or have the symbol randomly assigned.
* Implement a chat feature for players to communicate during the game.
* Add functionality to play over the internet, not just a local network.
* Add a replay game feature.