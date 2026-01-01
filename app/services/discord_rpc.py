import threading
import time
from pypresence import Presence

CLIENT_ID = "1456139803211993176"

class DiscordRPC:
    def __init__(self):
        self.rpc = None
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def _run(self):
        try:
            self.rpc = Presence(CLIENT_ID)
            self.rpc.connect()
            self.update_status("Jugando a Nexo Abierto Launcher", "Abierto")
            while True:
                time.sleep(15)
        except Exception as e:
            print("Discord no disponible:", e)

    def update_status(self, details: str, state: str):
        if self.rpc:
            try:
                self.rpc.update(
                    details=details,
                    state=state,
                    large_image="logo",
                    start=time.time()
                )
            except:
                pass
