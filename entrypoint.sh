#!/bin/sh
FROM python:3.9-alpine

RUN pip install --upgrade pip
RUN pip install zipfile
RUN python run.py $1
