"""
Example 09 - PrivilegeCheck

Objective:
    Determine whether a specific privilege is enabled in the access token
    of a running process.

Description:
    Demonstrates how to query a process access token to determine whether
    a specific privilege is currently enabled. The example first resolves
    a privilege name to its corresponding Locally Unique Identifier (LUID)
    using LookupPrivilegeValueW before calling PrivilegeCheck.

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId
    - OpenProcess
    - OpenProcessToken
    - LookupPrivilegeValueW
    - PrivilegeCheck
    - CloseHandle

Windows Structures:
    - LUID
    - LUID_AND_ATTRIBUTES
    - PRIVILEGE_SET

Concepts:
    - Windows access tokens
    - Security privileges
    - Locally Unique Identifiers (LUIDs)
    - Privilege lookup
    - Privilege verification
    - Access rights
    - Handle management
    - Resource cleanup

Reference:
    https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluew
    https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-privilegecheck
"""

import ctypes

from ctypes import wintypes

from common.winapi import kernel32,user32,advapi32
import common.prototypes  # Registers all API prototypes

from common import constants
from common import helpers
from common import structures

def main() -> None:
    """Check privileges associated with a primary access token for a running process."""

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

        print("Got LUID")
        ## check LUID LowPart and HighPart
        print("LowPart: {0}".format(luid.LowPart))
        print("HighPart: {0}".format(luid.HighPart))


        # check privilege
        required_privileges = structures.PRIVILEGE_SET()

        required_privileges.PrivilegeCount = 1
        required_privileges.Control = 0

        required_privileges.Privileges.Luid = luid
        required_privileges.Privileges.Attributes = constants.SE_PRIVILEGE_ENABLED
        
        ## start debugging
        print(f"PrivilegeCount : {required_privileges.PrivilegeCount}")
        print(f"Control        : {required_privileges.Control}")
        print(f"LUID LowPart   : {required_privileges.Privileges.Luid.LowPart}")
        print(f"LUID HighPart  : {required_privileges.Privileges.Luid.HighPart}")
        print(f"Attributes     : {required_privileges.Privileges.Attributes:#x}")
        ## end debugging

        if helpers.check_privilege(token, luid):
            print("Privilege enabled: {}".format(privilege_name))
        else:
            print("Privilege disabled: {0}".format(privilege_name))


        # init result 
        result = wintypes.BOOL()

        response = advapi32.PrivilegeCheck(token, ctypes.byref(required_privileges), ctypes.byref(result))

        if not response:
            raise RuntimeError(
                f"PrivilegeCheck failed!. Error: {ctypes.get_last_error()}"
            )

        print("Ran privilege check")

        if result.value:
            print("Priv enabled: {0}".format(privilege_name))
        else:
            print("Priv disabled: {0}".format(privilege_name))
    
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