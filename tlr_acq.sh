#!/bin/bash
# Put tlr_data.py full path.
# nohup will run script on background, all output and error prompt will redirected to /dev/null
# Script by: Tejo
# Modified by: Indra Rudianto

source /home/merapi/Projects/venv3/bin/activate
python3 /home/merapi/Projects/tlr/tlr_data.py &
