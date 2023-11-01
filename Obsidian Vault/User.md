- 로그인 JWT OAuth2.0 바탕으로 토큰 유효기간 설정하기 [참고](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/)
routers/users.py 에서

APIRouter로 라우터 객체 생성(prefix와 tags 사용)
```openssl rand -hex 32```로 비밀 키 생성

OAuth2.0 jwt를 활용한다.

토큰, 토큰 데이터, 유저, 유저(디비) 클래스 생성(pydantic BaseModel 이용)