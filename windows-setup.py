import os

script_path = os.path.abspath("ping_tool.py")
task_name = "PingTool"

# Create task: runs hourly
cmd = f'schtasks /Create /TN "{task_name}" /TR "pythonw {script_path}" /SC HOURLY /F'

os.system(cmd)
print("Task Scheduler job installed.")
