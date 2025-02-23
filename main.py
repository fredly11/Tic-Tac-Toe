import threading
from Peer import Peer

# Main function starts program, gets input to launch game, and gets the connection started
if __name__ == "__main__":
    choice = input("Do you want to host the game? (y/n): ").strip().lower()
    if choice == 'y':
        peer = Peer(host='127.0.0.1', port=5555, opponent_host='', opponent_port=5556, symbol='X')
        threading.Thread(target=peer.start_server).start()
        peer.gui.run()
    else:
        opponent_ip = input("Enter opponent's IP address: ")
        peer = Peer(host='127.0.0.1', port=5556, opponent_host=opponent_ip, opponent_port=5555, symbol='O')
        peer.connect_to_peer()