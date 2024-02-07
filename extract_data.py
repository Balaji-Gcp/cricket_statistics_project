import requests
import csv

url = "https://crickbuzz-official-apis.p.rapidapi.com/rankings/batsman/"

querystring = {"formatType":"odi"}

headers = {
	"X-RapidAPI-Key": "173d9288bdmsh5cd19990918258dp11d1fdjsn8c6ef70a3fc3",
	"X-RapidAPI-Host": "crickbuzz-official-apis.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('rank', [])  # Extracting the 'rank' data
    csv_filename = 'batsmen_rankings.csv'

    if data:
        field_names = ['rank', 'name', 'country','points','avg']  # Specify required field names

        # Write data to CSV file with only specified field names
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #writer.writeheader()
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)
