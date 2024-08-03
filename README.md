# FastAPI wrapper for [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)

## Requirements

- Python3.8 +
- 1.4GB for docker image
- 500MB+ RAM for docker

## Installation
1. __Set variables__.
    Create `.env` file with variables:
    ```shell
    MODEL_SIZE="tiny"
    PORT="8080"
    ```
2. __Run container__
    Simply use `docker-compose` for run container
    ```shell
    docker-compose up -d
    ```
3. Wait for some time while whisper model are downloading.

## Usage
### Endpoints
- http://127.0.0.1:8080/docs - fastapi auto documentation
- http://127.0.0.1:8080/transcribe - post audio endpoint
- http://127.0.0.1:8080/health - healthcheck endpoint

### examples
#### post example
```shell
curl -X 'POST' \
  'http://127.0.0.1:8080/transcribe' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'audio=@voice.ogg;type=video/ogg'
```
#### response example
```json
{
  "status": "ok",
  "response": "transcribed words from audio"
}
```

```json
{
  "status": "error",
  "response": "some error info"
}
```