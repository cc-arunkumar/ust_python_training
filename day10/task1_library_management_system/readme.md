## Commands

### **Book Management:**
- `1`: Add Book
- `2`: Update Book
- `3`: Remove Book
- `4`: Get Book Details
- `5`: List Books
- `6`: Search Books

### **User Management:**
- `7`: Add User
- `8`: Update User
- `9`: Get User Details
- `10`: List Users
- `11`: Deactivate/Activate/Ban User

### **Transaction Management:**
- `12`: Borrow Book
- `13`: Return Book
- `14`: View Active Loans
- `15`: View Overdue Loans
- `16`: View User Loan History

### **Miscellaneous:**
- `17`: Save Data to CSV
- `18`: Exit
- `19`: Help

## CSV File Format

The system reads and writes data from the following CSV files:

### **Books**:

- book_id, title, authors, isbn, tags, total_copies, available_copies

### **Users**:

- user_id, name, email, status, max_loans, password

### **Transactions**:

- tx_id, book_id, user_id, borrow_date, due_date, return_date, status


## Contributing

- If you'd like to contribute to this project, feel free to fork it and submit a pull request. Please ensure that any changes you make are well-documented.

## License

- This project is open-source and available under the MIT License.
