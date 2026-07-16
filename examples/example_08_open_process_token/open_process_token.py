"""
Example 08 - OpenProcessToken

Objective:
    Obtain a handle to the access token associated with a running process.

Description:
    Demonstrates how to open a process access token using the Win32
    OpenProcessToken API. Access tokens are used throughout Windows
    to represent the security context of a process or thread.

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId
    - OpenProcess
    - OpenProcessToken
    - CloseHandle

Concepts:
    - Windows access tokens
    - Process security
    - Process and token handles
    - Access rights
    - Handle management
    - Resource cleanup

Reference:
    https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken
"""

import ctypes

from ctypes import wintypes

from common.winapi import kernel32,user32
import common.prototypes  # Registers all API prototypes

from common import constants
from common import helpers

def main() -> None:
    """Obtain the primary access token for a running process."""

    hProcess = None
    token = None

    try:
        window_name = input("Enter window name: ")

        hWnd = helpers.get_window_handle(window_name)
        pid = helpers.get_process_id(hWnd)
        hProcess = helpers.open_process(pid)

        token = wintypes.HANDLE()

        success = kernel32.OpenProcessToken(hProcess, constants.TOKEN_ALL_ACCESS, ctypes.byref(token))

        if not success:
             raise RuntimeError(
                f"OpenProcessToken failed!. Error: {ctypes.get_last_error()}"
            )
        
        print(f"[INFO] Process Token Handle: {token.value:#x}")
    
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