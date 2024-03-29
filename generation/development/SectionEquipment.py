import logging

from generation.development.SectionBase import SectionBase


def root_log():
    logging.debug("This is a debug message from some_function")
    try:
        # Code that might raise an exception
        pass
    except Exception as e:
        logging.error("An error occurred: %s", str(e))


class SectionEquipment(SectionBase):
    pass