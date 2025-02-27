import requests
from typing import Dict, List, Optional, Union, Any
import datetime as dt


class SpectAppAPI:
    """
    A Python wrapper for the Spect'App API.

    This class provides methods to interact with the Spect'App API for retrieving
    show information from various festivals.
    """

    BASE_URL = "https://spectapp.linaki.org/api"

    def __init__(self, api_key: str = None):
        """
        Initialize the SpectApp API wrapper.

        Args:
            api_key (str, optional): Your Spect'App API key. If not provided,
                                    you'll need to set it later with set_api_key().
        """
        self.api_key = api_key

    def set_api_key(self, api_key: str) -> None:
        """
        Set or update the API key.

        Args:
            api_key (str): Your Spect'App API key
        """
        self.api_key = api_key

    def _make_request(self, endpoint: str, params: Dict[str, Any]) -> Dict:
        """
        Make a request to the Spect'App API.

        Args:
            endpoint (str): API endpoint to call
            params (dict): Parameters to include in the request

        Returns:
            dict: JSON response from the API

        Raises:
            ValueError: If API key is not set
            requests.RequestException: For any request-related errors
        """
        if not self.api_key:
            raise ValueError("API key is not set. Use set_api_key() to set it.")

        # Add API key to parameters
        params["key"] = self.api_key

        # Construct full URL
        url = f"{self.BASE_URL}/{endpoint}"

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            j=response.json()
            if j["status"]!="success":
                raise Exception(f"Error while requesting Spect'App API : {j['error']}")
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"HTTP Error : {e}")


    def list_shows(self, festival_id: str, page: int = 0) -> tuple:
        """
        Get a list of shows for a specific festival.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            page (int, optional): Page number for pagination. Defaults to 0.

        Returns:
            tuple: Shows list for the specified festival and page and number of results
        """
        params = {
            "festival": festival_id,
            "page": page
        }
        d=self._make_request("shows", params)
        return d["shows"], d["results"]

    def search_shows(self, festival_id: str, query: str, page: int = 0) -> tuple:
        """
        Get a list of shows for a specific festival.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            page (int, optional): Page number for pagination. Defaults to 0.

        Returns:
            tuple: Shows list for the specified festival and page and number of results
        """
        params = {
            "festival": festival_id,
            "page": page,
            "query" : query
        }

        d=self._make_request("shows", params)
        return d["shows"], d["results"]

    def get_show(self, festival_id: str, show_id: Union[str, int]) -> Dict:
        """
        Get detailed information about a specific show.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            show_id (str or int): Identifier of the show

        Returns:
            dict: Detailed information about the specified show
        """
        params = {
            "festival": festival_id,
            "id": show_id
        }
        r = self._make_request("show", params)
        return r["show"]

    def get_show_icon(self, festival_id: str, show_id: Union[str, int], use_api=True) -> str:
        """
        Get the show icon url.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            show_id (str or int): Identifier of the show
            use_api (bool): Specify if use API to get the url or format it locally

        Returns:
            string: url of the icon
        """
        if use_api:
            params = {
                "festival": festival_id,
                "id": show_id
            }
            r = self._make_request("show", params)
            return r["icon"]
        else:
            return f"https://spectapp.linaki.org/static/img/{festival_id}/icon/{show_id}.jpeg"

    def get_show_header(self, festival_id: str, show_id: Union[str, int], use_api=True) -> str:
        """
        Get the show header url.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            show_id (str or int): Identifier of the show
            use_api (bool): Specify if use API to get the url or format it locally

        Returns:
            string: url of the header
        """
        if use_api:
            params = {
                "festival": festival_id,
                "id": show_id
            }
            r = self._make_request("show", params)
            return r["header"]
        else:
            return f"https://spectapp.linaki.org/static/img/{festival_id}/header/{show_id}.jpeg"

    def get_show_dates(self, festival_id: str, show_id: Union[str, int]) -> Dict:
        """
        Get dates of the given show.

        Args:
            festival_id (str): Identifier of the festival (e.g., "chalon2024")
            show_id (str or int): Identifier of the show

        Returns:
            dict: Datetimes and places of the show
        """
        params = {
            "festival": festival_id,
            "id": show_id
        }
        r = self._make_request("dates", params)
        dates=[]
        for d in r["dates"]:
            dates.append((dt.datetime.fromisoformat(d["datetime"]), d["place"]))
        return dates

