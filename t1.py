import os
from subprocess import check_output

class T1:
    def downgrade(self):
        print("\033[34m[*] Listing devices...")
        p = check_output('adb devices -l', shell=True)
        if "q201".encode() not in p:
            print("\033[32m[-] Device not find, are you sure it is connected?\033[0m")
            os._exit(1)
        else:
            print("\033[34m[+] Device find, ready to flash boot...\033[0m")
            print("\033[36m[+] Uploading boot.img...\033[0m")
            os.system("adb push t1/boot.img /sdcard/boot.img")
            print("\033[36m[+] Flashing boot.img...\033[0m")
            os.system("adb shell dd if=/sdcard/boot.img of=/dev/block/boot")
            print("\033[36m[+] Removing boot.img...\033[0m")
            os.system("adb shell rm -f /sdcard/boot.img")
            print("\033[36m[+] Rebooting your n1...\033[0m")
            os.system("adb reboot")