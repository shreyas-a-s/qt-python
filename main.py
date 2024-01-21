#!/usr/bin/env python3

import subprocess
import sys
import os

# Run WelcomeDialog.py
subprocess.run(["python3", "WelcomeDialog.py"])

# Check for the existence of the exit signal file
if os.path.exists("exit_signal.tmp"):
    print("Exiting main.py as per user's request.")
    os.remove("exit_signal.tmp")  # Remove the signal file
    sys.exit()

subprocess.run(["python3", "DBCreds.py"])

