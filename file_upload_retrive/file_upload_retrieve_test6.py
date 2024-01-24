from fastapi import File, UploadFile, FastAPI, Form
from typing import List
import os
import time
from psycopg2 import Error
from pydantic import BaseModel

class FilePayload(BaseModel):
    path_key: str
    files: List[bytes]  # Change the type to List[bytes]

app = FastAPI()

@app.post("/upload-file")
async def upload(path_key: str = Form(...), files: List[UploadFile] = File(...)):
    # path_key to be of form "challenge-id _ contributor-id _ solution-id _ epoch"
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

        new_directory = new_directory + '/' + path_key + '_' + str(time.time())
    else:
        new_directory = current_directory + '/' + path_key + '_' + str(time.time())

    try:
        os.mkdir(new_directory)
    except FileExistsError:
        return {"upload":False,
                "message": "path_key already exists"}

    os.chdir(new_directory)

    # Verify the change
    updated_directory = os.getcwd()
    print("Updated Working Directory:", updated_directory)

    try:
        for file in files:
            try:
                contents = file.file.read()
                with open(file.filename, 'wb') as f:
                    f.write(contents)
            except Exception:
                return {"message": "There was an error uploading the file(s)"}
            finally:
                file.file.close()

        new_directory = updated_directory + '/..'
        os.chdir(new_directory)

        return {"upload": True,
                "message": f"Successfully uploaded {[file.filename for file in files]}"}
    
    except Error as e:
        new_directory = updated_directory + '/..'
        os.chdir(new_directory)
        return {"upload":False,
                "error": e}
