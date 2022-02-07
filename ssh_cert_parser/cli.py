import os
import sys
import json
import click
from .core import parse_from_file


@click.command()
@click.option('-f', '--file', 'file_location', help='File location', required=True)
@click.option('-j', '--json', 'json_output', help='Output as JSON', is_flag=True)
@click.option('-o', '--output', 'output_location', help='File location', required=False)
@click.option('--overwrite', 'overwrite', help='Overwrite output file', is_flag=True, default=False, required=False)
def router(file_location = None, json_output = False, output_location = None, overwrite = False):
    res = parse_from_file(file_location)
    if output_location is not None:
        if os.path.isfile(output_location) and not overwrite:
            print("File already exists. Use --overwrite to overwrite")
            sys.exit(1)
        else:
            with open(output_location, 'w') as f:
                json.dump(res.to_dict(), f, indent=4)
            sys.exit(0)
            
    if json_output:
        print(json.dumps(res.to_dict(), indent=4))
    else:
        print(str(res))