import requests
from fastapi import FastAPI, HTTPException
import json


app = FastAPI()


# แทนที่ด้วย API Key ของคุณที่ได้จาก Scopus
api_key = "d0015166cced5292a4264636dc52e087"

# URL ของ Scopus API
url = "https://api.elsevier.com/content/search/scopus"

# สร้าง headers ที่มี API Key เพื่อทำ authentication
headers = {
    "X-ELS-APIKey": api_key
}

# สร้าง parameters สำหรับค้นหานักวิจัยตามชื่อเต็ม
params = { 
    "query": f"AUTHLASTNAME(Chaowalit)",
    # "query": "TITLE(K-means and Support Vector Machines for Thai Language IT News Retrieval System)",
    # "query": "AUTHFIRST(Sunee)"
    # "query": "AFFIL(silpakorn university)", 
    # "count": 5  # จำนวนผลลัพธ์ที่ต้องการ
}

# ทำ HTTP request โดยใช้ requests.get และส่ง headers และ parameters ที่สร้างไว้
response = requests.get(url, headers=headers, params=params)

   # ตรวจสอบสถานะของการ request
if response.status_code == 200:
            # ดึงข้อมูล JSON จาก response
    data = response.json()

            # สร้างอาเรย์ลิสต์สำหรับเก็บ dc:identifier
    identifiers = []

            # ตรวจสอบว่า entry มีอยู่ในข้อมูลหรือไม่
    if'search-results' in data and 'entry' in data['search-results']:
        entries = data['search-results']['entry']
                
                # ดึงค่า dc:identifier จากแต่ละ entry
        for entry in entries:
            if 'dc:identifier' in entry:
                identifiers.append(entry['dc:identifier'])
    print(identifiers)
            # เรียก get_scopus_info สำหรับแต่ละ SCOPUS_ID
    scopus_info_list = [get_scopus_info(identifier) for identifier in identifiers]

    print ({"scopus_info": scopus_info_list})  # ส่งข้อมูล SCOPUS กลับไปยังเว็บไซต์
else:
            # หากไม่สามารถเรียกข้อมูลได้
    raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
    


def get_scopus_info(SCOPUS_ID):
    url = f"https://api.elsevier.com/content/article/scopus_id/{SCOPUS_ID}"
    resp = requests.get(url,
                        headers={'Accept':'application/json',
                                 'X-ELS-APIKey': "d0015166cced5292a4264636dc52e087"})
    results = json.loads(resp.text.encode('utf-8'))
    return results  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
  




# def get_scopus_info(SCOPUS_ID):
#     url = ("http://api.elsevier.com/content/abstract/scopus_id/"
#            + SCOPUS_ID
#            + "?field=authors,title,publicationName,volume,issueIdentifier,"
#            + "prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType")
#     resp = requests.get(url,
#                         headers={'Accept': 'application/json',
#                                  'X-ELS-APIKey': api_key})
#     results = json.loads(resp.text)
#     print(results)

# @app.get("/insert_author_sciencedirect")
# async def search_research(q: str):
#     url = "https://api.elsevier.com/content/search/sciencedirect"
#     headers = {
#         "Accept": "application/json",
#         "X-ELS-APIKey": "a128f8c73b1c58ba7612068e037f677a"  # Replace with your actual API key
#     }
#     params = {
#         "query": "AUTHLASTNAME(q)",
#     }
#     response = requests.get(url, headers=headers, params=params)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise HTTPException(status_code=response.status_code, detail=response.text)

# --------------------------------------------

# app = FastAPI()


# # แทนที่ด้วย API Key ของคุณที่ได้จาก Scopus


# url = "https://api.elsevier.com/content/search/sciencedirect"

# # สร้างข้อมูล query สำหรับค้นหา (เป็น JSON format)
# query = {
#     "query": "AUTHLASTNAME(Tantatsanawong)"
# }

# # สร้าง headers ที่มี API Key เพื่อทำ authentication
# headers = {
#     "X-ELS-APIKey": "a128f8c73b1c58ba7612068e037f677a"  # Replace with your actual API key
# }

# # ทำคำขอ HTTP GET เพื่อค้นหาข้อมูล
# response = requests.get(url, headers=headers, params=query)

# # ตรวจสอบสถานะของการ request
# if response.status_code == 200:
#     # ดึงข้อมูล JSON จาก response
#     data = response.json()

#     # ทำอะไรกับข้อมูลที่ได้ต่อไป
#     print(data)
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")
#     print(response.text)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)





# from fastapi import FastAPI, HTTPException
# import requests

# app = FastAPI()

# # กำหนด API key
# API_KEY = "d0015166cced5292a4264636dc52e087"

# @app.get("/research")
# async def get_research(author: str):
#     # สร้าง URL สำหรับค้นหางานวิจัยโดยใช้ชื่อนักวิจัย
#     url = f"https://api.sciencedirect.com/search?author={author}"

#     # สร้าง header พร้อม API key
#     headers = {
#         "X-ELS-APIKey": API_KEY
#     }

#     # ส่งคำขอ HTTP พร้อมกับ header
#     response = requests.get(url, headers=headers)

#     # ตรวจสอบสถานะการตอบกลับ
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

#     # ดึงข้อมูล JSON จาก response
#     research_data = response.json()

#     return research_data

