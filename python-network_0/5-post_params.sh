#!/bin/bash
# Sends a POST request with specific variables (email and subject)
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
