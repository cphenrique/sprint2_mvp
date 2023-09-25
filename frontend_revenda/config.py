import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
HOST = '0.0.0.0'
PORT = 5001
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@postgres-container:5432/revenda'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'hy#6JH-nb!#q=YS&6u$wJEYs@rcks5V3W!9MA+D8qa#Fck?7hH?RmQBG5n*#PemU'
APP_NAME = 'Revenda de Carros'