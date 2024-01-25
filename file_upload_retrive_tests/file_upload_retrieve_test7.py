from fastapi import File, UploadFile, FastAPI, Form
from typing import List
import os
import time
from psycopg2 import Error
from pydantic import BaseModel


from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import FileResponse
from typing import Dict
import os

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
"""
from fastapi.responses import FileResponse

@app.get("/get-files/{path_key}")
async def get_files(path_key: str):
    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files', path_key)

    if os.path.exists(files_directory):
        os.chdir(files_directory)

        file_list = []
        for root, dirs, files in os.walk(files_directory):
            for file in files:
                file_list.append(os.path.join(root, file))

        os.chdir(current_directory)
        
        return {"files_directory": files_directory, "files": file_list}
    else:
        return {"message": "Path key not found", "path_key": path_key}

"""



"""
from fastapi.responses import FileResponse

@app.get("/get-files/{path_key}/{filename}")
async def get_file(path_key: str, filename: str):
    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files', path_key)

    if os.path.exists(files_directory):
        file_path = os.path.join(files_directory, filename)

        if os.path.exists(file_path):
            return FileResponse(file_path, filename=filename)
        else:
            return {"message": "File not found", "filename": filename}
    else:
        return {"message": "Path key not found", "path_key": path_key}
"""


"""
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import FileResponse
from typing import Dict

app = FastAPI()

@app.post("/get-file")
async def get_file(payload: Dict[str, str] = Body(...)):
    path_key = payload.get("path_key")
    filename = payload.get("filename")

    if not path_key or not filename:
        raise HTTPException(status_code=400, detail="Both path_key and filename are required in the payload.")

    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files', path_key)

    if os.path.exists(files_directory):
        file_path = os.path.join(files_directory, filename)

        if os.path.exists(file_path):
            return FileResponse(file_path, filename=filename)
        else:
            raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    else:
        raise HTTPException(status_code=404, detail=f"Path key not found: {path_key}")

"""

"""
# from fastapi import FastAPI, HTTPException, Body
# from fastapi.responses import FileResponse
# from typing import Dict
# import os

# app = FastAPI()

@app.post("/get-file")
async def get_file(payload: Dict[str, str] = Body(...)):
    path_key = payload.get("path_key")
    filename = payload.get("filename")

    if not path_key or not filename:
        raise HTTPException(status_code=400, detail="Both path_key and filename are required in the payload.")

    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files', path_key)

    if os.path.exists(files_directory):
        file_path = os.path.join(files_directory, filename)

        if os.path.exists(file_path):
            try:
                return FileResponse(file_path, filename=filename)
            finally:
                os.remove(file_path)
        else:
            raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    else:
        raise HTTPException(status_code=404, detail=f"Path key not found: {path_key}")
"""

# from fastapi import FastAPI, HTTPException, Body
# from fastapi.responses import FileResponse
# from typing import Dict
# import os

# app = FastAPI()

@app.post("/get-file")
async def get_file(payload: Dict[str, str] = Body(...)):
    path_key = payload.get("path_key")
    filename = payload.get("filename")

    if not path_key or not filename:
        raise HTTPException(status_code=400, detail="Both path_key and filename are required in the payload.")

    current_directory = os.getcwd()
    files_directory = os.path.join(current_directory, 'files', path_key)
    file_path = os.path.join(files_directory, filename)

    try:
        if os.path.exists(file_path):
            return FileResponse(file_path, filename=filename,media_type="application/octet-stream")
        else:
            raise HTTPException(status_code=404, detail=f"File not found: {filename}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the request: {str(e)}")
    # finally:
        # Cleanup: Remove the file if it exists
        # if os.path.exists(file_path):
        #     os.remove(file_path)

    # finally:
    #     # Cleanup: Remove the file if it exists
    #     if os.path.exists(file_path):
    #         try:
    #             os.remove(file_path)
    #         except Exception as e:
    #             # Log the error, or handle it as needed
    #             print(f"Error while removing file: {str(e)}")

    # finally:
    #     # Cleanup: Remove the file if it exists
    #     if os.path.exists(file_path):
    #         try:
    #             os.remove(file_path)
    #             print(f"File removed successfully: {file_path}")
    #         except Exception as e:
    #             # Log the error, or handle it as needed
    #             print(f"Error while removing file: {str(e)}")
    #     else:
    #         print(f"File not found for removal: {file_path}")


