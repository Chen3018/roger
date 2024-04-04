from typing import Callable
from google.colab import auth
from google.cloud import aiplatform, storage

PROJECT_ID = "active-smile-416914"

client = storage.Client(project=PROJECT_ID)

auth.authenticate_user()

aiplatform.init(
    project=PROJECT_ID,

    location='us-central1',
)