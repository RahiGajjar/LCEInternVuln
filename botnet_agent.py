import socket
import os

HOST = "0.0.0.0"
PORT = 5050

def handle_client(conn):
    conn.sendall(b"Telemetry Agent v1.4\nAvailable: ?\n> ")
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break

        cmd = data.lower()

        if cmd.startswith("join"):
            conn.sendall(b"Connection to remote agent confirmed.\nFLAG{joined_botnet_successfully}\n")
        elif cmd.startswith("ping"):
            conn.sendall(b"PONG\n")
        elif cmd.startswith("exec"):
            os.system(cmd[5:])
            conn.sendall(f"Executed: {cmd[5:]}\n".encode())
        elif cmd.startswith("help") or cmd == "?":
            conn.sendall(b"Hint: This isn't documented... legacy engineers might remember.\n")
        else:
            conn.sendall(b"Unknown input.\n")
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Botnet interface listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()
