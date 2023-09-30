# Weather Forecast Email Automation

## Motivation and Description
I was talking to a friend who was going to study abroad in Amman, Jordan, and they mentioned that they couldn't convert temperature in Celsius to Fahrenheit in their head quickly.
With this I thought it'd be a good project to create an automated email notification system that would send an email to the recipient at the beginning of their day.

This system used two different APIs: the Meteomatics weather API (https://www.meteomatics.com/en/weather-api/weather-api-free/) and the Google Gmail API (https://developers.google.com/gmail/api/guides).
By calling the Weather API I could fetch the predicted weather for the day by providing the appropriate coordinates.
I could then pass this data into the Gmail API where I could send an email to the desire recipient, with a customized subject, body, and attachment.
