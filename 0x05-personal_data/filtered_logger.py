#!/usr/bin/env python3
"""0. Regex-ing"""

import re
from typing import List
import logging


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Regex-ing"""
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message
