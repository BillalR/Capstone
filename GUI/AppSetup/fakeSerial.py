import os, pty, serial

master, slave = pty.openpty()
s_name = os.ttyname(slave)
