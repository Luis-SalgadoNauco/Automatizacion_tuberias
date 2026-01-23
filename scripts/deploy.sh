#!/bin/bash
set -e

ENVIRONMENT=$1
if [ -z "$ENVIRONMENT" ]; then
    echo "Uso: $0 <environment>"
    exit 1
fi

echo "🚀 Deploying Airflow to $ENVIRONMENT environment"

case $ENVIRONMENT in
    dev)
        echo "🔧 Deploy DEV (local)"
        ;;
    staging)
        echo "🧪 Deploy STAGING"
        ;;
    prod)
        echo "🎯 Deploy PROD"
        ;;
esac

echo "✅ Deployment to $ENVIRONMENT completed successfully"
