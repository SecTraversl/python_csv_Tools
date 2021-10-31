# %%
#######################################
def import_csv(csv_file: str):
    """Reads a given csv file and returns a list of lists with each list corresponding to the row in the .csv file.

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
        csv_file (str): Reference a .csv file
    """
    import csv
#
    results_list = []
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f)
        # line_count = 0
        for row in csv_reader:
            results_list.append(row)
#
    return results_list

