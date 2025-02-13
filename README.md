# chameleon 카멜레온
카멜레온은 환경에 맞게 색을 바꾼다. 하지만 카멜레온은 카멜레온. 서버의 IP가 유동적으로 바뀌는 환경에서 도메인을 사용할 수 있게 한다. 

Chameleons change color to match their environment. But a chameleon is a chameleon. It allows you to use your domain in environments where your server's IP is in flux. 

# 프로젝트 구조
```
📂/
├─.gitignore
├─REACME.md
├─docker-compose.yml
├─📂/core
│   ├─Dockerfile
│   ├─main.py
│   └─requirements.txt
└─📂/web
    ├─📂/src
    │   ├─📂/main
    │   │   ├─📂/java/com/digging/chameleon
    │   │   │   └─ChameleonApplica
    │   │   └─📂/resources
    │   │       └─application.properties
    │   └─📂/test/java/com/digging/chameleon
    ├─README.md
    └─build.gradle
```

**파일 설명**
main.py
- 30초에 1회 외부 ip 를 체크합니다. 
- 만약 ip 가 변경되었다면, route53_records.json 으로, 기존 IP에 연결된 record의 IP를 변경된 IP로 업데이트합니다.
- 최종적으로, Domain 이 유동아이피의 서버와 연결됩니다. 

# 개발환경
- source venv/bin/activate

# 기능 요구사항
- IP 가 변경되면 도메인이 변경된다.
- Domain 을 관리할 수 있다. (조회, 수정, 추가, 삭제)
