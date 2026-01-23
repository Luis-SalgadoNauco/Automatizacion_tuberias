#!/bin/bash
set -e

ENVIRONMENT=$1

if [ -z "$ENVIRONMENT" ]; then
    echo "Uso: $0 <environment>"
    echo "Environment: dev | staging | prod"
    exit 1
fi

echo "🚀 Deploying Airflow to $ENVIRONMENT"

echo "📋 Running tests..."
pytest tests/dags -v

case $ENVIRONMENT in
  dev)
    echo "🔧 Deploy DEV (local / docker-compose)"
    echo "⚠️  Aquí iría docker-compose.dev.yml"
    ;;
  staging)
    echo "🧪 Deploy STAGING"
    echo "⚠️  Aquí iría kubectl apply -f k8s/staging/"
    ;;
  prod)
    echo "🎯 Deploy PROD"
    echo "⚠️  Aquí iría kubectl apply -f k8s/prod/"
    ;;
  *)
    echo "❌ Environment inválido"
    exit 1
    ;;
esac

echo "✅ Deploy completado correctamente"
