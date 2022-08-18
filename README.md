# P2P Backend
p2p의 django 기반의 백엔드 서버입니다.
rest api로 제공됩니다.
연결 데이터베이스는 PostgreSQL이며 초기 데이터베이스 설계와 구축, 데이터 수집은 [데이터 레포](https://github.com/goorm-k8s-Finalproject/data)를 참고해주시기 바랍니다.

## Requirements
- Python: 3.10.4
- Django: 4.1
- PostgreSQL: 14.2
- 그 외 파이썬 라이브러리에 대한 정보는 [requirements.txt](requirements.txt) 참조

## Environment variables
보안과 배포의 용이성을 위하여 별도의 환경변수로 분리한 제원이 있습니다.
- DJANGO_DB_USER: DB 접속 유저
- DJANGO_DB_PASSWORD: DB 접속 패스워드
- DJANGO_DB_NAME: 접속 database 명
- DJANGO_DB_HOST: 접속 DB 호스트
- DJANGO_DB_PORT: 접속 포트
- DJANGO_ALLOWED_HOSTS: 배포 시 Allowed Hosts
- DJANGO_SECRET_KEY: Django secret key
- TZ: 서버 타임존
- DJANGO_DEBUG: boolean, 디버그 모드 여부

# References
- [drf tutorial korean](https://blog.raccoony.dev/drf3-tutorial-1/)
- [field lookup](https://eunjin3786.tistory.com/338)
- [filter Integration with DRF](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html)
- [django-filter](https://django-filter.readthedocs.io/en/latest/index.html)
- [user](https://minwoo.kim/posts/create-register-and-jwt-login-api-using-django-rest-framework/)
