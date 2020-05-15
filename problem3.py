import math

print("***************** Welcome ********************")
print("seconds to human friendly time function")
print("python version 3.6+")
print("run this script to test the function by yourself")
print("or run test_problem3 for unittest script ")


def format_duration(number):
    # dictionary to save each time element and its value
    time_dict = {}
    py# list of strings , each string is the value and time element
    time_list = []
    # constants for calculations
    seconds_in_minute = 60
    seconds_in_hour = 3600  # 60 * 60
    seconds_in_day = 86400  # 24 * 60 * 60
    seconds_in_year = 31536000  # 365 * 24 * 60 * 60
    # calculate years and add to dictionary
    years = math.floor(number/seconds_in_year)
    time_dict['year'] = years
    # calculate days and add to dictionary
    remaining_days = number % seconds_in_year
    days = math.floor(remaining_days / seconds_in_day)
    time_dict['day'] = days
    # calculate hours and add to dictionary
    remaining_hours = number % seconds_in_day
    hours = math.floor(remaining_hours / seconds_in_hour)
    time_dict['hour'] = hours
    # calculate minutes and add to dictionary
    remaining_minutes = number % seconds_in_hour
    minutes = math.floor(remaining_minutes / seconds_in_minute)
    time_dict['minute'] = minutes
    # calculate seconds and add to dictionary
    remaining_seconds = number % seconds_in_minute
    seconds = math.ceil(remaining_seconds)
    time_dict['second'] = seconds
    # transfer all key,value in dictionary to list for join
    for key in time_dict:
        if time_dict[key] != 0:
            time_list.append("%d %s%s" %(time_dict[key],key,("s" if time_dict[key] > 1 else "")))
    # join all strings in list to form one sentence
    time_phrase = ", ".join(time_list)
    # calculate last comma (,) in sentence to replace with 'and'
    last_comma_index = int(max([index for index, char in enumerate(time_phrase) if char == "," ]))
    time_phrase = time_phrase[:last_comma_index] + " and" + time_phrase[last_comma_index+1:]
    return time_phrase


if __name__ == '__main__':
    number = int(input("Please Provide an integer number: "))
    print("Human readable form of {} : {}".format(number, format_duration(number)))
