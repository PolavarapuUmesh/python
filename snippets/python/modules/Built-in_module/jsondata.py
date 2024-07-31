import json
string='''
{
    "people": [
        {
            "name" : "jsonroy",
            "mobile" : 9990000900,
            "mail" : "jsonroy@gmail.com",
        },
        {
            "name" : "tixy",
            "mobile" : 9027278209,
            "mail" : "tixywolf82@gmail.com",
        }
    ]
}'''
data=json.loads(string)
print(data)