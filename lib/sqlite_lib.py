# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

import time
import sqlite3


class SqliteContext:
    '''sqlite操作上下文'''

    def __init__(self):
        self.conn = sqlite3.connect("..\\data\\sample.db")
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor, self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    pass
