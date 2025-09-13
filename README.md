# UniCoursePlanner

I developed a Python program that helps university professors plan their weekly schedules for attending the university. This program uses the **CSP Forward Checking** algorithm to generate weekly timetables for professors.

**Demo video:** [https://youtu.be/4Y8TF79PDTs](https://youtu.be/4Y8TF79PDTs)

## Key Features

- **Comprehensive Input:**  
    The program fully collects all necessary information, including professors’ available hours, course names and codes, and their assigned professors.
    
- **Data Intake:**  
    It accepts professor codes, course information, and their weekly schedules as input, which are essential for generating the final timetable.
    
- **Credit Assignment:**  
    Each course is assumed to be 3 credits, and the program assigns two time slots per course within the weekly schedule.
    
- **Conflict-Free Scheduling:**  
    The program schedules courses so that a professor’s classes never overlap, and courses given as input (e.g., courses A and B, both in semester 5) do not conflict either.
    
- **Single Instructor per Course:**  
    Each course is assigned to only one professor; the program ensures no course is taught by multiple instructors.
    

## Output

The program produces multiple HTML files that display the weekly schedules, highlighting the days professors are available on campus without conflicts.
