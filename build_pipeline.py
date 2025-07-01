import json
import yaml
from task_actions import AddTextTask, AddWebTask, AddQuestionTask

def get_task_order():
    pass

# TODO fix the headings (eg. system 1 task 1) to not be randomized
# TODO add questions after each figma
# TODO cleanup this function
def build_task_pipeline(used_order="task_order"):
    # Load task order JSON
    with open("task_order.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        task_order = data[used_order]

    # Rotate the task list
    task_order = task_order[1:] + task_order[:1]
    data[used_order] = task_order  # update only the selected list

    # Save updated task order back to JSON
    with open("task_order.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    if used_order == "task_order_jp":
        task_list_yaml = "task_list_jp.yaml"
    else:
        task_list_yaml = "task_list.yaml"

    # Load task list YAML
    with open(task_list_yaml, "r", encoding="utf-8") as f:
        TASK_LIST = yaml.safe_load(f)

    # Build pipeline
    task_pipeline = [
        AddTextTask(TASK_LIST["PRE_EXPERIMENT_TEXT"], TASK_LIST["PRE_EXPERIMENT_BUTTON_TEXT"]),
        AddTextTask(TASK_LIST["INTRODUCTION_TEXT"], TASK_LIST["INTRODUCTION_BUTTON_TEXT"]),
    ]

    # Build tasks from the task_order list of dicts
    for task in task_order:
        task_text = TASK_LIST[task["TEXT"]]
        task_url = TASK_LIST[task["WEBSITE_URL"]]

        task_pipeline.append(AddTextTask(task_text, TASK_LIST["TASK_START_TEXT"]))
        task_pipeline.append(AddWebTask(task_url))
        
        if "QUESTION" in task:
            task_question = TASK_LIST[task["QUESTION"]]
            task_pipeline.append(AddQuestionTask(task_question, TASK_LIST["QUESTION_BUTTON_TEXT"]))

    task_pipeline.append(AddTextTask(TASK_LIST["POST_EXPERIMENT_TEXT"], TASK_LIST["POST_EXPERIMENT_BUTTON_TEXT"]))

    return task_pipeline


def build_task_pipeline_japanese():
    return build_task_pipeline("task_order_jp")