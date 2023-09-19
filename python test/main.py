from developer import Developer
from project import Project
from task import Task


def main():
    project1 = Project('project 1', (2023, 1, 1))
    print(project1)
    task1 = Task('task1', (2023, 2, 2), project1, 5, 4)
    project1.add_task(project1)
    print(project1)


if __name__ == '__main__':
    main()
