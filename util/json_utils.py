import json

"""JSON데이터를 담당하는 유틸리티 기능"""

def open_json(file_path:str) -> json:
    with open(file_path, "r", encoding="utf-8") as f:
        # JSON 파일을 읽어서 파싱하여 반환
        return json.load(f)

def dumps_json(data:dict) -> json:
    return json.dumps(data, ensure_ascii=False, indent=4)