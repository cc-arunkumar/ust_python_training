
from crud.asset_crud import create_asset, read_all_assets, read_asset_by_id,  delete_asset

print(create_asset('UST-LTP-0025', 'Laptop', 'SN-DL-9988124', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available'))
# print(read_all_assets())
# print(read_asset_by_id(1))
# print(update_asset(1, asset_status="Repair"))
# print(delete_asset(2))
