# Build2Teach Dev Tools

This folder contains operational scripts for managing the test/production server.

## Scripts

- `backup_db.sh` – Backup current Postgres database.
- `restore_db.sh` – Restore a previous Postgres database backup.
- `clear_old_logs.sh` – Clean up Docker logs and unused images and remove log file.
- `apt_update_upgrade.sh` – Update and upgrade Ubuntu packages.
- `daily_healthcheck.py` – Check if Docker is running, app is up, logs disk usage.

## Usage

Make all scripts executable:

```bash
chmod +x backup_db.sh restore_db.sh clear_old_logs.sh apt_update_upgrade.sh daily_healthcheck.py
```

Example cron job to run system update weekly (every Sunday at 2am):

```bash
0 2 * * 0 /home/lien/dev/DWCraft/ops-scripts/apt_update_upgrade.sh >> /var/log/apt_update_upgrade.log 2>&1
```

## Planned for Production

- Prometheus + Grafana setup (metrics/monitoring).
- PostgreSQL migration.
- Automated cron tasks.
