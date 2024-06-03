SELECT 'CREATE DATABASE postgres'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'postgres')\gexec
\c mydb
-- CREATE DATABASE IF not EXISTS EXISTS;
-- USE logs_db;


CREATE TABLE IF NOT EXISTS logs (
    ids TEXT,
    msg_datetime TIMESTAMP WITH TIME ZONE,
    obj_track_id INTEGER,
    labels VARCHAR(128),
    scores NUMERIC,
    left_coords INTEGER,
    upper_coords INTEGER,
    right_coords INTEGER,
    down_coords INTEGER,
    created_at TIMESTAMP WITH TIME ZONE,
    PRIMARY KEY (ids, msg_datetime)
)
;

-- INSERT INTO logs (ids, msg_datetime, obj_track_id, labels, scores, left_coords, upper_coords, right_coords, down_coords) VALUES
-- ('98639d3c-debe-4f66-996b-cab2e595188c', '2024-05-24T00:51:34.444709', 8, 'person', 0.478506, 746, 404, 951, 715),
-- ('98639d3c-debe-4f66-996b-cab2e526373d', '2024-05-24T00:51:34.444710', 8, 'person', 0.745102, 746, 405, 952, 714),
-- ('98639d3c-dlhe-4f66-736b-cab2e595188c', '2024-05-24T00:51:34.444711', 8, 'person', 0.958475, 746, 406, 953, 713)
-- ;