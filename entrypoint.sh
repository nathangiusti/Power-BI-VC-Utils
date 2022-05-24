#!/bin/sh
python pip --no-cache-dir install zipfile
python /scripts/deserialize_pbix.py "$1" $2
