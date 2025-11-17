from order_processor import OrderProcessor
 
if __name__ == "__main__":
    processor = OrderProcessor(
        input_file="orders_raw.csv",
        processed_file="orders_processed.csv",
        skipped_file="orders_skipped.csv"
    )
 
    processor.process()
    
    
#     Processing Complete!
# Valid records → 86
# Skipped records → 64
# Skip summary → {'empty_row': 0, 'customer_name_missing': 4, 'invalid_state': 2, 'invalid_quantity': 37, 'invalid_price': 21, 'other_error': 0, 'total_skipped': 64}