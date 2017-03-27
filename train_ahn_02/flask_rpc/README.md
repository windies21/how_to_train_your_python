# Python Flask(RestFul) with gRPC
gRPC proto 생성과 메시지 작성 및 서버 생성은 손 선생님 코드를 대거 참조하였습니다


## Run
run gRPC listener first.
``` 
python listener.py 
```
then gRPC with Flask
```
python flask_grpc.py
```
or gRPC with Flask-Restful
``` 
python restful_grpc.py
```

## Usage
* "/"
    * 사용자 목록을 listener에 요청
* "/add/<사용자>"
    * listener에 사용자 추가를 요청
* "/del/<사용자>"
    * listener에 사용자 삭제를 요청
    
### 참고
* DB 없이 listener 에 사용자 리스트를 임시 저장.
* browser 테스트 위해 GET 방식만 구현.