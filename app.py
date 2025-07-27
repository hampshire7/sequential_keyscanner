import streamlit as st
from scanner import scan_slice
from utils import split_range

st.title("Sequential ECC Brute-Force Scanner")

target_pubkey = st.text_input("Target Compressed Public Key", "02cbb434aa7ae1700dcd15b20b17464817ec11715050e0fa192ffe9c29a673059f")
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
