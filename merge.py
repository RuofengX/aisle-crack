#!/bin/python3
import glob
import logging as log
import os
log.basicConfig(level=log.DEBUG)
log.debug('-----DEBUG LEVEL LOG-----')

RESULTS_DIR = './results/full'
APS_FIlE = './APs.csv'
DEVICES_FILE = './Devices.csv'

log.info(f'Results directory is: {RESULTS_DIR}')

csv_files_list = glob.glob(f'{RESULTS_DIR}/*.csv')
log.debug(f'CSV file list is: {csv_files_list}')

ap_lines = []
devices_lines = []

for file in csv_files_list:
    with open(file, "r") as f:
        _lines = f.readlines()
        _ap_change_line = _lines.index('Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs\n')  # Index the device line
        ap_lines = ap_lines + _lines[1:_ap_change_line]
        devices_lines = devices_lines + _lines[_ap_change_line + 1:]
    os.remove(file)

with open(APS_FIlE, "a+") as f:
    log.info('Writing APS_FILE...')
    f.write(''.join(ap_lines))
with open(DEVICES_FILE, "a+") as f:
    log.info('Writing DEVICES_FILE...')
    f.write(''.join(devices_lines))