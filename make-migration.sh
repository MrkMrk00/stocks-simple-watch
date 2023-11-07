#!/usr/bin/env bash

[[ -z "$1" ]] || NAME="migration" && NAME="$1"

touch "migrations/$(date +'%Y-%m-%d')-${NAME}.sql"
echo "-- $(date +'%Y-%m-%d')-${NAME}" >> $NAME

