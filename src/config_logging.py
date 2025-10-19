import logging


def setup_logging():
    """Настраивает логирование для приложения."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )


def get_logger(name):
    """
    Возвращает экземпляр логгера с заданным именем.
    """
    return logging.getLogger(name)
