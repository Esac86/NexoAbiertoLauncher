from app.ui.launcher_ui import Launcher
from app.services.discord_rpc import DiscordRPC

discord_rpc = DiscordRPC()

def onPlay():
    pass

if __name__ == "__main__":
    Launcher(onPlay).mainloop()
