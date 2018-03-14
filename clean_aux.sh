#! /usr/bin/bash

find -name  'build' | xargs rm -rf

if [ $? -eq 0 ]
then
    echo "Cleaned LaTeX build folders successfully"
fi
