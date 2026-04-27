import platform
import os
import datetime 
import shutil
import sys
from colorama import Fore, Style, init
import pyfiglet 

init()

print(Fore.CYAN + pyfiglet.figlet_format("PyOS") + Style.RESET_ALL)
print(Fore.YELLOW + "Made By Dhawal Bansod." + Style.RESET_ALL)
print()
print()
device_name = platform.node()
print(Fore.YELLOW + "The CLI(Command Line Interface)" + Style.RESET_ALL)
print(Fore.YELLOW + "Type 'help' to get the list of commands." + Style.RESET_ALL)
print()
print()
while True:
    try:
        prompt = (
            Fore.GREEN + "PyOS" + Style.RESET_ALL +
            Fore.WHITE + "@" +
            Fore.CYAN + device_name +Style.RESET_ALL +
            Fore.WHITE + ":" +
            Fore.YELLOW + os.getcwd() + Style.RESET_ALL +
            "$ "
        )
        raw_command = input(prompt)
        command = raw_command.strip().lower()
    
        if command=="help":
            print(Fore.MAGENTA + "\n=== COMMAND ===" + Style.RESET_ALL)
            print("help - Show this help message")
            print()
            print("exit - Exit the CLI")
            print()
            print("clear - Clear the screen")
            print()
            print("version - Show the version of the CLI")
            print()
            print("about - Show information about the CLI")
            print()
            print("calculator or calc - Open the calculator application")
            print()
            print("open [app_name] - Open a specific application (e.g., open notepad)")
            print()
            print("time - Show the current time")
            print()
            print("date - Show the current date")
            print()
            print("echo [message] - Print a message")
            print()
            print("systeminfo - Show system information")
            print()
            print("cd [path] - Change the current directory")
            print()
            print("ls - This command gives the list of files in directory")
            print()
            print("pwd - Show the current directory")
            print()
            print("cls - Clear the screen")
            print()
            print("files - Show the list of files in the current directory")
            print()
            print("run [command] - Run the command you given")
            print()
            print("mkdir [folder name] - This make a folder in your existing directory")
            print()
            print("rmdir [folder name] - This deletes the folder from your device")
            print()
            print("delete [file name] - This command deletes file")
            print()
            print("write [file name] [text] - This command writes in your file")
            print()
            print("append [file name] [text] - This command appends the text in file")
            print()
            print("rename [file name] [renamed file] - This command rename your file")
            print()
            print("copy [object] [location] - This command is used to copy the object to the given location")
            print()
            print("move [object] [location] - This command used to move object on the given location")
            print()
            print("search [file name] - This command is used to find the file in the directory")
            print()
            print("ip - This command is used to get info of ip")
            print()
            print("battery - This command gives report of Battery")
            print()
            print("shutdown - This command shutdown the system")
            print()
            print("restart - This command is used to restart the system")
            print()
            print("lock - This command lock the system")
            print()
            print("wlan - This command shows saved network and their info (only for Windows)")
            print()
        elif command=="exit":
            print(Fore.YELLOW + "Exiting the CLI..." + Style.RESET_ALL)
            sys.exit()
        elif command in ["clear","cls"]:
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command=="version":
            print("CLI Version 2.0.0")
        elif command=="about":
            print("This is a simple CLI built using Python. It is designed to be a basic command line interface for users to interact with their device.")
        elif command in ["calculator","calc"]:
            os.system('calc')
        elif command.startswith("open "):
            try:
                app_name = raw_command[5:].strip()
                os.startfile(app_name)
            except Exception:
                print(Fore.RED + f"Failed to open {app_name}. Please make sure the application name is correct." + Style.RESET_ALL)
        elif command=="time":
            print(datetime.datetime.now())
        elif command=="date":
            print(datetime.date.today())
        elif command.startswith("echo "):
            print(raw_command[5:])
        elif command=="systeminfo":
            print("System: ",platform.system())
            print("Node: ",platform.node())
            print("Release: ",platform.release())
            print("Version: ",platform.version())
            print("Architecture: ",platform.architecture())
            print("Machine: ",platform.machine())
            print("Processor: ",platform.processor())   
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
            except:
                print("Failed to change directory. Please make sure the path is correct.") 
        elif command in ["ls","files"]:
            for f in os.listdir():
                if os.path.isdir(f):
                    print(Fore.BLUE + f + Style.RESET_ALL)
                else:
                    print(f)
        elif command == "pwd":
            print(os.getcwd())  
        elif command.startswith("run "):
            cmd = raw_command[4:]
            os.system(cmd)
        elif command.startswith("mkdir "):
            name = raw_command[6:]
            try:
                os.mkdir(name)
                print(Fore.GREEN + "Folder created" + Style.RESET_ALL)
            except:
                print(Fore.RED + "Failed to create folder" + Style.RESET_ALL)
        elif command.startswith("rmdir "):
            name = raw_command[6:]
            try:
                shutil.rmtree(raw_command[6:].strip())
                print(Fore.GREEN + "Folder deleted" + Style.RESET_ALL)
            except:
                print(Fore.RED + "Failed to delete folder" + Style.RESET_ALL)
        elif command.startswith("delete "):
            name = raw_command[7:]
            confirm = input(f"Delete {name}? (y/n): ")
            if confirm.lower() == "y":
                try:
                    os.remove(name)
                    print(Fore.GREEN + "File deleted" + Style.RESET_ALL)
                except:
                    print(Fore.RED + "File not found" + Style.RESET_ALL)
        elif command.startswith("write "):
            try:
                parts = raw_command.split(" ",2)
                filename = parts[1]
                text = parts[2]

                with open(filename,"w") as f:
                    f.write(text)
                print(Fore.GREEN + "Written successfully" + Style.RESET_ALL)
            except:
                print("Usage: write filename text")
        elif command.startswith("append "):
            try:
                parts = raw_command.split(" ", 2)
                filename = parts[1]
                text = parts[2]

                with open(filename, "a") as f:
                    f.write("\n" + text)

                print(Fore.GREEN + "Appended successfully" + Style.RESET_ALL)
            except:
                print("Usage: append filename text")  
        elif command.startswith("rename "):
            try:
                parts = raw_command.split(" ",2)
                os.rename(parts[1], parts[2])
                print(Fore.GREEN + "Renamed successfully" + Style.RESET_ALL)
            except:
                print("Usage: rename old new")
        elif command.startswith("copy "):
            try:
                parts = raw_command.split(" ",2)
                shutil.copy(parts[1], parts[2])
                print(Fore.GREEN + "Copied successfully" + Style.RESET_ALL)
            except:
                print("Usage: copy source destination")
        elif command.startswith("move "):
            try:
                parts = raw_command.split(" ",2)
                shutil.move(parts[1], parts[2])
                print(Fore.GREEN + "Moved successfully" + Style.RESET_ALL)
            except:
                print("Usage: move source destination")
        elif command.startswith("search "):
            name = raw_command[7:]
            for file in os.listdir():
                if name in file:
                    print(file)
        elif command=="ip":
            os.system("ipconfig")
        elif command=="battery":
            os.system("powercfg /batteryreport")
            print("Battery report generated")
        elif command=="shutdown":
            if input("Are you sure? (y/n): ").lower()=="y":
                os.system("shutdown /s /t 0")
        elif command=="restart":
            if input("Are you sure? (y/n): ").lower()=="y":
                os.system("shutdown /r /t 0")
        elif command=="lock":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif command=="wlan":
            os.system("netsh wlan show profile")
            network = input("Enter the name of network shown above: ")
            os.system(f"netsh wlan show profile name=\"{network}\" key=clear")
        else:     
            print(Fore.RED + f"Unknown command: {command}. Type 'help'" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + "An error occurred. Please try again." + Style.RESET_ALL)