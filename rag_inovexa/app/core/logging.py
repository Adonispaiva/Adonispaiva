"""Configuração de logging estruturado."""

import logging

from app.core.config import Settings


def configure_logging(settings: Settings) -> None:
    """Inicializa logging global com nível configurável."""

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
