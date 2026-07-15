"""
Example 05 - TerminateProcess

Objective:
    Terminate a running process using the Win32 TerminateProcess API.

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId
    - OpenProcess
    - TerminateProcess

Concepts:
    - Window handles
    - Process IDs
    - Process handles
    - Access rights
    - Process termination

Reference:
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
   https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess
   https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess
"""


from common.winapi import kernel32
import common.prototypes  # Registers all API prototypes

from common import helpers

def main() -> None:
    """Terminate a process selected by its window title."""

    try:
        window_title = input("Enter window title: ")
        
        hWnd = helpers.get_window_handle(window_title)
        pid = helpers.get_process_id(hWnd)
        hProcess = helpers.open_process(pid)

        result = kernel32.TerminateProcess(hProcess, 0)

        if not result:
            raise RuntimeError(
                f"TerminateProcess failed!. Error: {ctypes.get_last_error()}"
            )

        print(f"Successfully terminated process (PID: {pid}).")

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)
    
    finally:
        kernel32.CloseHandle(hProcess)

if __name__ == "__main__":
    main()