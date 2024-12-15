-- Table: public.cluster

-- DROP TABLE IF EXISTS public.cluster;

CREATE TABLE IF NOT EXISTS public.cluster
(
    id bigint NOT NULL DEFAULT nextval('cluster_id_seq'::regclass),
    cluster_id integer,
    score_sum integer,
    day_diff integer,
    post_date date,
    num_of_comment integer,
    subreddit text COLLATE pg_catalog."default",
    list_of_post text[] COLLATE pg_catalog."default",
    CONSTRAINT cluster_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cluster
    OWNER to postgres;