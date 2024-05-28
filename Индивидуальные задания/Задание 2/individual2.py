#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from show_plane import show_plane
from pathlib import Path


def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(f'{spacer}+ {path.name}')


if __name__ == '__main__':
    p = Path("packet_hard")
    tree = tree(p)
    show_plane()