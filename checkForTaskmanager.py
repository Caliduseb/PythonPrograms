import os


def running():
    if os.system("tasklist /FI \"IMAGENAME eq taskmgr.exe\" 2>NUL | find /I /N \"taskmgr.exe\">NUL") == 0:
        return True
    return False
