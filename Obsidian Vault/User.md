# API 명세
| API 명| URL| 요청방법| 설명 |
|---|---|---|---|
|Domain: User|
|계정 생성|/user/create|POST||
|로그인|/user/login|POST||
||/user/me|GET|토큰 인증 확인|

~~- 계정 생성~~
~~- OAuth2.0 토큰 인증 과정 구현~~
- 계정 삭제
- 비밀번호 변경
- scopes(특정 권한 세트) 더 알아보고 활용해보기 [참고](https://fastapi.tiangolo.com/ko/tutorial/security/oauth2-jwt/#advanced-usage-with-scopes "Permanent link")