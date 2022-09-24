# UserAPI
Internship Assignment

By Deepak S. Patil 
24 sept 2022
23:33 pm

Above django project contains UserAPI based on REST 

User Model has following structure
```python
class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    EmailID=models.EmailField(unique=True)
    Age=models.IntegerField()
    Address=models.TextField()
```
*UserID field is autofield*

the API handles all CRUD operations 

Request Formats and examples : 

GET Request format:
```
http://127.0.0.1:8000/read?userid=<UserID to Read>
```
Example:
```http
http://127.0.0.1:8000/read?userid=1
```

POST Request format:
```
http://127.0.0.1:8000/create/
```
Json Data Example:

```json
{
  "Name" : "Deepak",
  "EmailID" : "dp@abc.com",
  "Age" : 20,
  "Address" : "A block , India"
}
```

PUT Request format:
```
http://127.0.0.1:8000/update/
```
Json Data To Update Example:

```json
{
  "Name" : "Deepak",
  "EmailID" : "dp@abc.com",
  "Age" : 21,
  "Address" : "A block , India"
}
```

DELETE Request format:
```
http://127.0.0.1:8000/delete?userid=<UserID to Delete>
```
Example:
```http
http://127.0.0.1:8000/delete?userid=1
```
