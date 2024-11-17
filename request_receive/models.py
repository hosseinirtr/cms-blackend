from django.db import models
from django.core.validators import URLValidator


class TeammateRequest(models.Model):
    ROLE_CHOICES = [
        # Team Management Roles
        ("team_leader", "Team Leader"),
        ("project_manager", "Project Manager"),
        ("finance_sponsorship_manager", "Finance & Sponsorship Manager"),
        # Technical Roles
        ("powertrain_engineer", "Powertrain Engineer"),
        ("fuel_system_engineer", "Fuel System Engineer"),
        ("cooling_system_engineer", "Cooling System Engineer"),
        (
            "battery_management_system_engineer",
            "Battery Management System (BMS) Engineer",
        ),
        ("chassis_engineer", "Chassis Engineer"),
        ("bodywork_aerodynamics_engineer", "Bodywork & Aerodynamics Engineer"),
        ("suspension_engineer", "Suspension Engineer"),
        ("steering_brakes_engineer", "Steering & Brakes Engineer"),
        ("electronics_engineer", "Electronics Engineer"),
        ("control_systems_engineer", "Control Systems Engineer"),
        ("software_telemetry_engineer", "Software & Telemetry Engineer"),
        ("transmission_engineer", "Transmission Engineer"),
        ("driveline_engineer", "Driveline Engineer"),
        # Vehicle Dynamics
        ("vehicle_dynamics_engineer", "Vehicle Dynamics Engineer"),
        ("simulation_testing_engineer", "Simulation & Testing Engineer"),
        # Manufacturing & Materials
        ("manufacturing_engineer", "Manufacturing Engineer"),
        ("materials_engineer", "Materials Engineer"),
        # Testing & Validation
        ("testing_engineer", "Testing Engineer"),
        ("data_analysis_engineer", "Data Analysis Engineer"),
        # Business & Marketing
        ("business_plan_manager", "Business Plan Manager"),
        ("marketing_media_manager", "Marketing & Media Relations"),
        ("event_coordinator", "Event Coordinator"),
        # Driver & Pit Crew
        ("driver", "Driver"),
        ("pit_crew", "Pit Crew"),
        # Safety & Compliance
        ("safety_officer", "Safety Officer"),
        ("compliance_engineer", "Compliance Engineer"),
        # Autonomous Systems (for Driverless Teams)
        ("autonomous_systems_engineer", "Autonomous Systems Engineer"),
        ("computer_vision_engineer", "Computer Vision Engineer"),
        ("lidar_sensor_integration_engineer", "LIDAR & Sensor Integration Engineer"),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ("undergraduate", "Undergraduate"),
        ("postgraduate", "Postgraduate"),
        ("phd", "PhD"),
        ("other", "Other"),
    ]

    STUDY_INTENTION_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=13)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    resume = models.FileField(upload_to="resumes/")
    linkedin = models.TextField(validators=[URLValidator()])
    website = models.TextField(validators=[URLValidator()])
    # fields for education
    last_education_academy_name = models.CharField(max_length=200)
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    wants_further_study = models.BooleanField(choices=STUDY_INTENTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_role_display()}"


class SponsorRequest(models.Model):
    SPONSORSHIP_TYPE_CHOICES = [
        ("financial", "Financial"),
        ("equipment", "Equipment"),
        ("services", "Services"),
        ("other", "Other"),
    ]

    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100,)
    company_website = models.TextField(validators=[URLValidator()])

    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
    )
    sponsorship_type = models.CharField(max_length=20, choices=SPONSORSHIP_TYPE_CHOICES)
    message = models.TextField(
        help_text="Describe your sponsorship offer or any questions."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.get_sponsorship_type_display()}"
