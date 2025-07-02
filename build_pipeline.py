import random
import yaml
import os
from task_actions import AddTextTask, AddWebTask, AddQuestionTask

def save_shuffle(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f)

def load_shuffle(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if data:
                return data
    return None


# TODO fix title (System 1 & 2 to not be shuffled)
def build_task_pipeline(used_order="task_order"):
    with open("task_order.yaml", "r", encoding="utf-8") as f:
        latin_square_result = yaml.safe_load(f)["latin_square_task_order"]

    if used_order == "task_order_jp":
        task_list_file = "task_list_jp.yaml"
        shuffle_file = "shuffled_order_jp.yaml"
    else:
        task_list_file = "task_list.yaml"
        shuffle_file = "shuffled_order_en.yaml"

    with open(task_list_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    task_map = data["TASK_MAP"]

    pool = load_shuffle(shuffle_file)
    if not pool:
        pool = random.sample(range(len(latin_square_result)), len(latin_square_result))
        save_shuffle(shuffle_file, pool)

    row_idx = pool.pop()
    save_shuffle(shuffle_file, pool)

    selected_labels = latin_square_result[row_idx]

    print(f"[INFO] Using row index: {row_idx}")
    print(f"[INFO] Task labels: {selected_labels}")
    print(f"[INFO] Remaining in pool ({'JP' if used_order == 'task_order_jp' else 'EN'}): {pool}")

    pipeline = [
        AddTextTask(data["PRE_EXPERIMENT_TEXT"], data["PRE_EXPERIMENT_BUTTON_TEXT"]),
        AddTextTask(data["INTRODUCTION_TEXT"], data["INTRODUCTION_BUTTON_TEXT"])
    ]

    for label in selected_labels:
        version = label[0]
        task_num = label[1:]
        task_key = f"TASK{task_num}"

        if task_key not in task_map:
            raise KeyError(f"Missing task: {task_key}")

        task = task_map[task_key]
        pipeline.append(AddTextTask(task["TASK_TEXT"], data["TASK_START_TEXT"]))
        pipeline.append(AddWebTask(task["FIGMA_URL"][f"VERSION_{version}"]))

        if "QUESTION" in task:
            pipeline.append(AddQuestionTask(task["QUESTION"], data["QUESTION_BUTTON_TEXT"]))

    pipeline.append(AddTextTask(data["POST_EXPERIMENT_TEXT"], data["POST_EXPERIMENT_BUTTON_TEXT"]))
    return pipeline

def build_task_pipeline_japanese():
    return build_task_pipeline("task_order_jp")
