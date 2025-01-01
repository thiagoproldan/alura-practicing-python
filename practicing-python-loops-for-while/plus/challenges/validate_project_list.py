"""
Ana is developing her portfolio to showcase the Python projects she has completed.
She organized a list with the name of each project but noticed that some items might be missing, appearing as None:

projects = ["website", "game", "data analysis", None, "mobile app"]

Create a program to help Ana iterate through the project list and display the names of the valid projects.
If it encounters a None item, the program should display the message: "Project missing".

Expected output:
website
game
data analysis
Project missing
mobile app
"""

projects = ["website", "game", "data analysis", None, "mobile app"]

for project in projects:
    print(f"Project: {project if project is not None else 'Project missing'}") # Terenary operator to check if the project is not None. If it is, the message "Project missing" is displayed. Otherwise, the project name is displayed.

"""
for project in projects:
    if project is None:
        print("Project missing")
    else:
        print(project)
"""