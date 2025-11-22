from pydantic import BaseModel, Field

class Employee(BaseModel):
    emp_id: int = Field(..., ge=1000, le=999999)
    name: str = Field(..., min_length=2)
    department: str = Field(default="General")

class SIM(BaseModel):
    number: str = Field(..., re=r"^\d{10}$")
    provider: str = Field(default="Jio")
    activation_year: int = Field(..., ge=2020, le=2025)

class Registration(BaseModel):
    employee: Employee
    sim: SIM

def run_tests():
    print("\nSuccess Case:")
    data_valid = {
        "employee": {"emp_id": 12345, "name": "Asha", "department": "Engineering"},
        "sim": {"number": "9876543210", "provider": "Airtel", "activation_year": 2023}
    }
    reg1 = Registration(**data_valid)
    print(reg1)

    print("\nDefault Assignment Case:")
    data_defaults = {
        "employee": {"emp_id": 12345, "name": "Asha"},
        "sim": {"number": "9876543210", "activation_year": 2023}
    }
    reg2 = Registration(**data_defaults)
    print(reg2)

    print("\nValidation Error Cases:")
    test_cases = [
        {"employee": {"emp_id": 999, "name": "Asha"}, "sim": {"number": "9876543210", "activation_year": 2023}},
        {"employee": {"emp_id": 12345, "name": "A"}, "sim": {"number": "9876543210", "activation_year": 2023}},
        {"employee": {"emp_id": 12345, "name": "Asha"}, "sim": {"number": "12345", "activation_year": 2023}},
        {"employee": {"emp_id": 12345, "name": "Asha"}, "sim": {"number": "9876543210", "activation_year": 2019}},
        {"employee": {"emp_id": 12345, "name": "Asha"}, "sim": {"number": "9876543210", "activation_year": 2030}},
    ]

    for i, case in enumerate(test_cases, start=1):
        try:
            print(f"\nTest {i}:")
            Registration(**case)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run_tests()
