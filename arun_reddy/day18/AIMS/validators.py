def validating(categories):
    valid_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    try:
        asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, asset_id = categories

        # asset_tag check removed since you don't pass it
        if asset_type not in valid_types:
            raise Exception("Invalid asset_type")
        if warranty_years <= 0:
            raise Exception("Warranty years must be greater than 0")
        if asset_status == "Assigned" and assigned_to is None:
            raise Exception("assigned_to must not be null when asset_status is Assigned")
        if asset_status in ["Available", "Retired"] and assigned_to is not None:
            raise Exception("assigned_to must be NULL")
        return "valid"
    except Exception as e:
        print("Validation Error:", e)
        return "invalid"
