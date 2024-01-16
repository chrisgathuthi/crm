# APIs

Assuming that you will run the project on localhost and default port ``` 8000 ``` all api endpoint will start with api. vue application will use default ```5173``` port

```python
baseUrl = "127.0.1.1:8000/api"
```

## 1. Authentication Endpoints

| Endpoint | Description | Response |
| --- | --- | --- |
| ```/api/accounts/provider-detail/``` | creating ISP instance | ```{"token":"kjk89sdf89d89g9s8ga8gs" }``` |
| ```/api/accounts/login/``` | ISP login page | ```{"token":"kjk89sdf89d89g9s8ga8gs" }``` |

For both endpoints it will return a token which is saved to the local storage. The token is used to identify ISP instances and is used in subsquent API calls.

## 2. Admin page

| Endpoint | Description | Response |
| --- | --- | --- |

## 3. Field work

| Endpoint | Description | Response |
| --- | --- | --- |
| ```/api/accounts/client/``` | creating client instancec | ```{}```|
