import datetime
import os

LOG_FILE = "DAILY_LOG.md"

def main():
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")

    # Check if the entry already exists
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            content = f.read()
            if f"| {date_str} |" in content:
                print(f"Entry for {date_str} already exists.")
                return

    with open(LOG_FILE, "a") as f:
        f.write(f"| {date_str} | Checked |\n")

    print(f"Added entry for {date_str}.")

if __name__ == "__main__":
    main()
