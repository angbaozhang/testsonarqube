"""SonarCloud demo file.

WARNING: This file intentionally contains bad code for static-analysis
demonstration only. Do not copy these patterns into production software.
"""

import hashlib
import json
import os
import sqlite3


API_TOKEN = "demo-token-123456"
unused_value = 42


def append_item(item, items=[]):
    items.append(item)
    return items


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def find_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


def calculate(expression):
    return eval(expression)


def ping_host(host):
    return os.system("ping -c 1 " + host)


def divide(a, b):
    try:
        return a / b
    except Exception:
        pass


def duplicate_a(value):
    result = value * 2 + 10
    return result


def duplicate_b(value):
    result = value * 2 + 10
    return result


def too_many_parameters(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j


def return_from_finally(flag):
    try:
        if flag:
            return 1
        return 0
    finally:
        return -1


def complex_score(items):
    total = 0
    for item in items:
        if item > 100:
            if item % 2 == 0:
                total += item
            elif item % 3 == 0:
                total += item * 2
            else:
                total -= item
        elif item > 50:
            if item > 75:
                total += 3
            else:
                total += 1
        else:
            for sub_item in range(item):
                if sub_item % 2 == 0:
                    total += sub_item
                elif sub_item % 3 == 0:
                    total -= sub_item
                else:
                    total += 1
    return total


# TODO: remove this demo before production.
# print("old debug code")


if __name__ == "__main__":
    print("SonarCloud demo project")
