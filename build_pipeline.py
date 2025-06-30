import json
import yaml
from task_actions import AddTextTask, AddWebTask

# Load YAML
with open("task_list.yaml", "r", encoding="utf-8") as f:
    TASK_LIST = yaml.safe_load(f)

def build_task_pipeline(used_order="task_order"):
    with open("task_order.json", "r") as f:
        data = json.load(f)
        task_order = data[used_order]

    # Rotate task list
    task_order = task_order[1:] + task_order[:1]

    # Save rotated task order
    with open("task_order.json", "w") as f:
        json.dump({"task_order": task_order}, f, indent=2)

    # Build pipeline
    task_pipeline = [
        AddTextTask(TASK_LIST["PRE_EXPERIMENT_TEXT"], TASK_LIST["PRE_EXPERIMENT_BUTTON_TEXT"]),
        AddTextTask(TASK_LIST["INTRODUCTION_TEXT"], TASK_LIST["INTRODUCTION_BUTTON_TEXT"]),
    ]

    website_url = TASK_LIST["WEBSITE_URL"]

    for name in task_order:
        task_pipeline.append(AddTextTask(TASK_LIST[name], TASK_LIST["TASK_START_TEXT"]))
        task_pipeline.append(AddWebTask(website_url))

    task_pipeline.append(AddTextTask(TASK_LIST["POST_EXPERIMENT_TEXT"], "Done"))

    return task_pipeline