# coding=utf-8
from datetime import datetime
from datetime import timedelta, timezone
from airflow.operators.bash import BaseOperator
from airflow.utils.context import Context
from airflow.utils.decorators import apply_defaults
from airflow.hooks.base import BaseHook
from airflow.models.dagrun import DagRun
from airflow.models.dag import DagModel
from croniter import croniter, croniter_range
from airflow.exceptions import AirflowException
from datetime import datetime
import pytz


"""
pip install apache-airflow==2.2.5
"""

class CheckOperator(BaseOperator):
    """
    使用CheckOperator检查上游任务状态：
    1. 上游与下游的运行周期可以不同，比如每天跑的dag检查每周跑的dag
    2. 下游可配置多个上游，在CheckOperator中一次性检查，而不是使用Airflow自带的ExternalTaskSensor（只能check单个dag）
    3. 任务修改schedule_interval后发布上线后，任务的运行记录失效，下游检查以最新的版本运行记录为依据，
        且dag的新版本上线后，手动触发的任务也在被check的范围之内
    """
    template_fields = ['pids']

    @apply_defaults
    def __init__(self, pids="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pids = pids

    def execute(self, context: Context) -> bool:
        self.log.info("检查上游任务状态: %s" % str(self.pids))
        self.log.info("=========================================检查开始========================================")
        checkhook = CheckHook(
            pids=self.pids
        )
        return checkhook.check()


class CheckHook(BaseHook):
    """
    检查的钩子，根据参数pids（逗号分割的dag列表），一个一个检查状态，所有dag状态为Success则放行，返回True，否则False
    """

    @apply_defaults
    def __init__(self, pids="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pids = pids

    def check(self) -> bool:
        """
        检查的逻辑在这里，一个一个pid去检查，有一个状态未成功，则返回False
        :return:
        """
        # 将pid的状态都放在list中，最后再判断list中是否有false值
        pids_status = []
        pids_list = self.pids.split(",")
        for pid in pids_list:
            self.log.info("--------------------------------------------------------------------------------------")

            # 初始化上游任务状态为False
            pid_status = False

            # 如果上游id为空，则跳过
            if pid == '':
                continue

            # 去除pid左右的空格
            pid = pid.strip()

            # 获取上游的运行记录
            # 根据上游任务的schedule_interval手动生成对应的计划运行时间execution_date，在计划运行时间点的自动触发及计划运行
            # 时间点之后手动触发的dagrun运行记录，均算作在内
            dag: DagModel = DagModel.get_dagmodel(dag_id=pid)

            # 这里使用croniter来解析crontab表达式，获取上游最近一次运行批次（以当前时间为准）
            prev_exec_date = self.get_exec_date(pid, dag.schedule_interval)

            # 查询出上游上次调度到now()的所有dagrun，包含手动触发的批次
            self.log.info("查询dagrun参数dag_id：%s" % pid)
            self.log.info("查询dagrun参数execution_date：%s" % prev_exec_date)
            dagruns: list[DagRun] = DagRun.find(dag_id=pid, execution_start_date=prev_exec_date)
            self.log.info("查询到所有dagrun：" + str(dagruns))
            if len(dagruns) > 0:
                execution_dates = [dagrun.execution_date for dagrun in dagruns]
                index_max = execution_dates.index(max(execution_dates))
                dagrun = dagruns[index_max]
                self.log.info("-- execution_date最大的dag_run: " + str(dagrun))
                if 'success' == dagrun.get_state():
                    pid_status = True
                pids_status.append(pid_status)
                self.log.info("任务：%s的状态为：%s" % (pid, pid_status))
            else:
                self.log.info("-- 未查询到dagrun")
                pids_status.append(pid_status)
                self.log.info("任务：%s的状态为：%s" % (pid, pid_status))
        self.log.info(
            "======================================所有任务检查完成======================================")

        self.log.info("所有的上游任务为：%s" % str(pids_list))
        self.log.info("所有的上游任务状态为：%s" % str(pids_status))

        if False in pids_status:
            raise AirflowException("检查上游任务状态失败，未完成任务为： %s" % (pids_list[pids_status.index(False)]))
        else:
            self.log.info("检查上游所有任务状态成功。")
        return True

    def get_exec_date(self, dag_id: str, schedule_interval: str) -> datetime:
        self.log.info("上游任务【%s】的调度周期：【%s】" % (dag_id, schedule_interval))
        # 取最近一次计划执行时间
        cron = croniter(schedule_interval, datetime.now())
        cron.get_prev()  # airflow中的execution_date为批次的开始时间，所以要执行两次get_prev()才能获取到上个批次的execution_date
        prev = cron.get_prev()
        prev_exec_date = datetime.fromtimestamp(prev, tz=timezone.utc)  # airflow不支持naive datetime
        self.log.info("上游最近一次执行计划时间：%s" % str(prev_exec_date))

        return prev_exec_date

