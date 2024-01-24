from fastapi import File, UploadFile, FastAPI
from typing import List
import os

app = FastAPI()

@app.post("/upload-file")
def upload(files: List[UploadFile] = File(...)):
    current_directory = os.getcwd()
    print("Current Directory: {}".format(current_directory))
    current_directory_split = current_directory.split('\\')
    if current_directory_split[-1] != 'files':
        new_directory = current_directory + '/files'
        print (new_directory)
        if os.path.exists(new_directory):
            os.chdir(new_directory)
            print(f"The directory '{new_directory}' exists.")
        else:
            os.mkdir(new_directory)
            os.chdir(new_directory)
            print(f"The directory '{new_directory}' exists.")

    for file in files:
        try:
            contents = file.file.read()
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}
