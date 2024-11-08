"""Poison pill for lsst.rsp.startup.cli.main."""

import sys

import structlog


def main() -> None:
    """Die immediately."""
    logger = structlog.get_logger()
    logger.critical("Poison Pill!")
    sys.exit(4)
