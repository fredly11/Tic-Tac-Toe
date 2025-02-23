import socket
import threading
from TicTacToe import TicTacToe
from TicTacToeGUI import TicTacToeGUI

# This class handles network connection and sending data
class Peer:
    def __init__(self, host, port, opponent_host, opponent_port, symbol):
        self.symbol = symbol
        self.gui = TicTacToeGUI(self)
        self.game = TicTacToe(self.gui)
        self.host = host
        self.port = port
        self.opponent_host = opponent_host
        self.opponent_port = opponent_port
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_socket = None
        self.connected = False

# checks for data being received
    def handle_connection(self, conn):
        self.connected_socket = conn
        self.connected = True
        while True:
            try:
                data = conn.recv(1024).decode()
                if data:
                    print(f"Received move: {data}")
                    move = int(data)
                    self.game.make_move(move)
                    self.gui.update_board()
                    self.gui.check_game_status()
                else:
                    print("Connection lost.")
                    self.connected = False
                    break
            except Exception as e:
                print(f"Error receiving data: {e}")
                break

# Sends a move data packet
    def send_move(self, move):
        print(f"Attempting to send move: {move}")
        if self.connected and self.connected_socket:
            try:
                self.connected_socket.send(str(move).encode())
                print(f"Move sent: {move}")
            except OSError as e:
                print(f"Error sending move: {e}")
                self.connected = False
        else:
            print("Error: No connection. Cannot send move.")

# Begins the server for host
    def start_server(self):
        print(f"Server starting on {self.host}:{self.port}")
        self.listening_socket.bind((self.host, self.port))
        self.listening_socket.listen(1)
        print(f"Server is now listening on {self.host}:{self.port}")
        print("Waiting for opponent to connect...")

        conn, addr = self.listening_socket.accept()
        print(f"Connected to {addr}")
        threading.Thread(target=self.handle_connection, args=(conn,)).start()

# Connects to host from client
    def connect_to_peer(self):
        print(f"Attempting to connect to {self.opponent_host}:{self.opponent_port}")
        try:
            self.connected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connected_socket.connect((self.opponent_host, self.opponent_port))
            print(f"Connected to {self.opponent_host}:{self.opponent_port}. Client-side port: {self.connected_socket.getsockname()[1]}")
            threading.Thread(target=self.handle_connection, args=(self.connected_socket,)).start()
            self.gui.run()

        except ConnectionRefusedError:
            print("Connection failed.")
            self.connected = False
