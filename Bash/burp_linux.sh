#!/bin/bash

cat <"END"
    \# You need to download Oracle-JDK-8 First
    \# Otherwise this package may not work
END

install() {
    sudo mkdir -p /opt/jdk
    sudo cp -rf jdk-8* /opt/jdk/
    sudo tar -zxf /opt/jdk/jdk-8*.gz
    sudo rm /opt/jdk/jdk-8*.gz
    sudo cp -r jdk1.8.0_241/* .
    /opt/jdk/bin/java -jar burp-loader.jar &
    /opt/jdk/bin/java -noverify -Xbootclasspath/p:burp-loader.jar -jar burpsuite_pro_v2020.1.jar
}

if [[ $1 == 'i' ]]; then
    install
else
    /opt/jdk/bin/java -noverify -Xbootclasspath/p:burp-loader.jar -jar burpsuite_pro_v2020.1.jar > /dev/null
    # /opt/jdk/bin/java -noverify -Xbootclasspath/p:burp-loader.jar -jar burpsuite_pro_v2020.1.jar 2> $1
fi