import requests
import os


print ("\n\n{}\n\n".format(os.path.expanduser("~")))

def download_file_from_api(api_url, payload, local_path):
    try:
        # Make a request to the API
        response = requests.post(api_url + "/get-file", json=payload)
        response.raise_for_status()  # Check for HTTP errors

        # Check if the response is successful
        if response.status_code == 200:
            # Extract the file content and filename from the response
            file_content = response.content
            filename = response.headers.get("Content-Disposition").split("filename=")[1]

            # Specify the local path where you want to save the file
            # local_path = f"downloaded_files/{filename}"  # Update the path as needed

            # Create the directory if it doesn't exist
            os.makedirs(local_path, exist_ok=True)

            # Save the file locally
            with open(local_path, "wb") as local_file:
                local_file.write(file_content)

            print(f"File '{filename}' downloaded and saved to '{local_path}' successfully.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}, Detail: {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
api_url = "http://127.0.0.1:8000"  # Replace with your actual API URL
payload = {"path_key": "234_sumanta.biswas@petonic.in_0_1706156954.217359", "filename": "tax.xlsx"}  # Replace with actual payload
# local_path = "C:\Users\JitendraNayak\Downloads\API-downloads\{}".format(payload["filename"])
# local_path = r"C:\Users\JitendraNayak\Downloads\API-downloads\{}".format(payload["filename"])
local_path = "C:\\Users\\JitendraNayak\\Desktop\\API-downloads\\{}".format(payload["filename"])


download_file_from_api(api_url, payload, local_path)
