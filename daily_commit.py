import subprocess
import random
import os
from datetime import datetime
import uuid

FILENAME = "daily_commit.txt"
COMMIT_MESSAGES = [
    "Refactored for future-proofing",
    "Daily grind begins",
    "Added legacy support for dinosaurs",
    "Optimised coffee consumption",
    "Deleted 400 lines of bad code",
    "Moved a div, felt alive",
    "This one’s for the green square",
    "Refactored the refactor",
    "Commented out the chaos",
    "Ctrl+C, Ctrl+V excellence"
]

# Generate a guaranteed-unique line using a UUID
unique_line = f"# Commit made at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} – {uuid.uuid4()}"

# Append the line to the tracked file
with open(FILENAME, "a") as f:
    f.write(unique_line + "\n")

# Git add and commit
subprocess.run(["git", "add", FILENAME], check=True)
commit_msg = random.choice(COMMIT_MESSAGES)
subprocess.run(["git", "commit", "-m", commit_msg], check=True)

# Git push using GitHub token
token = os.environ.get("GITHUB_TOKEN")
repo = os.environ.get("GITHUB_REPOSITORY")
subprocess.run([
    "git", "push", f"https://x-access-token:{token}@github.com/{repo}.git"
], check=True)

print(f"✅ Committed with message: '{commit_msg}'")