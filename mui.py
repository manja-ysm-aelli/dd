from beam import function
import subprocess
from pathlib import Path

@function(name="shell-test")
def momo():
    script = Path(__file__).parent / "script.sh"

    print("Mencari:", script)
    print("Ada:", script.exists())

    subprocess.run(["bash", str(script)], check=True)

    return "Selesai"
