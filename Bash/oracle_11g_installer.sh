#!/bin/bash

echo -e "Installing Oracle 11g XE..."


# unzip oracle-xe-11.2.0-1.0.x86_64.rpm.zip
# sudo apt-get install alien libaio1 unixodbc
# sudo alien --scripts -d oracle-*.rpm
# sudo alien -i --scripts oracle-*.rpm

echo -e "ALien..."
sudo touch /sbin/chkconfig
echo -e "Config creation success..."
echo '
#!/bin/bash
# Oracle 11gR2 XE installer chkconfig hack for Ubuntu
file=/etc/init.d/oracle-xe
if [[ ! `tail -n1 $file | grep INIT` ]]; then
    echo >> $file
    echo "### BEGIN INIT INFO" >> $file
    echo "# Provides: OracleXE" >> $file
    echo "# Required-Start: $remote_fs $syslog" >> $file
    echo "# Required-Stop: $remote_fs $syslog" >> $file
    echo "# Default-Start: 2 3 4 5" >> $file
    echo "# Default-Stop: 0 1 6" >> $file
    echo "# Short-Description: Oracle 11g Express Edition" >> $file
    echo "### END INIT INFO" >> $file
fi
update-rc.d oracle-xe defaults 80 01' | sudo tee /sbin/chkconfig


echo -e "Done!"
sudo chmod 755 /sbin/chkconfig

echo -e "Changing Kernel Parameters..."
echo "# Oracle 11g XE kernel parameters
fs.file-max=6815744
net.ipv4.ip_local_port_range=9000 65000
kernel.sem=250 32000 100 128
kernel.shmmax=536870912" | sudo tee /etc/sysctl.d/60-oracle.conf

sudo service procps start

echo -e "Kinda rebooting..."
sudo sysctl -q fs.file-max

echo -e "Writing loader script..."

echo "#!/bin/sh
case '$1' in
start)
    mkdir /var/lock/subsys 2>/dev/null
    touch /var/lock/subsys/listener
    rm /dev/shm 2>/dev/null
    mkdir /dev/shm 2>/dev/null
*)
    echo error
    exit 1
    ;;
esac" | sudo tee /etc/rc2.d/S01shm_load

sudo chmod 755 /etc/rc2.d/S01shm_load

sudo ln -s /usr/bin/awk /bin/awk
sudo mkdir /var/lock/subsys
sudo touch /var/lock/subsys/listener

sysctl -p /etc/sysctl.d/60-oracle.conf

sudo dpkg --install oracle-xe_11.2.0-2_amd64.deb
sudo /etc/init.d/oracle-xe configure

echo "export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
export ORACLE_SID=XE
export NLS_LANG=`$ORACLE_HOME/bin/nls_lang.sh`
export ORACLE_BASE=/u01/app/oracle
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$ORACLE_HOME/bin:$PATH" | sudo tee -a ~/.bashrc

source ~/.bashrc

sudo service oracle-xe start

sudo usermod -a -G dba $USER
