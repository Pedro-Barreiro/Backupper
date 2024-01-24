# Directory Backupper

This script is used to backup a directory at regular intervals. It uses Python's built-in `shutil`, `time` and `argparse` modules.

## Description

The script takes three command line arguments: the source directory to backup, the destination directory for the backups, and the number of hours between backups. It creates a timestamped backup of the source directory in the destination directory, then waits for the specified number of hours before creating the next backup.

## Usage

To use this script, you need to have Python installed on your machine. You can run the script from the command line like this:

```bash
python backupper.py "source_directory" "destination_directory" backup_interval_hours
```

example:

```bash
python backupper.py "C:\server\documents" "C:\Users\pedro\documents\serverBackups" 4
```
