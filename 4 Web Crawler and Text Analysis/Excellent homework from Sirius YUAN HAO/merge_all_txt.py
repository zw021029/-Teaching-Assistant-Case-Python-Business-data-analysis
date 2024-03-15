import glob

# 找到所有的 'comments_page_{page_number}.txt' 文件
filenames = glob.glob('comments_page_*.txt')

# 打开 'comments.txt' 文件
with open('comments.txt', 'w', encoding='utf-8') as outfile:
    for fname in filenames:
        # 打开每个 'comments_page_{page_number}.txt' 文件
        with open(fname, 'r', encoding='utf-8') as infile:
            # 将文件的内容写入到 'comments.txt' 文件中
            for line in infile:
                outfile.write(line)