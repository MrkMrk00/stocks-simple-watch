#!/usr/bin/env bash

parallel -j0 --lb ::: 'pnpm dev' 'python -m uvicorn asgi:app --port 3000 --reload'

