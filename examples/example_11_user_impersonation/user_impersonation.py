"""
Example 11 - User Impersonation

Objective:
    Duplicate the primary access token of a running process and create
    a new process under the security context of the target user.

Description:
    Demonstrates the complete Windows access token workflow required for
    user impersonation. The example opens a target process, obtains its
    primary access token, verifies that the current process has the
    required privileges, duplicates the target token, and launches a new
    process using CreateProcessWithTokenW.

    This example builds upon the concepts introduced in the previous
    examples covering OpenProcessToken, PrivilegeCheck, and
    AdjustTokenPrivileges.

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId
    - OpenProcess
    - OpenProcessToken
    - GetCurrentProcess
    - LookupPrivilegeValueW
    - PrivilegeCheck
    - AdjustTokenPrivileges
    - DuplicateTokenEx
    - CreateProcessWithTokenW
    - CloseHandle

Concepts:
    - Windows access tokens
    - Primary vs impersonation tokens
    - User impersonation
    - Token duplication
    - Token privileges
    - Security impersonation levels
    - Process creation using an existing token
    - Handle management
    - Resource cleanup

Reference:
    https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex
    https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-createprocesswithtokenw
"""

import ctypes

from ctypes import wintypes

from common.winapi import kernel32,user32,advapi32
import common.prototypes  # Registers all API prototypes

from common import constants
from common import helpers
from common import structures
from common import enums

def main() -> None:
    """Adjust privileges associated with a primary access token for a running process."""

    hProcess = None
    token = None

    try:
        
        ## Target user
        window_name = input("Enter window name: ")
        hWnd = helpers.get_window_handle(window_name)
        pid = helpers.get_process_id(hWnd)
        hProcess = helpers.open_process(pid)
        target_token = helpers.open_process_token(hProcess,constants.TOKEN_ALL_ACCESS)
    
        ## current user
        token = helpers.open_current_process_token(constants.TOKEN_ALL_ACCESS)         
        privilege_name  = "SeDebugPrivilege"
        luid = helpers.lookup_privilege_value(privilege_name)
        
        result = helpers.check_privilege(token, luid, privilege_name, constants.SE_PRIVILEGE_ENABLED)

        if result == constants.SE_PRIVILEGE_DISABLED:
            print("{0} is disabled, attempting to enable it".format(privilege_name))
            helpers.adjust_privilege(
                token,
                luid,
                constants.SE_PRIVILEGE_ENABLED
            )
        
        ## Duplicate
        lpTokenAttributes = structures.SECURITY_ATTRIBUTES()
        lpTokenAttributes.bInheritHandle = False
        lpTokenAttributes.lpSecurityDescriptor = ctypes.c_void_p()
        lpTokenAttributes.nLength = sizeof(lpTokenAttributes)

        impersonated_token = wintypes.HANDLE()
        success =  advapi32.DuplicateTokenEx(
            target_token, 
            constants.TOKEN_ALL_ACCESS, 
            ctypes.byref(lpTokenAttributes),  # Could also be None for Default security attributes
            enums.SECURITY_IMPERSONATION_LEVEL.Impersonation, 
            enums.TOKEN_TYPE.TokenPrimary, 
            ctypes.byref(impersonated_token))

        if not success:
            raise RuntimeError(
                f"DuplicateTokenEx failed!. Error: {ctypes.get_last_error()}"
            )

        print("DuplicateTokenEx success")
        print(f"Original token   : {target_token.value:#x}")
        print(f"Duplicate token  : {impersonated_token.value:#x}")

        lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
        dwLogonFlags = constants.LOGON_WITH_PROFILE
        lpCommandLine = None
        dwCreationFlags = 0x00000010 # create new console
        lpEnvironment = None
        lpCurrentDirectory = None
        lpProcessInformation = structures.PROCESS_INFORMATION()
        lpStartupInfo = structures.STARTUP_INFO()
        lpStartupInfo.wShowWindow = 0x1
        lpStartupInfo.dwFlags = 0x1   ## STARTF_USESHOWWINDOW 0x00000001

        # call api
        success = advapi32.CreateProcessWithTokenW(
            impersonated_token,
            dwLogonFlags,
            lpApplicationName,
            lpCommandLine,
            dwCreationFlags,
            lpEnvironment,
            lpCurrentDirectory,
            ctypes.byref(lpStartupInfo),
            ctypes.byref(lpProcessInformation)
        )

        if not success:
            raise RuntimeError(
                f"CreateProcessWithTokenW failed!. Error: {ctypes.get_last_error()}"
            )
        
        print("Process spawned successfully!")
       

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