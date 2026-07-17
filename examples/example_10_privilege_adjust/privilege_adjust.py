
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

        privilege_name  = "SeDebugPrivilege" ##"SeChangeNotifyPrivilege" SeImpersonatePrivilege
        luid = helpers.lookup_privilege_value(privilege_name)

        privilege_set = structures.PRIVILEGE_SET()

        privilege_set.PrivilegeCount = 1
        privilege_set.Control = 0

        privilege_set.Privileges.Luid = luid
        privilege_set.Privileges.Attributes = constants.SE_PRIVILEGE_ENABLED
   
        # init result 
        result = wintypes.BOOL()

        success = advapi32.PrivilegeCheck(token, ctypes.byref(privilege_set), ctypes.byref(result))

        if not success:
            raise RuntimeError(
                f"PrivilegeCheck failed!. Error: {ctypes.get_last_error()}"
            )

        if result.value:
            print("Privilege: {0}".format(privilege_name))
            # if enabled, disable it
            privilege_set.Privileges.Attributes = constants.SE_PRIVILEGE_DISABLED
        else:
            print("Privilege: {0}".format(privilege_name))
            # if disabled, enable it
            privilege_set.Privileges.Attributes = constants.SE_PRIVILEGE_ENABLED
    
        
        # Build the TOKEN_PRIVILEGES structure describing the new privilege state.

        # declare params
        disable_all_privileges = False
        token_privileges = structures.TOKEN_PRIVILEGES()
        buffer_length = ctypes.sizeof(token_privileges)
        previous_state = structures.TOKEN_PRIVILEGES()
        return_length = wintypes.DWORD()

        # setup new state
        token_privileges.PrivilegeCount = 1
        token_privileges.Privileges = privilege_set.Privileges

        success = advapi32.AdjustTokenPrivileges(
            token,
            disable_all_privileges,
            ctypes.byref(token_privileges),
            buffer_length,
            ctypes.byref(previous_state),
            ctypes.byref(return_length)
        )

        if not success:
            raise RuntimeError(
                f"AdjustTokenPrivileges failed. Error: {ctypes.get_last_error()}"
            )

        error = ctypes.get_last_error()

        if error == constants.ERROR_NOT_ALL_ASSIGNED:
            raise RuntimeError(
                f"Status: {privilege_name} is not present in this token."
            )

        print("Token flipped")

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