#!/bin/bash
# display all http methods that the server support
curl -si -X "OPTIONS" "$1" | grep "Allow" | cut -d" " -f2-
