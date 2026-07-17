
import ctypes

from ctypes import wintypes

from common.winapi import kernel32,user32,advapi32
import common.prototypes  # Registers all API prototypes

from common import constants
from common import helpers
from common import structures

def main() -> None:
    """Adjust privileges associated with a primary access token for a running process."""

    hProcess = None
    token = None

    try:
        window_name = input("Enter window name: ")
        hWnd = helpers.get_window_handle(window_name)
        pid = helpers.get_process_id(hWnd)
        hProcess = helpers.open_process(pid)
        token = helpers.open_process_token(hProcess,constants.TOKEN_ALL_ACCESS)
        # token = helpers.open_current_process_token(constants.TOKEN_ALL_ACCESS) 
        
        privilege_name  = "SeDebugPrivilege"
        luid = helpers.lookup_privilege_value(privilege_name)
        
        result = helpers.check_privilege(token, luid, privilege_name, constants.SE_PRIVILEGE_ENABLED)

        attribute = constants.SE_PRIVILEGE_DISABLED if result else constants.SE_PRIVILEGE_ENABLED

        helpers.adjust_privilege(
            token,
            luid,
            attribute
        )

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)
    
    finally:
        if hProcess:
            kernel32.CloseHandle(hProcess)
        
        if token:
            kernel32.CloseHandle(token)

if __name__ == "__main__":
    main()