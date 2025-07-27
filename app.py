import streamlit as st
from scanner import scan_slice
from utils import split_range

st.title("Sequential ECC Brute-Force Scanner")

target_pubkey = st.text_input("Target Compressed Public Key", "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16")
start_hex = "0x4000000000000000000000000000000000"
end_hex   = "0x7fffffffffffffffffffffffffffffffff"

if st.button("Start Scan"):
    st.write("Splitting range...")
    slices = split_range(start_hex, end_hex, 4)

    for i, (start, stop) in enumerate(slices):
        st.write(f"Worker {i}: Scanning {start} → {stop}")
        found_key = scan_slice(i, start, stop, target_pubkey, st)
        if found_key:
            st.success(f"Key found by worker {i}: {found_key}")
            break
    else:
        st.warning("Scan completed — no match found.")
