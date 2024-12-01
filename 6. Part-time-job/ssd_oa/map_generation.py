import requests
from PIL import Image
from io import BytesIO

NAVER_MAP_API_URL = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
NAVER_CLIENT_ID = "YOUR_CLIENT_ID"
NAVER_CLIENT_SECRET = "YOUR_CLIENT_SECRET"

def generate_map(postcodes, output_path):
    """네이버 지도 API로 우편번호 위치 표시"""
    markers = "|".join([f"pos:{lat},{lng}" for lat, lng in postcodes])
    params = {
        "w": 800,
        "h": 600,
        "markers": markers
    }

    headers = {
        "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET
    }

    response = requests.get(NAVER_MAP_API_URL, params=params, headers=headers)
    img = Image.open(BytesIO(response.content))
    img.save(output_path)
