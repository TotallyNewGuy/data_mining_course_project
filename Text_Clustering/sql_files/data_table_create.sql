-- Table: public.sports

-- DROP TABLE IF EXISTS public.sports;

CREATE TABLE IF NOT EXISTS public.sports
(
    private_id integer NOT NULL DEFAULT nextval('sports_private_id_seq'::regclass),
    post_id character varying(8) COLLATE pg_catalog."default" NOT NULL,
    subreddit character varying(25) COLLATE pg_catalog."default",
    post_title text COLLATE pg_catalog."default",
    post_content text COLLATE pg_catalog."default",
    post_score integer,
    post_create date,
    command_content text[] COLLATE pg_catalog."default",
    command_score integer[],
    command_create date[],
    CONSTRAINT sports_private_id_key UNIQUE (private_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sports
    OWNER to postgres;