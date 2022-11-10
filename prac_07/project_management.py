import datetime
from project import Project

FILENAME = "projects.txt"
MENU = " - (L)oad projects \n - (S)ave projects \n - (D)isplay projects \n - (F)ilter projects by date " \
       "\n - (A)dd new project \n - (U)pdate project \n - (Q)uit "


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":

        elif choice == "A":
            add(projects)
        elif choice == "U":
            update(projects)
        print(MENU)
        choice = input(">>> ").upper()
        save_projects(projects, FILENAME)

    # def add(projects):


def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strftime(parts[1], '%d/%m/%y')
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    with open(filename, "w", encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.datetime.strftime('%d/%m/%y')}\t{project.priority}"
                  f"{project.cost_estimate}\t {project.percent_complete}", file=out_file)


def display_projects(projects):
    print("Incomplete Projects: ")
    incomplete_projects = [project for project in projects if not projects.is_complete]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Completed projects: ")
    completed_projects = [project for project in projects if projects.is_complete]
    completed_projects.sort()
    for project in completed_projects:
        print(" ", project)


def update(projects):
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    try:
        percent_complete = int(input("New percentage: "))
        project.percent_complete = percent_complete
    except ValueError:
        pass
    try:
        priority = int(input("New priority: "))
        project.priority = priority
    except ValueError:
        pass


main()
