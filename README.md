# Windows API with Python

## Overview

The goal of this project is to develop a solid understanding of the Windows API using Python's `ctypes` library, with a focus on techniques commonly used during red team operations, malware analysis, and Windows internals research.

Rather than relying on third-party libraries, the exercises interact directly with native Windows API functions, providing hands-on experience with low-level Windows programming.

---

## Learning Objectives

Throughout this project I explore:

- Loading Windows DLLs with `ctypes`
- Calling native Win32 API functions
- Understanding handles, pointers, and memory addresses
- Working with Windows processes and threads
- Opening process handles with specific access rights
- Enumerating and interacting with Windows
- Reading Microsoft API documentation
- Marshaling C data types into Python
- Understanding common Win32 data structures
- Error handling using Windows error codes

---

## Technologies

- Python 3
- ctypes
- Windows API (Win32)
- Visual Studio Code
- Windows 11

---

## Topics Covered

Some of the APIs explored include:

- `FindWindowW`
- `GetWindowThreadProcessId`
- `OpenProcess`
- `TerminateProcess`
- `CloseHandle`

Additional APIs will be added as I progress through the course.

---

## Purpose

The purpose of this repository is to document my journey learning low-level Windows programming for:

- Red Team Operations
- Malware Development (Research & Education)
- Malware Analysis
- Windows Internals
- Offensive Security
- Detection Engineering
- Endpoint Security Research

All code is written for educational purposes within controlled lab environments.

---

## Disclaimer

This repository is intended solely for educational and defensive security research.

All demonstrations are performed against systems that I own or have explicit permission to test. The techniques demonstrated should never be used against systems without proper authorization.

---

## Acknowledgements

Course:

**Hacking the Windows API with Python – Real Ethical Hacking**

Provided by **RedTeamNation.com**

This repository contains my own notes, implementations, and experiments completed while following the course.