#!/bin/bash

# Minimal deployment script for Akash CLI

# CONFIGURE THIS
export AKASH_KEY_NAME="your-key"
export AKASH_ACCOUNT_ADDRESS="akash1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export AKASH_NODE="https://rpc-akash.pupmos.network:443"

# Generate cert only once per account (optional)
# provider-services tx cert generate client -from $AKASH_KEY_NAME
# provider-services tx cert publish client -from $AKASH_KEY_NAME

# 1. Create deployment
provider-services tx deployment create deploy.yaml -from $AKASH_KEY_NAME

# 2. Get DSEQ
read -p "Paste DSEQ from above output: " AKASH_DSEQ

# 3. Query available bids
provider-services query market bid list -owner=$AKASH_ACCOUNT_ADDRESS -node $AKASH_NODE -dseq $AKASH_DSEQ -state=open

# 4. Choose provider
read -p "Enter your chosen AKASH_PROVIDER: " AKASH_PROVIDER

# 5. Create lease
provider-services tx market lease create -dseq $AKASH_DSEQ -provider $AKASH_PROVIDER -from $AKASH_KEY_NAME

# 6. Upload manifest
provider-services send-manifest deploy.yaml -dseq $AKASH_DSEQ -provider $AKASH_PROVIDER -from $AKASH_KEY_NAME

# 7. Confirm lease and app URL
provider-services lease-status -dseq $AKASH_DSEQ -from $AKASH_KEY_NAME -provider $AKASH_PROVIDER
