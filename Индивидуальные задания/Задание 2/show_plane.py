﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os.path
import sys
import random
import pathlib


def display_plane(staff):
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 12
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолёта"
            )
        )
        print(line)
 
        for idx, planes in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                    idx,
                    planes.get('race', ''),
                    planes.get('number', ''),
                    planes.get('type', 0)
                )
            )
 
    print(line)

def get_plane(staff, race, number, type):
    staff.append(
        {
            "race": race,
            "number": number,
            "type": type,
        }
    )
    
    return staff

def save_plane(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)

def load_plane(file_name):
    with open(file_name, encoding="utf-8-sig") as fin:
        return json.load(fin)

def show_plane(command_line = None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action = "store",
        help = "The data file name"
    )

    parser = argparse.ArgumentParser("planes")
    parser.add_argument(
        "--version",
        action = "version",
        version = "%(prog)s 0.1.0"
    )
    
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add",
        parents = [file_parser],
        help = "Add a new race"
    )
    add.add_argument(
        "-r",
        "--race",
        action = "store",
        required = True,
        help = "Where plane supposed to go"
    )
    add.add_argument(
        "-n",
        "--number",
        action = "store",
        type = int,
        help = "Number of race"
    )
    add.add_argument(
        "-t",
        "--type",
        action = "store",
        type = int,
        required = True,
        help = "Plane type code"
    )
    _ = subparsers.add_parser(
        "display",
        parents = [file_parser],
        help = "Display all races"
    )

    select = subparsers.add_parser(
        "select",
        parents = [file_parser],
        help = "Select the race"
    )
    select.add_argument(
        "-P",
        "--period",
        action = "store",
        type = int,
        required = True,
        help = "The required period"
    )

    args = parser.parse_args(command_line)

    is_dirty = False
    if os.path.exists(args.filename):
        airport = load_plane(args.filename)
    else:
        airport = []

    if args.command == "add":
        airport = get_plane(
            airport,
            args.race,
            args.number,
            args.type
        )
        is_dirty = True

    elif args.command == "display":
        display_plane(airport)

    elif args.command == "select":
        selected = select_plane(airport, args.period)
        display_plane(selected)

    if is_dirty:
        save_plane(args.filename, airport)