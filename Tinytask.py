def main():
    window1 = get_hwnd("Keyboard Test Online - Google Chrome")



    while True:        
        press_key(window1, "A", 0.1)
        sleep(0.2)











def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print((hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)



def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds



def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result



def press_key(focused_window, key, duration):
    if (GetForegroundWindow()) != focused_window:
        focus_window(focused_window)
    if duration == 0:
        win32api.PostMessage(focused_window, win32con.WM_CHAR, keys[key], 0)
    else:
        win32api.PostMessage(focused_window, win32con.WM_KEYDOWN, keys[key], 0)
        sleep(duration)
        win32api.PostMessage(focused_window, win32con.WM_KEYUP, keys[key], 0)

    print("Pressed ", chr(keys[key]))



def get_hwnd(name):
    global hwnd, hwndChild
    hwnds = find_all_windows(name)
    print("\n\nMain HWND's: ",hwnds)
    hwnd = hwnds[0]
    hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    print("Child HWND: ", hwndChild, "\n")
    return hwnd



def focus_window(no):
    print("\n\nFocusing window: ", GetWindowText(no))

    win32gui.ShowWindow(no, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(no)

#list_window_names()
#get_inner_windows(hwnd1)

from time import sleep, time
import win32gui, win32ui, win32api, win32con, win32com.client
from win32con import (SW_SHOW, SW_RESTORE)
from win32gui import GetWindowText, GetForegroundWindow

hwnd = None
keys = {'A': 0x41, 'B': 0x42, 'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49, 'J': 0x4A, 'K': 0x4B, 'L': 0x4C, 'M': 0x4D, 'N': 0x4E, 'O': 0x4F, 'P': 0x50, 'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55, 'V': 0x56, 'W': 0x57, 'X': 0x58, 'Y': 0x59, 'Z': 0x5A, 'SPACE': 0x20}





main()
