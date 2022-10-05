#here is where CRUD are made
#QUESTION TO ASK TO GROUP, shall we do it in a CLASS or in different functions?
from src.core.board.configuration import Configuration
from src.core.board.associate import Associate
from src.core.board.discipline import Discipline
from src.core.db import db
from src.core.resource_manager import ResourceManager

disciplines=ResourceManager(db.session,Discipline)

def get_associate_by_id(associate_number):
    """ Get associate by id
    Args:
        - associate_number (integer): Associate number. Unique, autogenerated
    Returns:
        - Associate object
    """
    return Associate.query.get(associate_number)

def get_associate_by_DNI(DNI_number):
    """ Get associate by DNI
    Args:
        - DNI_number (integer): Associate DNI number
    Returns:
        - Associate object
    """
    return Associate.query.filter(Associate.DNI_number == DNI_number, Associate.deleted == False).first()

def list_associates():
    """ List all associates
    Returns:
        - List of Associate objects
    """
    return Associate.query.filter(Associate.deleted==False).all()

def create_associate(form):
    """ Create associate
    Returns:
        - Create associate
    """
    associate = Associate(**form.data)
    db.session.add(associate)
    db.session.commit()
    return associate

def update_associate(form_data,id):
    """ Update associate
    Returns:
        - Update associate
    """
    db.session.query(Associate).filter(Associate.associate_number==id).update(form_data)
    db.session.commit()

def delete_associate(id):
    """Delete associate
    Returns:
        - Delete associate
    """
    db.session.query(Associate).filter(Associate.associate_number==id).update({"deleted":True})
    db.session.commit()

def list_disciplines():
    """ List all disciplines
    Returns:
        - List of Discipline objects
    """
    return disciplines.query.all()

def get_discipline(id):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    return disciplines.query.filter(Discipline.id == id).one()

def delete_discipline(id):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    disciplines.query.filter(Discipline.id == id).update({"deleted":True})
    db.session.commit()

def update_discipline(id,discipline_data):
    """ Get discipline
    Returns:
        - Get discipline by id
    """
    disciplines.query.filter(Discipline.id == id).update(discipline_data)
    db.session.commit()


def add_discipline(discipline_data):
    """ Add discipline
    Returns:
        - Add discipline
    """
    disciplines.add(discipline_data)

# begin config repo
def get_cfg():
    """Get configuration
    Returns:
        - Gets configuration or creates it
    """
    try:
        return db.session.query(Configuration).one()
    except:
        return add_cfg(
            Configuration(
                {
                    "record_number": 6,
                    "ord_criteria": "ALPH",
                    "currency": "ARS",
                    "base_fee": 100,
                    "due_fee": 50,
                    "payment_available": True,
                    "contact": "villa elisa",
                    "payment_header": "pagos",
                }
            )
        )
    # TODO discuss default values


def add_cfg(cfg_data):
    """Add configuration
    Returns:
        - Added configuration
    """
    db.session.add(cfg_data)
    db.session.commit()
    return cfg_data


def update_cfg(cfg_data):
    """Update configuration
    Returns:
        - Updated configuration
    """
    cfg = get_cfg()
    cfg.record_number = cfg_data.record_number
    cfg.ord_criteria = cfg_data.ord_criteria
    cfg.currency = cfg_data.currency
    cfg.base_fee = cfg_data.base_fee
    cfg.due_fee = cfg_data.due_fee
    cfg.payment_available = cfg_data.payment_available
    cfg.contact = cfg_data.contact
    cfg.payment_header = cfg_data.payment_header

    # TODO change this
    db.session.commit()
    return cfg_data


# end config repo
