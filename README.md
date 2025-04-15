Part one:

The task was to create an app in flask and run package it with docker so that cunning a curl request to the /ping endpoint will return a `{'status':'ok'}` response

build with
```bash
docker build -t 'flasker'
```

run with
```bash
docker run -it -p 5000:5000 'flasker'
```

test with 
```bash
curl http://localhost:5000/ping
```
output:
```bash
{
  "status": "ok"
}
```

Part two:
