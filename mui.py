from beam import function
import subprocess

@function(name="shell-test")
def momo():
    subprocess.run(
        ["bash", "-lc", """
            echo "Mulai..."
            date
            hostname
            pwd
            echo "Selesai."
        """],
        check=True,
    )
