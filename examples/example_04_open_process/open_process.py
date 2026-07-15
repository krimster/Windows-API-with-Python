"""
Example 04 - OpenProcess

Objective:
    Obtain a handle to a running process using the Windows API.

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId
    - OpenProcess

Concepts:
    - Window handles
    - Process IDs
    - Process handles
    - Access rights

Reference:
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
   https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess
"""

from common import helpers

def main() -> None:
    """Find the process ID of a Window from its handle."""

    try:
        window_title = input("Enter window title: ")
        
        hWnd = helpers.get_window_handle(window_title)
        
        pid = helpers.get_process_id(hWnd)
        
        hProcess = helpers.open_process(pid)

        print(f"Process Handle: {hProcess:#x}")

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)
    
    finally:
        kernel32.CloseHandle(hProcess)

if __name__ == "__main__":
    main()