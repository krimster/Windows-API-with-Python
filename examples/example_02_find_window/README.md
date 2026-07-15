# Example 02 - FindWindowW

## Overview

This example demonstrates how to locate an existing window by its title using the Win32 `FindWindowW` function.

The function returns a window handle (`HWND`), which uniquely identifies a window within the Windows operating system. Window handles are used throughout the Win32 API to perform operations such as retrieving process information, sending messages, and manipulating windows.

---

## Learning Objectives

After completing this example you should understand how to:

- Load functions from `user32.dll`
- Call the `FindWindowW` Win32 API using `ctypes`
- Pass Unicode strings to native Windows APIs
- Obtain a window handle (`HWND`)
- Handle API success and failure

---

## Windows APIs Used

| API | Purpose |
|------|---------|
| `FindWindowW` | Retrieves the handle (`HWND`) of a top-level window matching the specified title or class name. |

---

## How It Works

1. Prompt the user for a window title.
2. Call `FindWindowW()`.
3. If the window exists, return its handle.
4. If no matching window is found, report the failure.

---

## Example Output

Successful lookup:

```text
Enter window title: Task Manager

Window Handle: 0x50320
```

Window not found:

```text
Enter window title: My Awesome Window

Could not find window: 'My Awesome Window'
```

---

## Concepts Introduced

- Win32 API
- `ctypes`
- Window Handles (`HWND`)
- Unicode (`UTF-16`)
- Function prototypes
- Return values

---

## Why Is an HWND Important?

Most Win32 APIs that interact with windows require an `HWND`.

In later examples, the window handle obtained here will be used to:

- Retrieve the owning process ID
- Open a handle to the owning process
- Interact with that process using additional Win32 APIs

Understanding `HWND` is a fundamental building block for Windows API programming.

---

## Microsoft Documentation

- [FindWindowW](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-findwindoww)
- [Windows Data Types](https://learn.microsoft.com/windows/win32/winprog/windows-data-types)

