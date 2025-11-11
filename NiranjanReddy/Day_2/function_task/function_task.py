from part_1_welcome import welcome_message
from part_2_efficiency import efficiency_score
from part_3_employee_report import formatted_report
from part_4_project_name import project_name
from part_5_average import average_efficiency_score

welcome_message()

print(project_name())

efficiency_1=efficiency_score(10,11)
efficiency_2=efficiency_score(8,9)
efficiency_3=efficiency_score(4,8)

formatted_report("Asha", "Finance", efficiency_1)
formatted_report("Rahul", "IT",efficiency_2)
formatted_report("Sneha","HR", efficiency_3)

average_efficiency_score(efficiency_1,efficiency_2,efficiency_3)