#!/bin/bash
set -e

BACKUP_DIR="/srv/build2teach/dev-tools/backups"
DB_NAME="dwh_db"
DB_USER="dwh_user"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
mkdir -p "$BACKUP_DIR"

pg_dump -U "$DB_USER" "$DB_NAME" > "$BACKUP_DIR/db_$DATE.sql"
echo "Backup completed: $BACKUP_DIR/db_$DATE.sql"