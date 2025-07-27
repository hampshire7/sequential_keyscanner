import os
from utils import int_to_bytes, bytes_to_hex, get_checkpoint
from fastecdsa.curve import secp256k1
from fastecdsa.point import Point

def scan_slice(worker_id, start_hex, stop_hex, target_pubkey, st=None):
    start = int(start_hex, 16)
    stop  = int(stop_hex, 16)
    checkpoint = get_checkpoint(worker_id)
    if checkpoint:
        start = checkpoint + 1

    G = secp256k1.G
    step = 1_000
    for k in range(start, stop):
        if k % step == 0:
            with open(f"worker_{worker_id}_checkpoint.txt", "w") as f:
                f.write(str(k))
            if st: st.write(f"Worker {worker_id} at {hex(k)}")

        P = k * G
        pubkey_bytes = b'\x02' + int_to_bytes(P.x, 32) if P.y % 2 == 0 else b'\x03' + int_to_bytes(P.x, 32)
        if bytes_to_hex(pubkey_bytes) == target_pubkey.lower():
            return hex(k)

    return None
