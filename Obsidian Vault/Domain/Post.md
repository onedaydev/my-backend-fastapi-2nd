# API 명세
| API 명| URL| 요청방법| 설명 |
|---|---|---|---|
|||||

- Create
- Read
- Update [참고](https://fastapi.tiangolo.com/ko/tutorial/body-updates/)
- Category(Use Enum)
- JSONResponse+status codes
- Path, Query, Header, Cookie, Body, Form, File 중 examples과 openapi_examples를 사용해보기   [참고](https://fastapi.tiangolo.com/ko/tutorial/schema-extra-example/)
- 쿠키 사용하기[참고](https://fastapi.tiangolo.com/ko/tutorial/cookie-params/)
- JSON이 아닌 방식으로 데이터 받을 때 사용하는 Form() 이용해서 데이터 받기
- 권한 없는 경우(수정 권한 등) 에러 메시지 표출하기 [참고](https://fastapi.tiangolo.com/ko/tutorial/handling-errors/)
- response_model, response_description 사용해 문서화
- jsonable_encoder 사용해서 자료형 변환하기 [참고](https://fastapi.tiangolo.com/ko/tutorial/encoder/)
- body로 받아오는 파라미터 객체에 pydantic의 BaseModel을 상속받은 객체 선언하고 각 변수에 Field 사용으로 validation 설정하기