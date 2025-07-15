#!/bin/bash
set -e

BACKUP_FILE="$1"
DB_NAME="dwh_db"
DB_USER="dwh_user"

if [ -z "$BACKUP_FILE" ]; then
  echo "Usage: $0 <backup_file.sql>"
  exit 1
fi

if [ ! -f "$BACKUP_FILE" ]; then
  echo "Backup file does not exist: $BACKUP_FILE"
  exit 1
fi

echo "Restoring PostgreSQL database $DB_NAME from $BACKUP_FILE..."
psql -U "$DB_USER" -d "$DB_NAME" < "$BACKUP_FILE"
echo "Database restored from: $BACKUP_FILE"

# usage:
# ./restore_db.sh /srv/build2teach/dev-tools/backups/db_2025-07-15_10-00-00.sql
