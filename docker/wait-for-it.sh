#!/bin/bash

set -e

host="$1"
port="$2"
shift
cmd="$@"

until nc -z "$host" "$port" > /dev/null 2>&1; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
