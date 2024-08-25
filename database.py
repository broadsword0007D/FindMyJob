from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://avnadmin:AVNS_Pt-JwTOsyw48zx7sT2V@mysql-findmyjob-findmyjob.h.aivencloud.com:15865/defaultdb?charset=utf8mb4")

def load_jobs(): 
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
        jobs=[]
        rows = result.fetchall()  # Use fetchall() to retrieve all results
        for row in rows:
           jobs.append(dict(row))
    return jobs
    