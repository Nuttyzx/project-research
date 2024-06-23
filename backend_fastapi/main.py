from typing import Union, List, Optional, Dict
from fastapi import FastAPI, HTTPException,Query

from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from pydantic import BaseModel
import requests
import json

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000/",
    "bolt://localhost:7687"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


    
class Neo4jDriver:
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        self._driver = None

    def close(self):
        if self._driver is not None:
             self._driver.close()
             

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))
        return self._driver

    def run_query(self, query, parameters=None, db=None):
        with self._driver.session(database=db) as session:
            result = session.run(query, parameters)
            return result.data()

# Configuration for your Neo4j database
neo4j_config = {
    "uri": "bolt://localhost:7687",
    "user": "neo4j",
    "password": "0147258369"
}

neo4j_driver = Neo4jDriver(neo4j_config["uri"], neo4j_config["user"], neo4j_config["password"])
neo4j_driver.connect()

#@app.on_event("startup")
# def startup_event():
#    await neo4j_driver.connect()*/

@app.on_event("shutdown")
def shutdown_event():
    neo4j_driver.close()

@app.get("/all_author")
def read_node_authors():
    query = f"MATCH (n:Author) RETURN n  ORDER BY n.full_name ASC"
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result



@app.get("/search_author/{query}")
def search_node(query: str):
    query = f"MATCH (n:Author) WHERE toLower(n.full_name) CONTAINS toLower('{query}') OR toLower(n.name_th) CONTAINS toLower('{query}') RETURN n , id(n) AS id ORDER BY n.full_name ASC"
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result


@app.get("/search_research/{query}")
def search_node(query: str):
    query = f"""
    MATCH (n:Article) 
    WHERE toLower(n.title) CONTAINS toLower('{query}') OR 
        toLower(n.abstract) CONTAINS toLower('{query}') OR 
        toLower(n.keyword) CONTAINS toLower('{query}') 
    RETURN n, id(n) AS id 
    ORDER BY n.publication_year DESC
    """
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result



@app.get("/search_expertise")
def read_node_authors():
    query = f"MATCH (n:Expertise) RETURN n , id(n) AS id ORDER BY n.expertise_name ASC"
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result

# @app.post("/add_expertise")
# async def generate_unique_id(name: Name):
#     hashed_name = hashlib.sha256(name.name.encode()).hexdigest()
#     return {"uniqueID": int(hashed_name, 16)}  # แปลงรหัสจากฐานสิบหก (hexadecimal) เป็นจำนวนเต็ม





@app.get("/graph_data_author/{id_author}")
def read_graph_data(id_author: int):
    query = f"""
    MATCH (t:Article)-[:HAS_AUTHOR]->(n:Author)
    WHERE id(n) = {id_author}

    OPTIONAL MATCH (n)-[:have_expertise]->(e:Expertise)

    OPTIONAL MATCH (t)-[:HAS_AUTHOR]->(n1:Author)  

    OPTIONAL MATCH (t1:Article)-[:HAS_AUTHOR]->(n1)

    OPTIONAL MATCH (n1)-[:have_expertise]->(e1:Expertise)

    OPTIONAL MATCH (e)<-[:have_expertise]-(n2:Author)

    OPTIONAL MATCH (t2:Article)-[:HAS_AUTHOR]->(n2)

    OPTIONAL MATCH (n2)-[:have_expertise]->(e2:Expertise)

    RETURN 
            collect (distinct t) AS article,
            n AS author,
            COLLECT(DISTINCT e) AS expertise,
            n1 AS author_1,
            COLLECT(DISTINCT t1) AS article_1,
            COLLECT(DISTINCT e1) AS expertise_1,
            n2 AS author_2,
            COLLECT(DISTINCT t2) AS article_2,
            COLLECT(DISTINCT e2) AS expertise_2,
            COLLECT(DISTINCT id(t)) AS id_nodeArticle,
            id(n) AS id_nodeAuthor,
            COLLECT(DISTINCT id(e)) AS id_nodeExpertise,
            id(n1) AS id_nodeAuthor_1,
            COLLECT(DISTINCT id(t1)) AS id_nodeArticle_1,
            COLLECT(DISTINCT id(e1)) AS id_nodeExpertise_1,
            id(n2) AS id_nodeAuthor_2,
            COLLECT(DISTINCT id(t2)) AS id_nodeArticle_2,
            COLLECT(DISTINCT id(e2)) AS id_nodeExpertise_2
    """
    result = neo4j_driver.run_query(query)

    graph_data = {"nodes": [], "links": []}
    existing_node_ids_author = set()
    existing_node_ids_article = set()
    existing_node_ids_expertise = set()
    existing_links = set()
    for record in result:
        author_id = record["id_nodeAuthor"]
        article_id = record["id_nodeArticle"]
        expertise_id = record["id_nodeExpertise"]
        author_data = record["author"]
        article_data = record["article"]
        expertise_data = record["expertise"]
        if author_id not in existing_node_ids_author and author_id is not None:
            graph_data["nodes"].append({
                "id": author_id,
                "labels": ["Authors"],
                "properties": author_data,
            })
            existing_node_ids_author.add(author_id)
        for article_datas, article_ids in zip(article_data, article_id):
            if article_ids == 0:
                if article_ids not in existing_node_ids_article and article_ids is not None:
                    graph_data["nodes"].append({
                        "id": article_ids,
                        "labels": ["Articles"],
                        "properties": article_datas,
                    })
                    existing_node_ids_article.add(article_ids)
                    link = (article_ids, author_id, "HAS_AUTHOR")
                    if link not in existing_links:
                        graph_data["links"].append({
                            "source": article_ids,
                            "target": author_id,
                            "type": "HAS_AUTHOR",
                        })
                        existing_links.add(link)
            else:
                if  article_ids not in existing_node_ids_article and article_ids is not None:
                    graph_data["nodes"].append({
                        "id": article_ids,
                        "labels": ["Articles"],
                        "properties": article_datas,
                    })
                    
                    existing_node_ids_article.add(article_ids)

                    link = (article_ids, author_id, "HAS_AUTHOR")
                    if link not in existing_links:
                        graph_data["links"].append({
                            "source": article_ids,
                            "target": author_id,
                            "type": "HAS_AUTHOR",
                        })
                        existing_links.add(link)
        for expertise_datas, expertise_ids in zip(expertise_data, expertise_id):
            if expertise_ids is not None and expertise_ids not in existing_node_ids_expertise:
                graph_data["nodes"].append({
                    "id": expertise_ids,
                    "labels": ["Expertises"],
                    "properties": expertise_datas,
                })
                existing_node_ids_expertise.add(expertise_ids)

                # เพิ่มลิงก์ระหว่าง Author และ Expertise
                link = (author_id, expertise_ids, "have_expertise")
                if link not in existing_links:
                    graph_data["links"].append({
                        "source": author_id,
                        "target": expertise_ids,
                        "type": "have_expertise",
                    })
                    existing_links.add(link)
        print(existing_node_ids_author)
        print(existing_node_ids_article )
        print(existing_node_ids_expertise)
    

    for record in result:
        author_id = record["id_nodeAuthor"]
        article_id = record["id_nodeArticle"]
        expertise_id = record["id_nodeExpertise"]

        author_id_1 = record["id_nodeAuthor_1"]
        article_id_1 = record["id_nodeArticle_1"]
        expertise_id_1 = record["id_nodeExpertise_1"]

        author_id_2 = record["id_nodeAuthor_2"]
        article_id_2 = record["id_nodeArticle_2"]
        expertise_id_2 = record["id_nodeExpertise_2"]

        author_data = record["author"]
        article_data = record["article"]
        expertise_data = record["expertise"]

        author_1_data = record["author_1"]
        article_1_data = record["article_1"]
        expertise_1_data = record["expertise_1"]

        author_2_data = record["author_2"]
        article_2_data = record["article_2"]
        expertise_2_data = record["expertise_2"]

        # เพิ่มโหนด Author ในกรณีที่ยังไม่เคยเพิ่มไว้
        if author_id not in existing_node_ids_author and author_id is not None:
            graph_data["nodes"].append({
                "id": author_id,
                "labels": ["Authors"],
                "properties": author_data,
            })
            existing_node_ids_author.add(author_id)

        # เพิ่มโหนด Article ถ้ามี
        for article_datas, article_ids in zip(article_data, article_id):
            if article_ids == 0:
                if article_ids not in existing_node_ids_article and article_ids is not None:
                    graph_data["nodes"].append({
                        "id": article_ids,
                        "labels": ["Articles"],
                        "properties": article_datas,
                    })
                    existing_node_ids_article.add(article_ids)
                    link = (article_ids, author_id, "HAS_AUTHOR")
                    if link not in existing_links:
                        graph_data["links"].append({
                            "source": article_ids,
                            "target": author_id,
                            "type": "HAS_AUTHOR",
                        })
                        existing_links.add(link)
            else:
                if  article_ids not in existing_node_ids_article and article_ids is not None:
                    graph_data["nodes"].append({
                        "id": article_ids,
                        "labels": ["Articles"],
                        "properties": article_datas,
                    })
                    
                    existing_node_ids_article.add(article_ids)

                    link = (article_ids, author_id, "HAS_AUTHOR")
                    if link not in existing_links:
                        graph_data["links"].append({
                            "source": article_ids,
                            "target": author_id,
                            "type": "HAS_AUTHOR",
                        })
                        existing_links.add(link)
        

         # # เพิ่มโหนด Expertise ถ้ามี
        for expertise_datas, expertise_ids in zip(expertise_data, expertise_id):
            if expertise_ids is not None and expertise_ids not in existing_node_ids_expertise:
                graph_data["nodes"].append({
                    "id": expertise_ids,
                    "labels": ["Expertises"],
                    "properties": expertise_datas,
                })
                existing_node_ids_expertise.add(expertise_ids)

                # เพิ่มลิงก์ระหว่าง Author และ Expertise
                link = (author_id, expertise_ids, "have_expertise")
                if link not in existing_links:
                    graph_data["links"].append({
                        "source": author_id,
                        "target": expertise_ids,
                        "type": "have_expertise",
                    })
                    existing_links.add(link)

        if  author_id_1 is not None and  author_id_1 not in existing_node_ids_author:
                graph_data["nodes"].append({
                    "id":  author_id_1,
                    "labels": ["Author"],
                    "properties": author_1_data,
                })
                existing_node_ids_author.add( author_id_1)

                link = (article_ids,  author_id_1, "HAS_AUTHOR")
                if link not in existing_links:
                    graph_data["links"].append({
                        "source": article_ids,
                        "target":  author_id_1,
                        "type": "HAS_AUTHOR",
                    })
                    existing_links.add(link)
        
       
        
        for article_1_datas, article_ids_1 in zip(article_1_data, article_id_1):
            if article_ids_1 not in existing_node_ids_article and article_ids_1 is not None:
                    graph_data["nodes"].append({
                        "id": article_ids_1,
                        "labels": ["Article"],
                        "properties": article_1_datas,
                    })
                    existing_node_ids_article.add(article_ids_1)

            if  article_ids_1 in existing_node_ids_article and article_ids_1 is not None:
                    link = (article_ids_1, author_id_1, "HAS_AUTHOR")
                    if link not in existing_links:
                        graph_data["links"].append({
                            "source": article_ids_1,
                            "target": author_id_1,
                            "type": "HAS_AUTHOR",
                        }) 
                        existing_links.add(link)
        
        for expertise_1_datas, expertise_ids_1 in zip(expertise_1_data, expertise_id_1):
            if expertise_ids_1 and expertise_ids_1 not in existing_node_ids_expertise and expertise_id_1 is not None:
                graph_data["nodes"].append({
                    "id": expertise_ids_1,
                    "labels": ["Expertise"],
                    "properties": expertise_1_datas,
                })
                existing_node_ids_expertise.add(expertise_ids_1)

            if  expertise_ids_1 in existing_node_ids_expertise and expertise_ids_1 is not None:
                link = (author_id_1, expertise_ids_1, "have_expertise")
                if link not in existing_links:
                # เพิ่มลิงก์ระหว่าง Author และ Expertise
                    graph_data["links"].append({
                        "source": author_id_1,
                        "target": expertise_ids_1,
                        "type": "have_expertise",
                    })
                    existing_links.add(link)

        print(existing_node_ids_expertise)
        
        if author_id_2 not in existing_node_ids_author and author_id_2 is not None:
            graph_data["nodes"].append({
                "id": author_id_2,
                "labels": ["Author"],
                "properties": author_2_data,
            })
            existing_node_ids_author.add(author_id_2)
            
            # แปลง link เป็น tuple และใช้เป็นคีย์ใน existing_links
            link = (author_id_2, expertise_ids, "have_expertise")
            if link not in existing_links:
                graph_data["links"].append({
                    "source": author_id_2,
                    "target": expertise_ids,
                    "type": "have_expertise",
                })
                existing_links.add(link)
        
        
        for article_2_datas, article_ids_2 in zip(article_2_data, article_id_2):
            
            
            if article_ids_2 not in existing_node_ids_article and article_ids_2 is not None:
                graph_data["nodes"].append({
                    "id": article_ids_2,
                    "labels": ["Article"],
                    "properties": article_2_datas,
                })
                   
                existing_node_ids_article.add(article_ids_2)

            if article_ids_2 in existing_node_ids_article and article_ids_2 is not None:
                link = (article_ids_2, author_id_2, "HAS_AUTHOR")
                if link not in existing_links:
                    graph_data["links"].append({
                        "source": article_ids_2,
                        "target": author_id_2,
                        "type": "HAS_AUTHOR",
                    })
                    existing_links.add(link)
        
        # print(existing_node_ids_article)
        for expertise_2_datas, expertise_ids_2 in zip(expertise_2_data, expertise_id_2):
            if expertise_ids_2 not in existing_node_ids_expertise and  expertise_id_2 is not None:
                graph_data["nodes"].append({
                    "id": expertise_ids_2,
                    "labels": ["Expertise"],
                    "properties": expertise_2_datas,
                })
                existing_node_ids_expertise.add(expertise_ids_2)
            if  expertise_ids_2 in existing_node_ids_expertise and expertise_ids_2 is not None:
                    link = (author_id_2, expertise_ids_2, "have_expertise")
                    if link not in existing_links:
                        # เพิ่มลิงก์ระหว่าง Author และ Expertise
                        graph_data["links"].append({
                            "source": author_id_2,
                            "target": expertise_ids_2,
                            "type": "have_expertise",
                        })
                        existing_links.add(link)
    
        
            

    # print(existing_node_ids_author)
    # print(existing_node_ids_article )
    # print(existing_node_ids_expertise)
    # print(existing_links)
    return {"graph_data": graph_data}



@app.get("/graph_data_expertise/{id_expertise}")
def read_graph_data(id_expertise: int):
    query = f"""
    match (e:Expertise) where id(e) = {id_expertise}
    optional match (e)<-[:have_expertise]-(n:Author)
    optional match (e1:Expertise)<-[:have_expertise]-(n:Author)
    return e AS expertise ,n AS author ,collect(DISTINCT(e1)) AS expertise_1 , id(e) AS id_nodeExpertise , id(n) AS id_nodeAuthor , collect(DISTINCT id(e1)) AS id_nodeExpertise_1
    """
    result = neo4j_driver.run_query(query)
    
    # สร้างข้อมูล nodes และ links
    graph_data = {"nodes": [], "links": []}
    existing_node_ids_expertise = set()
    existing_node_ids_author = set()
    existing_links = set()
    
    # เพิ่มข้อมูล nodes และ links
    for record in result:  
        author_data = record["author"]
        expertise_data = record["expertise"]
        expertise_1_data = record["expertise_1"]
        id_nodeAuthor = record["id_nodeAuthor"]
        id_nodeExpertise = record["id_nodeExpertise"]
        id_nodeExpertise_1 = record["id_nodeExpertise_1"]

        if id_nodeExpertise not in existing_node_ids_expertise:
            graph_data["nodes"].append({
                "id": id_nodeExpertise,
                "labels": ["Expertise"],
                "properties": expertise_data,
            })
            existing_node_ids_expertise.add(id_nodeExpertise)
        
        # เพิ่มข้อมูล Node สำหรับ Author
        if author_data:
            if id_nodeAuthor not in existing_node_ids_author:
                author_node = {
                    "id": id_nodeAuthor,
                    "labels": ["Author"],
                    "properties": author_data,
                }
                graph_data["nodes"].append(author_node)
                author_node["properties"]["expertise"] = expertise_data
                existing_node_ids_author.add(id_nodeAuthor)
                
                link = (id_nodeAuthor, id_nodeExpertise, "HAVE_EXPERTISE")
                if link not in existing_links:
                    graph_data["links"].append({
                            "source": id_nodeAuthor,
                            "target": id_nodeExpertise,
                            "type": "HAVE_EXPERTISE",
                    })
                    existing_links.add(link)
        
            # เพิ่มข้อมูล Node สำหรับ Expertise
            for expertise_1_data, id_nodeExpertise_1 in zip(expertise_1_data, id_nodeExpertise_1):
                if id_nodeExpertise_1 not in existing_node_ids_expertise:
                    expertise_node = {
                        "id": id_nodeExpertise_1,
                        "labels": ["Expertises"],
                        "properties": expertise_1_data,
                    }
                    graph_data["nodes"].append(expertise_node)
                    existing_node_ids_expertise.add(id_nodeExpertise_1)
                    
                    link = (id_nodeAuthor, id_nodeExpertise_1, "HAVE_EXPERTISE")
                    if link not in existing_links:
                    # เพิ่ม links ระหว่าง Author กับ Expertise
                        graph_data["links"].append({
                            "source": id_nodeAuthor,
                            "target": id_nodeExpertise_1,
                            "type": "HAVE_EXPERTISE",
                        })
                        existing_links.add(link)
                else: 
                    link = (id_nodeAuthor, id_nodeExpertise_1, "HAVE_EXPERTISE")
                    if link not in existing_links:
                    # เพิ่ม links ระหว่าง Author กับ Expertise
                        graph_data["links"].append({
                            "source": id_nodeAuthor,
                            "target": id_nodeExpertise_1,
                            "type": "HAVE_EXPERTISE",
                        })
                        existing_links.add(link)

            
            
    # print(existing_node_ids_author)
    # print(existing_node_ids_expertise)
    # print(graph_data["links"])
    # print(graph_data["nodes"])
    return {"graph_data": graph_data}



@app.get("/author")
def read_node_authors(search: str = Query(None, alias="search")):
    query = f"""MATCH (n:Author) WHERE toLower(n.full_name) CONTAINS toLower($search) OR toLower(n.name_th) CONTAINS toLower($search)
            OPTIONAL MATCH (n)<-[:HAS_AUTHOR]-(t:Article)
            OPTIONAL MATCH (n)-[:have_degree]->(d:Degree)
            OPTIONAL MATCH (n)-[:have_expertise]->(e:Expertise)
            RETURN n, COLLECT(DISTINCT d) AS degrees, COLLECT(DISTINCT e) AS expertises ,id(n) AS id_author , COLLECT(DISTINCT id(d)) AS id_degree , COLLECT(DISTINCT id(e)) AS id_expertise
            ORDER BY n.name_th asc
                """
    params = {"search": search}          
    result = neo4j_driver.run_query(query, parameters=params)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result



@app.get("/all_researchs")
def read_node_researchs(search: str = Query(None, alias="search")):
    query = f"""MATCH (t:Article) 
    WHERE toLower(t.title) CONTAINS toLower($search)
    RETURN t , id(t) AS id ORDER BY t.publication_year DESC
    """
    params = {"search": search}  
    result = neo4j_driver.run_query(query, parameters=params)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result

@app.get("/single_research/{query_id}")
def read_node_researchs(query_id:int):
    query = f"MATCH (t:Article) where id(t) = {query_id} RETURN t , id(t) AS id "
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result

@app.get("/single_user/{query_id}")
def read_node_researchs(query_id:int):
    query = f"""MATCH (n:Author) where id(n) = {query_id}
            OPTIONAL MATCH (n)<-[:HAS_AUTHOR]-(t:Article)
            OPTIONAL MATCH (n)-[:have_degree]->(d:Degree)
            OPTIONAL MATCH (n)-[:have_expertise]->(e:Expertise)
            RETURN n, COLLECT(DISTINCT t) AS article , COLLECT(DISTINCT d) AS degree, COLLECT(DISTINCT e) AS expertise ,id(n) AS id_author ,COLLECT(DISTINCT id(t)) AS id_article ,COLLECT(DISTINCT id(d)) AS id_degree , COLLECT(DISTINCT id(e)) AS id_expertise
            ORDER BY n.full_name asc""" 
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result

@app.get("/single_author_graph/{id_author}")
def read_node_researchs(id_author: int):
    query = f"""
    MATCH (n:Author) 
    WHERE id(n) = {id_author}
    OPTIONAL MATCH (n)<-[:HAS_AUTHOR]-(t:Article)
    OPTIONAL MATCH (n)-[:have_degree]->(d:Degree)
    OPTIONAL MATCH (n)-[:have_expertise]->(e:Expertise)
    WITH n, 
        COLLECT(DISTINCT t) AS articles, 
        COLLECT(DISTINCT d) AS degrees, 
        COLLECT(DISTINCT e) AS expertises, 
        id(n) AS id_author

    WITH n, 
        [a IN articles | a {{.*, id: id(a)}}] AS article ,  
        [b IN degrees | b {{.*, id: id(b)}}] AS degree, 
        [c IN expertises | c {{.*, id: id(c)}}] AS expertise, 
        id_author

    UNWIND article AS article_order
    WITH n, degree, expertise, id_author, article_order
    ORDER BY article_order.publication_year DESC

    WITH n, 
    COLLECT(article_order) AS article, 
    degree, 
    expertise, 
    id_author

    RETURN n, 
        article, 
        degree, 
        expertise, 
        id_author

    """ 
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=500, detail="Node not found")
    return result

@app.get("/single_research_graph/{id_research}")
def read_node_researchs(id_research:int):
    query = f"""
    MATCH (t:Article)
    WHERE id(t) = {id_research}
    OPTIONAL MATCH (t)-[:HAS_AUTHOR]->(n:Author)

    WITH
        t,
        COLLECT(DISTINCT n) AS authors,  
        id(t) AS id_article

    // แยกข้อมูล author และ map ข้อมูล author กับ degree , expertise , id

    UNWIND authors AS author
    OPTIONAL MATCH (author)-[:have_degree]->(d:Degree)
    WITH author, COLLECT({{degrees: d, id: id(d)}}) AS author_degrees ,t,id_article

    OPTIONAL MATCH (author)-[:have_expertise]->(e:Expertise)
    WITH author,author_degrees , t,id_article , COLLECT({{expertises: e, id: id(e)}}) AS author_expertises

    // Collect authors with their ids and degrees
    WITH t, author, author_degrees, author_expertises, id_article
    ORDER BY author.full_name ASC

    WITH
        t,
        COLLECT({{author: author {{.*, id: id(author)}}, degree: author_degrees, expertise:author_expertises}}) AS authors_w_degrees_w_expertises,id_article

    RETURN t, authors_w_degrees_w_expertises, id_article

    """

    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result


@app.get("/single_expertise_graph/{id_expertise}")
def read_node_researchs(id_expertise:int):
    query = f"""
    MATCH (e:Expertise)
    WHERE id(e) = {id_expertise}
   
    OPTIONAL MATCH (n:Author)-[:have_expertise]->(e:Expertise)
    WITH
        e,
        COLLECT(DISTINCT n) AS authors  

    
      
    UNWIND authors AS author
    OPTIONAL MATCH (author)-[:have_expertise]->(e1:Expertise)
    
    WITH 
        author, 
        COLLECT({{expertises: e1, id: id(e1)}}) AS author_expertises
     

 
    OPTIONAL MATCH (author)-[:have_degree]->(d:Degree)
 
    WITH 
        author, author_expertises,
        COLLECT({{degrees: d, id: id(d)}}) AS author_degrees

    WITH author, author_expertises, author_degrees
    ORDER BY author.full_name ASC

    WITH 
        author,
        COLLECT({{author: author {{.*, id: id(author)}}, degree: author_degrees, expertise:author_expertises}}) AS authors_w_degrees_w_expertises
        
    return authors_w_degrees_w_expertises

    """

    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    return result

@app.get("/insert_author_ieee")
async def get_data(author: str):
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")




# class Name(BaseModel):
#     name: str

# @app.post("/generate_unique_id")
# async def generate_unique_id(name: Name):
#     hashed_name = hashlib.sha256(name.name.encode()).hexdigest()
#     return {"uniqueID": int(hashed_name, 16)}  # แปลงรหัสจากฐานสิบหก (hexadecimal) เป็นจำนวนเต็ม

@app.get("/query_id_research")
def read_node_researchs(name_research: str):
    query = f"MATCH (t:Article {{title: '{name_research}'}}) RETURN id(t) AS id_research"  
    result = neo4j_driver.run_query(query)
    if not result:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    return result[0]["id_research"]  # ส่งค่าเดียวกลับเป็นเลขธรรมดา



class EditArticle(BaseModel):
    abstract: Optional[str] = None
    title: Optional[str] = None 
    publication_year: Optional[int] = None 
    publication_title: Optional[str] = None
    article_number: Optional[str] = None
    content_type: Optional[str] = None 
    start_page: Optional[str] = None
    end_page: Optional[str] = None
    doi: Optional[str] = None   
    publisher: Optional[str] = None 
    abstract_url: Optional[str] = None
    keyword: Optional[str] = None 
    
@app.put("/edit_research/{query_id}")
async def edit_research(data: EditArticle , query_id: int):
    print(data)
    try:
        query = """
            UNWIND $data AS article 
            MATCH (t:Article) WHERE id(t) = $query_id
            SET t.abstract = article.abstract,
                t.title = article.title,
                t.publication_year = article.publication_year,
                t.publication_title = article.publication_title,
                t.article_number = article.article_number,
                t.content_type = article.content_type,
                t.start_page = article.start_page,
                t.end_page = article.end_page,
                t.doi = article.doi,
                t.publisher = article.publisher,
                t.abstract_url = article.abstract_url,
                t.keyword = article.keyword
            
        """

        params = {"data": data.dict(), "query_id": query_id}  # สร้างพารามิเตอร์เพื่อส่งไปยัง Cypher query
        result = neo4j_driver.run_query(query, parameters=params)

        return {"message": "Data edit successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

class Author(BaseModel):
    authorUrl: Optional[str] = None
    full_name: str
    id: Optional[int] = None
    office: Optional[str] = None  # เพิ่ม office
    province: Optional[str] = None  # เพิ่ม province
    country: Optional[str] = None  # เพิ่ม country
    
    
class Article(BaseModel):
    abstract_url: Optional[str] = None
    article_number: Optional[str] = None
    authors: List[Author] #  class Author ไม่ได้ใช้ dict
    content_type: Optional[str] = None  
    doi: Optional[str] = None 
    end_page: Optional[str] = None
    publication_title: Optional[str] = None
    publication_year: Optional[str] = None 
    publisher: Optional[str] = None 
    start_page: Optional[str] = None
    title: Optional[str] = None 
    abstract: Optional[str] = None 
    keyword: Optional[str] = None 
 
    
class ImportData(BaseModel):
    articles: List[Article]


@app.post("/import_data")
async def import_data(data: ImportData):
    # print(data)
    try:
        query = """
        UNWIND $articles AS article 
        MERGE (a:Article {
            title: article.title    
        })
        ON CREATE SET 
            a.abstract_url = article.abstract_url,
            a.article_number = article.article_number,
            a.content_type = article.content_type,
            a.doi = article.doi,
            a.end_page = article.end_page,
            a.publication_title = article.publication_title,
            a.publication_year = article.publication_year,
            a.publisher = article.publisher,
            a.start_page = article.start_page,
            a.title = article.title,  
            a.abstract = article.abstract,
            a.keyword = article.keyword 

        WITH a, article.authors AS authors
        UNWIND authors AS author
        MERGE (auth:Author {
            full_name: author.full_name
        })
        ON CREATE SET 
            auth.authorUrl = author.authorUrl,
            auth.full_name = author.full_name,
            auth.id = author.id,
            auth.office = COALESCE(author.office, ''), 
            auth.province = COALESCE(author.province, ''),   
            auth.country = COALESCE(author.country, '')  // ใช้ COALESCE เพื่อกำหนดค่าเริ่มต้นให้ 'country' เป็นสตริงว่างหากเป็น null  
        
            
        WITH a, COLLECT(auth) AS authors
        UNWIND authors AS auth
        MERGE (a)-[:HAS_AUTHOR]->(auth)
        """
  
        article_data = [article.dict() for article in data.articles]
        result = neo4j_driver.run_query(query, parameters={"articles": article_data})
        
        return {"message": "Data imported successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")




class ImportDegree(BaseModel):
    degree_name: Optional[str] = None
    # id_d: str

class ImportExpertise(BaseModel):
    expertise_name: Optional[str] = None
    # id_e: str

class ExpertiseEdit(BaseModel):
    expertise_name: str
    new_expertise_name: str

class ImportAuthor(BaseModel):
    authorUrl: Optional[str] = None
    website: Optional[str] = None
    pic_name: Optional[str] = None
    full_name: str
    name_th: Optional[str] = None
    office: Optional[str] = None
    expertise: List[ImportExpertise]
    country: Optional[str] = None
    email: Optional[str] = None
    degree: List[ImportDegree]  
    id: Optional[int] = None
    province: Optional[str] = None

class ImportArticle(BaseModel):
    article_number: str
    authors: List[ImportAuthor]
    content_type: str
    doi: Optional[str] = None
    end_page: str
    publication_title: str
    publication_year: str
    publisher: str
    start_page: str
    title: str
    abstract: str
    keyword: str
    abstract_url: str

    
@app.put("/edit_user/{query_id}")
async def edit_research(data: ImportAuthor , query_id: int):
    print(data.expertise)
    print(data.degree)
    print(data.website)
    try:
        query = """
            UNWIND $data AS author
            MATCH (n:Author) WHERE id(n) = $query_id
            SET n.full_name = author.full_name,
                n.name_th = author.name_th,
                n.office = author.office,
                n.country = author.country,
                n.email = author.email,
                n.id = author.id,
                n.province = author.province,
                n.pic_name = author.pic_name,
                n.authorUrl = author.authorUrl,
                n.website = author.website
        """

        params = {"data": data.dict(), "query_id": query_id}  # สร้างพารามิเตอร์เพื่อส่งไปยัง Cypher query
        result = neo4j_driver.run_query(query, parameters=params)

        # ตรวจสอบค่าของ expertise ในข้อมูลที่ส่งมา
        new_expertises = [expertise.expertise_name for expertise in data.expertise]
        print(new_expertises)

        # ดึงข้อมูลเก่าของโหนด author
        author_query = """
        MATCH (n:Author)-[r:have_expertise]->(e:Expertise)
        WHERE id(n) = $query_id
        RETURN collect(e.expertise_name) AS expertise_names
        """
        author_result = neo4j_driver.run_query(author_query, parameters={"query_id": query_id})
        old_expertises = [record["expertise_names"] for record in author_result][0] #ได้รายชื่อ expertise เก่า ออกมา
        print(old_expertises)
        removed_expertises = [expertise for expertise in old_expertises if expertise not in new_expertises] #ได้expertiseที่ไม่ได้อยู๋ในข้อมูลใหม่
        added_expertises = [expertise for expertise in new_expertises if expertise not in old_expertises] #ได้ expertise ใหม่ ไม่ได้อยู๋ข้อมูลเก่า
        print(removed_expertises)
        print(added_expertises)
        # ลบเส้นเชื่อม EXPERT_IN ที่ไม่มีอยู่ในข้อมูลใหม่
        for expertise in removed_expertises:
            delete_query = """
                MATCH (n:Author)-[r:have_expertise]->(e:Expertise {expertise_name: $expertise_name})
                WHERE id(n) = $query_id
                DELETE r
                """ 
            neo4j_driver.run_query(delete_query, parameters={"query_id": query_id, "expertise_name": expertise})

        # เพิ่มเส้นเชื่อม EXPERT_IN ที่มีในข้อมูลใหม่ แต่ไม่มีในข้อมูลเก่า
        for expertise in added_expertises:
            create_query = """
                MATCH (n:Author), (e:Expertise {expertise_name: $expertise_name})
                WHERE id(n) = $query_id
                CREATE (n)-[:have_expertise]->(e)
                """
            neo4j_driver.run_query(create_query, parameters={"query_id": query_id, "expertise_name": expertise})
        
        for expertise in added_expertises:
            create_query = """
                MATCH (n:Author)
                WHERE id(n) = $query_id
                MERGE (e:Expertise {expertise_name: $expertise_name})
                MERGE (n)-[:have_expertise]->(e)
            """
            neo4j_driver.run_query(create_query, parameters={"query_id": query_id, "expertise_name": expertise})

        # ตรวจสอบค่าของ degree ในข้อมูลที่ส่งมา
        new_degrees = [degree.degree_name for degree in data.degree]
        print(new_degrees)
        # ดึงข้อมูลเก่าของโหนด author
        degree_query = """
        MATCH (n:Author)-[r:have_degree]->(d:Degree)
        WHERE id(n) = $query_id
        RETURN collect(d.degree_name) AS degree_names
        """
        degree_result = neo4j_driver.run_query(degree_query, parameters={"query_id": query_id})
        old_degrees = [record["degree_names"] for record in degree_result][0]
        
        print(old_degrees)
        # แยกข้อมูล degree ที่ต้องการลบและเพิ่ม    
        removed_degrees = [degree for degree in old_degrees if degree not in new_degrees]
        added_degrees = [degree for degree in new_degrees if degree not in old_degrees]

        print(removed_degrees)
        print(added_degrees)
        

        # ลบเส้นเชื่อม have_degree ที่ไม่มีอยู่ในข้อมูลใหม่
        for degree in removed_degrees:
            delete_query = """
            MATCH (n:Author)-[r:have_degree]->(d:Degree {degree_name: $degree_name})
            WHERE id(n) = $query_id
            DELETE r
            """
            neo4j_driver.run_query(delete_query, parameters={"query_id": query_id, "degree_name": degree})

        # เพิ่มเส้นเชื่อม have_degree ที่มีในข้อมูลใหม่ แต่ไม่มีในข้อมูลเก่า
        for degree in added_degrees:
            create_query = """
            MERGE (d:Degree {degree_name: $degree_name})
            """
            neo4j_driver.run_query(create_query, parameters={"degree_name": degree})
            create_relation_query = """
            MATCH (n:Author), (d:Degree {degree_name: $degree_name})
            WHERE id(n) = $query_id
            CREATE (n)-[:have_degree]->(d)
            """
            neo4j_driver.run_query(create_relation_query, parameters={"query_id": query_id, "degree_name": degree})

        return {"message": "Data imported successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

  
class Author(BaseModel):
    full_name: str

class Data(BaseModel):
    authors: List[Author]
    title: str

@app.put("/edit_author_indatabase")
async def edit_research(data: Data):
    try:
        new_authors = [author.full_name for author in data.authors]
        print(new_authors)

        new_title = data.title

        # ดึงข้อมูลเก่าของโหนด article
        article_query = """
        MATCH (a:Article {title: $new_title})-[r:HAS_AUTHOR]->(n:Author)
        RETURN collect(n.full_name) AS author_names
        """
        article_result = neo4j_driver.run_query(article_query, parameters={"new_title": new_title})
        old_authors = [record["author_names"] for record in article_result][0]  # ได้รายชื่อ author เก่าออกมา
        print(old_authors)

        # เปรียบเทียบข้อมูลเก่าและข้อมูลใหม่
        removed_authors = [author for author in old_authors if author not in new_authors]  # ได้ author ที่ไม่ได้อยู่ในข้อมูลใหม่
        added_authors = [author for author in new_authors if author not in old_authors]  # ได้ author ใหม่ที่ไม่ได้อยู่ในข้อมูลเก่า
        print(removed_authors)
        print(added_authors)

        # ลบความสัมพันธ์ written_by ที่ไม่มีอยู่ในข้อมูลใหม่
        for author in removed_authors:
            delete_query = """
                MATCH (a:Article {title: $new_title})-[r:HAS_AUTHOR]->(n:Author {full_name: $author_name})
                DELETE r
            """
            neo4j_driver.run_query(delete_query, parameters={"new_title": new_title, "author_name": author})

        # เพิ่มความสัมพันธ์ written_by ที่มีในข้อมูลใหม่แต่ไม่มีในข้อมูลเก่า
        for author in added_authors:
            create_query = """
                MATCH (a:Article {title: $new_title}), (n:Author {full_name: $author_name})
                CREATE (a)-[:HAS_AUTHOR]->(n)
            """
            neo4j_driver.run_query(create_query, parameters={"new_title": new_title, "author_name": author})

        # สร้างโหนด Author ใหม่หากยังไม่มีอยู่ และเพิ่มความสัมพันธ์ written_by
        for author in added_authors:
            create_query = """
                MATCH (a:Article {title: $new_title})
                
                MERGE (n:Author {full_name: $author_name})
                MERGE (a)-[:HAS_AUTHOR]->(n)
            """
            neo4j_driver.run_query(create_query, parameters={"new_title": new_title, "author_name": author})

        return {"message": "Data imported successfully", "result": "success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


class ListEditExpertise(BaseModel):
    expertise_name: str

class ListEditDegree(BaseModel):
    degree_name: str

class ListEditAuthor(BaseModel):
    authorUrl: str
    website: str
    pic_name: str
    full_name: str
    name_th: str
    office: str
    country: str
    email: str
    id: int
    province: str
    expertise: List[ListEditExpertise]
    degree: List[ListEditDegree]

@app.put("/edit_many_user")
async def edit_users(data: List[ListEditAuthor]):
    try:
        for author_data in data:
            query_id = author_data.id
            print(author_data.expertise)
            print(author_data.degree)
            print(author_data.website)
            try:
                query = """
                    UNWIND $data AS author
                    MATCH (n:Author {id: $query_id}) 
                    SET n.full_name = author.full_name,
                        n.name_th = author.name_th,
                        n.office = author.office,
                        n.country = author.country,
                        n.email = author.email,
                        n.id = author.id,
                        n.province = author.province,
                        n.pic_name = author.pic_name,
                        n.authorUrl = author.authorUrl,
                        n.website = author.website
                """

                params = {"data": author_data.dict(), "query_id": query_id}
                result = neo4j_driver.run_query(query, parameters=params)

                new_expertises = [expertise.expertise_name for expertise in author_data.expertise]

                author_query = """
                MATCH (n:Author {id: $query_id})-[r:have_expertise]->(e:Expertise)
                RETURN collect(e.expertise_name) AS expertise_names
                """
                author_result = neo4j_driver.run_query(author_query, parameters={"query_id": query_id})
                old_expertises = [record["expertise_names"] for record in author_result][0]

                removed_expertises = [expertise for expertise in old_expertises if expertise not in new_expertises]
                added_expertises = [expertise for expertise in new_expertises if expertise not in old_expertises]

                for expertise in removed_expertises:
                    delete_query = """
                        MATCH (n:Author {id: $query_id})-[r:have_expertise]->(e:Expertise {expertise_name: $expertise_name})
                        DELETE r
                    """ 
                    neo4j_driver.run_query(delete_query, parameters={"query_id": query_id, "expertise_name": expertise})

                for expertise in added_expertises:
                    create_query = """
                        MATCH (n:Author {id: $query_id}), (e:Expertise {expertise_name: $expertise_name})
                        CREATE (n)-[:have_expertise]->(e)
                    """
                    neo4j_driver.run_query(create_query, parameters={"query_id": query_id, "expertise_name": expertise})
                
                new_degrees = [degree.degree_name for degree in author_data.degree]

                degree_query = """
                MATCH (n:Author {id: $query_id})-[r:have_degree]->(d:Degree)
                RETURN collect(d.degree_name) AS degree_names
                """
                degree_result = neo4j_driver.run_query(degree_query, parameters={"query_id": query_id})
                old_degrees = [record["degree_names"] for record in degree_result][0]

                removed_degrees = [degree for degree in old_degrees if degree not in new_degrees]
                added_degrees = [degree for degree in new_degrees if degree not in old_degrees]

                for degree in removed_degrees:
                    delete_query = """
                    MATCH (n:Author {id: $query_id})-[r:have_degree]->(d:Degree {degree_name: $degree_name})
                    DELETE r
                    """
                    neo4j_driver.run_query(delete_query, parameters={"query_id": query_id, "degree_name": degree})

                for degree in added_degrees:
                    create_query = """
                    MERGE (d:Degree {degree_name: $degree_name})
                    """
                    neo4j_driver.run_query(create_query, parameters={"degree_name": degree})
                    create_relation_query = """
                    MATCH (n:Author {id: $query_id}), (d:Degree {degree_name: $degree_name})
                    CREATE (n)-[:have_degree]->(d)
                    """
                    neo4j_driver.run_query(create_relation_query, parameters={"query_id": query_id, "degree_name": degree})

            except Exception as e:
                raise HTTPException(status_code=500, detail=f"An error occurred while processing author with ID {query_id}: {str(e)}")

        return {"message": "Data imported successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/form_import_data")
async def import_data(data: ImportArticle):
    print(data)
    #UNWIND คือ แปลง array ให้กลายเป็นหลายแถวตามปกติ
    try:
        query = """
        UNWIND $data AS article 
        MERGE (a:Article {
            title: article.title
        })
        ON CREATE SET 
            a.article_number = article.article_number,
            a.content_type = article.content_type,
            a.doi = article.doi,
            a.end_page = article.end_page,
            a.publication_title = article.publication_title,
            a.publication_year = article.publication_year,
            a.publisher = article.publisher,
            a.start_page = article.start_page,
            a.title = article.title,
            a.abstract = article.abstract,
            a.keyword = article.keyword,
            a.abstract_url = article.abstract_url


        WITH a, $data.authors AS authors
        UNWIND authors AS author
        MERGE (auth:Author {
            full_name: author.full_name
            
        })
        ON CREATE SET 
            auth.authorUrl = author.authorUrl,
            auth.website = author.website,
            auth.pic_name = author.pic_name,
            auth.full_name = author.full_name,
            auth.name_th = author.name_th,
            auth.office = author.office,
            auth.country = author.country,
            auth.email = author.email,
            auth.id = author.id,
            auth.province = author.province

        MERGE (a)-[:HAS_AUTHOR]->(auth)

        WITH author, auth
        UNWIND author.expertise AS expertise

        WITH author, auth, expertise
        
        WHERE expertise.expertise_name IS NOT NULL AND expertise.expertise_name <> '' 
        MERGE (e:Expertise {expertise_name: expertise.expertise_name})
        ON CREATE SET e.expertise_name = expertise.expertise_name

        MERGE (auth)-[:have_expertise]->(e)
        
        WITH author, auth
        UNWIND author.degree AS degree  

        WITH author, auth, degree
        WHERE degree.degree_name IS NOT NULL AND degree.degree_name <> ''
        
        MERGE (d:Degree {degree_name: degree.degree_name})
        ON CREATE SET d.degree_name = degree.degree_name

        MERGE (auth)-[:have_degree]->(d) 


        """
        result = neo4j_driver.run_query(query, parameters={"data": data.dict()})


        return {"message": "Data imported successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")



@app.get("/insert_author_scopus")
async def get_data(scopus_id: int):
    try:
        # กำหนดพารามิเตอร์สำหรับค้นหา
        params = {
            # "query": f"AUTHLASTNAME({author})",
            # "query": f"AUTHLASTNAME({author}) ",
            # "query": f"AUTHFIRST({firstname})",
            # "query": f"AUTHLASTNAME({author}) AND AUTHFIRST({firstname})",
            'query': f"AU-ID({scopus_id})",
            # "query": f"AFFIL({study})", 
        }

        headers = {
            "X-ELS-APIKey": "d0015166cced5292a4264636dc52e087"
        }
        
        # ทำ HTTP request
        response = requests.get("https://api.elsevier.com/content/search/scopus", headers=headers, params=params)

        # ตรวจสอบสถานะของการ request
        if response.status_code == 200:

            data = response.json()


            return data  # ส่งข้อมูลที่ถูกกรองกลับไปยังเว็บไซต์
        else:
            # หากไม่สามารถเรียกข้อมูลได้
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")






# สร้าง API สำหรับลบโหนด Author และการจัดการโหนดที่เกี่ยวข้อง
@app.delete("/delete_author/{author_id}")
async def delete_author(author_id: int):
    try:
        # ตรวจสอบความสัมพันธ์กับโหนด degree
        degree_query = """
        MATCH (author:Author)-[:have_degree]->(degree:Degree)
        WHERE id(author) = $author_id
        RETURN degree , id(degree) AS id_degree
        """
        degree_result = neo4j_driver.run_query(degree_query, parameters={"author_id": author_id})

        for record in degree_result:
            degree_id = record["id_degree"]

            # ตรวจสอบว่าโหนด degree มีความสัมพันธ์กับโหนด author อื่นๆ หรือไม่
            #id(author) <> $author_id  คือ โหนด author ไม่มี id ตรงกับ $author_id
            other_authors_with_degree_query = """
            MATCH (author:Author)-[:have_degree]->(degree:Degree)
            WHERE id(degree) = $degree_id AND id(author) <> $author_id 
            RETURN count(author) as count
            """
            other_authors_with_degree_result = neo4j_driver.run_query(other_authors_with_degree_query, parameters={"degree_id": degree_id, "author_id": author_id})
            for result in other_authors_with_degree_result:
                count = result["count"]

                if count == 0:
                    # ถ้าโหนด degree ไม่มีความสัมพันธ์กับโหนด author อื่นๆ
                    # ให้ลบโหนด degree และเส้นเชื่อม have_degree
                    delete_degree_query = """
                    MATCH (degree:Degree)
                    WHERE id(degree) = $degree_id
                    DETACH DELETE degree
                    """
                    neo4j_driver.run_query(delete_degree_query, parameters={"degree_id": degree_id})
                else: #มากกว่า 0
                    # ถ้าโหนด degree มีความสัมพันธ์กับโหนด author อื่นๆ
                    # ให้ลบแค่เส้นเชื่อม have_degree
                    delete_degree_relationship_query = """
                    MATCH (author:Author)-[r:have_degree]->(degree:Degree)
                    WHERE id(author) = $author_id AND id(degree) = $degree_id
                    DELETE r
                    """
                    neo4j_driver.run_query(delete_degree_relationship_query, parameters={"author_id": author_id, "degree_id": degree_id})

        # ตรวจสอบความสัมพันธ์กับโหนด expertise
        expertise_query = """
        MATCH (author:Author)-[r:have_expertise]->(expertise:Expertise)
        WHERE id(author) = $author_id
        DELETE r
        """
        neo4j_driver.run_query(expertise_query, parameters={"author_id": author_id})

        # ตรวจสอบความสัมพันธ์กับโหนด article
        article_query = """
        MATCH (author:Author)-[r:HAS_AUTHOR]->(article:Article)
        WHERE id(author) = $author_id
        DELETE r
        """
        neo4j_driver.run_query(article_query, parameters={"author_id": author_id})

        # ลบโหนด author
        delete_author_query = """
        MATCH (author:Author)
        WHERE id(author) = $author_id
        DETACH DELETE author
        """
        neo4j_driver.run_query(delete_author_query, parameters={"author_id": author_id})

        return {"message": "Author deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.delete("/delete_research/{article_id}")
async def delete_article(article_id: int):
    try:
        # ตรวจสอบว่าโหนด article มีเส้นเชื่อม HAS_AUTHOR กับโหนด author หรือไม่
        check_has_author_query = """
        MATCH (article:Article)-[:HAS_AUTHOR]->()
        WHERE id(article) = $article_id
        RETURN count(*) as count
        """
        has_author_result = neo4j_driver.run_query(check_has_author_query, parameters={"article_id": article_id})
         
        for result in has_author_result:
            has_author_count = result["count"]#ได้จำนวนเส้นเชื่อม HAS_AUTHOR 

            if has_author_count > 0:
                # มีเส้นเชื่อม
                # ลบเส้นเชื่อม HAS_AUTHOR ที่เชื่อมกับโหนด author
                delete_has_author_query = """
                MATCH (article:Article)-[r:HAS_AUTHOR]->(author:Author)
                WHERE id(article) = $article_id
                DELETE r
                """
                neo4j_driver.run_query(delete_has_author_query, parameters={"article_id": article_id})

        # ลบโหนด article
        delete_article_query = """
        MATCH (article:Article) WHERE id(article) = $article_id
        DELETE article
        """
        neo4j_driver.run_query(delete_article_query, parameters={"article_id": article_id})

        return {"message": "Article deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    

@app.post("/add_expertise")
async def create_expertise(expertise: ImportExpertise):
    query = """
    CREATE (n:Expertise {expertise_name: $expertise_name})
    RETURN n, id(n) AS id
    """
    parameters = {"expertise_name": expertise.expertise_name}
    result = neo4j_driver.run_query(query, parameters)
    
    if not result:
        raise HTTPException(status_code=404, detail="Node not created")
    
    created_node = result[0]
    return {
        "node": dict(created_node["n"]),
        "id": created_node["id"]
    }

@app.put("/edit_expertise")
async def edit_expertise(expertise: ExpertiseEdit):
    query = """
    MATCH (n:Expertise {expertise_name: $expertise_name})
    SET n.expertise_name = $new_expertise_name
    RETURN n, id(n) AS id
    """
    parameters = {
        "expertise_name": expertise.expertise_name,
        "new_expertise_name": expertise.new_expertise_name
    }
    result = neo4j_driver.run_query(query, parameters)
    
    if not result:
        raise HTTPException(status_code=404, detail="Node not found")
    
    updated_node = result[0]
    return {
        "node": dict(updated_node["n"]),
        "id": updated_node["id"]
    }

@app.delete("/delete_expertise")
async def delete_expertise(expertise: ImportExpertise):
    query = """
    MATCH (n:Expertise {expertise_name: $expertise_name})
    DETACH DELETE n
    RETURN COUNT(n) AS deleted_count
    """
    parameters = {"expertise_name": expertise.expertise_name}
    result = neo4j_driver.run_query(query, parameters)
    
    if result[0]["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="Node not found")
    
    return {"message": "Node deleted successfully"}