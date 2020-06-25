def parse_line(line):
    """Parse log information into dictionary

    :param line: log line data parsed into a dictionary
    :return dictionary of log data
    """
    d = dict()
    for item in line:
        if "=" in item:
            i = item.split("=")
            d[i[0].strip()] = i[1].strip()      
    return d

def clean_date(info):
    """Finds formatted date of birth param and cleans the data

    :param info: dictionary of data containing log information
    :return: dictionary of data with cleaned date of birth
    """
    if "DOB" in info:
        date = info["DOB"]
        date = date.replace("'","")
        new_date = "X/X/" + date[-4:]
        info["DOB"] = new_date
    elif "DATE_OF_BIRTH" in info:
        date = info["DATE_OF_BIRTH"]
        date = date.replace("'","")
        new_date = "X/X/" + date[-4:]
        info["DATE_OF_BIRTH"] = new_date
    return info

def format_new_line(line, new_data):
    """Transform dictionary into string and append it to log

    :param line: initial log line to get time stamp
    :param new_data: dictionary of data with cleaned date
    :return: single string with all data 
    """
    flattened = ''

    for k, v in new_data.items():
        flattened += k+'='+v + ' '

    return line[:29] + flattened