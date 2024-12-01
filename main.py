import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
NUM_COMMITS = 100  # Total number of commits to generate
COMMIT_MESSAGES = [
    "Refactor code for better readability",
    "Fix bug in data processing pipeline",
    "Update documentation and README",
    "Add unit tests for core modules",
    "Optimize database queries",
    "Improve error handling",
    "Add new feature to user interface",
    "Remove deprecated functions",
    "Update dependencies",
    "Improve performance of data processing",
]
FILE_NAMES = [
    "feature.py",
    "bugfix.py",
    "README.md",
    "utils.py",
    "database.sql",
    "config.yaml",
    "test_module.py",
    "main.py",
    "setup.py",
    "requirements.txt"
]

def random_date():
    """Generate a random datetime within the past year."""
    now = datetime.now()
    past_year = now - timedelta(days=365)
    random_days = random.randint(0, 365)
    random_seconds = random.randint(0, 86400)
    return past_year + timedelta(days=random_days, seconds=random_seconds)

def make_commit(commit_message, commit_date, file_name):
    """Make a git commit with a specific message, date, and file."""
    with open(file_name, "a") as f:
        f.write(f"{commit_date}: {commit_message}\n")

    # Set the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str

    subprocess.run(["git", "add", file_name], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True, env=env)

def main():
    # Generate multiple commits per day
    for _ in range(NUM_COMMITS):
        commit_message = random.choice(COMMIT_MESSAGES)
        commit_date = random_date()
        file_name = random.choice(FILE_NAMES)
        make_commit(commit_message, commit_date, file_name)

    print(f"{NUM_COMMITS} random commits created over the past year across multiple files.")

if __name__ == "__main__":
    main()

2024-02-26 10:22:52.831260: Fix bug in data processing pipeline
2024-11-19 22:35:00.989594: Update dependencies
2024-07-30 12:34:01.011951: Improve error handling
2024-11-04 08:58:36.033712: Optimize database queries
2024-04-30 06:57:58.041010: Fix bug in data processing pipeline
2024-10-07 06:09:48.235303: Remove deprecated functions
2024-12-01 06:54:03.463128: Remove deprecated functions
