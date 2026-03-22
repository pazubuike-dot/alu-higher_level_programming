#!/bin/bash
# Sends a request to a URL and displays the size of the body in bytes
curl -sI "$1" | grep -i "Content-Length" | cut -d' ' -f2

