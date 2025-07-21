from typing import NamedTuple, Literal
from subprocess import Popen, PIPE
from exceptions import CantGetCoordinates
from config import USE_ROUNDED_COORDS


# from typing import Literal
# from typing import TypedDict
# from dataclasses import dataclass

# class Coordinates(TypedDict):
#     latitude: float
#     longitude: float


# @dataclass
# class Coordinates:
#     latitude: float
#     longitude: float
    
# def get_gps_coordinates() -> Coordinates:
#     #     """Returns current coordinates using MacBook GPS"""
#     return Coordinates(latitude=10.0, longitude=20.0)
    

# def get_gps_coordinates() -> Coordinates:
#     """Returns current coordinates using MacBook GPS"""
#     return Coordinates(latitude=0.0, longitude=0.0)

# def get_gps_coordinates() -> dict[str, float]:
#     """Returns current coordinates using MacBook GPS"""
#     return {"latitude": 10.0, "longtitude": 20.0}

# def get_gps_coordinates() -> dict[Literal["latitude"] | Literal["longitude"], float]:
#     """Returns current coordinates using MacBook GPS"""
#     return {"latitude": 10.0, "longitude": 20.0}

# def get_gps_coordinates() -> Coordinates:
#     """Returns current coordinates using MacBook GPS"""
#     return Coordinates(**{"latitude": 10.0, "longitude": 20.0})


class Coordinates(NamedTuple):
    latitude: float
    longitude: float
    

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    # process = Popen(["""curl -s https://ipinfo.io/json | jq -r '"latitude: \(.loc | split(",")[0])\nlongitude: \(.loc | split(",")[1])"'"""])
    # (output, err) = process.communicate()
    # exit_code = process.wait()
    
    # if err is not None and exit_code != 0:
    #     raise CantGetCoordinates
    
    # output_lines = output.decode().strip().lower().split("\n")
    
    coordinates = _get_whereami_coordinates()
    return _round_coordinates(coordinates)


def _get_whereami_coordinates() -> Coordinates:
    whereami_output = _get_whereami_output()
    coordinates = _parse_coordinates(whereami_output)
    return coordinates


def _get_whereami_output() -> bytes:
    output = b"""city: minsk
region: minsk city
country: by
timezone: europe/minsk
readme: https://ipinfo.io/missingauth
latitude: 53.9000
longitude: 27.5667"""

    if not output:
        raise CantGetCoordinates
    
    return output

def _parse_coordinates(whereami_output: bytes) -> Coordinates:
    try:
        output_lines = whereami_output.decode().strip().lower().split("\n")
    
    except UnicodeDecodeError:
        raise CantGetCoordinates
    
    return Coordinates(
        latitude=_parse_coord(output_lines, "latitude"),
        longitude=_parse_coord(output_lines, "longitude")
    )
    
    
def _parse_coord(
    output: list[str],
    coord_type: Literal["latitude"] | Literal["longitude"]
) -> float:
    for line in output:
        line = line.strip()
        if line.startswith(f"{coord_type}:"):
           return _parse_float_coordinate(line.split(":")[1].strip())
       
    raise CantGetCoordinates
            
 
def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates
    
    
def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUNDED_COORDS:
        return coordinates
    
    return Coordinates(
        *map(lambda c: round(c, 1), [coordinates.latitude, coordinates.longitude])
    ) 
            

# coordinates = get_gps_coordinates()
# print(coordinates.latitude)
# print(coordinates["latitude"])
# print(coordinates["longitude"])
# print(coordinates["longitude"])


# print(coordinates.latitude)
# print(coordinates.longitude)