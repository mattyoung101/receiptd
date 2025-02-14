#!/usr/bin/env python3
import argparse
import subprocess
import socket
import tempfile
import shlex
from datetime import datetime
from typing import Optional

# Name of the receipt printer to use
PRINTER = "EPSON"


def do_print(name: str, status: str, log: str, hostname: Optional[str] = None):
    if status not in ["ok", "fail"]:
        raise RuntimeError(f"Invalid status: {status}. Acceptable: 'ok', 'fail'")

    if hostname is None:
        hostname = socket.gethostname().upper()
    else:
        # ensure uppercase
        hostname = hostname.upper()

    display_status = "NOMINAL" if status == "ok" else "FAILURE"
    time = datetime.now().strftime("%d/%m/%Y %I:%M %p").upper()

    with tempfile.NamedTemporaryFile("wb", delete=False, prefix="receiptd_", suffix=".pdf") as f:
        command = (f"typst compile --input name=\"{name.upper()}\" --input "
                   f"status=\"{display_status}\" --input hostname=\"{hostname}\" --input time=\"{time}\" "
                   f"--input log=\"{log.upper()}\" receipt.typ {f.name}")
        print(f"Writing to {f.name}")
        print(f"Command: {command}")
        print(f"Command split: {shlex.split(command)}")

        # compile with typst
        subprocess.check_call(shlex.split(command))

        # now print it!
        subprocess.check_call(["lpr", "-P", PRINTER, str(f.name)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name of the job that ran")
    parser.add_argument("status", help="Status of the job, either 'ok' or 'fail'")
    parser.add_argument("log", help="Log file of the job") # FIXME this should really be path to log
    args = parser.parse_args()

    do_print(args.name, args.status, args.log)
