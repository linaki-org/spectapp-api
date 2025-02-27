import spectapp_api
# Usage examples
if __name__ == "__main__":
    api = spectapp_api.SpectAppAPI("YOUR_API_KEY") #Get yours on https://spectapp.linaki.org/api

    shows, number_of_shows = api.list_shows(festival_id="chalon2024", page=0) #List all shows (one page=10 shows)
    print(f"All shows : {shows}")
    print(f"Total shows : {number_of_shows}")

    results, number_of_results = api.search_shows(festival_id="chalon2024", query="rollmops", page=0) #Search for 'rollmops' and get the first results page
    print(f"Results : {results}")
    print(f"Total results : {number_of_results}")

    show_details = api.get_show(festival_id="chalon2024", show_id=128) #Get details about the show with id 128
    print(f"Details : {show_details}")

    show_icon_url = api.get_show_icon(festival_id="chalon2024", show_id=128) #Get the URL of the icon of the show 128
    print(f"Icon URL : {show_icon_url}")

    show_header_url = api.get_show_header(festival_id="chalon2024", show_id=128)  #Get the URL of the header of the show 128
    print(f"Header URL : {show_header_url}")

    show_dates = api.get_show_dates(festival_id="chalon2024", show_id=128) #Get dates and places of the show 128
    print(f"Dates : {show_dates}")