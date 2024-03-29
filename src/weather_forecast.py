import datetime as dt
import pytz
import meteomatics.api as api

from credentials import USERNAME, PASSWORD


def millimeters_to_inches(mm):
    return mm/25.4


def get_time(long_time):
    return long_time[11:15]


amman_jordan_coordinates = [('31.6690094','36.3060338')]
kgu_coordinates = [('34.7684','137.3468')]
home_coordinates = [('41.537724', '-90.365695')]

amman_timezone = 'Asia/Amman'
japan_timezone = 'Japan'


def adjust_for_timezone(desired_timezone):
    now_in_utc = dt.datetime.utcnow().replace(tzinfo=pytz.utc)
    local_time = now_in_utc.astimezone(pytz.timezone(desired_timezone))
    return local_time


def get_dataframe(coordinates=home_coordinates, username=USERNAME, password=PASSWORD):
    # now = dt.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    # now = adjust_for_timezone(amman_timezone)
    now = dt.datetime.now()
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
    return api.query_time_series(coordinates, startdate_ts, enddate_ts, interval_ts, parameters_ts, USERNAME, PASSWORD)


def write_email_body():
    todays_date = (adjust_for_timezone(amman_timezone)).strftime("%B %d, %Y")
    df = get_dataframe()
    body = ("Good morning,\n" +
            "Here is your daily forecast for {} in Amman, Jordan:\n".format(todays_date) +
            "The high for the day is {}°F and the low is {}°F.\n".format(round(df.iloc[7, 2]), round(df.iloc[7, 1])) +
            "       12:00AM: {}°F\n".format(round(df.iloc[0, 0])) +
            "       1:00AM: {}°F\n".format(round(df.iloc[1, 0])) +
            "       2:00AM: {}°F\n".format(round(df.iloc[2, 0])) +
            "       3:00AM: {}°F\n".format(round(df.iloc[3, 0])) +
            "       4:00AM: {}°F\n".format(round(df.iloc[4, 0])) +
            "       5:00AM: {}°F\n".format(round(df.iloc[5, 0])) +
            "       6:00AM: {}°F\n".format(round(df.iloc[6, 0])) +
            "       7:00AM: {}°F\n".format(round(df.iloc[7, 0])) +
            "       8:00AM: {}°F\n".format(round(df.iloc[8, 0])) +
            "       9:00AM: {}°F\n".format(round(df.iloc[9, 0])) +
            "       10:00AM: {}°F\n".format(round(df.iloc[10, 0])) +
            "       11:00AM: {}°F\n".format(round(df.iloc[11, 0])) +
            "       12:00PM: {}°F\n".format(round(df.iloc[12, 0])) +
            "       1:00PM: {}°F\n".format(round(df.iloc[13, 0])) +
            "       2:00PM: {}°F\n".format(round(df.iloc[14, 0])) +
            "       3:00PM: {}°F\n".format(round(df.iloc[17, 0])) +
            "       4:00PM: {}°F\n".format(round(df.iloc[16, 0])) +
            "       5:00PM: {}°F\n".format(round(df.iloc[17, 0])) +
            "       6:00PM: {}°F\n".format(round(df.iloc[18, 0])) +
            "       7:00PM: {}°F\n".format(round(df.iloc[19, 0])) +
            "       8:00PM: {}°F\n".format(round(df.iloc[20, 0])) +
            "       9:00PM: {}°F\n".format(round(df.iloc[21, 0])) +
            "       10:00PM: {}°F\n".format(round(df.iloc[22, 0])) +
            "       11:00PM: {}°F\n".format(round(df.iloc[23, 0])) +
            "       12:00AM: {}°F\n".format(round(df.iloc[24, 0])) +
            "There will be a total of {} inches of precipitation today.\n"
                .format(round(millimeters_to_inches(round(df.iloc[7, 3])))) +
            "Sunrise: {}, Sunset: {}".format(df.iloc[0, 6], df.iloc[0, 7]))
    return body
