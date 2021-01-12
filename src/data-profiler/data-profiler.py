import pandas as pd
import numpy as np
import sys
import os
import glob

# in bytes
MAX_FILE_SIZE = 1024 * 1024 * 1024

if __name__ == '__main__':

    input_folder = os.environ.get('CA_INPUT_FOLDER', '/mnt/input')
    output_folder = os.environ.get('CA_OUTPUT_FOLDER', '/mnt/output')
   
    if not os.path.isdir(input_folder):
        print(f'Input folder missing or invalid: {input_folder}')
        exit(1) 
    if not os.path.isdir(output_folder):
        print(f'Output folder missing or invalid: {output_folder}')
        exit(1)
    if not os.access(output_folder, os.W_OK):
        print(f'Output folder is not writeable: {output_folder}')
        exit(1)

    print(f'Input: {input_folder}')
    print(f'Output: {output_folder}')
   
    # for each csv file in the input_folder

    print(glob.glob(f'{input_folder}/*.csv'))

    for f in glob.glob(f'{input_folder}/*.csv'):
        # check if too large
        size = os.path.getsize(f)
        if size > MAX_FILE_SIZE:
            print(f'File to large: {f} ({size})')
        else:
            print(f'Processing: {f}')
                
            # get the basename 
            basename = os.path.basename(os.path.splitext(f)[0])

            # read in as a 
            df = pd.read_csv(f)
            
            # generate a summary of all the fields (numeric & others)   
            # transpose it so each field is a row
            all_summary = df.describe(include='all').transpose()
    
            # drop the 'top' column if present - for our short term purposes it causes too many problems
            if 'top' in all_summary.columns:
                all_summary = all_summary.drop(columns=['top']) 

            # write out to output_folder
            all_summary_path = f'{output_folder}/{basename}_summary.csv'

            # transpose needs a column name for the 'field_name' first column
            all_summary.to_csv(all_summary_path, index_label = 'field_name')

            print(f'Summary of fields: {all_summary_path}')
