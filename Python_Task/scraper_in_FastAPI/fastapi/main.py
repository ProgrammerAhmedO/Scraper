from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import List, Optional

DATABASE_URL = "postgresql://postgres:Cliver@98@localhost/Puffin"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ScrapeData(Base):
    __tablename__ = "scraped_data"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/scrape/")
def scrape_website():
    try:
        import requests
        from bs4 import BeautifulSoup

        website_url = "https://example.com"  
        response = requests.get(website_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title_element = soup.find("h1")
        description_element = soup.find("p")
        
        if title_element and description_element:
            title = title_element.text
            description = description_element.text
            scraped_data = {
                "title": title,
                "description": description
            }

            db = SessionLocal()
            db_data = ScrapeData(**scraped_data)
            db.add(db_data)
            db.commit()
            db.refresh(db_data)
            db.close()

            return db_data
        else:
            raise HTTPException(status_code=500, detail="Failed to extract data from website")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/scraped_data/")
def get_scraped_data(title: Optional[str] = None, description: Optional[str] = None):
    db = SessionLocal()
    query = db.query(ScrapeData)

    if title:
        query = query.filter(ScrapeData.title.ilike(f"%{title}%"))
    if description:
        query = query.filter(ScrapeData.description.ilike(f"%{description}%"))

    data = query.all()
    db.close()
    return data
