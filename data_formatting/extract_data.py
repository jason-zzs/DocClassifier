import os, re
import pandas as pd

def get_folders(tags):
    folders = []
    for tag in tags:
        tag = re.sub(r'[:\/*?"<|]', '', tag)
        tag = tag.replace(' -> ', '/')
            
        folders.append(tag.split(','))
        
    return folders

def make_folders(tags):
    def make_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)
       
    for folders in tags:
        for folder in folders:
            make_dir(folder.strip())
            
def add_docs(doc_ids, titles, contents, folders):
    for i in range(len(doc_ids)):
        folder_list = folders[i]
		
        for folder in folder_list:
            path = folder.strip() + '/' + str(doc_ids[i])
                    
            file = open(path, 'w')
            file.write(titles[i] + '\n\n' + contents[i])
            file.close()


data_file = 'training_data.csv'
data = pd.read_csv(data_file, engine='python')
print(data.info())

folders = get_folders(data['Indexes'])
make_folders(folders)
add_docs(data['DocID'], data['Precis'], data['DOC_CONTENT'], folders)
