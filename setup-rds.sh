#1/bin/bash

set -eu

sudo yum localinstall -y https://dev.mysql.com/get/mysql80-community-release-el7-2.noarch.rpm
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
sudo yum update
sudo yum install -y mysql-community-client