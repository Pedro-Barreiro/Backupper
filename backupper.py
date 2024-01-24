import shutil
import time
import argparse

def backup_directory(source_dir, destination_dir, interval_hours):
    while True:
        # Create a timestamped folder name for the backup
        timestamp = time.strftime("%Y%m%d%H%M%S")
        backup_dir = f"{destination_dir}/backup_{timestamp}"

        # Copy the contents of the source directory to the backup directory
        shutil.copytree(source_dir, backup_dir)

        # Wait for the specified interval before creating the next backup
        time.sleep(interval_hours * 3600)

# Create the parser
parser = argparse.ArgumentParser(description="Backup a directory at regular intervals")

# Add the arguments
parser.add_argument("source_directory", type=str, help="The source directory to backup")
parser.add_argument("destination_directory", type=str, help="The destination directory for the backups")
parser.add_argument("backup_interval_hours", type=int, help="The number of hours between backups")

# Parse the arguments
args = parser.parse_args()

# Call the backup_directory function with the parsed arguments
backup_directory(args.source_directory, args.destination_directory, args.backup_interval_hours)
