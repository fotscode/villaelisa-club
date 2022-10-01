from datetime import datetime
import enum
from sqlalchemy import Column, String, Integer, Sequence , Enum, Boolean
from src.core.db import db

associate_disciplines = db.Table(
    "associate_disciplines",
    Column("associate_id", Integer, db.ForeignKey("associates.associate_number"), primary_key=True),
    Column("discipline_id", Integer, db.ForeignKey("disciplines.id"), primary_key=True),
)

class GenderOptions(enum.Enum):
    male = 1
    female = 2
    other = 3
    
class DNIOptions(enum.Enum):
    DNI = 1
    LE = 2
    LC = 3

class Associate(db.Model):
    """ Club associate model
    Args:
        - DNI type (select) : list with all different DNI types ex: DNI, LE, LC
        - DNI number (integer) :  Associate DNI number
        - gender (select) : Associate gender ex: M|F|Otro
        - associate number (integer): Associate number. Unique, autogenerated
        - address (text) : associate address .
        - phone number (optional) (text): Associate Phone number.
        - Entry date  (datetime): Entry-date autogenerated
        
    """    
    __tablename__ = "associates"
    associate_number = Column(Integer, primary_key=True)
    name= Column(String(50), nullable=False)
    surname= Column(String(50), nullable=False)
    active=Column(Boolean, default=True)
    email=Column(String(50), nullable=False)
    DNI_number = Column(Integer,unique=True)
    DNI_type = Column(Enum(DNIOptions,validate_string=True))
    gender = Column(Enum(GenderOptions,validate_string=True))
    address = Column(String(255))
    phone_number= Column(String,nullable=True)
    entry_date=Column(db.DateTime)
    payments = db.relationship("Payment", back_populates="associate", lazy=True)
    disciplines = db.relationship("Discipline", secondary="associate_disciplines", back_populates="associates")

    def __init__(self, **data):
        self.DNI_number = data["DNI_number"]
        self.name= data["name"]
        self.surname= data["surname"]
        self.email= data["email"]
        self.DNI_type = data["DNI_type"]
        self.gender = data["gender"]
        self.address = data["address"]
        self.phone_number = data["phone_number"]
        self.active=True
        self.entry_date=datetime.utcnow()

    def __repr__(self):
        #TODO add user relation  
        return f"""con el dni {self.DNI_number} con el correo {self.email}, del genero {self.gender}"""
        