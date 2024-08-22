import requests

API_key = "f62144dc794d3dc5977c603bddc62866"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    date = [dict["dt_txt"] for dict in filtered_data]
    return filtered_data, date


if __name__ == "__main__":
    data, dates = get_data(place="Tokyo", forecast_days=3)
    print(data)
    print(dates)
