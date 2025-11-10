#Task1: UST Employee DailyWork Report Automation System
from Task1_WelcomeMessage import welcome_msg
from Task4_Current_ProjectName import current_active_project_name
from Task2_Efficiency_score import efficiency_score 
from Task3_Performance_Calculator import overview_performance
from Task5_Average_EfficiencyScore import avg_efficiency_score



welcome_msg()
print(current_active_project_name())
eff_of_asha=efficiency_score(30,8)
eff_of_rahul=efficiency_score(45,10)
eff_of_sneha=efficiency_score(45,15)
overview_performance("Asha","Finance",eff_of_asha)
overview_performance("Asha","Finance",eff_of_rahul)
overview_performance("Sneha","HR",eff_of_sneha)
print(avg_efficiency_score(eff_of_sneha,eff_of_asha,eff_of_rahul))
