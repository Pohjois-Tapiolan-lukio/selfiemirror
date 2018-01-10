#/bin/bash

sudo pip3 install flask requests picamera
[[ $? == '0' ]] && echo -e "\nSUCCESS" || echo -e "\nFAIL"
