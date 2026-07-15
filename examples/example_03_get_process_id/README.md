# Example 03 - GetWindowThreadProcessId

## Overview

This example demonstrates how to retrieve the Process ID (PID) and Thread ID (TID) associated with a window using the Win32 `GetWindowThreadProcessId` function.

Building on the previous example, we first obtain a window handle (`HWND`) using `FindWindowW`, then use that handle to identify the process and thread that own the window.

Understanding how to move from a window handle to a process ID is an essential step before interacting with a process using APIs such as `OpenProcess`.

---

## Learning Objectives

After completing this example you should understand how to:

- Obtain a window handle (`HWND`) using `FindWindowW`
- Call the `GetWindowThreadProcessId` Win32 API
- Retrieve the owning Process ID (PID)
- Retrieve the owning Thread ID (TID)
- Use output parameters with `ctypes.byref()`

---

## Windows APIs Used

| API | Purpose |
|------|---------|
| `FindWindowW` | Retrieves the handle (`HWND`) of an existing window. |
| `GetWindowThreadProcessId` | Retrieves the thread ID and process ID associated with a window. |

---

## How It Works

1. Prompt the user for a window title.
2. Locate the window using `FindWindowW`.
3. Obtain the corresponding `HWND`.
4. Call `GetWindowThreadProcessId()`.
5. Read the returned Thread ID (TID).
6. Read the Process ID (PID) from the output parameter.

---

## Data Flow

```text
Window Title
      │
      ▼
FindWindowW()
      │
      ▼
    HWND
      │
      ▼
GetWindowThreadProcessId()
      │
      ├──────────────┐
      ▼              ▼
Thread ID (TID)   Process ID (PID)
```

---

## Example Output

```text
Enter window title: Task Manager

Window Handle : 0x50320
Thread ID     : 9188
Process ID    : 4544
```

---

## Concepts Introduced

- Window Handles (`HWND`)
- Process IDs (`PID`)
- Thread IDs (`TID`)
- Output parameters
- `ctypes.byref()`
- Function return values

---

## Key Takeaways

One of the more interesting aspects of this example is that `GetWindowThreadProcessId` returns **two values**:

- The **Thread ID** is returned as the function's return value.
- The **Process ID** is written to a memory location supplied by the caller.

Because the Process ID is an output parameter, Python's `ctypes.byref()` function is required to pass a pointer to a writable `DWORD`.

Understanding output parameters is fundamental when interacting with the Win32 API, as many functions return additional information through pointers rather than as the function's return value.

---

## Microsoft Documentation

- [FindWindowW](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-findwindoww)
- [GetWindowThreadProcessId](https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid)
