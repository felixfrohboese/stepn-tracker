#!/bin/bash
for (( ; ; ))
do
  python3 ingest_cmc_data.py
  python3 pause_5sec.py
  python3 transform_cmc_data.py
  python3 pause_55sec.py
done
