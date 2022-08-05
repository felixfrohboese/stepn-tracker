#!/bin/bash
python3 ingest_cmc_data.py

python3 pause.py

python3 transform_cmc_data.py

python3 pause.py
