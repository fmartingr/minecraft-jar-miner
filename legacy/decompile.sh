#!/bin/bash

# Jarfile
JARFILE=$1

if [ "$JARFILE" != "" ]; then
    echo "[] Preparing files from JAR: $JARFILE []"
    # Remove old
    rm -rf ./jarfile ./classes

    # Create directories
    mkdir jarfile
    mkdir classes

    # Decompress the jarfile into the jarfile folder
    echo "    Unpackaging jar file"
    unzip -qq $JARFILE -d ./jarfile

    # Find all the classes and pass then through JAD
    #find . -type d -name *.class -exec rm -rf {} \;
    echo "    Decompiling classes"
    ls ./jarfile/*.class | xargs -n1 ./tools/jad/jad -sjava -dclasses &> /dev/null

    # Remove classfiles and left only other files
    echo "    Cleaning"
    rm ./jarfile/*.class
else
    echo "[!] No jarfile specified!"
    exit -1
fi
