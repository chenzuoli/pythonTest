import pandas as pd

data = {'名字': ['张三', '李四'],
        '分数': [100, 100]
        }
df = pd.DataFrame(data)

df.to_excel('./data/student.xlsx', sheet_name='成绩', index=False)  # index = False表示不写入索引

