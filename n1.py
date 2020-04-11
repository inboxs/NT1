import os
from subprocess import check_output

class N1:
    def downgrade(self):
        print("\033[34m[*] Listing devices...\033[0m")
        p = check_output('adb devices -l', shell=True)
        if "p230".encode() not in p:
            print("\033[31m[-] Device not find, are you sure it is connected?\033[0m")
            os._exit(1)
        else:
            print("\033[32m[+] Device find, ready to flash boot...\033[0m")
            print("\033[36m[+] Uploading boot.img...\033[0m")
            os.system(r"adb push n1\\boot.img /sdcard/boot.img")
            print("\033[36m[+] Flashing boot.img...\033[0m")
            os.system("adb shell dd if=/sdcard/boot.img of=/dev/block/boot")
            print("\033[36m[+] Removing boot.img...\033[0m")
            os.system("adb shell rm -f /sdcard/boot.img")
            print("\033[36m[+] Rebooting your n1...\033[0m")
            os.system("adb reboot")

    def flash(self):
        print("\033[35m[!] 请确保USB双头线已连接\033[0m")
        print("\033[34m[*] Listing devices...\033[0m")
        p = check_output('adb devices -l', shell=True)
        if "p230".encode() not in p:
            print("\033[32m[-] Device not find, are you sure it is connected?\033[0m")
            os._exit(1)
        else:
            print("\033[36m[+] Rebooting your n1...\033[0m")
            os.system("adb shell reboot update")

    def udisk(self):
        print("\033[34m[*] Listing devices...\033[0m")
        p = check_output('adb devices -l', shell=True)
        if "p230".encode() not in p:
            print("\033[32m[-] Device not find, are you sure it is connected?\033[0m")
            os._exit(1)
        else:
            print("\033[36m[+] Rebooting your n1...\033[0m")
            os.system("adb shell reboot update")
