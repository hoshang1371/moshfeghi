

from datetime import datetime
import convert_numbers


def getDuration(then, now = datetime.now(), interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 
    
    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        # return " {}, {} روز, {} ساعت, {} دقیقه".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]))
        # return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))
        # return {
        # 'years':y[0],
        # 'days':d[0],
        # 'hours':h[0],
        # 'minutes':m[0],
        # 'seconds':s[0]
        # }
        return {
        'years':convert_numbers.english_to_persian(str(int(y[0]))),
        'days':convert_numbers.english_to_persian(str(int(d[0]))),
        'hours':convert_numbers.english_to_persian(str(int(h[0]))),
        'minutes':convert_numbers.english_to_persian(str(int(m[0]))),
        'seconds':convert_numbers.english_to_persian(str(int(s[0])))
        }



    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]
    # return {
    #     'years': int(years()[0]),
    #     'days': int(days()[0]),
    #     'hours': int(hours()[0]),
    #     'minutes': int(minutes()[0]),
    #     'seconds': int(seconds()),
    # }