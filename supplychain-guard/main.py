# - Read command
# - Detect package manager
# - Call pip_manager or npm_manager
# - Call scanner
# - Show report
# - Ask proceed/cancel

import sys, subprocess
from package_managers.pip_manager import pip_dry_run

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: supplyguard <package manager> install <package>")
        return
    
    manager = args[0]
    real_args = args[1:]

    print(f"Scanning command: {manager} {' '.join(real_args)}")
    command = f"{manager} {' '.join(real_args)}"

    if manager == 'pip':
        pip_dry_run(command)

    elif manager == 'npm':
        pass

if __name__ == "__main__":
    main()
