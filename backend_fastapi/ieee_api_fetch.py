# import requests
# from fastapi import FastAPI, HTTPException

# app = FastAPI()


# # ใส่ API key ของคุณที่ได้จาก IEEE
# api_key = "2xc3uaecmm3hxzbfhpbxhn8m"

# # สร้าง URL สำหรับค้นหา Metadata
# url = "https://ieeexploreapi.ieee.org/api/v1/search/articles"

# # กำหนดพารามิเตอร์สำหรับค้นหา
# params = {
#     "apikey": api_key,
#     "author": "Sunee Pongpinigpinyo",
#     # "author": "Supachai Tangwongsan",
#     # "affiliation": "Silpakorn University",
#     # "index_terms": "research_collaboration",
# }

# # ทำ HTTP request
# response = requests.get(url, params=params)
# print(response)

# # ตรวจสอบสถานะของการ request
# if response.status_code == 200:
#     # ดึงข้อมูล JSON จาก response
#     data = response.json()
#     print(data)
#     # ดึงข้อมูลที่ต้องการ
#     for result in data.get('records', []):
#         abstract = result.get('abstract', '')
#         authors = result.get('authors', [])
#         article_title = result.get('article_title', '')
#         article_number = result.get('article_number', '')
#         doi = result.get('doi', '')
#         isbn = result.get('isbn', '')
#         issn = result.get('issn', '')
#         is_number = result.get('is_number', '')
#         publication_title = result.get('publication_title', '')
#         publication_year = result.get('publication_year', '')
#         content_type = result.get('content_type', '')
#         author_order = result.get('author_order', '')
#         conference_location = result.get('conference_location', '')
#         volume = result.get('volume', '')
#         start_page = result.get('start_page', '')
#         affiliation = result.get('affiliation', '')

#         # ทำอะไรกับข้อมูลที่ดึงมาได้ต่อไป
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# เส้นทางสำหรับรับค่า author และค้นหาข้อมูลจาก API ของ IEEE
@app.get("/insert_author_ieee")
async def get_data(author: str):
    # กำหนดพารามิเตอร์สำหรับค้นหา
    params = {
        "apikey": "2xc3uaecmm3hxzbfhpbxhn8m",
        "author": author,
    }
    
    # ทำ HTTP request
    response = requests.get("https://ieeexploreapi.ieee.org/api/v1/search/articles", params=params)

    # ตรวจสอบสถานะของการ request
    if response.status_code == 200:
        # ดึงข้อมูล JSON จาก response
        data = response.json()
        print(data)
        return data  # ส่งข้อมูล JSON กลับไปยังเว็บไซต์
    else:
        # หากไม่สามารถเรียกข้อมูลได้
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
