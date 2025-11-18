import csv
import os
from typing import Dict

class Inventory:
    def __init__(self, items: Dict[str, int]):
        self.items=items

    @classmethod
    def from_csv(cls, path: str)->'Inventory':
        cls.create_sample_data()
        items={}
        with open(path, mode='r', newline='') as file:
            reader=csv.DictReader(file)
            for row in reader:
                items[row['item_id']]=int(row['available_stock'])
        return cls(items)

    @classmethod
    def create_sample_data(cls):
        data_dir='data'
        inventory_file=os.path.join(data_dir, 'inventory.csv')
        orders_file=os.path.join(data_dir, 'orders.csv')

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        inventory_data=[
            {"item_id": "ITM1", "available_stock": "5"},
            {"item_id": "ITM2", "available_stock": "2"}
        ]

        orders_data=[
            {"order_id": "O1", "item_id": "ITM1", "quantity": "2"},
            {"order_id": "O2", "item_id": "ITM1", "quantity": "4"},
            {"order_id": "O3", "item_id": "ITM2", "quantity": "1"},
            {"order_id": "O4", "item_id": "ITM999", "quantity": "1"}
        ]

        if not os.path.exists(inventory_file):
            with open(inventory_file, mode='w', newline='') as file:
                fieldnames=['item_id', 'available_stock']
                writer=csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(inventory_data)
            print(f"Created {inventory_file}")

        if not os.path.exists(orders_file):
            with open(orders_file,mode='w',newline='') as file:
                fieldnames=['order_id', 'item_id', 'quantity']
                writer=csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(orders_data)
            print(f"Created {orders_file}")

    def allocate(self,item_id: str,qty: int)->bool:
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id]-=qty
            return True
        return False

    def release(self,item_id: str,qty: int)->None:
        if item_id in self.items:
            self.items[item_id]+=qty
