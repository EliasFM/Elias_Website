#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env.sh
uv sync --no-dev --locked

# Convert static asset files
uv run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
uv run python manage.py migrate
