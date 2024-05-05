# pip install datasets
# docs: https://huggingface.co/docs/datasets/process


from datasets import load_dataset
from datasets.dataset_dict import DatasetDict, Dataset

dataset_dict: DatasetDict = load_dataset("fka/awesome-chatgpt-prompts")
# columns: act, prompt

print(type(dataset_dict))  # <class 'datasets.dataset_dict.DatasetDict'>
print(dataset_dict)

copy = dataset_dict.copy()
print(copy)

dataset: Dataset = copy['train']

print(dataset.num_columns)
print(dataset.num_rows)
# print(dataset.__dict__)


# get one row by filtering
linux_terminal = dataset_dict.filter(lambda example: example["act"].startswith("Linux Terminal"))
print(linux_terminal)
print(len(linux_terminal))
print(linux_terminal['train']['prompt'])

# from_csv
# from_text
# from_sql
# from_spark
# ...
