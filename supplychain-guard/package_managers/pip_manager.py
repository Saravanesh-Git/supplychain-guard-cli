# - Run pip dry-run
# - Generate dependency report
# - Parse package names and versions
# - Return normalized dependency list

import subprocess, sys, json

def parse_pip_dependencies(real_args, action):
    print(real_args)
    cmd = [
        sys.executable,
        "-m",
        "pip",
        action,
        *real_args,
        "--dry-run",
        "--ignore-installed",
        "--report",
        "-",
        "--quiet",
        "--disable-pip-version-check"
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"pip resolve failed:\n{result.stderr.strip()}"
            )

        if not result.stdout.strip():
            raise RuntimeError("pip did not return a JSON report.")
        
        report = json.loads(result.stdout)
        packages = []

        for item in report.get("install", []):
            metadata = item.get("metadata", {})

            name = metadata.get("name")
            version = metadata.get("version")

            if not name or not version:
                continue

            packages.append({
                "ecosystem": "PyPI",
                "name": name,
                "version": version,
                "direct": item.get("requested", False),
            })

        return packages
    except json.JSONDecodeError:
        raise RuntimeError(
            f"Failed to parse pip JSON report.\nOutput was:\n{result.stdout}"
        )