from fastapi import FastAPI
from starlette_admin import Admin


def setup_admin(app: FastAPI):
    admin = Admin(title="Fast Config Admin")
    admin.mount_to(app=app)