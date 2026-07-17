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
        privilege_name = "SeDebugPrivilege"

        window_name = input("Enter window name: ")
        hWnd = helpers.get_window_handle(window_name)
        pid = helpers.get_process_id(hWnd)
        hProcess = helpers.open_process(pid)
        token = helpers.open_process_token(hProcess,constants.TOKEN_ALL_ACCESS)
        # token = helpers.open_current_process_token(constants.TOKEN_ALL_ACCESS) 
        luid = helpers.lookup_privilege_value(privilege_name)

        #print("Got LUID")
        #print("LowPart: {0}".format(luid.LowPart))
        #print("HighPart: {0}".format(luid.HighPart))

        # check privilege
        helpers.check_privilege(token, luid, privilege_name)

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