#!/bin/bash
set -e

echo "💡 Attente de la base de données..."
# Attente simple (optionnel, pour éviter que la migration échoue si Postgres n'est pas prêt)
sleep 5

echo "📦 Exécution des migrations..."
python manage.py migrate

echo "🚀 Lancement de Daphne..."
exec "$@"
