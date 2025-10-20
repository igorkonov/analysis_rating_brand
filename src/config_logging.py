import logging


def setup_logging():
    """Настраивает логирование для приложения."""
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)-8s: %(message)s",
        datefmt="%H:%M:%S",
        force=True,
    )
