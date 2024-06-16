name = [
    {
        "name": "Lawrence",
        "age": 7,
        "company": "zempaa.com"
        },
    
    {
       "name": "Izundu",
        "age": 21,
        "companyName": [
            {
            "name": "zempaa.com",
            "secondName": "zempay.com",
            }
        ]
    }
]

print(f"I have a company named {name[1]['companyName'][0]['name']}")
