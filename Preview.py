# 이 파일은 threestudio 프로젝트 루트 폴더에서 실행해야 함
# python ./Preview.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import common_method
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# json-server 정보 세팅
common_method.load_config()
# setting 정보 세팅
common_method.get_setting_json_server()

app.mount("/data", StaticFiles(directory="data"), name="data")

uvicorn.run(app, host="0.0.0.0", port=common_method.SETTING["port"])