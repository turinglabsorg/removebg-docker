# Create docker

docker build --tag removebg .

# Run docker

docker run removebg

# Check status

Go to http://172.17.0.2:5000

# Remove bg

```[POST] http://172.17.0.2:5000/remove
{url: "https://to.img"}
```
