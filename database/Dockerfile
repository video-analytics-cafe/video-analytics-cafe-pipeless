FROM postgres:14-alpine

# Set the working directory inside the container
WORKDIR /docker-entrypoint-initdb.d

# Copy the SQL script into the container
COPY ./database/init_db.sql /docker-entrypoint-initdb.d/init_db.sql

# Expose the default PostgreSQL port
EXPOSE 5432
