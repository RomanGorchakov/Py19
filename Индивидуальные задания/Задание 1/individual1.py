#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from show_plane import show_plane
from pathlib import Path


if __name__ == '__main__':
    p = Path("schedule.txt")
    show_plane()