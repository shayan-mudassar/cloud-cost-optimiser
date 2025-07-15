"""Notification utilities."""
from typing import Optional
import logging


logger = logging.getLogger(__name__)


def notify(message: str, channel: Optional[str] = None) -> None:
    """Notify user via the given channel. For now, log the message."""
    if channel:
        logger.info("Sending to %s: %s", channel, message)
    else:
        logger.info("Notification: %s", message)
