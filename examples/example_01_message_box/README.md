# Example 01 - MessageBoxW

## Overview

This example demonstrates how to display a native Windows message box using the Win32 API from Python.

The example uses Python's `ctypes` library to call `MessageBoxW` directly from `user32.dll`, illustrating the basics of interacting with unmanaged Windows APIs.

---

## Learning Objectives

After completing this example you should understand how to:

- Load Windows DLLs using `ctypes`
- Call a Win32 API function
- Pass Unicode strings to native Windows APIs
- Interpret the function's return value
- Define function prototypes using `argtypes` and `restype`

---

## Windows APIs Used

| API | Purpose |
|------|---------|
| `MessageBoxW` | Displays a modal message box containing a message and buttons for user interaction. |

---

## Expected Output

When executed, Windows displays a dialog similar to:

```
+----------------------------------+
| Windows API with Python          |
|----------------------------------|
| Hello World!                     |
|                                  |
|          [ OK ] [ Cancel ]       |
+----------------------------------+
```

The script prints the user's selection to the console.

Example:

```
User clicked OK.
```

or

```
User clicked Cancel.
```

---

## Concepts Introduced

- Win32 API
- `ctypes`
- DLL loading
- Unicode (UTF-16)
- Function prototypes
- Return values

---

## Microsoft Documentation

- MessageBoxW
- user32.dll
- ctypes
