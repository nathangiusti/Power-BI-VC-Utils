#!/bin/sh
FROM python:3.9-alpine
pip install --upgrade pip
pip install zipfile
python run.py $1
