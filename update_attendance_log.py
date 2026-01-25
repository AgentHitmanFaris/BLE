import datetime
import random
import secrets
import os
import subprocess

ATTENDANCE_FILE = "Attendance.md"
OPERATIVES = [
    "Code: TUA-H",
    "Code: PER-AK",
    "Code: TER-AWIS",
    "Code: KIL-AU",
    "Code: JUN-A",
    "Code: BAH-AMAN",
    "Code: JAN-GGUT"
]

def get_current_branch():
    try:
        return subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()
    except Exception:
        return "unknown-branch"

def main():
    # Gather Data
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    operative_id = random.choice(OPERATIVES)
    branch = get_current_branch()
    commit = "PENDING"
    action_summary = "Routine security audit log update."
    classification = "[INFO: SYSTEM STABLE]"
    signature = secrets.token_hex(4) # 4 bytes = 8 hex chars

    # Prepare Line
    # | Timestamp | Operative ID | Branch | Commit | Action Summary | Classification | Signature |
    line = f"| {timestamp} | {operative_id} | {branch} | {commit} | {action_summary} | {classification} | {signature} |\n"

    # Write to File
    new_file = not os.path.exists(ATTENDANCE_FILE) or os.stat(ATTENDANCE_FILE).st_size == 0

    with open(ATTENDANCE_FILE, "a") as f:
        if new_file:
            f.write("--- [ RED TEAM OPERATIONAL ENGAGEMENT LOG ] ---\n")
            f.write("CONFIDENTIALITY LEVEL: INTERNAL // AUDIT ONLY\n\n")
            f.write("| Timestamp | Operative ID | Branch | Commit | Action Summary | Classification | Signature |\n")
            f.write("|---|---|---|---|---|---|---|\n")

        f.write(line)

    print(f"Updated {ATTENDANCE_FILE} with entry:")
    print(line.strip())

if __name__ == "__main__":
    main()
