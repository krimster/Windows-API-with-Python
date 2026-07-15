"""
Example 06 - CreateProcessW

Objective:
    Create a new process using the Win32 CreateProcessW API.

Description:
    Demonstrates how to spawn a new process from Python by calling the
    Windows CreateProcessW function through ctypes.

Windows APIs:
    - CreateProcessW

Windows Structures:
    - SECURITY_ATTRIBUTES
    - STARTUPINFOW
    - PROCESS_INFORMATION

Concepts:
    - Process creation
    - Process handles
    - Thread handles
    - Windows structure definitions
    - Passing structures by reference
    - Win32 API function prototypes

Reference:
    https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
"""
import ctypes

from common.winapi import kernel32
import common.prototypes  # Registers all API prototypes

from common import structures

def main() -> None:
    """Spawn a new process."""

    try:
        lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
        lpCommandLine = None
        lpProcessAttributes = None
        lpThreadAttributes = None 
        lpEnvironment = None
        lpCurrentDirectory = None

        dwCreationFlags = 0x00000010 # create new console

        bInheritHandle = False

        lpProcessInformation = structures.PROCESS_INFORMATION()

        lpStartupInfo = structures.STARTUP_INFO()
        lpStartupInfo.wShowWindow = 0x1
        lpStartupInfo.dwFlags = 0x1   ## STARTF_USESHOWWINDOW 0x00000001

        # call api
        response = kernel32.CreateProcessW(
            lpApplicationName,
            lpCommandLine,
            lpProcessAttributes,
            lpThreadAttributes,
            bInheritHandle,
            dwCreationFlags,
            lpEnvironment,
            lpCurrentDirectory,
            ctypes.byref(lpStartupInfo),
            ctypes.byref(lpProcessInformation)
            
        )

        if not response:
            raise RuntimeError(
                f"CreateProcessW failed!. Error: {ctypes.get_last_error()}"
            )
        
        print("Process spawned successfully!")
    
    except RuntimeError as e:
        print(e)
        raise SystemExit(1)
            
if __name__ == "__main__":
    main()







