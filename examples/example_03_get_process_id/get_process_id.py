"""
Example 03 - GetWindowThreadProcessId

Description:
   Demonstrates how to obtain the process ID to an existing window 
   using the Win32 GetWindowThreadProcessId function by using its handle (HWND).

Learning Objectives:
    - Retrieve a window handle (HWND)
    - Call the GetWindowThreadProcessId Win32 API
    - Obtain the owning process ID (PID)
    - Obtain the owning thread ID (TID)
    - Understand output parameters using ctypes.byref()

Windows APIs:
    - FindWindowW
    - GetWindowThreadProcessId

Reference:
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
"""

import common.helpers as helpers

def main() -> None:
    """Find the process ID of a Window from its handle."""

    try:
        window_title = input("Enter window title: ")
        hWnd = helpers.get_window_handle(window_title)

        pid = helpers.get_process_id(hWnd)

        print("Process ID:", pid)

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)

   

if __name__ == "__main__":
    main()