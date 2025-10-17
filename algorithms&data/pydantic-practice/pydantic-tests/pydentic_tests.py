

from pydantic import BaseModel, ValidationError, \
    Field, field_validator, model_validator
    
from pprint import pprint

class Tag(BaseModel):
    id: int
    tag: str
    


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')
    tags: list[Tag]
    
    @field_validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError("Work with SPB!")
        return v
    
    # @model_validator(mode='after')
    # def validate_values(cls, values):
    #     print('values', values)
    #     return values
            
    
    
class UserWithoutPassword(BaseModel):
    name: str
    email: str
    
class User(UserWithoutPassword):
    password: str
    
        
    
    

input_json = """
{
    "city_id": 123,
    "cityFullName": "Moscow",
    "tags": [
        {
        "id": 1,
        "tag": "capital"
        },
        {
            "id": 2,
            "tag": "big city"
        }
    ]
}
"""


try:
    city = City.model_validate_json(
        json_data=input_json
    )
except ValidationError as e:
    print("Exception: ", e.json(indent=4))

else:
    tag = city.tags[1]
    city_model = city
    print(tag.model_dump_json())
    print(city.model_dump_json(), end='\n\n')
    print(city.name, end='\n\n')
    print(city.model_dump_json(by_alias=True,
                               exclude={'city_id'}))