from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from database import create_item, read_item, read_all_items, update_item, delete_item

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=300)

class UpdateItem(BaseModel):
    description: Optional[str] = Field(None, max_length=300)

@app.post("/items/", response_model=dict)
def create_item_endpoint(item: Item):
    try:
        item_id = create_item(item.dict())
        return {"id": str(item_id)}
    except Exception as e:
        print(f"Error creating item: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/items/{name}", response_model=dict)
def read_item_endpoint(name: str):
    try:
        item = read_item({"name": name})
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    except Exception as e:
        print(f"Error reading item: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/items/", response_model=List[dict])
def read_all_items_endpoint():
    try:
        items = read_all_items()
        return items
    except Exception as e:
        print(f"Error reading all items: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/items/{name}", response_model=dict)
def update_item_endpoint(name: str, item: UpdateItem):
    try:
        update_count = update_item({"name": name}, item.dict(exclude_unset=True))
        if update_count == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"updated": update_count}
    except Exception as e:
        print(f"Error updating item: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/items/{name}", response_model=dict)
def delete_item_endpoint(name: str):
    try:
        delete_count = delete_item({"name": name})
        if delete_count == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"deleted": delete_count}
    except Exception as e:
        print(f"Error deleting item: {e}")
        raise HTTPException(status_code=500, detail=str(e))
