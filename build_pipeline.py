import random
import yaml
from task_actions import AddTextTask, AddWebTask, AddQuestionTask

shuffled_indices_en = []
shuffled_indices_jp = []

def build_task_pipeline(used_order="task_order"):
    global shuffled_indices_en, shuffled_indices_jp

    # === Load Latin square task order ===
    with open("task_order.yaml", "r", encoding="utf-8") as f:
        latin_square_result = yaml.safe_load(f)["latin_square_task_order"]

    # === Choose task list ===
    if used_order == "task_order_jp":
        task_list_file = "task_list_jp.yaml"
        pool = shuffled_indices_jp
    else:
        task_list_file = "task_list.yaml"
        pool = shuffled_indices_en

    with open(task_list_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    task_map = data["TASK_MAP"]

    # === Draw a row index (random, without replacement) ===
    if not pool:
        pool.extend(random.sample(range(len(latin_square_result)), len(latin_square_result)))

    row_idx = pool.pop()
    selected_labels = latin_square_result[row_idx]

    print(f"[INFO] Using row index: {row_idx}")
    print(f"[INFO] Task labels: {selected_labels}")
    print(f"[INFO] Remaining in pool ({'JP' if used_order == 'task_order_jp' else 'EN'}): {pool}")

    pipeline = [
        AddTextTask(data["PRE_EXPERIMENT_TEXT"], data["PRE_EXPERIMENT_BUTTON_TEXT"]),
        AddTextTask(data["INTRODUCTION_TEXT"], data["INTRODUCTION_BUTTON_TEXT"])
    ]

    for label in selected_labels:
        version = label[0]      # 'A' or 'B'
        task_num = label[1:]    # '1', '2', etc.
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