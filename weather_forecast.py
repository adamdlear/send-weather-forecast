import datetime as dt
import meteomatics.api as api

def millimetersToInches(mm):
    return mm/25.4

def get_time(long_time):
    return long_time[11:15]

username = 'na_lear'
password = 'VfjD7LO1l6'

amman_jordan_coordinates = [('31.9737142','37.977477')]
kgu_coordinates = [('34.7684','137.3468')]
des_moines_coordinates = [('41.6031','93.6546')]

def get_dataframe(coordinates=des_moines_coordinates, username=username, password=password):
    now = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    startdate_ts = now
    enddate_ts = startdate_ts + dt.timedelta(days=1)
    interval_ts = dt.timedelta(hours=1)
    parameters_ts = ['t_2m:F',  
                't_min_2m_24h:F',
                't_max_2m_24h:F',
                'precip_1h:mm', 
                'precip_24h:mm', 
                'sunrise:sql', 
                'sunset:sql', 
                'weather_symbol_1h:idx', 
                'weather_symbol_24h:idx']
    return api.query_time_series(coordinates, startdate_ts, enddate_ts, interval_ts, parameters_ts, username, password)

def write_email_body():
    df = get_dataframe()
    body = ("Good morning my love,\n" + 
    "Here is your daily forecast for Amman, Jordan:\n" +
    "The high for the day is {}°F and the low is {}°F.\n".format(round(df.iloc[7,2]), round(df.iloc[7,1])) +
    "   12:00AM: {}\n".format(round(df.iloc[0,0]))+
    "   1:00AM: {}\n".format(round(df.iloc[1,0]))+
    "   2:00AM: {}\n".format(round(df.iloc[2,0]))+ 
    "   3:00AM: {}\n".format(round(df.iloc[3,0]))+ 
    "   4:00AM: {}\n".format(round(df.iloc[4,0]))+ 
    "   5:00AM: {}\n".format(round(df.iloc[5,0]))+ 
    "   6:00AM: {}\n".format(round(df.iloc[6,0]))+ 
    "   7:00AM: {}\n".format(round(df.iloc[7,0]))+ 
    "   8:00AM: {}\n".format(round(df.iloc[8,0]))+ 
    "   9:00AM: {}\n".format(round(df.iloc[9,0]))+ 
    "   10:00AM: {}\n".format(round(df.iloc[10,0])) + 
    "   11:00AM: {}\n".format(round(df.iloc[11,0])) +
    "   12:00PM: {}\n".format(round(df.iloc[12,0])) +
    "   1:00PM: {}\n".format(round(df.iloc[13,0])) +
    "   2:00PM: {}\n".format(round(df.iloc[14,0])) +
    "   3:00PM: {}\n".format(round(df.iloc[17,0])) +
    "   4:00PM: {}\n".format(round(df.iloc[16,0])) +
    "   7:00PM: {}\n".format(round(df.iloc[17,0])) +
    "   6:00PM: {}\n".format(round(df.iloc[18,0])) +
    "   7:00PM: {}\n".format(round(df.iloc[19,0])) +
    "   8:00PM: {}\n".format(round(df.iloc[20,0])) +
    "   9:00PM: {}\n".format(round(df.iloc[21,0])) +
    "   10:00PM: {}\n".format(round(df.iloc[22,0])) +
    "   11:00PM: {}\n".format(round(df.iloc[23,0])) +
    "   12:00AM: {}\n".format(round(df.iloc[24,0])) +
    "There will be a total of {} inches of precipitation today.\n".format(round(millimetersToInches(round(df.iloc[7,3])))) +
    "Sunrise: {}, Sunset: {}".format(df.iloc[0,6], df.iloc[0,7]))
    return body