#!/bin/bash
# Takes in a URL and sends a POST request and displays response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
