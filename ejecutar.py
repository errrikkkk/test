import os
import subprocess
from colorama import init, Fore

# Inicializar Colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')

def show_menu():
    clear_screen()
    print(Fore.CYAN + "██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗")
    print(Fore.CYAN + "██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗████╗ ████║██╔════╝")
    print(Fore.CYAN + "██║   ██║███████╗██║     ██║   ██║██████╔╝██╔████╔██║███████╗")
    print(Fore.CYAN + "╚██╗ ██╔╝╚════██║██║     ██║   ██║██╔══██╗██║╚██╔╝██║╚════██║")
    print(Fore.CYAN + " ╚████╔╝ ███████║███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║")
    print(Fore.CYAN + "  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    print(Fore.CYAN + "By erriiikkkk.")
    print("\nSeleccione una opción:")
    print("1. Escaneo de WiFi")
    print("2. Instalar todas los paquetes")
    print("0. Salir")

def scan_wifi():
    clear_screen()
    print(Fore.GREEN + "Escaneando redes WiFi...\n")
    try:
        # Ejecutar el comando wpa_cli para escanear redes WiFi
        output = subprocess.check_output(['wpa_cli', 'scan']).decode('utf-8')
        print(output)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Error: No se pudo escanear redes WiFi. ¿Tienes instalada la herramienta 'wpa_cli'?")
    input(Fore.WHITE + "\nPresione Enter para continuar...")

def otra_cosa():
    clear_screen()
    print("Haciendo otra cosa...")
    # Aquí puedes agregar tu lógica para la otra opción

def main():
    while True:
        show_menu()
        option = input("\nIngrese el número de opción deseada: ")

        if option == '1':
            scan_wifi()
        elif option == '2':
            otra_cosa()
        elif option == '0':
            print("Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
