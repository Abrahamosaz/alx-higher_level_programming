#!/bin/bash
# send a http reques to the url and display the response
curl -Is "$1" | grep "Content-Length" | cut -d" " -f2
