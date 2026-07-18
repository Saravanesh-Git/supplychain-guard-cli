# - Read command
# - Detect package manager
# - Call pip_manager or npm_manager
# - Call scanner
# - Show report
# - Ask proceed/cancel

import sys, subprocess
from package_managers.pip_manager import parse_pip_dependencies
from package_managers.npm_manager import parse_npm_dependencies

def main():
    args = sys.argv[1:]
    
    if not args:
        print("Usage: supplyguard <package manager> install <package>")
        return
    
    manager = args[0]
    action = args[1]
    real_args = args[2:]

    print(f"Scanning command: {manager} {action} {' '.join(real_args)}")

    if manager == 'pip' and action == 'install':
        report = parse_pip_dependencies(real_args, action)

    elif manager == 'npm' and action == 'install':
        report = parse_npm_dependencies(real_args, action)

    print(report)
    
if __name__ == "__main__":
    main()
