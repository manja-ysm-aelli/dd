from beam import function
from pathlib import Path
import os

@function(name="shell-test")
def momo():
    print("=== BEAM DEBUG ===")
    print("cwd:", os.getcwd())
    print("mui.py:", __file__)

    base = Path(__file__).parent
    print("base:", base)

    print("files:")
    for p in base.iterdir():
        print(" -", p)

    script = base / "script.sh"
    print("script path:", script)
    print("script exists:", script.exists())

    if not script.exists():
        raise FileNotFoundError(
            f"script.sh tidak ditemukan. Dicari di: {script}"
        )

    return "script.sh ditemukan"
