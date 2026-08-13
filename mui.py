from beam import function
import subprocess
from pathlib import Path


@function(name="shell-test")
def momo():
    script = Path(__file__).parent / "script.sh"

    print("Script path:", script)
    print("Script exists:", script.exists())

    if not script.exists():
        raise FileNotFoundError(f"script.sh tidak ditemukan: {script}")

    result = subprocess.run(
        ["bash", str(script)],
        capture_output=True,
        text=True,
        check=True,
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return {
        "status": "success",
        "output": result.stdout,
    }
