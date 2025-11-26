class Asset:
    def __init__(self, data: dict):
        self.asset_id = data.get("asset_id")
        self.asset_tag = data.get("asset_tag")
        self.asset_type = data.get("asset_type")
        self.serial_number = data.get("serial_number")
        self.manufacturer = data.get("manufacturer")
        self.model = data.get("model")
        self.purchase_date = data.get("purchase_date")
        self.warranty_years = data.get("warranty_years")
        self.assigned_to = data.get("assigned_to")
        self.asset_status = data.get("asset_status")
        self.last_updated = data.get("last_updated")

    def __repr__(self):
        return f"<Asset {self.asset_id}: {self.asset_tag}, {self.asset_status}>"
