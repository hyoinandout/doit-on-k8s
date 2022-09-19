from sqlalchemy.orm import Session
from . import models, schemas


def get_atom(db: Session, atom_id: str):
    return db.query(models.Atom).filter(models.Atom.atom_id == atom_id).all()


def get_all_atoms(db: Session):
    return db.query(models.Atom).all()


def create_atom(db: Session, atom: schemas.Atom):
    db_atom = models.Atom(atom_id=atom.atom_id, status=atom.status)
    db.add(db_atom)
    db.commit()
    db.refresh(db_atom)
    return db_atom


def update_atom(db: Session, atom_id: str, status: str):
    db_atom = db.query(models.Atom).filter(models.Atom.atom_id == atom_id).first()
    db_atom.status = status
    db.commit()
    return db_atom
