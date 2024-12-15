-- Table: public.cluster_info

-- DROP TABLE IF EXISTS public.cluster_info;

CREATE TABLE IF NOT EXISTS public.cluster_info
(
    id bigint NOT NULL DEFAULT nextval('cluster_info_id_seq'::regclass),
    subreddit text COLLATE pg_catalog."default",
    post_date date,
    num_of_post integer,
    avg_num_comment numeric,
    avg_len_content numeric,
    avg_score numeric,
    cluster_id bigint,
    number_of_comment bigint,
    CONSTRAINT cluster_info_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cluster_info
    OWNER to postgres;