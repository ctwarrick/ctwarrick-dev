#!/usr/bin/env bash
# scripts/validate-infra.sh — local compile-check for infra/main.bicep +
# infra/main.bicepparam.
#
# Why: catches param/command-shape mismatches (e.g. a missing/unused param —
# BCP258) before a real deploy. Requires only the Bicep CLI (bundled with the
# Azure CLI); no Azure login or subscription access needed.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

az bicep build-params --file infra/main.bicepparam
