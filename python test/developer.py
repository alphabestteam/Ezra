class Developer:
    _tasks_done: list
    _work_days: int
    _overall_reward: float
    _tasks_todo: list
    _seniority: int

    def __init__(self, name: str) -> None:
        self._name = name
        self._tasks_done = []
        self._work_days = 0
        self._overall_reward = 0.0
        self._tasks_todo = []
        self._seniority = 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def tasks_done(self) -> list:
        return self._tasks_done

    @property
    def work_days(self) -> int:
        return self._work_days

    @work_days.setter
    def work_days(self, new_work_days: int) -> None:
        self._work_days = new_work_days

    @property
    def overall_reward(self) -> int:
        return self._overall_reward

    @overall_reward.setter
    def overall_reward(self, new_overall_reward: float) -> None:
        self._overall_reward = new_overall_reward

    @property
    def tasks_todo(self) -> list:
        return self._tasks_todo

    @property
    def seniority(self) -> int:
        return self._seniority

    @seniority.setter
    def seniority(self, new_seniority: int) -> None:
        self._seniority = new_seniority

    def done_task(self, task: object) -> None:
        if task in self.tasks_todo:
            self.tasks_done.append(task)
            self.tasks_todo.remove(task)
            self.work_days += task.days
            self.seniority += task.complexity
            self.overall_reward += task.reward
            task.task_done = True
        else:
            raise Exception
