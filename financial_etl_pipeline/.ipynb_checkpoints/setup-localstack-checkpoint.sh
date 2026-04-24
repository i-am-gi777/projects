#!/bin/bash
echo "🚀 Setting up LocalStack AWS environment..."

# Wait for services
sleep 20

# Create S3 bucket
aws --endpoint-url=http://localhost:4566 s3 mb s3://financial-ledger-bucket --region us-east-1

# Upload raw data
aws --endpoint-url=http://localhost:4566 s3 cp data/sales.csv s3://financial-ledger-bucket/raw/sales/
aws --endpoint-url=http://localhost:4566 s3 cp data/tax.csv s3://financial-ledger-bucket/raw/tax/

# Create bucket structure
aws --endpoint-url=http://localhost:4566 s3api put-object --bucket financial-ledger-bucket --key processed/consolidated/

echo "✅ S3 bucket 'financial-ledger-bucket' ready with sample data!"
echo "📁 Raw data uploaded to: s3://financial-ledger-bucket/raw/"
