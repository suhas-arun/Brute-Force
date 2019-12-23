# Weather Webapp (For Google Code-In)

The app uses the [OpenWeather API](https://openweathermap.org/current) to access weather data (temperature, wind speed, sunrise and sunset).

It also uses the [TimeZoneDB API](https://timezonedb.com/api) to access timezone information for locations. This was necessary for converting sunrise and sunset times to local time from UTC.

Note: the TimeZoneDB API uses http for requests, which works fine on Edge and Firefox but for Chrome you have to click "load unsafe scripts" for the app to work.

The code is in https://github.com/suhas-arun/Google-Code-In/tree/master/docs.

The webapp is hosted on Github Pages at https://suhas-arun.github.io/Google-Code-In/.