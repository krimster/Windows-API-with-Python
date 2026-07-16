"""
Example 02 - FindWindowW

Description:
   Demonstrates how to obtain a handle (HWND) to an existing window 
   using the Win32 FindWindowW function by searching for its title.

Learning Objectives:
    - Call the FindWindowW Win32 API from Python
    - Pass Unicode strings to the Windows API
    - Obtain a window handle (HWND)
    - Handle API success and failure

Windows APIs:
    - FindWindowW

Reference:
   https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
"""

from common import helpers

def main() -> None:
    """Find a window by its title."""

    try:
        window_title = input("Enter window title: ")
        hWnd = helpers.get_window_handle(window_title)
   
        print(f"Window Handle: {hWnd:#x}")

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
