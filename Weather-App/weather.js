// weatherKey is the API key for openweathermap API
// timeZoneKey is for TimeZoneDB API (which I needed to get the timezone of a city for sunrise and sunset times)
const weatherKey = "e21500776538d0e6bcdfeb5bc40305e6"
const timeZoneKey = "9YJ3KPAJ2EIB"

const titleElement = document.querySelector(".app-title")
const temperatureElement = document.querySelector(".temperature")
const windElement = document.querySelector(".wind")
const sunriseElement = document.querySelector(".sunrise")
const sunsetElement = document.querySelector(".sunset")

// stores the weather information
const weather = {
    temperature : {
        value: "-",
        unit: "celsius"
    },
    wind : {
        value: "-",
        unit: "kph"
    },
    sunrise : "-",
    sunset :  "-"
};


function getWeather(city){
    // The city's weather is queried by its id (as instructed by the api docs)
    let city_id = city.id
    let weather_api = `https://api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${weatherKey}`

    fetch(weather_api)
        .then(response => response.json())
        .then(data => {
            titleElement.innerHTML = `<p>${data.name}, ${data.sys.country}</p>`
            weather.temperature.value = Math.floor(data.main.temp - 273);
            weather.wind.value = Math.floor(msToKph(data.wind.speed))
            sunrise_time = data.sys.sunrise
            sunset_time = data.sys.sunset
            // note these times are in UTC and need to be converted

            //gets the time zone of the city
            fetch(`http://api.timezonedb.com/v2.1/get-time-zone?key=${timeZoneKey}&format=json&by=position&lat=${city.coord.lat}&lng=${city.coord.lon}`)
                .then(response => response.json())
                .then(data => data.gmtOffset)
                .then(timeDiff => {
                    sunrise_time += timeDiff
                    sunset_time += timeDiff

                    // the timestamps are converted to HH:MM:SS
                    weather.sunrise = unixToTime(sunrise_time)
                    weather.sunset = unixToTime(sunset_time)
                })
                .then(function(){
                    displayWeather();
                });
        })
}


function unixToTime(unix) {
    // converts timestamps to HH:MM:SS (for the sunrise and sunset times)
    let date = new Date(unix*1000);
    let hours = date.getHours();
    let minutes = "0" + date.getMinutes();
    let seconds = "0" + date.getSeconds();

    let formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
    return formattedTime
}


function celsiusToFarenheit(temperature) {
    return temperature * 9/5 + 32
}

function msToKph(speed) {
    return speed * 3.6
}

function kphToMph(speed) {
    return speed / 1.609
}

function capitalise(word) {
    // equivalent of .title() in Python
    words = word.split(" ")
    new_words = []
    for (let i=0; i < words.length; i++) {
        word = words[i]
        new_words.push(word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    }
  	return new_words.join(" ")
}

function displayWeather() {
    temperatureElement.innerHTML = `${weather.temperature.value}°<span>C</span>`
    windElement.innerHTML = `<label>Wind speed:</label> ${weather.wind.value} <span>kph</span>`
    sunriseElement.innerHTML = `<label>Sunrise:</label> ${weather.sunrise}`
    sunsetElement.innerHTML = `<label>Sunset:</label> ${weather.sunset}`

}


// If you click on the temperature, it converts between celsius and farenheit
temperatureElement.addEventListener("click", function() {
    if (weather.temperature.value == "-") {return}
    if (weather.temperature.unit == "celsius"){
        let farenheit = celsiusToFarenheit(weather.temperature.value)
        farenheit = Math.floor(farenheit)
        temperatureElement.innerHTML = `${farenheit}°<span>F</span>`
        weather.temperature.unit = "farenheit"
    }else {
        temperatureElement.innerHTML = `${weather.temperature.value}°<span>C</span>`
        weather.temperature.unit = "celsius"
    }
});

// If you click on the wind speed, it converts between kph and mph
windElement.addEventListener("click", function() {
    if (weather.wind.value == "-") {return}
    if (weather.wind.unit == "kph"){
        let mph = kphToMph(weather.wind.value)
        mph = Math.floor(mph)
        windElement.innerHTML = `<label>Wind speed:</label> ${mph} <span>mph</span>`
        weather.wind.unit = "mph"
    } else {
        windElement.innerHTML = `<label>Wind speed: </label>${weather.wind.value} <span>kph</span>`
        weather.wind.unit = "kph"
    }
});

let cities;

// the data in city.list.json is saved to the cities variable
fetch('city.list.json')
    .then(response => response.json())
    .then(data => cities = data)
    .then(function() {
        let city_name = capitalise(window.prompt("Enter a city name:"))

        isFound = false
        let cities_found = []
        
        while (cities_found.length == 0) {
            for (let obj=0;obj<cities.length;obj++) {
                if (cities[obj].name == city_name) {
                    cities_found.push(cities[obj])
                }
            }
            if (cities_found.length == 1) {
                return cities_found[0]

            } else if (cities_found.length > 1) {
                // if more than one city has the same name, the user is asked which city they are referring to
                
                let message = ""
                for (let i=0; i < cities_found.length; i++) {
                    message += `[${i+1}]: ${cities_found[i].name}, ${cities_found[i].country}\n`
                }
                let city_number = window.prompt(`Which ${city_name} are you referring to?\n${message}`)
                
                while (isNaN(parseInt(city_number)) || parseInt(city_number) < 1 || parseInt(city_number) > cities_found.length) {
                    city_number = window.prompt(`Which ${city_name} are you referring to?\n${message}`)
                }
                
                return cities_found[city_number-1]
                
            } else {
            
            alert("City not found")
            city_name = capitalise(window.prompt("Enter a city name:"))

            }
        }
    })
    .then(city => getWeather(city))