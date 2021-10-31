# %%
#######################################
def export_csv_multiline_string(multiline_string: str, output_file: str):
    """Writes a given multiline string as a .csv file.

    Examples:
        >>> manystring = '''
        ... bob, 21, janitor, sanitization team, 02
        ... alice, 22, secretary, admin team, 03
        ... chuck, 23, plumber, construction team, 04
        ... '''
        >>> 
        >>> export_csv_multiline_string(manystring, 'mytest.csv')\n
        >>> import os\n
        >>> [file for file in os.listdir() if file.startswith('my')]\n
        ['mytest.csv']
        >>> 
        >>> import_csv('mytest.csv')\n
        [['bob', ' 21', ' janitor', ' sanitization team', ' 02'], ['alice', ' 22', ' secretary', ' admin team', ' 03'], ['chuck', ' 23', ' plumber', ' construction team', ' 04']]

    References:
        https://realpython.com/python-csv/

    Args:
        multiline_string (str): Reference a multiline string
        output_file (str): Reference a file name for the new .csv file
    """
    import csv
#   
    prep_work = [line.split(',') for line in multiline_string.strip().splitlines()]
#   
    with open(output_file, 'w') as f:
        csv_writer = csv.writer(f)
        [csv_writer.writerow(line) for line in prep_work]


