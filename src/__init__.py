from typing import Callable
from google.cloud import aiplatform, storage
from google.auth import default

PROJECT_ID = "active-smile-416914"

client = storage.Client(project=PROJECT_ID)

credentials,_ = default()

aiplatform.init(
    project=PROJECT_ID,
    location='us-central1',
    credentials=credentials
)