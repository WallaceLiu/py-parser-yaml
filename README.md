# py-parser-yaml
using python lang, by reflect, parse .yaml file to object instance, 
support inject variables, const...
# example 1
```text
debug: True
name: your_project_name
cmd:
  loc: "./your_spark_file.py"
  option:
    - ["option1", "option 1", "--option1", False, 0]
    - ["option2", "option 2", "--option2", False, 0]
    - ["option3", "option 3", "--option3", False, '{const.TODAY}']
task:
  name: "your_task_{name}"
  spark:
    shell:
      - [--master, yarn-client]
      - [--num-executors, 10]
      - [--executor-memory, 5g]
      - [--executor-cores, 4]
      - [--driver-memory, 10g]
      - [--conf, spark.pyspark.python=python2.7]
      - [--spark.default.parallelism, 100]
  hive: ~
dfs:
  name_node: ns
  data_mart: your_dept
  base: hdfs://{dfs.name_node}/user
  dfs  : "{dfs.base}/{dfs.data_mart}"
  schema  : "{dfs.dfs}/<?e>.db"
model:
  url:
    input:
      - timeseries:
        - "{dfs.schema}/app_your_timeseries/key=sales"
        - "{dfs.schema}/app_your_timeseries/key=priceBeforeDiscount"
        - "{dfs.schema}/app_your_timeseries/key=priceAfterDiscount"
        - "{dfs.schema}/app_your_timeseries/key=stockQuantity"
        - "{dfs.schema}/app_your_timeseries/key=vendibility"
    output:
      dir: "{dfs.dfs}/app_your_forecast_result/dt={v_ps}/forecast_{dc}_{cate}"
      file: "{model.url.output.dir}/result_{period}_{predict}"
```
执行：
```python
print('---------------------------------------')
print('|    Biz Meta Info')
print('---------------------------------------')
op = Env.create("test_demo_complex.yml")
print('     ---------------------------------------')
print('     |    property Result Info')
print('     ---------------------------------------')
print('op.debug', getattr(op, "debug", "<debug> Not Found"))
print('---------------------------------------------------')
print('op.name', getattr(op, "name", "<name> Not Found"))
print('---------------------------------------------------')
print('op.cmd.loc', getattr(op.cmd, "loc", "<loc> Not Found"))
print('op.cmd.option', getattr(op.cmd, "option", "<option> Not Found"))
print('---------------------------------------------------')
print('op.task.name', getattr(op.task, "name", "<name> Not Found"))
print('op.task.spark', getattr(op.task, "spark", "<spark> Not Found"))
print('op.task.hive', getattr(op.task, "hive", "<hive> Not Found"))
print('---------------------------------------------------')
print('op.cmd.loc', getattr(op.cmd, "loc", "<loc> Not Found"))
print('op.cmd.option', getattr(op.cmd, "option", "<option> Not Found"))
print('---------------------------------------------------')
print('op.dfs.name_node', getattr(op.dfs, "name_node", "<name_node> Not Found"))
print('op.dfs.data_mart', getattr(op.dfs, "data_mart", "<data_mart> Not Found"))
print('op.dfs.base', getattr(op.dfs, "base", "<base> Not Found"))
print('op.dfs.dfs', getattr(op.dfs, "dfs", "<dfs> Not Found"))
print('op.dfs.hive', getattr(op.dfs, "hive", "<hive> Not Found"))
print('---------------------------------------------------')
```
结果：
```text
|    Env Meta Info
---------------------------------------
dfs.raw {'debug': True, 'name': 'your_project_name', 'cmd': {'loc': './your_spark_file.py', 'option': [['option1', 'option 1', '--option1', False, 0], ['option2', 'option 2', '--option2', False, 0], ['option3', 'option 3', '--option3', False, '{const.TODAY}']]}, 'task': {'name': 'your_task_{name}', 'spark': {'shell': [['--master', 'yarn-client'], ['--num-executors', 10], ['--executor-memory', '5g'], ['--executor-cores', 4], ['--driver-memory', '10g'], ['--conf', 'spark.pyspark.python=python2.7'], ['--spark.default.parallelism', 100]]}, 'hive': None}, 'dfs': {'name_node': 'ns', 'data_mart': 'your_dept', 'base': 'hdfs://{dfs.name_node}/user', 'dfs': '{dfs.base}/{dfs.data_mart}', 'schema': '{dfs.dfs}/<?e>.db'}, 'model': {'url': {'input': [{'timeseries': ['{dfs.schema}/app_your_timeseries/key=sales', '{dfs.schema}/app_your_timeseries/key=priceBeforeDiscount', '{dfs.schema}/app_your_timeseries/key=priceAfterDiscount', '{dfs.schema}/app_your_timeseries/key=stockQuantity', '{dfs.schema}/app_your_timeseries/key=vendibility']}], 'output': {'dir': '{dfs.dfs}/app_your_forecast_result/dt={v_ps}/forecast_{dc}_{cate}', 'file': '{model.url.output.dir}/result_{period}_{predict}'}}}}
dfs.rawFile test_demo_complex.yml
---------------------------------------
|    property Info
---------------------------------------
env.debug True
---------------------------------------------------
env.name your_project_name
---------------------------------------------------
env.cmd.loc ./your_spark_file.py
env.cmd.option [['option1', 'option 1', '--option1', False, 0], ['option2', 'option 2', '--option2', False, 0], ['option3', 'option 3', '--option3', False, '2018-04-29']]
---------------------------------------------------
env.task.name your_task_your_project_name
env.task.spark.shell [['--master', 'yarn-client'], ['--num-executors', 10], ['--executor-memory', '5g'], ['--executor-cores', 4], ['--driver-memory', '10g'], ['--conf', 'spark.pyspark.python=python2.7'], ['--spark.default.parallelism', 100]]
env.task.hive None
---------------------------------------------------
env.dfs.name_node ns
env.dfs.data_mart your_dept
env.dfs.base hdfs://ns/user
env.dfs.dfs hdfs://ns/user/your_dept
env.dfs.schema hdfs://ns/user/your_dept/dev.db
---------------------------------------------------
env.model.url.input[0].timeseries ['hdfs://ns/user/your_dept/dev.db/app_your_timeseries/key=sales', 'hdfs://ns/user/your_dept/dev.db/app_your_timeseries/key=priceBeforeDiscount', 'hdfs://ns/user/your_dept/dev.db/app_your_timeseries/key=priceAfterDiscount', 'hdfs://ns/user/your_dept/dev.db/app_your_timeseries/key=stockQuantity', 'hdfs://ns/user/your_dept/dev.db/app_your_timeseries/key=vendibility']
env.model.url.output.dir hdfs://ns/user/your_dept/app_your_forecast_result/dt={v_ps}/forecast_{dc}_{cate}
env.model.url.output.file hdfs://ns/user/your_dept/app_your_forecast_result/dt={v_ps}/forecast_{dc}_{cate}/result_{period}_{predict}
```
