#!/bin/bash
# send a post request to the server
curl -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
