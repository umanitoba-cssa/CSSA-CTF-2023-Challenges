#!/bin/sh
# Add your startup script

bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
