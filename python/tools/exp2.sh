#!/usr/bin/expect
set timeout 30
spawn ssh -l root 192.168.59.128
expect "*password*"
send "abcd1234\r"
interact
