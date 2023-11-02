# API 명세
| API 명| URL| 요청방법| 설명 |
|---|---|---|---|
|Domain: User|
|계정 생성|/user/create|POST||
|로그인|/user/login|POST||

- 계정 삭제
- 비밀번호 변경
- OAuth2.0 jwt를 활용한다.
- + 로그인 JWT OAuth2.0 바탕으로 토큰 유효기간 설정하기 [참고](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/)
- 토큰, 토큰 데이터, 유저, 유저(디비) 클래스 생성. pydantic BaseModel 이용)



