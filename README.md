# ETL Pipeline for Healthcare Associated Infections Data

**Author**: Janaki Chandrapalakal  
**Student ID**: G02550105  

## 1. Project Overview

**Project Title**: ETL Pipeline for Healthcare Associated Infections Data

**Description**:  
This project builds an end-to-end ETL pipeline that extracts healthcare infection data, cleans and transforms it, and loads it into a PostgreSQL database using Docker. Final visualizations uncover trends in infection types.

---

## 2. Development Environment

| Component            | Tool / Setup Used           |
|----------------------|-----------------------------|
| IDE                  | Visual Studio Code          |
| Programming Language | Python 3.x                  |
| Database             | PostgreSQL (via Docker)     |
| Data Storage         | CSV file (raw & clean)      |
| Orchestration        | Manual Python scripts       |
| Containerization     | Docker + docker-compose     |
| Visualization        | Matplotlib / Seaborn        |

---

## 3. Data Extraction

**Source of Data**:  
[CMS Healthcare-Associated Infections Dataset](https://data.cms.gov/provider-data/dataset/77hc-ibv8)

**Extraction Method**:  
Used `pandas` to read the CSV file and saved it to the local directory.

---

## 4. Data Transformation

**Transformations Performed**:
- Dropped missing or duplicate values
- Converted data types
- Engineered new feature: *Infection Rate*

---

## 5. Data Loading

**Target Database**:  
PostgreSQL running in a Docker container.

**Method Used**:  
Used `psycopg2` to insert cleaned records into a PostgreSQL table.

---

## 6. ETL Pipeline Integration

The ETL pipeline is orchestrated through a main Python script that integrates extraction, transformation, and loading steps, and runs a verification query on the target database.

---

## 7. Data Analysis & Visualization

**Analysis**:  
- Descriptive statistics
- Grouping by infection type
- Calculation of average infection scores

**Visualizations Created**:
- Bar chart of Top 15 Infection Types by Average log(Score)
- Bar chart of Average log(Score + 1) by State

---

## 8. Challenges and Troubleshooting

**Issues Faced**:
- Docker networking errors
- Missing columns in raw data
- Data type mismatches during loading

**Solutions**:
- Used Docker Compose to properly link services
- Used `.fillna()` to manage null values
- Explicitly converted data types before loading into the database

---

## 9. Conclusion

This project demonstrates a practical ETL pipeline for healthcare data. I learned to apply real-world techniques including Docker-based containerization, PostgreSQL integration, data validation, and visualization using Python.
