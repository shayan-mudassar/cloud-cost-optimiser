"""Basic in-process task scheduler."""
import threading
import time
from typing import Callable


def schedule(task: Callable, interval: int) -> threading.Thread:
    """Run *task* every *interval* seconds in a background thread."""
    def loop():
        while True:
            task()
            time.sleep(interval)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    return thread
