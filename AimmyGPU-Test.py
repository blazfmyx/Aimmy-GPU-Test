import winreg, sys, time; from colorama import Fore, Style; from os import system

# Title
system("title Blaz's GPU Test")

#Typewriter Function
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0225)

# Logo
print(Fore.MAGENTA + '\
███████████████████████████████████████▀██████████████\n\
█▄─▄─▀█▄─▄████▀▄─██░▄▄░▄█░█─▄▄▄▄███─▄▄▄▄█▄─▄▄─█▄─██─▄█\n\
██─▄─▀██─██▀██─▀─███▀▄█▀█▄█▄▄▄▄─███─██▄─██─▄▄▄██─██─██\n\
▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▄▀▀\n' + Style.RESET_ALL)

# Getting GPU Information from Registry
def get_gpu_info():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}")
        subkey_count, _, _ = winreg.QueryInfoKey(key)
        for i in range(subkey_count):
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)
            gpu_name = winreg.QueryValueEx(subkey, "DriverDesc")[0]
            if "NVIDIA" in gpu_name or "AMD" in gpu_name or "Intel" in gpu_name or "Radeon" in gpu_name or "GTX" in gpu_name or "RTX" in gpu_name:
                return gpu_name
    except Exception as e:
        print(f"Error getting GPU information: {e}")
        return None

# Determining whether or not you can use Aimmy with your current GPU
gpu_info = get_gpu_info()
if gpu_info:
    print_slow(Fore.LIGHTBLUE_EX + "GPU: " + gpu_info + Fore.LIGHTRED_EX), print ('\n')
    if "NVIDIA" in gpu_info and ("RTX" in gpu_info):
        print_slow(Fore.LIGHTGREEN_EX + "Aimmy should work well for you!")
    elif "NVIDIA" in gpu_info and ("TX" in gpu_info):
        print_slow(Fore.LIGHTYELLOW_EX +"May work great or not")
    elif "NVIDIA"in gpu_info and ("GT" in gpu_info):
        print_slow(Fore.RED + "Aimmy will not work for you.")
    elif "NVIDIA" in gpu_info and ("MX" in gpu_info):
        print_slow(Fore.YELLOW + "Aimmy will most likely not work for you or will be bad")
    if "AMD" in gpu_info or "Radeon" in gpu_info and ("XT" in gpu_info):
        print_slow(Fore.LIGHTGREEN_EX + "Aimmy should work well for you!")
    elif "AMD" in gpu_info and ("VEGA" in gpu_info):
        print_slow(Fore.LIGHTRED_EX + "Aimmy will most likely not work for you")
    elif "AMD" in gpu_info or "Radeon" in gpu_info and ("RX" in gpu_info):
        print_slow(Fore.LIGHTGREEN_EX + "If it's above a 560 you should be good.")
    elif "AMD" in gpu_info and ("R9" in gpu_info):
        print_slow(Fore.LIGHTBLACK_EX + "You'll be good")
    if "Intel" in gpu_info and ("UHD" in gpu_info):
        print_slow(Fore.RED + "Aimmy will not work for you.")
    elif "Intel" in gpu_info and ("HD" in gpu_info):
        print_slow(Fore.RED + "Aimmy will not work for you.")
    elif "Intel" in gpu_info and ("Arc" in gpu_info):
        print_slow(Fore.YELLOW +"May or may not work")
    elif "Intel" in gpu_info and ("Iris" in gpu_info):
        print_slow(Fore.RED + "Aimmy will not work for you")

# Trolling and Additional Information
print_slow(Fore.CYAN + "\n\nIf you have more than one GPU, make sure to specify that Aimmy uses your dedicated one.\nAlso if you got a blank message with no information please dm blazfmy on Discord.")
time.sleep(120)
print_slow("\nWhy are you still here??"), time.sleep(2000)
print_slow("\nDawg close the damn terminal!"), time.sleep(300)
