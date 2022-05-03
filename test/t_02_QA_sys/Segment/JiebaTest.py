import jieba

seg_list = jieba.cut("604的兄弟姐妹都是湖北工业大学数一数二的帅哥美女！", cut_all=False)
print("Default Mode :" + "/ ".join(seg_list))

jieba.add_word("湖北工业大学")
seg_list = jieba.cut("604的兄弟姐妹都是湖北工业大学数一数二的帅哥美女！", cut_all=False)
print("Default Mode :" + "/ ".join(seg_list))
