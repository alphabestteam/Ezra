class Task:
    _finishing_date: int
    _developer_association: object
    _reward: int
    _task_done: bool

    def __init__(
        self,
        description: str,
        opening_date: int,
        project_association: object,
        days: int,
        complexity: int,
    ):
        self._description = description
        self._opening_date = opening_date
        self._finishing_date = 0
        self._project_association = project_association
        self._days = days
        self._complexity = complexity
        self._developer_association = None
        self._reward = 0
        self._task_done = False

    def __str__(self) -> str:
        return f"description: {self.description} \nopening date: {self.opening_date} \nfinishing data: {self.finishing_date} \nproject association: {self._project_association} \ndays: {self._days} \ncomplexity: {self._complexity} \ndeveloper association: {self._developer_association} \nreward: {self._reward} \ntask done: {self._task_done}"

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, new_description) -> None:
        self._description = new_description

    @property
    def opening_date(self) -> int:
        return self._opening_date

    @property
    def finishing_date(self) -> int:
        return self._finishing_date

    @finishing_date.setter
    def finishing_date(self, new_finishing_date) -> None:
        self._finishing_date = new_finishing_date

    @property
    def project_association(self) -> object:
        return self._project_association

    @project_association.setter
    def project_association(self, new_project_association) -> None:
        self._project_association = new_project_association

    @property
    def days(self) -> int:
        return self._days

    @days.setter
    def days(self, new_days) -> None:
        self._days = new_days

    @property
    def complexity(self) -> int:
        return self._complexity

    @complexity.setter
    def complexity(self, new_complexity) -> None:
        self._complexity = new_complexity

    @property
    def developer_association(self) -> object:
        return self._developer_association

    @developer_association.setter
    def developer_association(self, new_developer_association) -> None:
        self._developer_association = new_developer_association

    @property
    def reward(self) -> int:
        return self._reward

    @reward.setter
    def reward(self, new_reward) -> None:
        self._reward = new_reward

    @property
    def task_done(self) -> bool:
        return self._task_done

    @task_done.setter
    def task_done(self, new_task_done) -> None:
        self._task_done = new_task_done

    def association_to_developer(self, developer: object) -> None:
        self.developer_association = developer
        self.reward(self, developer.seniority * self.complexity / self.days)
