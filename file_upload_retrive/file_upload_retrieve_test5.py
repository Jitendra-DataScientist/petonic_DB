from fastapi import File, UploadFile, FastAPI
from typing import List
import os
from pydantic import BaseModel

class FilePayload(BaseModel):
    path_key: str
    files: List[UploadFile]

app = FastAPI()

@app.post("/upload-file")
def upload(payload: FilePayload):
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

    new_directory = new_directory + '/' + payload.path_key
    try:
        os.mkdir(new_directory)
    except FileExistsError:
        return {"message": "path_key already exists"}

    os.chdir(new_directory)

    # Verify the change
    updated_directory = os.getcwd()
    print("Updated Working Directory:", updated_directory)
    updated_directory

    for file in payload.files:
        try:
            contents = file.file.read()
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfully uploaded {[file.filename for file in payload.files]}"}
