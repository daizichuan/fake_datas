#-- coding:UTF-8 --
#!/usr/bin/env python
"""

"""

from functools import wraps

def Singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper