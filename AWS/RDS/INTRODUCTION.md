# AWS RDS and Database Types Overview

## Relational Database - AWS RDS

- **Structured Data**: Data stored in tables with a fixed **schema**.
- **Entity**: A row in the table.
- **Attributes**: Columns or metadata of the entity.
- Requires data to **fit perfectly** into predefined table structures.

### Supported Database Engines in AWS RDS:
- SQL
- PostgreSQL
- MySQL
- Oracle
- MariaDB
- Amazon Aurora

### SQL (Structured Query Language):
- Used to manage and manipulate relational databases.
- Supports:
  - Complex **queries**
  - **JOIN** operations
  - **Transactions**

---

## NoSQL - Non-Relational Database

- Example: **Amazon DynamoDB**
- Designed for **semi-structured** or **unstructured** data.
- No fixed schema.
- Uses **document-oriented** or **key-value** data models.
- Suitable for **big data applications** needing:
  - High performance
  - Low latency
- May contain **duplicated data** in a single, denormalized table.

### Data Types:
- **Semi-structured**: Organized, but no strict schema (e.g., JSON).
- **Unstructured**: No organization or schema (e.g., videos, logs, etc.)

### Unstructured Data Storage:
- **Amazon S3**
- Local file systems

---

## Use Case Comparison

| Database Type | Structure        | Examples            | Best For                                        |
|---------------|------------------|----------------------|--------------------------------------------------|
| Relational    | Structured        | MySQL, PostgreSQL    | Complex queries, strict data integrity           |
| NoSQL         | Semi-structured   | DynamoDB             | Scalability, performance, flexible data models   |
| Storage       | Unstructured      | S3                   | Media files, backups, logs                       |