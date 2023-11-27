import datetime


class Task:
    _finishing_date: datetime
    _developer_association: object
    _reward: float
    _task_done: bool

    def __init__(
        self,
        description: str,
        opening_date: datetime,
        project_association: object,
        days: int,
        complexity: int,
    ):
        self._description = description
        self._opening_date = opening_date
        self._days = days
        self._finishing_date = self.opening_date + \
            datetime.timedelta(days=self.days)
        self._project_association = project_association
        self._complexity = complexity
        self._developer_association = None
        self._reward = 0.0
        self._task_done = False

    def __str__(self) -> str:
        return f"description: {self.description} \nopening date: {self.opening_date} \nfinishing data: {self.finishing_date} \nproject association: {self.project_association} \ndays: {self.days} \ncomplexity: {self.complexity} \ndeveloper association: {self.developer_association} \nreward: {self.reward} \ntask done: {self.task_done}"

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

    @property
    def project_association(self) -> object:
        return self._project_association

    @project_association.setter
    def project_association(self, new_project_association: object) -> None:
        raise Exception

    @property
    def days(self) -> int:
        return self._days

    @days.setter
    def days(self, new_days: int) -> None:
        self._days = new_days

    @property
    def complexity(self) -> int:
        return self._complexity

    @complexity.setter
    def complexity(self, new_complexity: int) -> None:
        self._complexity = new_complexity

    @property
    def developer_association(self) -> object:
        return self._developer_association

    @developer_association.setter
    def developer_association(self, new_developer_association: object) -> None:
        self._developer_association = new_developer_association
        new_developer_association.tasks_todo.append(self)
        self.reward = new_developer_association.seniority * self.complexity / self.days
        self.project_association.developer_list.append(
            new_developer_association)

    @property
    def reward(self) -> int:
        return self._reward

    @reward.setter
    def reward(self, new_reward: float) -> None:
        self._reward = new_reward

    @property
    def task_done(self) -> bool:
        return self._task_done

    @task_done.setter
    def task_done(self, new_task_done: bool) -> None:
        self._task_done = new_task_done
        if self.task_done == True:
            self.project_association.finished_task(self)
