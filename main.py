"""The script run `NUMBER_OF_DRIVERS` parallel driver."""
#!/usr/bin/python3
import threading

from src.drivers.driver import Driver

NUMBER_OF_DRIVERS = 1

if __name__ == "__main__":
    drivers = [Driver() for i in range(NUMBER_OF_DRIVERS)]
    threads = [threading.Thread(target=item.run) for item in drivers]
    for item in threads:
        item.start()
    for item in threads:
        item.join()
