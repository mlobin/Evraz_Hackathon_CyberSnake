from fastapi import HTTPException


ObjectAlreadyExistsError = HTTPException(status_code=409, detail="Object already exists")

ObjectNotFoundError = HTTPException(status_code=404, detail="Object doesn't exist")

RecordsNotLoadedError = HTTPException(status_code=400, detail="Records hasn't loaded from kafka yet")
