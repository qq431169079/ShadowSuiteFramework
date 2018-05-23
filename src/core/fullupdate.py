import subprocess
import urllib

from core import misc
from core import error
from core import version

def check_for_updates(debugging, silent=False):
    print(misc.CG + "[i] Checking for updates..." + misc.END)
    if debugging == True:
        print("[LOGGER] Getting current version from repository...")

    try:
        remote_version = urllib.request.urlopen("https://raw.githubusercontent.com/Sh4d0w-T34m/ShadowSuiteFramework/master/core/version.py")

    except urllib.error.URLError:
        print(error.ERROR0010)
        return "ERRED", "ERRED"

    except Exception as urllib_err:
        print(error.ERROR0020.format(str(urllib_err)))
        return "ERRED", "ERRED"

    remote_version = remove_version.split('\n')
    got_it = False
    for lines in remote_version:
        if 'VNUMBER' in lines:
            remote_version = lines.replace("VNUMBER = ", '')
            got_it = True

        else:
            got_it = False
            continue

    if got_it == True:
        pass

    else:
        print(error.ERROR0021)
        return "ERRED", "ERRED"

    current_version = version.VNUMBER
    # print("Current: " + current_version)
    # print("Remote: " + remote_version)
    if remote_version != current_version:
        if silent == True:
            return True, remote_version

        print()
        print("[i] There's a new version! New version: " + remote_version)
        print()
        print("[i] Type 'update program' to update.")
        print("    To manually update or you didn't cloned the repository,")
        print("    go to 'https://github.com/Sh4d0w-T34m/ShadowSuiteFramework'")
        print("    and clone the repository.")
        print()
        return True, remote_version # Needs update
    
    else:
        if silent == True:
            return False, ""

        print()
        print("[i] You are using the latest version of SSF!")
        print()
        print("[i] If you have any suggestions, opinions, feature requests, or")
        print("    even issues, don't hesitate to contact us at the following")
        print("    accounts:")
        print()
        print("        Catayao56@xmpp.jp")
        print("        sh4d0wh4x0r@xmpp.jp")
        print()
        return False, "" # Up-to-date


def update(global_variables, debugging):
    try:
        update_needed, remote_version = check_for_updates(debugging, True)
        if update_needed == "ERRED" or remote_version == "ERRED":
            print(error.ERROR0020.format("Unknown error occured."))
            return None

        else:
            pass

    except Exception as check4updates_err:
        print(error.ERROR0020.format(str(check4updates_err)))
        return None

    if update_needed == True:
        success = subprocess.call([global_variables['BINARY_PATH'] + "git", "pull", "origin", "master"])
        if success == 0:
            print("[i] SSF is now updated to " + remote_version + "! Please restart SSF to use the updated version.")

        else:
            print("[i] " + error.ERROR0020.format("Process returned error code " + str(success) + '.'))

        return None

    else:
        print("[i] You are using the latest version of SSF!")
        print()
        print("[i] If you have any suggestions, opinions, feature requests, or")
        print("    even issues, don't hesitate to contact us at the following")
        print("    accounts:")
        print()
        print("        Catayao56@xmpp.jp")
        print("        sh4d0wh4x0r@xmpp.jp")
        print()
        return None
