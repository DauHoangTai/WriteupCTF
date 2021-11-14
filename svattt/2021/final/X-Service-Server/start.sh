#!/bin/bash

echo KEY=`python3 -c "import uuid;import hashlib;print(hashlib.md5(uuid.uuid4().hex.encode()).hexdigest())"` > .env
rm flag*
echo ASCIS2021{`cat /proc/sys/kernel/random/uuid | sed 's/[-]//g' | head -c 40`} > flag_`cat /proc/sys/kernel/random/uuid | sed 's/[-]//g' | head -c 20;`

docker-compose up -d --build