import sys
import platform
import os

def get_system_info():
    print("System Information:")
    print(f"Python Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Processor: {platform.processor()}")
    
    # Check installed packages
    try:
        import pkg_resources
        print("\nInstalled Packages:")
        for package in pkg_resources.working_set:
            print(f"{package.key} == {package.version}")
    except ImportError:
        print("Could not list installed packages")

    # Check Python path
    print("\nPython Path:")
    for path in sys.path:
        print(path)

if __name__ == "__main__":
    get_system_info()