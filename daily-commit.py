import os
import subprocess
import random
from datetime import datetime

# --- Configuration ---
FILENAME = "daily_commit.txt"
COMMIT_MESSAGES = [
    "Optimised synergy algorithm",
    "Refactored monolith into microservices",
    "Patched quantum entanglement bug",
    "Legacy migration done ✅",
    "Removed a semicolon, changed the world",
    "Daily hustle: #noDaysOff",
    "Production ready 🚀",
    "AI-assisted line break implemented",
    "Added meaningful whitespace",
    "Preparing for demo we’ll never have"
]

# --- Modify/Create file ---
with open(FILENAME, "a") as f:
    f.write(f"# Commit made on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# --- Git Add ---
subprocess.run(["git", "add", FILENAME], check=True)

# --- Git Commit with random message ---
commit_msg = random.choice(COMMIT_MESSAGES)
subprocess.run(["git", "commit", "-m", commit_msg], check=True)

# --- Git Push ---
subprocess.run(["git", "push"], check=True)

print(f"✅ Committed with message: '{commit_msg}'")