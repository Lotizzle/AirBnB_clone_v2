from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State


new = State(name="California")
print(new.name)