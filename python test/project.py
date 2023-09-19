import datetime


class Project:
    _finishing_date: datetime
    _tasks_todo: list
    _tasks_done: list
    _project_cost: int
    _project_done: bool
    task_list: list
    _developer_list: list

    def __init__(
        self,
        description: str,
        opening_date: datetime,
    ) -> None:
        self._description = description
        self._opening_date = opening_date
        self._finishing_date = 0
        self._task_list = []
        self._developer_list = []
        self._tasks_todo = []
        self._tasks_done = []
        self._project_cost = 0
        self._project_done = False

    def __str__(self) -> str:
        return f"description: {self.description} \nopening date: {self.opening_date} \nfinishing data: {self.finishing_date} \ntask list: {self.task_list} \ndeveloper list: {self.developer_list} \ntasks todo: {self.tasks_todo} \ntasks done: {self.tasks_done} \nproject cost: {self.project_cost} \nproject done: {self.project_done}"

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        self._description = new_description

    @property
    def opening_date(self) -> datetime:
        return self._opening_date

    @property
    def finishing_date(self) -> datetime:
        return self._finishing_date

    @finishing_date.setter
    def finishing_date(self, new_finishing_date: datetime) -> None:
        self._finishing_date = new_finishing_date

    @property
    def task_list(self) -> list:
        return self._task_list

    @property
    def developer_list(self) -> list:
        return self._developer_list

    @property
    def tasks_todo(self) -> list:
        return self._tasks_todo

    @property
    def tasks_done(self) -> bool:
        return self._tasks_done

    @property
    def project_cost(self) -> int:
        return self._project_cost

    @project_cost.setter
    def project_cost(self, new_project_cost: int) -> None:
        self._project_cost = new_project_cost

    @property
    def project_done(self) -> bool:
        return self._project_done

    @project_done.setter
    def project_done(self, new_project_done: bool) -> None:
        self._project_done = new_project_done
        if self.project_done == True:
            for days in self.tasks_done:
                self.finishing_date + datetime.timedelta(days=days)
            print(f"project {self.description} is done! \n")
            print(self)

    def add_task(self, new_task: object) -> None:
        if new_task not in self.task_list:
            self.task_list.append(new_task)
            self.tasks_todo.append(new_task)

    def remove_task(self, task_r: object) -> None:
        if task_r in self.tasks_todo:
            self.tasks_todo.remove(task_r)
            for developer in self.developer_list:
                if task_r in developer.tasks_todo:
                    developer.tasks_todo.remove(task_r)
                    break

    # fix this, maybe needs to be a dictionary

    def search_task(self, task_s: object) -> object:
        if task_s in self.task_list:
            return self.task_list[task_s]

    def finished_task(self, task: object) -> None:
        self.remove_task(task)
        self._tasks_done.append(task)
        self.project_cost += task.reward
        if len(self.tasks_todo) == 0:
            self.project_done == True
