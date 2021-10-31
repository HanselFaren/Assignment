import time

def delay(x: str, y: int):
    time.sleep(y)
    print(x)

delay("This is message", 5)