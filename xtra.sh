#!/bin/bash

if [ -d "./xml_projects" ]
then
    echo 'Saving files to ./xml_projects'
else
    mkdir xml_projects &&
    echo 'Saving files to ./xml_projects'
fi
