from task_order import task_order  # load current order
import TASK_LIST  # your constants module
from task_actions import *
# Rotate left by 1
task_order = task_order[1:] + task_order[:1]

# Save the rotated order back to file
with open("task_order.py", "w") as f:
    f.write(f"task_order = {task_order}\n")

# Map task names to actual TASK_LIST attributes
task_texts = [getattr(TASK_LIST, name) for name in task_order]

# Build the pipeline
task_pipeline = [
    AddTextTask(TASK_LIST.PRE_EXPERIMENT_TEXT, TASK_LIST.PRE_EXPERIMENT_BUTTON_TEXT),
]

for text in task_texts:
    task_pipeline.append(AddTextTask(text, TASK_LIST.TASK_START_TEXT))
    task_pipeline.append(AddWebTask(TASK_LIST.WEBSITE_URL_1))

task_pipeline.append(AddTextTask(TASK_LIST.POST_EXPERIMENT_TEXT, "Done"))

print(task_pipeline)
