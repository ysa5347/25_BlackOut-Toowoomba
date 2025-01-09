#!/bin/bash
cd /25_BlackOut-Toowoomba/backend
echo $DB_CONNECTION_ENV > .env
uvicorn main:app --reload