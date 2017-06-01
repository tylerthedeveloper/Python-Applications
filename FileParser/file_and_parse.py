import csv

# class runner_data(object):
# 	def __init__(self):

MY_FILE = "./sample_user_data.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)
    
    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()
	
    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
	
	# Close the CSV file
    opened_file.close()
    
    return parsed_data

	

def main():
    # Call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")
	# Let's see what the data looks like!
	print new_data


if __name__ == "__main__":
    main()