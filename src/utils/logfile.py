"""the module will generate an independently random name for the log file"""
import uuid


def generate_unique_name() -> str:
    """function generates independently random names."""
    return uuid.uuid4()
