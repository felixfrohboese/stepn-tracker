#!/bin/bash
for (( ; ; ))
do
  python3 ingest_cmc_data.py
  python3 pause_short.py
  python3 transform_cmc_data.py
  python3 pause_long.py
done
