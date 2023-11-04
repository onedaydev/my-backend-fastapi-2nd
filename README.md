# API 명세
| API 명| URL| 요청방법| 설명 |
|---|---|---|---|
|Domain: User|
|회원 가입|/user/create|POST||
|로그인|/user/login|POST||

# Run it

1. download requirements
```
pip install -r requirements.txt
```

2. DB init

- Obsidian Vault의 alembic.md 참고

3. .env

```openssl rand -hex 32``` or ```import secrets; secrets.token_hex(32)```로 생성한 key를 사용


