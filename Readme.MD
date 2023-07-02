# API DOCUMENTATION

## Installation

```bash
git clone <repo>
cd <repo>
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## Endpoints

### GET /api/students


```bash
curl -X GET http://127.0.0.1:5000/api/students
```
## Response 

```json
[
  {
    "_id": {
      "$oid": "64a1a7dae7cffac79526ee3e"
    },
    "name": "aniket1",
    "age": 90,
    "email": "A@gmail.com",
    "college": "JGEC"
  },
  {
    "_id": {
      "$oid": "64a1a99860064017e502215b"
    },
    "name": "avijit sen",
    "age": 26,
    "email": "as2440@it.jgec.ac.in",
    "college": "dd"
  },
  {
    "_id": {
      "$oid": "64a1ac211a2b95e65eaa4278"
    },
    "name": "JGEC",
    "age": 26,
    "email": "avijitsen.me@gmail.com",
    "college": "dd"
  },
  {
    "_id": {
      "$oid": "64a1aef20cc65683bfdedbe4"
    },
    "name": "JGECss",
    "age": 26,
    "email": "avijitsen.me@gmail.com",
    "college": "dd"
  }
]
```

### GET /api/students/<id>

```bash
curl -X GET http://localhost:5000/api/students/64a1a7dae7cffac79526ee3e
```
## Response

```json
{
  "_id": {
    "$oid": "64a1a7dae7cffac79526ee3e"
  },
  "name": "aniket1",
  "age": 90,
  "email": "A@gmail.com"
}
```

### POST /api/students

```bash
curl -X POST http://localhost:5000/api/students -H 'Content-Type: application/json' -d '{"name": "aniket1", "age": 90, "email": "A@gmail.com"
}'
```

## Response

```json
{
  "id": "64a1b3a59b63dc6da781b7ee"
}
```

### Author

Avijit Sen

### Version

1.0.0





