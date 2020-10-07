#!/usr/bin/env bash

set -e -o pipefail -u

TOKEN=$(curl -d 'client_id=web' -d 'username=gh-content' -d "password=$AUTH_PASSWORD" -d 'grant_type=password' "$AUTH_URL" | jq .access_token --raw-output)

curl --request POST \
  --url "${API_URL}courses/update" \
  --header "authorization: Bearer $TOKEN" \
  --header 'content-length: 0'

