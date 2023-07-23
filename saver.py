import os
import pandas
def collect_zip_file_names(folder_path):
    zip_file_names = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.zip') and os.path.isfile(os.path.join(folder_path, filename)):
            zip_file_names.append(filename)
    return zip_file_names

def save_to_csv(file_names):
    finalList= []

    for file in file_names:
        finalList.append(
            {
                "Filename":file
            }
        )

    df= pandas.DataFrame(finalList)
    df.to_csv("zip_files.csv",index=False)
    



def main(folder_path):
    zip_file_names = collect_zip_file_names(folder_path)
    save_to_csv(zip_file_names)




    
