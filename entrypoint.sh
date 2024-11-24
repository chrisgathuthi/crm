#!/bin/bash
gunicorn core.wsgi:application --config gconfig.py