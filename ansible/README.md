# Ansible Infrastructure for Build2Teach

This folder contains the infrastructure-as-code (IaC) setup for deploying the Build2Teach Django project.

## Structure

- `inventory.ini`: Server inventory file.
- `playbooks/`: Main Ansible playbooks:
   - `server-setup.yml`: Install Docker & prepare server.
   - `deploy.yml`: Deploy the Django project.
- `roles/`: Modular tasks:
   - `docker/`: Docker installation tasks.
   - `app_deploy/`: Pull project from Git and run containers.
   - `common/`: (Optional) Shared system tasks.

## Usage

```bash
# Bootstrap server (Docker + user setup)
ansible-playbook -i inventory.ini playbooks/server-setup.yml

# Deploy Django app
ansible-playbook -i inventory.ini playbooks/deploy.yml
