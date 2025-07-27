def split_range(start_hex, stop_hex, num_slices):
    start = int(start_hex, 16)
    stop  = int(stop_hex, 16)
    step = (stop - start + 1) // num_slices
    return [(hex(start + i * step), hex(start + (i + 1) * step - 1)) for i in range(num_slices)]

def int_to_bytes(val, length):
    return val.to_bytes(length, 'big')

def bytes_to_hex(b):
    return b.hex()

def get_checkpoint(worker_id):
    try:
        with open(f"worker_{worker_id}_checkpoint.txt", "r") as f:
            return int(f.read().strip())
    except:
        return None
