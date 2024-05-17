# Module 1 HW
## Docker & SQL
### Question 1 - Docker tags
**Steps**
```
docker --help
docker build --help
docker run --help
```

From lists of command above, we get information about the tags option we can use.
The text `Automatically remove the container when it exits` stands for tag `--rm` from command `docker run --help

### Question 2 - Docker 1st run
**Steps**
```
docker run -it --entrypoint bash python:3.9
```
- `docker run` starts a new Docker container
- `-it` stands for interactive terminal
- `--entrypoint` bash sets the entrypoint of the container to bash
- `python:3.9` specifies the Docker image to use

```
pip list
```
The version of the package `wheel` is 0.43.0

### Question 3 - 