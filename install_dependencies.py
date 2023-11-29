import subprocess
import os

def handler(event, context):
    try:
        # Install dependencies using pip
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

        # You can also add any other setup steps here if needed

        return {
            "statusCode": 200,
            "body": "Dependencies installed successfully"
        }
    except subprocess.CalledProcessError as e:
        return {
            "statusCode": 500,
            "body": f"Failed to install dependencies: {str(e)}"
        }
