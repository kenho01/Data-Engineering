# Data Warehouse

# OLTP Vs OLAP
| Aspect                   | OLTP (Online Transaction Processing)                    | OLAP (Online Analytical Processing)                                       |
|--------------------------|---------------------------------------------------------|---------------------------------------------------------------------------|
| **Purpose**              | Control and run essential business operations in real time | Plan, solve problems, support decisions, discover hidden insights         |
| **Data updates**         | Short, fast updates, initiated by user                  | Data periodically refreshed with scheduled, long-running batch jobs       |
| **Database Design**      | Normalized databases for efficiency                     | Denormalized databases for analysis                                       |
| **Space Requirements**   | Generally small if historical data is archived          | Generally large due to aggregating large datasets                         |
| **Backup and Recovery**  | Regular backups required to ensure business continuity and meet legal and governance requirements | Lost data can be reloaded from OLTP database as needed in lieu of regular backups |
| **Productivity**         | Increases productivity of end users                     | Increases productivity of business managers, data analysts, and executives |
| **Data View**            | Lists day-to-day business transactions                  | Multi-dimensional view of enterprise data                                 |
| **User Examples**        | Customer-facing personnel                               | Data analysts, business analysts, etc.                                    |

# Partitioning Vs Clustering
A partitioned table is a table divided to sections by partitions. Dividing a large table into smaller partitions allows for improved performance and reduced costs by controlling the amount of data retrieved from a query.

Clustering sorts the data based on one or more columns in the table. The order of the clustered columns determines the sort order of the data. Clustering can improve the performance of certain types of queries, such as queries that use filter clauses and queries that aggregate data. Clustering is useful when the cardinality of the number of values in a column or a group or columns is large.

Table with data size < 1GB, do not show significant improvement with partitioning and clustering.