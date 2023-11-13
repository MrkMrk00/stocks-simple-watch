#!/usr/bin/env bash

export WATCHFILES_IGNORE_PERMISSION_DENIED=true
export DB_DSN="dbname=stocks user=postgres password=strongpassword host=0.0.0.0"

parallel -j0 --lb ::: 'pnpm dev' 'python -m uvicorn asgi:app --port 3000 --reload'

