from typing import List
import json

from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from .k8s import write_yaml, apply_yaml

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/v1/atom/{atom_id}", response_model=List[schemas.AtomBase])
def read_atom(atom_id: str, db: Session = Depends(get_db)):
    atom_changes = crud.get_atom(db, atom_id)
    if atom_changes is None:
        raise HTTPException(status_code=404, detail="Atom not found")
    return atom_changes


@app.get("/api/v1/atoms", response_model=List[schemas.AtomBase])
def read_all_atoms(db: Session = Depends(get_db)):
    atoms = crud.get_all_atoms(db)
    return atoms


@app.post("/api/v1/atoms", response_model=schemas.AtomBase)
def create_atom(atom: schemas.Atom, db: Session = Depends(get_db)):
    db_atom = crud.create_atom(db, atom)
    json_compatible_atom_data = jsonable_encoder(atom)
    json_bytes = json.dumps(json_compatible_atom_data).encode()
    write_yaml(
        atom_id=atom.atom_id,
        name=atom.name,
        cpu=atom.requirements.cpu,
        mem=atom.requirements.mem,
        priority=atom.priority,
        serialized=str(json_bytes)[0] + str(json_bytes)[2:-1],
    )
    # here I need to pass serialized atom data in form of string type rather than dict
    if apply_yaml():
        update_atom = crud.update_atom(db, atom.atom_id, "running")
    else:
        update_atom = crud.update_atom(db, atom.atom_id, "failed")
    return update_atom


@app.delete("/api/v1/atom/{atom_id}", response_model=schemas.AtomBase)
def terminate_atom(atom_id: str, db: Session = Depends(get_db)):
    updated_atom = crud.update_atom(db, atom_id, "complete")
    return updated_atom
