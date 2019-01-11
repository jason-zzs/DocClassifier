import os, json, time
from os.path import isfile

metadata = []
topic_dict = {}
global_doc_topic_id = -1
        
def doc_meta_index(metadata, path):
    for i in range(len(metadata)):
        if metadata[i]["doc_name"] == path:
            return i
    return -1

def build_metadata_and_topic_dict(current_dir, current_topic_id, current_level, metadata, topic_dict):
    global global_doc_topic_id

    hasFile = False
    for path in os.listdir(current_dir):
        if isfile(path):
            hasFile = True
            break

    if not hasFile:
        global_doc_topic_id -= 1

    for path in os.listdir(current_dir):
        if not isfile(path):
            if path == '__pycache__':
                continue
                
            global_doc_topic_id += 1
            os.chdir(os.getcwd() + '/' + path)
            build_metadata_and_topic_dict(os.getcwd(), global_doc_topic_id, current_level+1, metadata, topic_dict)
            os.chdir(current_dir)
            

        elif current_level != 0:
            topic_name = '/'.join(current_dir.split('\\')[-current_level:])
            
            if current_topic_id not in topic_dict.keys():
                topic_dict[current_topic_id] = topic_name
                
            doc_index = doc_meta_index(metadata, path)
            if doc_index == -1:
                metadata.append({
                    "doc_name": path,
                    "doc_topic": [topic_name],
                    "doc_topic_id": [current_topic_id],
                    "doc_date": time.ctime(os.path.getmtime(path))[4:],
                    "doc_size": os.path.getsize(path)
                })
            else:
                metadata[doc_index]["doc_topic"].append(topic_name)
                metadata[doc_index]["doc_topic_id"].append(current_topic_id)

if __name__ == '__main__':           
    build_metadata_and_topic_dict(os.getcwd(), global_doc_topic_id, 0, metadata, topic_dict)

    json.dump(metadata, open('metadata.json', 'w'))
    json.dump(topic_dict, open('topic_dict.json', 'w'))