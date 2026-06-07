# SQL Week 3 Challenge — Chocolate Sales Analysis

**Score: 24 / 25**

## Overview

A 20-question SQL challenge built around a chocolate sales dataset. Raw data was imported into PostgreSQL using Python (pandas + SQLAlchemy), then queried to answer business questions spanning aggregations, joins, subqueries, and window functions.

## Dataset

Five tables: `sales`, `products`, `stores`, `customers`, `calendar`

## Tech Stack

- **Python** — pandas, SQLAlchemy, pathlib
- **PostgreSQL** — query execution and data storage
- **Custom utility** — `psql_insert_copy` (via `db_utils`) for fast bulk data loading
- **Google Docs** — query screenshots and submission

## Topics Covered

- Aggregates: `SUM`, `AVG`, `COUNT`
- `GROUP BY` and `HAVING`
- Joins (inner, multi-table)
- Subqueries
- `CASE` statements
- Window functions
- CTEs

## Questions Tackled

| # | Question |
|---|----------|
| 1 | Total orders in the sales table |
| 2 | Unique product categories |
| 3 | Total registered customers |
| 4 | Stores and their cities |
| 5 | Products with cocoa percentage > 70% |
| 6 | Product count per brand |
| 7 | Sales where a discount was applied |
| 8 | Total revenue across all sales |
| 9 | Total profit from all orders |
| 10 | Min and max profit from a single order |
| 11 | Total quantity sold per product category |
| 12 | Store name, city, and total revenue per store |
| 13 | Brand with the highest total profit |
| 14 | Country generating the most total revenue |
| 15 | Revenue by loyalty vs non-loyalty members |
| 16 | Top 5 products by total quantity sold |
| 17 | Revenue by store type (retail, online, etc.) |
| 18 | Average order revenue by customer gender |
| 19 | City with the highest number of orders |
| 20 | Products priced above the average unit price |

## Files

- `import_data.py` — loads CSVs into PostgreSQL via pandas + SQLAlchemy
- `dataset` - contains the CSV files used 
- `db_utils.py` — contains the `psql_insert_copy` helper for bulk inserts
- `queries.sql` — all 20 queries with comments
- `screenshots/` — query output screenshots (as submitted)
