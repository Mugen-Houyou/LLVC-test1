# LLVC API Specification

This document describes a simple REST API for interacting with the LLVC (Low-Latency Low-Resource Voice Conversion) model in this repository. The API is designed for demonstration and can be extended for production usage.

## Base URL
`http://<server-address>/api/v1`

## Authentication
No authentication is included in this demonstration API.

## Endpoints

### `GET /models`
Returns a list of available voice conversion models on the server.

**Response**
```json
[
  {
    "model_id": "llvc_default",
    "description": "Pretrained LLVC model",
    "sample_rate": 16000
  }
]
```

### `POST /convert`
Converts an input audio file using a specified model. Accepts multipart form data.

**Request Parameters**
- `model_id` (string, optional): ID of the model to use. Defaults to `llvc_default`.
- `stream` (boolean, optional): If `true`, the server performs streaming inference.
- `file` (binary, required): Audio file to convert (WAV/MP3/OGG, etc.).

**Response**
```
HTTP/1.1 202 Accepted
{
  "job_id": "abc123"
}
```
The server begins processing the audio and returns a job ID for polling.

### `GET /jobs/{job_id}`
Returns status information about a conversion job.

**Response (running)**
```json
{
  "job_id": "abc123",
  "status": "processing"
}
```
**Response (completed)**
```json
{
  "job_id": "abc123",
  "status": "done",
  "download_url": "/api/v1/jobs/abc123/result"
}
```

### `GET /jobs/{job_id}/result`
Downloads the converted audio file once a job has completed. The server returns the audio as `audio/wav`.

### `GET /health`
Simple endpoint that returns `{"status": "ok"}` to verify that the service is running.

## Example Workflow
1. List models: `GET /api/v1/models`
2. Submit a file for conversion: `POST /api/v1/convert`
3. Poll the job status: `GET /api/v1/jobs/{job_id}`
4. Download the result when ready: `GET /api/v1/jobs/{job_id}/result`

---
This specification can be implemented using the `infer.py` script in this repository to perform the conversion.
