import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False