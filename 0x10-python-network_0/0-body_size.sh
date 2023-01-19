#!/bin/bash
# script that send a request to a URL and dislay the content-length
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2 
