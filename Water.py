import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water now",
            message = "Humans need 3.7 litre of water everyday, so please drink water.",
            app_icon = "C:/Users/aditya/Documents/Programming/Projects/Water-remainder/Glass-Water-icon.ico",
            timeout = 10
        )
        time.sleep(60*60)