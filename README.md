# flask-hands-on
### Create Image:
```shell
docker build -t flaskappimage .
```

### Run:
```shell
docker run -itd --name flaskapp \
--mount type=bind,source="$(pwd)/src/",dst=/app/src \
-p 5000:5000 \
flaskappimage
```

### see logs,
```shell
docker logs -f flaskapp
```

### see stats,
```shell
docker stats
```

### To test
```shell
docker exec -it flask python3 -m unittest discover -v -s src
```
