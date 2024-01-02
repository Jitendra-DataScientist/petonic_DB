--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: challenge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.challenge (
    challenge_id smallint NOT NULL,
    initiator_id character varying,
    initiation_timestamp timestamp without time zone,
    industry character varying,
    process character varying,
    domain character varying,
    creation_timestamp timestamp without time zone,
    name character varying(255),
    description text
);


ALTER TABLE public.challenge OWNER TO postgres;

--
-- Name: challenge_json_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.challenge_json_data (
    challenge_identifier character varying NOT NULL,
    json_data json
);


ALTER TABLE public.challenge_json_data OWNER TO postgres;

--
-- Name: challenge_params; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.challenge_params (
    challenge_param_id smallint NOT NULL,
    challenge_id smallint,
    question_id smallint,
    question character varying,
    key character varying,
    value double precision,
    description character varying
);


ALTER TABLE public.challenge_params OWNER TO postgres;

--
-- Name: challenge_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.challenge_status (
    challenge_id smallint NOT NULL,
    challenge_status character varying
);


ALTER TABLE public.challenge_status OWNER TO postgres;

--
-- Name: COLUMN challenge_status.challenge_status; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.challenge_status.challenge_status IS 'UD, RA, RS, CC, dup, reject';


--
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    company_id smallint NOT NULL,
    company_name character varying,
    company_description character varying
);


ALTER TABLE public.company OWNER TO postgres;

--
-- Name: define_challenge; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.define_challenge (
    challenge_name character varying,
    challenge_id smallint NOT NULL
);


ALTER TABLE public.define_challenge OWNER TO postgres;

--
-- Name: define_challenge_variables; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.define_challenge_variables (
    key character varying,
    value double precision,
    description character varying,
    challenge_id smallint
);


ALTER TABLE public.define_challenge_variables OWNER TO postgres;

--
-- Name: domain_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.domain_list (
    domain_id smallint NOT NULL,
    industry_id smallint,
    name character varying
);


ALTER TABLE public.domain_list OWNER TO postgres;

--
-- Name: financial_impact_criteria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financial_impact_criteria (
    fin_impact_id integer NOT NULL,
    impact_area character varying,
    impact_description character varying
);


ALTER TABLE public.financial_impact_criteria OWNER TO postgres;

--
-- Name: financial_impact_criteria_fin_impact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.financial_impact_criteria_fin_impact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.financial_impact_criteria_fin_impact_id_seq OWNER TO postgres;

--
-- Name: financial_impact_criteria_fin_impact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.financial_impact_criteria_fin_impact_id_seq OWNED BY public.financial_impact_criteria.fin_impact_id;


--
-- Name: financial_impact_parameters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financial_impact_parameters (
    fin_impact_id smallint,
    parameter_name character varying,
    parameter_description character varying
);


ALTER TABLE public.financial_impact_parameters OWNER TO postgres;

--
-- Name: financial_summary_projections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financial_summary_projections (
    challenge_id smallint,
    year smallint,
    analysis_name character varying,
    param_name character varying,
    projected integer,
    actual integer
);


ALTER TABLE public.financial_summary_projections OWNER TO postgres;

--
-- Name: financial_summary_static; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.financial_summary_static (
    challenge_id smallint NOT NULL,
    start_year smallint,
    end_year smallint,
    end_notes character varying
);


ALTER TABLE public.financial_summary_static OWNER TO postgres;

--
-- Name: industry_domain_process_key_factors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.industry_domain_process_key_factors (
    industry text,
    domain text,
    process text,
    key_factor text,
    suggested_values text,
    description text
);


ALTER TABLE public.industry_domain_process_key_factors OWNER TO postgres;

--
-- Name: industry_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.industry_list (
    industry_id smallint NOT NULL,
    name character varying
);


ALTER TABLE public.industry_list OWNER TO postgres;

--
-- Name: non_financial_impact_criteria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.non_financial_impact_criteria (
    non_fin_impact_id integer NOT NULL,
    impact_area character varying,
    impact_description character varying
);


ALTER TABLE public.non_financial_impact_criteria OWNER TO postgres;

--
-- Name: non_financial_impact_criteria_non_fin_impact_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq OWNER TO postgres;

--
-- Name: non_financial_impact_criteria_non_fin_impact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq OWNED BY public.non_financial_impact_criteria.non_fin_impact_id;


--
-- Name: non_financial_impact_parameters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.non_financial_impact_parameters (
    non_fin_impact_id smallint,
    parameter_name character varying,
    parameter_description character varying
);


ALTER TABLE public.non_financial_impact_parameters OWNER TO postgres;

--
-- Name: non_financial_summary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.non_financial_summary (
    challenge_id smallint NOT NULL,
    end_notes character varying,
    analysis_name character varying,
    param_name character varying,
    type character varying,
    start_date timestamp without time zone,
    end_date timestamp without time zone
);


ALTER TABLE public.non_financial_summary OWNER TO postgres;

--
-- Name: process_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.process_list (
    process_id smallint NOT NULL,
    domain_id smallint,
    name character varying
);


ALTER TABLE public.process_list OWNER TO postgres;

--
-- Name: scenario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scenario (
    key character varying
);


ALTER TABLE public.scenario OWNER TO postgres;

--
-- Name: scenario_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scenario_user (
    challenge_id smallint NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.scenario_user OWNER TO postgres;

--
-- Name: score_params; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.score_params (
    name character varying
);


ALTER TABLE public.score_params OWNER TO postgres;

--
-- Name: score_params_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.score_params_user (
    challenge_id smallint NOT NULL,
    desirability smallint,
    feasibility smallint,
    visibility smallint,
    innovation_score smallint,
    investment smallint,
    investment_in_time smallint,
    investment_in_money smallint,
    strategic_fit smallint
);


ALTER TABLE public.score_params_user OWNER TO postgres;

--
-- Name: user_login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_login (
    user_id character varying NOT NULL,
    company_id smallint,
    email character varying,
    password character varying,
    role character varying
);


ALTER TABLE public.user_login OWNER TO postgres;

--
-- Name: COLUMN user_login.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.user_login.user_id IS 'generated in backend while signup';


--
-- Name: user_signup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_signup (
    f_name character varying,
    l_name character varying,
    user_id character varying NOT NULL
);


ALTER TABLE public.user_signup OWNER TO postgres;

--
-- Name: COLUMN user_signup.user_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.user_signup.user_id IS 'generated in backend';


--
-- Name: validation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.validation (
    user_id character varying NOT NULL
);


ALTER TABLE public.validation OWNER TO postgres;

--
-- Name: financial_impact_criteria fin_impact_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_impact_criteria ALTER COLUMN fin_impact_id SET DEFAULT nextval('public.financial_impact_criteria_fin_impact_id_seq'::regclass);


--
-- Name: non_financial_impact_criteria non_fin_impact_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.non_financial_impact_criteria ALTER COLUMN non_fin_impact_id SET DEFAULT nextval('public.non_financial_impact_criteria_non_fin_impact_id_seq'::regclass);


--
-- Name: challenge_json_data challenge_json_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge_json_data
    ADD CONSTRAINT challenge_json_data_pkey PRIMARY KEY (challenge_identifier);


--
-- Name: challenge_params challenge_params_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge_params
    ADD CONSTRAINT challenge_params_pkey PRIMARY KEY (challenge_param_id);


--
-- Name: challenge challenge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_pkey PRIMARY KEY (challenge_id);


--
-- Name: challenge_status challenge_status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_pkey PRIMARY KEY (challenge_id);


--
-- Name: company company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (company_id);


--
-- Name: define_challenge define_challenge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.define_challenge
    ADD CONSTRAINT define_challenge_pkey PRIMARY KEY (challenge_id);


--
-- Name: domain_list domain_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.domain_list
    ADD CONSTRAINT domain_pkey PRIMARY KEY (domain_id);


--
-- Name: financial_impact_criteria financial_impact_criteria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_impact_criteria
    ADD CONSTRAINT financial_impact_criteria_pkey PRIMARY KEY (fin_impact_id);


--
-- Name: financial_summary_static financial_summary_static_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_summary_static
    ADD CONSTRAINT financial_summary_static_pkey PRIMARY KEY (challenge_id);


--
-- Name: industry_list industry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.industry_list
    ADD CONSTRAINT industry_pkey PRIMARY KEY (industry_id);


--
-- Name: non_financial_impact_criteria non_financial_impact_criteria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.non_financial_impact_criteria
    ADD CONSTRAINT non_financial_impact_criteria_pkey PRIMARY KEY (non_fin_impact_id);


--
-- Name: non_financial_summary non_financial_summary_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.non_financial_summary
    ADD CONSTRAINT non_financial_summary_pkey PRIMARY KEY (challenge_id);


--
-- Name: process_list process_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.process_list
    ADD CONSTRAINT process_pkey PRIMARY KEY (process_id);


--
-- Name: scenario_user scenario_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scenario_user
    ADD CONSTRAINT scenario_user_pkey PRIMARY KEY (challenge_id);


--
-- Name: score_params_user score_params_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_pkey PRIMARY KEY (challenge_id);


--
-- Name: user_login user_login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_pkey PRIMARY KEY (user_id);


--
-- Name: user_signup user_signup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_pkey PRIMARY KEY (user_id);


--
-- Name: validation validation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_pkey PRIMARY KEY (user_id);


--
-- Name: challenge challenge_initiator_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_initiator_id_fkey FOREIGN KEY (initiator_id) REFERENCES public.user_login(user_id);


--
-- Name: challenge_params challenge_params_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge_params
    ADD CONSTRAINT challenge_params_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: challenge_status challenge_status_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: define_challenge define_challenge_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.define_challenge
    ADD CONSTRAINT define_challenge_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: define_challenge_variables define_challenge_variables_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.define_challenge_variables
    ADD CONSTRAINT define_challenge_variables_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: domain_list domain_industry_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.domain_list
    ADD CONSTRAINT domain_industry_id_fkey FOREIGN KEY (industry_id) REFERENCES public.industry_list(industry_id);


--
-- Name: financial_impact_parameters financial_impact_parameters_fin_impact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_impact_parameters
    ADD CONSTRAINT financial_impact_parameters_fin_impact_id_fkey FOREIGN KEY (fin_impact_id) REFERENCES public.financial_impact_criteria(fin_impact_id);


--
-- Name: financial_summary_projections financial_summary_projections_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_summary_projections
    ADD CONSTRAINT financial_summary_projections_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: financial_summary_static financial_summary_static_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.financial_summary_static
    ADD CONSTRAINT financial_summary_static_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: non_financial_impact_parameters non_financial_impact_parameters_non_fin_impact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.non_financial_impact_parameters
    ADD CONSTRAINT non_financial_impact_parameters_non_fin_impact_id_fkey FOREIGN KEY (non_fin_impact_id) REFERENCES public.non_financial_impact_criteria(non_fin_impact_id);


--
-- Name: non_financial_summary non_financial_summary_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.non_financial_summary
    ADD CONSTRAINT non_financial_summary_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: process_list process_domain_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.process_list
    ADD CONSTRAINT process_domain_id_fkey FOREIGN KEY (domain_id) REFERENCES public.domain_list(domain_id);


--
-- Name: scenario_user scenario_user_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scenario_user
    ADD CONSTRAINT scenario_user_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: score_params_user score_params_user_challenge_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);


--
-- Name: user_login user_login_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.company(company_id);


--
-- Name: user_signup user_signup_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_login(user_id);


--
-- Name: validation validation_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_signup(user_id);


--
-- Name: validation validation_user_id_fkey1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_user_id_fkey1 FOREIGN KEY (user_id) REFERENCES public.user_login(user_id);


--
-- PostgreSQL database dump complete
--

