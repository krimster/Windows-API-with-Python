"""
Example 01 - MessageBox

Description:
    Demonstrates how to call the Win32 MessageBoxW function from Python
    using ctypes to display a native Windows dialog.

Learning Objectives:
    - Load functions from user32.dll
    - Call a Win32 API using ctypes
    - Pass Unicode strings to the Windows API
    - Handle the function's return value

Windows APIs:
    - MessageBoxW

Reference:
    https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-messageboxw
"""

import ctypes
from ctypes import wintypes
import common.constants as constants
from common.winapi import user32
import common.prototypes  # Registers all API prototypes

def main() -> None:
    """Display a native Windows message box."""

    result = user32.MessageBoxW(
        None,
        "Hello World!",
        "Windows API with Python",
        constants.MB_OKCANCEL,
    )

    if result == constants.IDOK:
        print("User clicked OK.")

    elif result == constants.IDCANCEL:
        print("User clicked Cancel.")


if __name__ == "__main__":
    main()