from fastapi import FastAPI, HTTPException, APIRouter
from typing import Optional
from ..models.assetsinventory import AssetInventory, StatusValidate
from ..crud.asset_crud import AssetCrud

# Initialize the AssetCrud instance to interact with the asset database
asset_reader = AssetCrud()

# Create the APIRouter instance for asset-related routes with a prefix "/asset"
asset_router = APIRouter(prefix="/asset")

# Route to create a new asset record in the database
@asset_router.post("/create")
def create_asset(asset: AssetInventory):
    try:
        # Call the create_asset method from AssetCrud to insert the asset
        return asset_reader.create_asset(asset)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a list of all assets, or filter by status
@asset_router.get("/list")
def get_all_asset(status: Optional[str] = "ALL"):
    try:
        # Call the get_all_asset method from AssetCrud to fetch assets by status
        return asset_reader.get_all_asset(status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve a specific asset by its ID
@asset_router.get("/{id}")
def get_asset_by_id(id: int):
    try:
        # Call the get_asset_by_id method from AssetCrud to fetch asset by ID
        return asset_reader.get_asset_by_id(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update a specific asset by its ID
@asset_router.put("/{id}")
def update_asset(id: int, data: AssetInventory):
    try:
        # Call the update_asset method from AssetCrud to update asset by ID
        return asset_reader.update_asset(id, data)
    except Exception as e:
        # Log the error and raise a 404 HTTPException with a message
        print(str(e))
        raise HTTPException(status_code=404, detail="Not Found")

# Route to update the status of a specific asset by its ID
@asset_router.patch("/{id}/status")
def update_asset_status(id: int, status: StatusValidate):
    try:
        # Print the status for debugging purposes
        print(status)
        # Call the update_asset_status method from AssetCrud to update the asset's status
        return asset_reader.update_asset_status(id, status.asset_status)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to delete a specific asset by its ID
@asset_router.delete("/{id}")
def delete_asset(id: int):
    try:
        # Call the delete_asset method from AssetCrud to delete the asset by ID
        return asset_reader.delete_asset(id)
    except Exception:
        # If an error occurs, raise a 404 HTTPException with a message
        raise HTTPException(status_code=404, detail="Not Found")

# Route to search for an asset by a specific keyword (e.g., 'asset_tag') and value
@asset_router.get("/search/keyword")
def get_asset_by_keyword(keyword: str, value: str):
    try:
        # Call the get_asset_by_keyword method from AssetCrud to search assets
        return asset_reader.get_asset_by_keyword(keyword, value)
    except Exception as e:
        # Log the error and raise a 404 HTTPException with a message
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")

# Route to retrieve the count of all assets
@asset_router.get("/list/count")
def get_count():
    try:
        # Call the get_all_asset_count method from AssetCrud to get the asset count
        return asset_reader.get_all_asset_count()
    except Exception as e:
        # Log the error and raise a 404 HTTPException with a message
        print(e)
        raise HTTPException(status_code=404, detail="Not Found")
