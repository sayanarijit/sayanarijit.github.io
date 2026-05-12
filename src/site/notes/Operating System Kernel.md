---
layout: note
tags:
  - tech
  - os
---

# Operating System Kernel

An operating system kernel is the core of an [[Operating System]].

Examples:

- [[Linux]]
- Windows NT
- XNU

Generally, you cannot use a kernel directly since you need an OS, i.e. a software which will mediate communication between you and the kernel.

Example:

- Ubuntu mediates between you and Linux.
- Windows mediates between you and Windows NT.
- MacOS mediates between you and XNU.

## Unikernel / NanoVM

- [A kernel designed to run one and only one application in a virtualized environment](https://nanos.org/)
- [A Rust-based, lightweight unikernel](https://github.com/hermit-os/hermit-rs)
