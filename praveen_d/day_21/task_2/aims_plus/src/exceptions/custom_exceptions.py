class DatabaseConnectionError(Exception):
    def __init__(self, message="Error while connecting to the database"):
        self.message = message
        super().__init__(self.message)

class QueryExecutionError(Exception):
    def __init__(self, query, message="Error while executing the query"):
        self.query = query
        self.message = message
        super().__init__(f"{self.message}: {self.query}")
        
class AssetNotFoundError(Exception):
    def __init__(self, asset_id, message="Asset not found in the inventory"):
        self.asset_id = asset_id
        self.message = f"Asset with ID {self.asset_id} {message}"
        super().__init__(self.message)

class AssetUpdateError(Exception):
    def __init__(self, asset_id, message="Failed to update asset information"):
        self.asset_id = asset_id
        self.message = f"Could not update asset with ID {self.asset_id}. {message}"
        super().__init__(self.message)
