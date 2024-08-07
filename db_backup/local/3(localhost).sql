PGDMP  '        
             |            postgres    16.0    16.0 f    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    5    postgres    DATABASE     {   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE postgres;
                postgres    false            �           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    5017                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            �           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    17835 	   challenge    TABLE     �  CREATE TABLE public.challenge (
    challenge_id smallint NOT NULL,
    initiator_id character varying,
    initiation_timestamp timestamp without time zone,
    industry character varying,
    process character varying,
    domain character varying,
    creation_timestamp timestamp without time zone,
    name character varying(255),
    description text,
    contributor_id character varying(255),
    approver_id character varying(255)
);
    DROP TABLE public.challenge;
       public         heap    postgres    false            �            1259    18069    challenge_json_data    TABLE     u   CREATE TABLE public.challenge_json_data (
    challenge_identifier character varying NOT NULL,
    json_data json
);
 '   DROP TABLE public.challenge_json_data;
       public         heap    postgres    false            �            1259    17856    challenge_params    TABLE       CREATE TABLE public.challenge_params (
    challenge_param_id smallint NOT NULL,
    challenge_id smallint,
    question_id smallint,
    question character varying,
    key character varying,
    value double precision,
    description character varying
);
 $   DROP TABLE public.challenge_params;
       public         heap    postgres    false            �            1259    17842    challenge_status    TABLE     �   CREATE TABLE public.challenge_status (
    challenge_id smallint NOT NULL,
    challenge_status character varying,
    json_data json
);
 $   DROP TABLE public.challenge_status;
       public         heap    postgres    false            �           0    0 (   COLUMN challenge_status.challenge_status    COMMENT     ]   COMMENT ON COLUMN public.challenge_status.challenge_status IS 'UD, RA, RS, CC, dup, reject';
          public          postgres    false    222            �            1259    17781    company    TABLE     �   CREATE TABLE public.company (
    company_id smallint NOT NULL,
    company_name character varying,
    company_description character varying
);
    DROP TABLE public.company;
       public         heap    postgres    false            �            1259    18390    contributor_json    TABLE     �   CREATE TABLE public.contributor_json (
    challenge_identifier character varying(255),
    contributor_id character varying(255),
    json_data json
);
 $   DROP TABLE public.contributor_json;
       public         heap    postgres    false            �            1259    17873    define_challenge    TABLE     s   CREATE TABLE public.define_challenge (
    challenge_name character varying,
    challenge_id smallint NOT NULL
);
 $   DROP TABLE public.define_challenge;
       public         heap    postgres    false            �            1259    17880    define_challenge_variables    TABLE     �   CREATE TABLE public.define_challenge_variables (
    key character varying,
    value double precision,
    description character varying,
    challenge_id smallint
);
 .   DROP TABLE public.define_challenge_variables;
       public         heap    postgres    false            �            1259    18378    domain_list    TABLE     a   CREATE TABLE public.domain_list (
    domain_id bigint,
    industry_id bigint,
    name text
);
    DROP TABLE public.domain_list;
       public         heap    postgres    false            �            1259    17893    financial_impact_criteria    TABLE     �   CREATE TABLE public.financial_impact_criteria (
    fin_impact_id integer NOT NULL,
    impact_area character varying,
    impact_description character varying
);
 -   DROP TABLE public.financial_impact_criteria;
       public         heap    postgres    false            �            1259    17892 +   financial_impact_criteria_fin_impact_id_seq    SEQUENCE     �   CREATE SEQUENCE public.financial_impact_criteria_fin_impact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 B   DROP SEQUENCE public.financial_impact_criteria_fin_impact_id_seq;
       public          postgres    false    231            �           0    0 +   financial_impact_criteria_fin_impact_id_seq    SEQUENCE OWNED BY     {   ALTER SEQUENCE public.financial_impact_criteria_fin_impact_id_seq OWNED BY public.financial_impact_criteria.fin_impact_id;
          public          postgres    false    230            �            1259    17901    financial_impact_parameters    TABLE     �   CREATE TABLE public.financial_impact_parameters (
    fin_impact_id smallint,
    parameter_name character varying,
    parameter_description character varying
);
 /   DROP TABLE public.financial_impact_parameters;
       public         heap    postgres    false            �            1259    17920    financial_summary_projections    TABLE     �   CREATE TABLE public.financial_summary_projections (
    challenge_id smallint,
    year smallint,
    analysis_name character varying,
    param_name character varying,
    projected integer,
    actual integer
);
 1   DROP TABLE public.financial_summary_projections;
       public         heap    postgres    false            �            1259    17885    financial_summary_static    TABLE     �   CREATE TABLE public.financial_summary_static (
    challenge_id smallint NOT NULL,
    start_year smallint,
    end_year smallint,
    end_notes character varying
);
 ,   DROP TABLE public.financial_summary_static;
       public         heap    postgres    false            �            1259    18036 #   industry_domain_process_key_factors    TABLE     �   CREATE TABLE public.industry_domain_process_key_factors (
    industry text,
    domain text,
    process text,
    key_factor text,
    suggested_values text,
    description text
);
 7   DROP TABLE public.industry_domain_process_key_factors;
       public         heap    postgres    false            �            1259    18373    industry_list    TABLE     M   CREATE TABLE public.industry_list (
    industry_id bigint,
    name text
);
 !   DROP TABLE public.industry_list;
       public         heap    postgres    false            �            1259    17907    non_financial_impact_criteria    TABLE     �   CREATE TABLE public.non_financial_impact_criteria (
    non_fin_impact_id integer NOT NULL,
    impact_area character varying,
    impact_description character varying
);
 1   DROP TABLE public.non_financial_impact_criteria;
       public         heap    postgres    false            �            1259    17906 3   non_financial_impact_criteria_non_fin_impact_id_seq    SEQUENCE     �   CREATE SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 J   DROP SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq;
       public          postgres    false    234            �           0    0 3   non_financial_impact_criteria_non_fin_impact_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public.non_financial_impact_criteria_non_fin_impact_id_seq OWNED BY public.non_financial_impact_criteria.non_fin_impact_id;
          public          postgres    false    233            �            1259    17915    non_financial_impact_parameters    TABLE     �   CREATE TABLE public.non_financial_impact_parameters (
    non_fin_impact_id smallint,
    parameter_name character varying,
    parameter_description character varying
);
 3   DROP TABLE public.non_financial_impact_parameters;
       public         heap    postgres    false            �            1259    17925    non_financial_summary    TABLE     ,  CREATE TABLE public.non_financial_summary (
    challenge_id smallint NOT NULL,
    end_notes character varying,
    analysis_name character varying,
    param_name character varying,
    type character varying,
    start_date timestamp without time zone,
    end_date timestamp without time zone
);
 )   DROP TABLE public.non_financial_summary;
       public         heap    postgres    false            �            1259    18383    process_list    TABLE     a   CREATE TABLE public.process_list (
    domain_id bigint,
    process_id bigint,
    name text
);
     DROP TABLE public.process_list;
       public         heap    postgres    false            �            1259    17830    scenario    TABLE     <   CREATE TABLE public.scenario (
    key character varying
);
    DROP TABLE public.scenario;
       public         heap    postgres    false            �            1259    17849    scenario_user    TABLE     �   CREATE TABLE public.scenario_user (
    challenge_id smallint NOT NULL,
    name character varying,
    description character varying
);
 !   DROP TABLE public.scenario_user;
       public         heap    postgres    false            �            1259    17863    score_params    TABLE     A   CREATE TABLE public.score_params (
    name character varying
);
     DROP TABLE public.score_params;
       public         heap    postgres    false            �            1259    17868    score_params_user    TABLE     3  CREATE TABLE public.score_params_user (
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
 %   DROP TABLE public.score_params_user;
       public         heap    postgres    false            �            1259    17795 
   user_login    TABLE     �   CREATE TABLE public.user_login (
    user_id character varying NOT NULL,
    company_id smallint,
    email character varying,
    password character varying,
    role character varying
);
    DROP TABLE public.user_login;
       public         heap    postgres    false            �           0    0    COLUMN user_login.user_id    COMMENT     T   COMMENT ON COLUMN public.user_login.user_id IS 'generated in backend while signup';
          public          postgres    false    218            �            1259    17788    user_signup    TABLE     �   CREATE TABLE public.user_signup (
    f_name character varying,
    l_name character varying,
    user_id character varying NOT NULL
);
    DROP TABLE public.user_signup;
       public         heap    postgres    false            �           0    0    COLUMN user_signup.user_id    COMMENT     H   COMMENT ON COLUMN public.user_signup.user_id IS 'generated in backend';
          public          postgres    false    217            �            1259    17802 
   validation    TABLE     K   CREATE TABLE public.validation (
    user_id character varying NOT NULL
);
    DROP TABLE public.validation;
       public         heap    postgres    false            �           2604    17896 '   financial_impact_criteria fin_impact_id    DEFAULT     �   ALTER TABLE ONLY public.financial_impact_criteria ALTER COLUMN fin_impact_id SET DEFAULT nextval('public.financial_impact_criteria_fin_impact_id_seq'::regclass);
 V   ALTER TABLE public.financial_impact_criteria ALTER COLUMN fin_impact_id DROP DEFAULT;
       public          postgres    false    230    231    231            �           2604    17910 /   non_financial_impact_criteria non_fin_impact_id    DEFAULT     �   ALTER TABLE ONLY public.non_financial_impact_criteria ALTER COLUMN non_fin_impact_id SET DEFAULT nextval('public.non_financial_impact_criteria_non_fin_impact_id_seq'::regclass);
 ^   ALTER TABLE public.non_financial_impact_criteria ALTER COLUMN non_fin_impact_id DROP DEFAULT;
       public          postgres    false    233    234    234            }          0    17835 	   challenge 
   TABLE DATA           �   COPY public.challenge (challenge_id, initiator_id, initiation_timestamp, industry, process, domain, creation_timestamp, name, description, contributor_id, approver_id) FROM stdin;
    public          postgres    false    221   =�       �          0    18069    challenge_json_data 
   TABLE DATA           N   COPY public.challenge_json_data (challenge_identifier, json_data) FROM stdin;
    public          postgres    false    239   ��       �          0    17856    challenge_params 
   TABLE DATA           |   COPY public.challenge_params (challenge_param_id, challenge_id, question_id, question, key, value, description) FROM stdin;
    public          postgres    false    224   Ȅ       ~          0    17842    challenge_status 
   TABLE DATA           U   COPY public.challenge_status (challenge_id, challenge_status, json_data) FROM stdin;
    public          postgres    false    222   �       x          0    17781    company 
   TABLE DATA           P   COPY public.company (company_id, company_name, company_description) FROM stdin;
    public          postgres    false    216   Y�       �          0    18390    contributor_json 
   TABLE DATA           [   COPY public.contributor_json (challenge_identifier, contributor_id, json_data) FROM stdin;
    public          postgres    false    243   څ       �          0    17873    define_challenge 
   TABLE DATA           H   COPY public.define_challenge (challenge_name, challenge_id) FROM stdin;
    public          postgres    false    227   ��       �          0    17880    define_challenge_variables 
   TABLE DATA           [   COPY public.define_challenge_variables (key, value, description, challenge_id) FROM stdin;
    public          postgres    false    228   �       �          0    18378    domain_list 
   TABLE DATA           C   COPY public.domain_list (domain_id, industry_id, name) FROM stdin;
    public          postgres    false    241   1�       �          0    17893    financial_impact_criteria 
   TABLE DATA           c   COPY public.financial_impact_criteria (fin_impact_id, impact_area, impact_description) FROM stdin;
    public          postgres    false    231   Ύ       �          0    17901    financial_impact_parameters 
   TABLE DATA           k   COPY public.financial_impact_parameters (fin_impact_id, parameter_name, parameter_description) FROM stdin;
    public          postgres    false    232   ��       �          0    17920    financial_summary_projections 
   TABLE DATA           y   COPY public.financial_summary_projections (challenge_id, year, analysis_name, param_name, projected, actual) FROM stdin;
    public          postgres    false    236   m�       �          0    17885    financial_summary_static 
   TABLE DATA           a   COPY public.financial_summary_static (challenge_id, start_year, end_year, end_notes) FROM stdin;
    public          postgres    false    229   ��       �          0    18036 #   industry_domain_process_key_factors 
   TABLE DATA           �   COPY public.industry_domain_process_key_factors (industry, domain, process, key_factor, suggested_values, description) FROM stdin;
    public          postgres    false    238   ��       �          0    18373    industry_list 
   TABLE DATA           :   COPY public.industry_list (industry_id, name) FROM stdin;
    public          postgres    false    240   /      �          0    17907    non_financial_impact_criteria 
   TABLE DATA           k   COPY public.non_financial_impact_criteria (non_fin_impact_id, impact_area, impact_description) FROM stdin;
    public          postgres    false    234   \0      �          0    17915    non_financial_impact_parameters 
   TABLE DATA           s   COPY public.non_financial_impact_parameters (non_fin_impact_id, parameter_name, parameter_description) FROM stdin;
    public          postgres    false    235   �3      �          0    17925    non_financial_summary 
   TABLE DATA              COPY public.non_financial_summary (challenge_id, end_notes, analysis_name, param_name, type, start_date, end_date) FROM stdin;
    public          postgres    false    237   �D      �          0    18383    process_list 
   TABLE DATA           C   COPY public.process_list (domain_id, process_id, name) FROM stdin;
    public          postgres    false    242   �D      |          0    17830    scenario 
   TABLE DATA           '   COPY public.scenario (key) FROM stdin;
    public          postgres    false    220   �                0    17849    scenario_user 
   TABLE DATA           H   COPY public.scenario_user (challenge_id, name, description) FROM stdin;
    public          postgres    false    223   ,�      �          0    17863    score_params 
   TABLE DATA           ,   COPY public.score_params (name) FROM stdin;
    public          postgres    false    225   I�      �          0    17868    score_params_user 
   TABLE DATA           �   COPY public.score_params_user (challenge_id, desirability, feasibility, visibility, innovation_score, investment, investment_in_time, investment_in_money, strategic_fit) FROM stdin;
    public          postgres    false    226   f�      z          0    17795 
   user_login 
   TABLE DATA           P   COPY public.user_login (user_id, company_id, email, password, role) FROM stdin;
    public          postgres    false    218   ��      y          0    17788    user_signup 
   TABLE DATA           >   COPY public.user_signup (f_name, l_name, user_id) FROM stdin;
    public          postgres    false    217   ��      {          0    17802 
   validation 
   TABLE DATA           -   COPY public.validation (user_id) FROM stdin;
    public          postgres    false    219   }�      �           0    0 +   financial_impact_criteria_fin_impact_id_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public.financial_impact_criteria_fin_impact_id_seq', 1, false);
          public          postgres    false    230            �           0    0 3   non_financial_impact_criteria_non_fin_impact_id_seq    SEQUENCE SET     b   SELECT pg_catalog.setval('public.non_financial_impact_criteria_non_fin_impact_id_seq', 1, false);
          public          postgres    false    233            �           2606    18077 ,   challenge_json_data challenge_json_data_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.challenge_json_data
    ADD CONSTRAINT challenge_json_data_pkey PRIMARY KEY (challenge_identifier);
 V   ALTER TABLE ONLY public.challenge_json_data DROP CONSTRAINT challenge_json_data_pkey;
       public            postgres    false    239            �           2606    17862 &   challenge_params challenge_params_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.challenge_params
    ADD CONSTRAINT challenge_params_pkey PRIMARY KEY (challenge_param_id);
 P   ALTER TABLE ONLY public.challenge_params DROP CONSTRAINT challenge_params_pkey;
       public            postgres    false    224            �           2606    17841    challenge challenge_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_pkey PRIMARY KEY (challenge_id);
 B   ALTER TABLE ONLY public.challenge DROP CONSTRAINT challenge_pkey;
       public            postgres    false    221            �           2606    17848 &   challenge_status challenge_status_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_pkey PRIMARY KEY (challenge_id);
 P   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT challenge_status_pkey;
       public            postgres    false    222            �           2606    17787    company company_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (company_id);
 >   ALTER TABLE ONLY public.company DROP CONSTRAINT company_pkey;
       public            postgres    false    216            �           2606    17879 &   define_challenge define_challenge_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.define_challenge
    ADD CONSTRAINT define_challenge_pkey PRIMARY KEY (challenge_id);
 P   ALTER TABLE ONLY public.define_challenge DROP CONSTRAINT define_challenge_pkey;
       public            postgres    false    227            �           2606    17900 8   financial_impact_criteria financial_impact_criteria_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.financial_impact_criteria
    ADD CONSTRAINT financial_impact_criteria_pkey PRIMARY KEY (fin_impact_id);
 b   ALTER TABLE ONLY public.financial_impact_criteria DROP CONSTRAINT financial_impact_criteria_pkey;
       public            postgres    false    231            �           2606    17891 6   financial_summary_static financial_summary_static_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.financial_summary_static
    ADD CONSTRAINT financial_summary_static_pkey PRIMARY KEY (challenge_id);
 `   ALTER TABLE ONLY public.financial_summary_static DROP CONSTRAINT financial_summary_static_pkey;
       public            postgres    false    229            �           2606    17914 @   non_financial_impact_criteria non_financial_impact_criteria_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.non_financial_impact_criteria
    ADD CONSTRAINT non_financial_impact_criteria_pkey PRIMARY KEY (non_fin_impact_id);
 j   ALTER TABLE ONLY public.non_financial_impact_criteria DROP CONSTRAINT non_financial_impact_criteria_pkey;
       public            postgres    false    234            �           2606    17931 0   non_financial_summary non_financial_summary_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.non_financial_summary
    ADD CONSTRAINT non_financial_summary_pkey PRIMARY KEY (challenge_id);
 Z   ALTER TABLE ONLY public.non_financial_summary DROP CONSTRAINT non_financial_summary_pkey;
       public            postgres    false    237            �           2606    17855     scenario_user scenario_user_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.scenario_user
    ADD CONSTRAINT scenario_user_pkey PRIMARY KEY (challenge_id);
 J   ALTER TABLE ONLY public.scenario_user DROP CONSTRAINT scenario_user_pkey;
       public            postgres    false    223            �           2606    17872 (   score_params_user score_params_user_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_pkey PRIMARY KEY (challenge_id);
 R   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT score_params_user_pkey;
       public            postgres    false    226            �           2606    18396 #   contributor_json unique_combination 
   CONSTRAINT     ~   ALTER TABLE ONLY public.contributor_json
    ADD CONSTRAINT unique_combination UNIQUE (challenge_identifier, contributor_id);
 M   ALTER TABLE ONLY public.contributor_json DROP CONSTRAINT unique_combination;
       public            postgres    false    243    243            �           2606    17801    user_login user_login_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_pkey PRIMARY KEY (user_id);
 D   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_pkey;
       public            postgres    false    218            �           2606    17794    user_signup user_signup_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_pkey PRIMARY KEY (user_id);
 F   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT user_signup_pkey;
       public            postgres    false    217            �           2606    17808    validation validation_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_pkey PRIMARY KEY (user_id);
 D   ALTER TABLE ONLY public.validation DROP CONSTRAINT validation_pkey;
       public            postgres    false    219            �           2606    17937 %   challenge challenge_initiator_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_initiator_id_fkey FOREIGN KEY (initiator_id) REFERENCES public.user_login(user_id);
 O   ALTER TABLE ONLY public.challenge DROP CONSTRAINT challenge_initiator_id_fkey;
       public          postgres    false    218    4798    221            �           2606    17942 3   challenge_params challenge_params_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge_params
    ADD CONSTRAINT challenge_params_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 ]   ALTER TABLE ONLY public.challenge_params DROP CONSTRAINT challenge_params_challenge_id_fkey;
       public          postgres    false    221    4802    224            �           2606    17992 3   challenge_status challenge_status_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 ]   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT challenge_status_challenge_id_fkey;
       public          postgres    false    221    4802    222            �           2606    17977 3   define_challenge define_challenge_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.define_challenge
    ADD CONSTRAINT define_challenge_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 ]   ALTER TABLE ONLY public.define_challenge DROP CONSTRAINT define_challenge_challenge_id_fkey;
       public          postgres    false    221    4802    227            �           2606    17982 G   define_challenge_variables define_challenge_variables_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.define_challenge_variables
    ADD CONSTRAINT define_challenge_variables_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 q   ALTER TABLE ONLY public.define_challenge_variables DROP CONSTRAINT define_challenge_variables_challenge_id_fkey;
       public          postgres    false    221    228    4802            �           2606    18012 J   financial_impact_parameters financial_impact_parameters_fin_impact_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.financial_impact_parameters
    ADD CONSTRAINT financial_impact_parameters_fin_impact_id_fkey FOREIGN KEY (fin_impact_id) REFERENCES public.financial_impact_criteria(fin_impact_id);
 t   ALTER TABLE ONLY public.financial_impact_parameters DROP CONSTRAINT financial_impact_parameters_fin_impact_id_fkey;
       public          postgres    false    232    4816    231            �           2606    17967 M   financial_summary_projections financial_summary_projections_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.financial_summary_projections
    ADD CONSTRAINT financial_summary_projections_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 w   ALTER TABLE ONLY public.financial_summary_projections DROP CONSTRAINT financial_summary_projections_challenge_id_fkey;
       public          postgres    false    221    236    4802            �           2606    17962 C   financial_summary_static financial_summary_static_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.financial_summary_static
    ADD CONSTRAINT financial_summary_static_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 m   ALTER TABLE ONLY public.financial_summary_static DROP CONSTRAINT financial_summary_static_challenge_id_fkey;
       public          postgres    false    4802    221    229            �           2606    18017 V   non_financial_impact_parameters non_financial_impact_parameters_non_fin_impact_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.non_financial_impact_parameters
    ADD CONSTRAINT non_financial_impact_parameters_non_fin_impact_id_fkey FOREIGN KEY (non_fin_impact_id) REFERENCES public.non_financial_impact_criteria(non_fin_impact_id);
 �   ALTER TABLE ONLY public.non_financial_impact_parameters DROP CONSTRAINT non_financial_impact_parameters_non_fin_impact_id_fkey;
       public          postgres    false    235    4818    234            �           2606    17972 =   non_financial_summary non_financial_summary_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.non_financial_summary
    ADD CONSTRAINT non_financial_summary_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 g   ALTER TABLE ONLY public.non_financial_summary DROP CONSTRAINT non_financial_summary_challenge_id_fkey;
       public          postgres    false    237    4802    221            �           2606    17987 -   scenario_user scenario_user_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.scenario_user
    ADD CONSTRAINT scenario_user_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 W   ALTER TABLE ONLY public.scenario_user DROP CONSTRAINT scenario_user_challenge_id_fkey;
       public          postgres    false    221    223    4802            �           2606    17957 5   score_params_user score_params_user_challenge_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_challenge_id_fkey FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 _   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT score_params_user_challenge_id_fkey;
       public          postgres    false    226    4802    221            �           2606    18007 %   user_login user_login_company_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.company(company_id);
 O   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_company_id_fkey;
       public          postgres    false    216    4794    218            �           2606    17932 $   user_signup user_signup_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_login(user_id);
 N   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT user_signup_user_id_fkey;
       public          postgres    false    4798    218    217            �           2606    17947 "   validation validation_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.user_signup(user_id);
 L   ALTER TABLE ONLY public.validation DROP CONSTRAINT validation_user_id_fkey;
       public          postgres    false    219    217    4796            �           2606    17952 #   validation validation_user_id_fkey1    FK CONSTRAINT     �   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_user_id_fkey1 FOREIGN KEY (user_id) REFERENCES public.user_login(user_id);
 M   ALTER TABLE ONLY public.validation DROP CONSTRAINT validation_user_id_fkey1;
       public          postgres    false    219    4798    218            }   ^   x�3����,�L,�/���,I�K)J��K�L�v(H-���L����4202�54�54V04�26�21�tr�J-I����.M�p����CF\1z\\\ �'      �      x������ � �      �      x������ � �      ~   d   x�Mͱ�@���#�{�|^Rh���2���z�'ׅណ}ZGt]�R�]�9�)�[��lK�/��BW��l��$��)��ȌpH6Ѵ>�R�]�      x   q   x�uʻ�0 �:7�'�� %�c'��!�R`[���鮻���q�]��g��~u/�='���Pp�rY�\N.�����1r�r͘��\'�(Węk�k��k�kEw`�d�pk�O�'      �      x������ � �      �      x������ � �      �      x������ � �      �   �  x��X]s�:}ƿL��.2�����IU�Ʌԝ�}����ef��~OK,>��ejҧ-���Z���{�͗&|�\U!���N�j��	�줪dQ��}mĦ"��v[����*�򊯄�`쏆������n4�
a��Ͷ��g�i�������r��~o;�׼)��t��-H�;���E�iYrz��Jo�Ad�m��֕؛�}{���j΍�F��AF�o9B��ږJ��u����1G���SV+�"7Mi�r`3��?��_.}~N6��X�m7C���*w�6����Ȼ����VZMi����n�� ���IVn��`�r�)N��.Q|���_?;|���U��)뀍Z���%*U��u�r@�t�zΡMa�ljKBD"�q)QCA'�Vh����7� �͒��P�vQ�1�Ǎ��+�bBy)\M�Y � �`h�0�/��w�;�R��� ���(ࣻ5�F0_M�����\/pyr8~�b]�R��`2��x)q����^+���YP��wd��WTƒ����_ld]?��*K�zLh�b#J2�x�'�Pע�����xٴq���ǝyn6�"�FHm�Ͷ��'^�ݕgy��To�͡8u�8yѽb֋{��r�]0�`���:�u*P��$��M�TB�Xh�>��w{�~3Q���v�_t������3���k��a<�~�̮v�z�#@�bc��VQ���ۀwR��������KK��ɀ䆇�/��z��@S�
%��@2V��OX/�]��pgK���Q�F��C�@�JK�C;Jb��E���1��+�[ՇTO�����~�҂�������A��af��s�V|Q�ڄo[��r ����O�NU�x�j/�{F�� e��,�/<,&<]� ��t�w<u`0�#� L7���W�4�Vc)䮔���\�@�OJ�-m\�j���nHض�B�t�A��']S�cb�޹"��š�U)4��N��;��o�������pUsd|n�u����wl�b�}d���&� �YB�ǝ,����,��/j6���� �a;�z�h �L �e�{#�����(Glc��$P��<���"�`8�c�/:�(��;*���)�wֻF���{���CU� �����υ1���~� �}��ӫp"~�z���@:de�^9)���Ue׋\>�yB�5�ה��O��Q� �|T�E�u�<�Eް� έ`k��b�J�4���&l��*��]I8�."�;��]��e�~�yFn�~���l7�����*	��j�2!|�����!J�v ���܈�,���%�ˬ9"-*P�*�F^���{>�]qP!��T۷���P��*I����$�ّE2$�*%Io֝eګC��3��c8�\��,�a����@ꜝ)��/�<���h2'ߌ|�FU1���S?��3�K�C�'�v����J[�{��Q7+�Q��C�����f�C�)r�E���ؐ��a
HL����'�hW8$��%Ɣ�7��N�:.�tI�<-F�E�� r����(H�vA��~�`jB"L�l����(��� ؁\��j���E��4�^�2p�ɍ^h�/��𡑥U�^�PA�6�?�PI!߻'�����j�v?��8~B����� ��[|�<3(v��5w`�L�+R6ji��{�Fd��g_�ڞ��9W'O�Vm��'6 1B�I����w��['���D���3(yد�l��IQ0�z�^���;�W���	��І�*�@4��;yF�y#;a>������/���]]�a�y�B5��N���0��L�[jrV�
̦3���OF>�. ����=���0���P�_m�н�'��Ĉ ;���Ы;�F:��7Y�� ^_-+�x~���w�W$IBء�ҍi����7��-����{�1> �~?1< {�M�gS�_y1<��*�v�p�H)+s��Oh)�ޖK:@7���ח�����,�F
�F���j��+&��Z|
�u�d���A��aF�&�A��?� rn�T��/��^��E1���Tcę��d����0Z���k��3�XL����}s-��9�O����0j qi�=a� ���n*A�G�GNH`�`��	Ðs���4��&��G�5x[Y      �   �  x�uU�r�6<�_1G�JV���ש�!唓�^ r(b J�~}z ��l��9h�t�>n�]����XG�,}��LA���Q�QE�Ν(vL�O4xWst�Ɛ�CL��k+���C��@5`Ö�Xw��w~K=j�V_p��w�����g>��m�Y^	}a��5��.���"=WjJ���0�ģ��K���CǞ�2�����7T�!���MT�K`�Z�wb_����̖[W��B���F{�#(�GR��5$i h�R���=ZS�׾%��:��ʳI8��;�A���3�0m�8���l7e'rQԘݠ�3�0�;e\��$g��]��6:Nל���^M��Vd�O�g��� -8PVO���MߙN'�P>%�H�@xu�8[|.�mKt!�
1�[oU��T+T!�w� ��v��� ��X���!��t���x��p�L=�)	@4�� �~�k ��#����Z��}�R����"�6����8(y���v6H�L�D -R�Ɗ�I�lbI�*L�c3j�fUW�	U-�"��L��[�cW��FCG8�~w�D��+Ju+�W��w6����x�yf�3;�Te8ݢ��R��ӏ-�5f�Vv��P���I��&�9����ͳ/�����"���s��ٶ� ʔF[��A���]p1�PFv4�3���b����d��3i^x�#¦�F������ �v�o�s��z�5 ]F�t�>��&�O{�v�Eœl�h@��+��s<1[ܙ!y=��$,! ǐ�p��'5�Ew�?˒�=_}�D+k��!��|�Ŕ�	����g�����l����.ک�6���rzR��^�[�_���o�ʛ(�@��C�st�c������>JCy^}�v������O����~U��~�%��O��k���w!'�2ސ���P�w}�Uy�첟��뮪�� 0�	�      �   �  x��ZIw�>˿���{��6��G�'~�+��S.`7H"�n� h�̯�W��zI.�j��~����Uz_��uc�G�6��݇_o��oe�`�����;ʪQF֮�񐭄��V�ɦzQ�XF7c��Cu�Ŵ��4'UK��^��=����uk�WG��j��ڟy�[+N�=ڸ�WNI[�����;�{z�E���c}�x��N��F�T�2J�^�M����U�d_�7���0���#eG�n_�p�N� >ǆ�^g<���W/� I�
���N�r�h;Z�Ȗ-#?���b�5d7��,��h���,F�$D�ڀ�~���k������kl�U�T�O^��i�;���X������I�8Is����Ç������vl$�OB"��`�M5:ղ����T��3��$�:^����"	*l���hG��8��f�p���e��f��b�Y����!+;�ZnH4y�N�j�C���F��j�BR|59Ĝ7����9W�E�@ _��;X%~ݥ�+$�oI�$^-�9{Y8X-�33Qe�)W���V:��)�)o�Fӓ�6�=|�j����V}0nK�F���_��V�侗�p���~>�t)���};Y�ʪC�`+�P�S^B�\x-��hU�o��I��/�ڣ��6e���F5���	�h���3Bh�Mt���:H�#�V@"�������F����^���*V��������|�K̑R��Y!Q���B�h�x8���t>�Xha�%)���C4��d�R�:x�p���z��fږ��S{,����PB�w��N;���I�?8�EY���ԙ��GG�(���xT�7�Y�&��RV�Gvl� �L@���Hڼ�/ �*�6�=��x�E�X-�6����bE�}5��2����� 8�����y�X��I�5#����yK�K�u�L�ōw�)L	d� ����I�dDo��V����D�͉?�� ;W<dFS�� ��╥o������#g�G��+	v�7��Q�/9��H'����L�#���{�B�)v�ȩ����a;��,�N�ډ]+�գ�o(�T�S-�C�a��:����So)�����m����Bg�j"¸m3�-XR+���?�ࠗ\�?Cf��+TǷ.s���PG=���J�KB����wGaz����ב�P�,	b���D�K������%����4�!a!��ӱ�I�'b�A���|�J#|��de)#���)�&��x�A����I+�(?u�H���X�$b�������.d����c�4*��z����)�&����ck�oTت�0��#%s�&/���V���d$�4�	ܼ�mT�YM"�āM��/�d�Dl){������&�@Փ��Z`8Q���ү(�[uD�@�`�a�.�a�TH�V�[�:��}���)��6�O(�x�BlV�جc�p���ۛ+��3mMI�^�<i	1��YD)"� 7v�Y���+�.�O�iHd��ba�ʰ �_l)�@ZN*@�&�S%�r���2��ye��W����ī��yESqLN&��r9���5E�TX��z�Z�IҞ�b��ݶzG����j���EP�
u@���1�1���^��`H������ٻ��Ӱ�AU�����:�����Z7����gwXu��:e}�ܘ�\e�$�?��Nmൽ�w1��S,��!Ncm���rj� X�2�V���)�|��4|#�[��D,5��2j��"��u��:=����Hj�L�s{�D,Y�(82�ȡZ�
����6녊�9e�t��/2����#��3�X�%��8d�ۜ�1�ag���*4��!��t��1K Zd��`.�\�a�V
.G�mD���<�PE��Nɋ� &�u�J� �&�
��J`�Y�q�v��3���˫ey�M�"1aF�p>iC�"��;SaN`��ӭ�qf����(*��j1(7���H[�q�����n�oѸ�	f~?�C���"��2"���v����j5�$�δ;�
�|�=PD')�R�^�e�ɥ&̜����H�WMy�n��3;<A�Jq�j�w�p;Y��?����MƏ�E�������$�]��B�4�[�5/�v"��$�<���:�並����mN_��8�D�\=0�=`�(�v�ftF�6E~=vT|��$�s��
�gLٖ7$���t�Y��Y�cM��p�Q� �T�L��]�lA�k��.s�ZX@t�_����@� �p-F��Ң���^i��%��r�|2�'�yV/ ƌ��~M��8!�:����`q�u��V;9�$Q:�<��O���1u�}D
{�Q�ѭ�~ yzl��3K�TW�$�,ً��[�1�����W1��ق��%�6�9窧Hgn��2�}���4%6$�X����8���!��B�Σ,���G�Ɣee�;�0�!M��ʉ�fC$�I�v���I{	
~�>/M5�Qk�q=j�\�P�ǵa�.�˂z\�����ȹ����MC[������U|<��{��	���m�|��2Ͻ<ߘ�Ed,A:�ȉ��,��Y�0N��T��/�*v�kp6;X�&_qg0W�f܍�v��k��U������EyOO���w�땦��<�tҺE<M�gs�m�7����;>�E�5�,��[d��Q�j�Uo�thc���nl����C���F��(
mf�% �P'yC?]�ޣ?�N�LFͲE���p��}���e�LC�X
�EY3A�oVA�2-X�Cu}'���7�?H�W�P8Y{�j
�)|� r�r��Ȅl�I�v�����O�H�/�|H8<K9T����Vx������%�D�a;�+'�ˆ%�`�jh�26k����U?l,��]�w�S�(��ý	ϵK����+�g�y��~�B�Lo�C
������<t�(����񻁃���b��֠.�����?���A؛��Ŭ���j�>S&���~,�/nD��tw2g)Yi���>�tx[�tH�N�L#���|�W>��"|�V�u��Kgh�vQV:B �1�V(��،��p���^�Q���o�n�a:k���H��4uS
��X��-$j��4_�)'&��Aц����Z&W��r�+ ��z���i�I�c'�^ !�ѧ8Df�3}��W,u"&�6�`�o����Ƶ9Xj:N��S����b777���$J�p�&?�\z��ȃ�Cc����~�=��*���G�Y�L+|y Z�/n�gN+����l��r������u��?�V�i�3�|�����|����-��J򛤤�
��4���4s��!�z��1M��tY!��������Ȣ�-�{qVP���?c2��W�[$'���x�O�A��������Z�1�#��y>� �ly�M����q�s]��r�0��U�Ko�B`��M�����hP&�݅E��A�%98�+o�;����_n�fr�Ey�gHߑ_�:=ܶ�/��s,nV���;�O}i8*=Y�&s(�v|HS̎��2��ĕs��6r}�D�xu� ��#���.��Jq��+L�?@����{�"݃��uGޛ�:O�,xX�ϝW����V���tE�,19T{��M�/3�D���ӱ����X���G:Y��3��s��٥Mr]��i�p^Up��#�ǅ�G�i�z���}F�<��h<@|�.$�`�VQ�	�$C��
�	������c4�\�k��ի����#      �      x������ � �      �      x������ � �      �      x�̽�v�H�6z������W�nI.uٳky-�T��}�H���/!��&	6@Z����a��~����D��E@�ך�H �@f�#�x�/�����߲��2_N�|�]��rZ4ٓ��/��>���b���ͺZ��b����y�G�l�y�������UUg���tٔ�7�f�f��ME��L��)���}S5��ɛ�7OG?d��ッ��"o6u��o�l��TWY�����eq�M�i�8��~�?[\]�ӲX��j��f]�Z�ˢy��~<:?�W�բ�������Py8>:��ߗ3 b�/gD�Z^O�E�Ⱦ�MH��u����X��VuY�@���7����)���ԛM������@�����/u>�J���z
+ɯ��aټȿ�c���W��Ʀ�<ܬ�PW���X����b�������ʧx����˃�	ܘg�4���O��U���|�V4@S�K�7,�
@]\u�����j��E1��ǟW��^o�p��ft��w����t�뻺�*{�Y5po�ғ�U]�6�uC�4�^$�ϲ��w��1h䏲���.F�tD���~���i������ق�5�M��vWm��j�����op�+�+�A��"���\~�7��������I�,_g�7���lo��\1F^V+�J,7��X5��'��������
m �@$��kQ-�7����f��҈�VK8��u��iA�m�~�(��W�u��L�r�u�EDn��/�OG�q�`�N�,�X��,r\6�;�w��Ѩ���5N�䏲~Ա�������B>xvL���(*8�뺚*٭�'HG��|����%q�"�OZ��>}2�:�p�)pL��ח=�*<���&�O7s=H�������B?�vU���r^��gSB�?��d�>Ա��S�1��ۛ*[�_�lV4e���X<�~6������(�W�zz��1}�Ľ[���N�2��3��y��HbA���r��1}Q�C?�2��9�Əj� R�]���7���!�s\�ص���q��跳�ZThX]L+8KO>��sBv���J+g�̫�|��#5/���fHD]�f�u�XM���^+��j���n��
D(��S"d^{k4��ރ��!��.�~0����mK�.e�I�00�%)������F/�`�|L�fc�_�F9V�w�9�ȟ�����[U�@P,a�h~_���[b���g�H(�P��X�����f] π���W@4PfMI2��h9c�6��A���X�����%<�g���M��B�@Wd�������"�� �[�lDf�d&���@���e4&�jr���Tඕ��4��A�}f�T�JFX���ӻ���2�&�O8q Ep��b�?���G?����p�k]ݮox�\�8���!'��.S/@�i��5h�
���>�EO�W��֙,�����~��kX��fV�H����-��#WfUL�1�1���C���ƴ�����%���c��)��f
@����l��t(
�Ws�I��6pH#�dt���ϵ��^�/��,.�ar7����77�f>�n�o���.��8�ż���`��kU�7�-X�s6�����8��
�w�Y�'�B�p?��P+?�5g�?f۶���C��Z�N��_�5�l�0���(�3�����X������������C��XT��8�Mv����|,<�t�T�������ʚ�㑙y�P4|��c��~~�W��|���^���)��^��@��;׫��jK��L��nU�^ϫk���j�,\�75� �yG�fS�Rn�������`$lZ ӆ[�3����C�`�~3��ez�:qZ�BdM�<�v����܂���������^ߡX�WW�y�*���>@?>�_|n��|�-�u�O���|�_�*��Bcs�*X>wuCo�E�1�(6��W�vY��`�u��KdǸ�&�s|��j�ѻn[��bf�7��@/f��E��=��肓�m�7�l#߾N��XT,�Eg��lJp%�������y/�/�u?�?خ���/�vXc-ʦy@�yg�O4>�KU͛ѯUu�^6��wk���L� ����Aq��f,8bO��x����D��ytFa�o���F��/Nk����[r��	��a�ś��ѹ�+E��Q�pȍ����&i ��ʚe�'P<^a�6��~yw�@��gy�Y�ܔ+\+���33By�+�V�j�A����?��pf��ʿ�r>��?�\�3�e8�PO�|+-W�����f3#�p>W���� 锑|���6��|�h?����K��=\b�,3���W��gh��-0=�\��X�O|k�e��[2�r�I�~9�;Wx��䳒SE�|�w%pD	ϙ�A��/��C��k�q�`=y���i�z�^�w_�?�c�}^� K����O�,���Y	��&��$��۲5�6�۰�ӫp/�ę��1�&�%D?=��6�n��`P�ik?T�,�d�l�ߝ5a�/��mF��J�K嚣��0�%H�i!5x�h]�T�ۃ���E�	~���؋X�x�٨ï�;P�zEjc�%�ᒈ���rr?"���]�%�a�)e52�	�x����S�Ď4�F�u��;Cv��(��ߘ��n� �h6S3��qX%����H���j�L�D?���%���6���������dt>�eJ�ox��,���Y�^�ZɅ�Х7�ʹ.9��oj��M� �)�kS�s/�U[=�a����[�K������9��h��V<���WsL�A%&�a(/��0�f�f�ڬ�V��w��u��>���9,�t�������:&󅍞ʀh)XjP4h��)kLF	2 8V�0"}H�8e|���'n�,��"�9Q���X�@�=�E/�9v��S��H$�%G��0O�u�#c0TQi̝yA�M|(�����	�+Q��	�i�Dbb�����DlnL��Ѕ�~�����p�@|��%a��I���9�]'/Z,�+���xT�զ���(��v���&����ٛ�(��Ĩ��{T9���P�pl��u��D?<����%�CW4|�Ruq�D/<`�#�S,�Q/�!��҂m�������|��	��)�g�
KQ��4\=)��]-FX:��xT[#8Φ��Q3GV�>M{4�� &��e;ȚrΕ�Itva��dQnlb����7yd\�uՒӁ���w#��S�o�l�S��
1����3j�է_���yᨗK+�)�]` �fۇ|��qǲ��'���S�0((~#�قWE1�ĸ2�����7��'�f9RȺ��#�w4jD�����<.�³������m�,��Z.��dż�$�l1�R�E]�6���b��iJ��#
�.�����,1����?{_sp��;�s��K.�=�P�{�G9���� �N�ޑ���zQ�����7����-ԝ�FH��r^]s��}��m��7K������n��]i��<Z䎎���,�3�E�ܛ.��|��RP8�)�_����7=�5H��\�|}����Ñ��lʷx��j��S�ńn$���l���;Eû��ƞ"<-d!X����!���Hکо���I0[Q��Q�m\s;~x�m'��������������������������/��R�H��ۍڸ�(V�������"��YG�X�c �n�7N)�|�,���<go��d���]��T|@�{��~_��\��B�	����Щ:>HԢ������)��g�>�m>�p鶐=��r�N=��[6L��W]�m��럕زwL��h�`!�k�>"%F !KVbX6M�d�T��=�FG�)QD�=e�j���	�ۓFk�����2!���kH:�����Y��tE����B������m���R�bF��h"F��L�F�{� p��\���X�+�u`�a��I"o5�=�����W_N��Y�ɦ}�v[�f>�֯o`w`s~>�XV��.�֠9]$Z3>a!Lh�^ܫw�s�\^���E>����V���-�ނ��_r�*��휉'��\D�{���!���5��f��G�    ���k��9�e��vU����V�:~��9���47.�k-]7���e'T�1���Q3�iee���Lc�˛j�-��
l���Y�B��s[_�H6�hVX��{ �p��PBAZ AƘYGh�e&�*�`�Ό����"�� S�-#��9G&0���M~@��3H���/��IdQ)w��R8l.�]�,���\�3�͚�y$��<����-���MR�Hj�S�Q�Yu�ز��=��\|��������{̩�9z>�90a�ϐ�*H�_��3O5�B�����;� ���]�o]o��U*�($B����=����O�ar�rz�q(6港|S�>K^ٻ��C��5�n��g���� &E�8
�b�Z���t�iD�)10\,�>�"�����s��M�X�|Pg�V��/|M1��b�,�"8�����7�\�M:Μi?/���i6�/XN'��� ��-�]���)i=������))#1A����`���oP$�{rGa��wsXA��T�Z`���Eå,�V'kO'�_��W�7.��$uQ/T�b@�NF`�\�)� ���s�[q�=�dzS�㝽��Y��89�jڔ����K�S�+I:�Q�̇hY��x@�#Mgt.���QP6�S�iT�3����1�
�n�rb��9;ǸEaUz�(����0�O�M%�]���[��B�Tt��)���:"(dԼVL��3�]NI�|VJw��ݎ��`�p��_�(1�Vƙg'��i��}]I�k��ÆP1.ͣ	�>(����|2C�`�\?Lp�|E�AƩ,ޗ���o�lcBU?r����ݗ�M����;$�"(Q�.g�b�$R|rj�Π{��4�s(��U��֧�%��W
���N�b�o�F�܂FF=��:>T�6��BP1s�a�ÿ�x<����$׮�o�W��C���&+��O��"����Z[��t�]}�6i���/߶�4�f�MoV��1 )���E^�ю� �X,|�5�jRtְki)� �b@3�V�U�l
�j�d3_�c$����AR��r�Pa��uZX�Z�D�"��%�k�r�f���TUz�����c�b|�$c�S���i�7����Z���6�$�
��U%����ou�2x�G?��7u� �j�=ka9G��?��10W�X���ڂ_���bUP_N��Ԏ._`F��Y�a$K�J�Y�r�^t�ϙ���v���^���W˯��'I��&o������g�+i�v�y�㢋�]�Vܱnp�N��E��w� ὆�����/>o���?����R��o���wu���oQ��`Z�vs�T+���}k�--�`A ��B���.�Dx�I��H[��c��B�D�<y�uw�P�%���� W�A������:1R�@/:��ܿ(��޲'��0-�ME=lD��q����bx�g6��������>�B����ݎ���R{n~>6��5'�RA��AO�T�&�K�95Q03*ݳ�P
�r�t�*������.��A���Q�<��ѶN]a"1.�)�=־[����~f<n��%�e�Sr]����~���*ʺd���`�7�oК�w�%�sR:�S�o��Ǒ�G	�.m���uQ�ם2̚C�
У	vJ��J�Ԝ>�y���|�V���>//+�ã��VI�,�#0�9��]�1�纻�*��� X}��ܫ�ץ��P���ωT:�u1-@͸O���D��m_˶���5��M���T����ɠ=�<�#@z�ũ64��'XC��Ë��f�@]k���]/���y����A�zB-<C�hzdc5��	O\Ε�LWrk \S��8���@��k{g-�N@�;!�p��W�J�0�!!�C���Z�v��\}SaO�#�'s#����s8������L_����QW��V�)�X�c����t����q%��S�}�V��bW!Vٮ5ݠƇe�،�]}v;���,�7@�Źa~�zT�k�ݑ��w坏����G{��c4�u(�Yth���\�ۣ_|�ر/V��ys���h�Hn���@O��T�父����=v���wT�׌mv^5��gl^NL��,�|�z����Y5�2z�[A�L�y�K���G��u��P��p��ZQ��)�����<�~:>:�٧�4�� �q=�K}QO�j������m��A8�3��Q<�X�[n��E֗�N�I��o�78H��1���1ؐ�C<��]߁�]9T���e��2d�\�h����t�݀F]��l�r�����Gu�f�B����nE����P��rB��
�8x��6r^���"ZNVz�O�h.���[`��-1�%����1d<'�<_5N��ݥN�c��)Ԛ�܃hV�P�?�A��GUN��h~�j����R��&kfR��1_��M�O�f��ӛe��Q���PKi�����9]��?�S[�!-Ҟʘ�QG�/��SV��&՘��O�ݢ�<_1�\�Cl�ʃ�}��|�����˃�"B_ȤIbMHQ=϶�l)�<��'��t9�G�;��$�� Ժ��5�V�J�E��l��p�u�EGu�H>��ù[�-r����$ݱr��:ޚ��̰��Qgh�!8�ԫ���h�0���lb;=�&$#�)�s�ru�sG(��M��k�5��K��������(DD�vCfɤ���w~�-��<$� �Ɖ��HB8�M�Y��,@w�٢�UI�?�8�����~kN�П���9��"�R,Y w�ٲ���_Vެ�&j��SS&n�Ď���!�3)��2!2�~cA�R�\N)�g�����IB�?��fA��#Ǵ���`������!�?�<<mp��.�nuN:N��y��iAuY�wmш;�o*�e��[�$���ߴ_a��C�:3*��*w��zh{��K�]�D��,�g�j�v��e$0��k�;Œ����.������Q|��?EPhH���@���ٲ��DHM�	��=����i�!t��Ňx�C���P!Shƀ�N����b�W�T�9��3V¾����ʿ��S��qZ� �J���2R6 �`����ak�Df&p�2�_�y�1�t��qO[9C(��b�)1��洩I��fO�\�H��1�r"NTҷb�k�Q�TҽaW��\�3EH$E�MnQ�vo��Q�/�����'(�|����IH�(��I�82�~�"�3#Y�=餓F����|Ən0~>���5n��n~��3��f5Y����xo��;��o�L���o���װS�a���FЋGP�.=�4��!�]�B*-�o�4�?w,_"�>D��qـ��j{���� �!\��y6��cB�b��R �S�FS�{g+#��q{<?�'�a�|�P~�$�{Mu�q
<D�GF_�i9<N9$�O��:�h)9)����>�;�։E��2��,���0�-w�\}%7CHZ�e��T)�Ƭ� ��-�K>��������eG��2`����h��*h��{U��sR��YӮ�	L��x����EL���S>0ݗ��_:-���!7��S���!�~�4ϥ��P1�<0����߯.�-��i �CJ��	�|�i�Wmaߍ]w�"�9~�7!
�(©(�w|�J.�t�
;��k�("�E"i8���똆P��	�����l'�����/��e8O�z�,!U`��I�O�5(��D�[sbS�j]�>���A��mT���K��	�.�Z��7���ER��}c���h�i���@0�7\Q��ô��ӧ��4�gt$��9A�BA/L�¾ �����6�ۺL
�AW-)��d�gm�SGd�K�~zfK�����ڰɌ�Xq����F_<b��)��n!�ƪ?V��1�~�Fo������.�UK��oUTF�Z�6r���J�r��}��b�kYܒ�y���$ۖ�UXj�h���#o�D�̓�H^K��:ơ(��������3���6t� �b+����F�ǭ�]d�K����au>\Gp��nU    L�/?�3�1٬��8�[֡bö���� d٬�M{x�ٶ� m��L9q
���v�L�d�V#��[or,^a3a�}�+�أ�~+A�����k��Ň#<��p��7�aXq�
I�?)����� BLQ���+s�~��h��H�K�PL�:�~�	��
�%#i�ƶ8��8�2��[5�f$WӾlo��tu@��I�m���8/��X+�!ga�bU�jH�Ѹc��3=�uq���(�D�{����lR����+����<B��	+�,I(Zt8�r�ǒ�,�.�%rH옏��L~82�vB��-�w,���+��6�+����)���k��
�����FS���v�$��'~��ud��/�����e��R����(4Z9�>Av��""팦��<����k06W
Zq��Y0Uk;����8�Ơ6��9�#닑��@Jw�-�S #?����m�R��QԵ�(xx�Y����'Cäc��8e7�y�)�c��D9�1!��WjKÅK����f+4,%g=l؎4�	��''>�k�9�6N� 7�$�A�K�AN@a�0{�}��Y��S�3�WM��#�w�3�Y��4��i0s��gN[�N3�ܛy�P��dn�X9ݺ�_�olh�ワ�����qe|�E�H��O���E�ƨ�[�i��#�����ד7g�����Dpgʇ��~|��4� � s~�4�$�K�t>h�+��~��~�S��)�,�`���!f=�ŷ`c�<�灲Sux��LAБ���a���q��s�gUw�~�0�X�%�X����6�M�
`�����{!]���Guǆ���\ _c�$�:�'=֙��k����,�A��<��V��0�E����ʀ1G�����O���"�OZ��I�5\�ݤ��~*7��� g�o��e�u�����ll��8�9�~���K��C��c�JS�!��GS�#7H�m~���c����l��nW5b��d���I�G`�W���.��}�H[p���$���eI���x�e]��`FU��ꎂ��"��w�5��a %`׌�=��܏&OVب��OxWX �z�9	C�NgB���w�Y�Z��o��%���7R��8�.4�xhX�q���
)���W��fm���yiX�٦�׸zh��D�������Ԧ�^���_��XDHھ����?�M1H����h(F5�W��К��k��t����E<5pac��x �3�{��}e1��n��i}��C����m:�I�����i�0]&vFe ��:R
Lޮ���x_R�96�c�_�r�w.I�F�_�p����F~|�?M��,���r��G�޶ew�Ղ�`��Re�I �8��M��@p�m$�	��x?�d+3��5fU�Є`�tL.��T����Q��4.` ^����a�u����+'��O�')�3���0�ih�IRR�+��<a O�)D�ʇ��PR�W7���t�T�+�B˸�u�1d>5M31�i�_���b�	��N���/+���Ć����l�\��a��t�H;�/`y�O	~���%k��)9�'ǉr(}oSU��e�����dۃ,Y����Ɔ����Q���	!b�ցh�y�ݶ��u��I?{���{��y��������&�oq����W8:���\�_
���
T6+j4���9!"��������BU�`���'��!��u�� -�@"�C5�d����-Z$1�{�`Q��k��b��@�q�����M��m���]�=V��S������
7kn8�o4�v�|1��&p�v���n�-O@�ԭ�G��j�|�V?���y��ft�M�y���OSL�V�� 5ujq����g��=K�t�_��Ҋ<�Y�:���\�&��h�ӏ�J��EN�x��-�C�����uh)�m����FU[,�����މ�����Ags���s�e2S��@�	m��/��%��S�-�:nM���UF0��8b�C,-���>����@��7؜Mcv^�a�(�R��ưQP#rh�fs}�6M���D6 	+04+hhW��S���ѣ�J�*3}������r(U�$�M�y�!t����qb�V|d� ~ش��4���.����]b�ο��ciBNNU���i��i�=B	�����E��)�@]��	K� ��2�D��8�x!�G�+�A��ܡ_&؇�Ϳ�Yp����Anm/��]�N� �*�#�T��t�k��|^������|�� 
0t����
Q"�p?���?S�0�iu2�14�"�)����[^���9�V:���
�D!l�� ���^z��[�u�yzuw�)��4$�nn��|�F��!�Mŷ9�Cϴo�~����.���;6�/e�$�����4�{����<F>���F�zg&�����/Q:9�%_���sWf�����r+�MJ*}`�����{�#XN���4��S�O��"�l�n�8zcت>�IXF�R�����
�+��AH���M
`]^8pž�$�%��F�p҈ʵ)�3���7�^�E�$<�šX�@@������,��TU�C���cj�rBN�t�m����7"�W{��̞{Ҹqjd�ꅠ7� o�`���IMm���T�cσ�Y��(�
�� �Q�&�3��O�s�(�����,[��+"����N�~�NQ+��S͹	��iBk��K3dC���p�#���=wPVHOjn�P���2�m�Ԯ��<����N_�hǜvͯ�lR�ٲ͒G��w�r�'���!ǐ�|�1-.�l>�3zQC��&�.r���C��
[&7��ˢia�Z���+Ɉ����1�}�AM��dn��ƞ��ﵧ��Mg�Dh��j&��Ogٓ�0�xtnư8F�(�1�Lfg�|B�fu�P���iZ����[6Ag\Z��4t^�\!�Oj�7k5�]�d��Xd��{�E��A�{j��d 0�+�h՜�j�'��}��ڜ-�����OD\�bƒ�1�����#�[�E�1&�&�0G�Y�����5]�{SS�:�k�� ,b�`@"Vl��}i��3�>�%���@�2 ��[�J�b5��Wy���>��`~*��I\4fH�Jl���P6"Ʌ�|:��ID��3O�>�#vI���8o�UHDCEY{_������9��TױQ�q���73/����!���$^'�ug�G����;$b�-Z��DAʻ���,J@;O�f� �˟�B�G�p7P	U[��.)\y�+�.[���._̮z����4PmŃ�"��W���Mib�R��n�ʛu`/�,uXPq�/xv�/���q��{td�՞as+��ލ}��nC�=�T���F�W���\��	Y-tv����0?`4�"=u^�u5'Ce��m�G=�%T����8Ǒ�!t�<@@x�"�}�?�B���şeT쑪��H^'�4��e�.2�����f�M:��c@|�{^!sr �D9I��b�ێe�/ψ�6�`��ş��"u�H�{Kx�Wj��c�=�D����	Ki�L�e1���&__V�M�Z)�J,��؇*_���Dp�I�9^��|W�?�	8h90�}��^���KG�P(|�B93�*a�E��c�vQ��_z%��JYu☽�x��K���p@f��H�h*�������X��	VO,�4���9���ĞJ�
U�AqMhLU���Έ.�����mq�cͶ9�a-xJ(�a#���#�[��F:��5�ɝq.�;gW�j[���8�����#����d���*�m6���6��� ����8��G���{�<��z:8��;�&��f���mIa�v6)���'ܲ��Ԓ�m������?� ���	v���:n���q؄��*I<jWռ���*{�:�V��~�����ҳ�q.�� ��Ԁ�K�o��?%wOYa�(G�"� zf�/*laZ�WW���Ps���NѠS,3nǓM6�:v��b��л�s�!�c>X-�t�U+�>�v0(@K+Bp7�����    �u�0ߪp��4�I$�̹�c���bVr&X���z���-�E9u�o���>1�2h�Y��s1].�թ#j���{�K߷e��ָ޹A<��H谑ɷ����ihv����J�6�O��$ldWC���$"a�_���L��j{A�X�<�|^p�A pA��n �P⎬ �)�8"j@oCw�U|�M����s������$pB/�5��#�<j�6��6*:i�lo�����2@�'+�ROv물��A6���0�qKԝ���X���莔YsWCM*-9���"�����@�G�{�"\e�7]5N��\��ƌ6��4���i��`���l��D2�	�:�N�Rv�@(����}Qg���~=��.�O�Q�$<J�'H����:,mZ�]f��*/����2:�ف�(&�a�<˵ܕ\�b�
�M485U!��/H½��m�x�k�xlF4�%2����ڙ�\�H/�|g�L�vk�j������t�F�^	�+j��2���L���Dc���\4�杇ۖ� �}�oA�aqu��k�O��+�Kf��5�Y�ri�)�T���sbO3l�G��1��g�����y� ��M�H�;�I�1����h�t��]��5���iЮc����;ڵF�}|�����e3�g@>�P�"2��Wr��C��hb�U'2�i Q�2=�5v��RK���NJ�s�K�ܸ����=����#�]��C�wa��/���'�Ͳ������������<���r�\2;�0쳩��N�ǈy�c�8�}��_�4�6譮6��Ͱ����x��R,��H<�9�'��9�2�� ƭo��;-��y�����G3D��_�n�_�t�ĕ��㨆#�W
1��@?E��ir)��Ŀ���N�.���}c�	0��A���y#��t��[�H?�B��~O�6\B��uq0?_��p+����$���}�b#/���3����(�]�
f���c����J��nG�Pf��C�F���f��c�i�.���7�T�V�4�%��u4�	 ~�}*g,Wq�`��V��1�CoZtN�Ab� y�-:�I������`r�- ?<�P��ҷ�H�.��;�<�N�z�/E�D7����惆
����	��)̕�u���M
��&�H.kQ����^�j�p��/�c��Ӵ*Pm���%� ��N���2�G�VqY����p�L�Lr�0�罕���mF8���-j�-�L��7��a����h��� ��vg��[N��Ii�Y��%	PvwI�oUn�\!8���{����G�[�]KiZ=�A�S�A:�-C�`o[O���b��{@*z��3��=��)j}���L.h#����Y�8��Z��?,l�Xu�wdx0�������V)����;C3E�k�{}+P�!�~!7�am�	�2v�M�0�p���cL��W�|E��A��G]滚i��$iSN�8,T�#5iI�F�2���&���>4H7i��J.U��R�	���*<^�W+��Y�s�Lm0�H�q>�/+M?���ci�q<�#`tH�1�eb�R�㱛K����&��ڣgm�Pb_��˩|��`c�s�k��C^��Tr��,�3%s_��{I}��=�w�x�`j�(H ��>̨��Q�ɑ\�~G�Oϼ��j����T�ptp���H�����+�o%����?9O�� �A�+`�1����Y�l�� =x��u�A{��]�8���7恎��d�3������3���d�����
���S)��"�0\� ��I=$��g/��J	�6�-߄�a�@
$TXER��}��:գ���4�$~�,�u,�Ѭy�:�C2z���բ�.��g]Q���U/�e� !+��!��0{�s���_&�,6���%�k�H"��H2���יK�>��{'Lu��U�}�Gp�˂zu���}�,�7��qz�/1S�~8x&*��P�N5n��A�΂�[$k�bC�l�|��FwF��F^Fi�hv��E�s����C�|ie;�&\��V��(��F�Nd��~�4�:\wKz��4��N�	|��pb8��y5 �d�9���9./X{R�vz4�s���`jm)XYT��2b�~*���D'����	�d.�W����[��/i��������X�W�~�a	��~4����S����-�A7�����NݓԈ_��S�w��Gr�e����[�.������ߎ�3���}��*I-���T��+�=��zhl�i��蛧��UW�|��r���!��Q�f�(}�}����1����h"l�C�%A�J��KO�MŸl��k�j��&74���F���R��]���THʅ�ZE_O^��C4��
����A~���So?~V�qCM�'�t|�͝��&��� �K�9��<���TjRY�d�d$����w͊E�~���.�q��+q�F�VW�o%wPb�aa]�f�Z5s��v�H��������W$�ٵ��cC�n.g*S`mm{g���v핤T+������#�g��:� ۲��}�>;�@�7��]?ȶ�J�P���`Re��јJC
�h��OM.�YĽ�\�ڬ�9Wal@�67�j�)���S(ij�;���G[1�.w2�K�cd�M�G�S/>^<��3E��,2���T�W%2�5�݁���?y������ls_MO�2g�Ƙ**Y�c���,4�-�$�Y����);۶5�L�i�$A4��3���rN����u8��iS�-�)���q��V���<ysA�%�
Lu��|�Ύ�,�W:��c�|�a��2G��r~׷nP�6B���V��S*�wl��@����-���I��p������,5�uA��p��h/;ݡV��D�<+�%Xm��L`;l��NRt�h(y�Q�i#��=��0Awm�
�l�awͽ�y6G#�/��#�����|`D�M��mv��l�i�h��L��`�_�bt���m�g����ʪ�Om�SW��h��#:#���#;�|�+�������s��Ol��7�zH'<�rüМ&[_�x�X��c�����w&Sc���H:�Dހ�.�>�����Q���K5[��JA��� ^3,e���ƽ����R�437�-n�����LZЕB�&���s��̠&�?��>`wY��|�Y�s�-��i�.S����6��P�;�<(!<Բs<��o��K�����lܣ��84�=�h�EW�`���$�>�g5 �@�g&�p,�md�%�Q%��K�=ۄ%�e��X�Gw�&��|a)c)��y�E||��
��(7��÷�s���^�o�P%&�7�a�b���Y16�~I� V�Ml4�;@ՠ�@���^<�?\-F�:+6�Aۭ[b?얄��5��p�q�h�P0	��v�N`�$[��(���#P�[I`�n��68�%�I��ޭ����ɧ��YU���g$V�;;	_�����bO�L9��0e� ��p�w>l�t�)�Iuα=�Z�X�����z���i+9�}�Zeo����g�I�^�N�\2�9<p���cAX��e�L�/XCd�����K�8�^k!�f�Q1���ꔾ�~r���y��.6~ԁ�&�pMJ�Lt�W�0HXQ�ht��x,}��%��[RYn��p$���I]=k y���k8oaJ����s{���Z�RD�!��O&Mt��5�=�a�-�`�Nf��L&g�Fg[!z��R�@�vru Ǧp8u�}$��p*�������!�A�o�f��qǋ���Q�W���n"��L��x���dXI��@��˸��i
c<�t'@�($էE2PEE�XCBqG̋Xm��|t^1ވL91��X�a���ƼŶ"o^�N��.b��ʒ�g��J���t֙3��>� ��yC��6w4r��gB��r��$(�b=ęv�di�������)(��W�Y?����i�M�OQ�Sl�R�nʶ��zq�S��X�.�$VLc�2�'<"�=A����r��dJI�(q�$��*<"�� ���|f�<�X�!����(��?,��ԥ�~7�#^�|�,E��Qa    �P9��8,���f�r����W��I4�^PL�И*U���r[����Oe ����k�khM��:�xd��!��W�d��FFL��}�pOӂ��ioO�)�:#��6��h��.��&!��b�l��jg��.n=��[����5U.�{�RꦴU��"������ʒh��s��i�F'uM�7U5�p��,2
M�D�5rm33�A�e'����|�'Cl`�Ա,��X��0��ۺZU�v y��rq&Wkϔ��͚��h�G´�w
��!��@�58v��ص5Oj����=��#��n!9���v	W��*vX��*�$�W?G���
&�{��JƇ��9	���kL�����s4 �6�`��h;ܞ�T]A����`�@��;�}~�1� B[;]�ë[�+s��h��D5B�U�݉���+��O6�W��hՒ��n_��ܧm��ׅ��9��P�f:(��
a����4�5'v|�TFR�4J�Z����Ϫ���ZQV*7ՖM�d��o�	N�U*΃"�N@��
�0عo��沙�%�����'o������K��`��'���ヿ�$�d#Dw���68����䂘��kJ����a#<��yM��#+~ ?JwoxB�|�n���Y���s�����������{yx�oo
�f9µ3��t���$��w�9���L4�lC�:����2 z~���u�w�"���U��*����e]�ɡdm8 E`�T�����d�'87���mm����a�\��;3=]��7�W���Ǒ�#+�f��d���.IEu֮G9�$���� ���9w_��@���@�6[��3��k��պX�%3a(8}y��?W�s�`p�r���a�zÓ����ݟSp�D�f�"fP^Ů5#�Ȭa-����rfo����7�Pa�`�p����&�M�c@r�o�ίݩ�>t2� d#�o� R�8����֦	ҭ�؍d�ȹ���u��x,Es��9_���l�A��Y1�݇,�vX��͊�-J�P'(��߯��֓�`9�x���ߑ���7����Q�(�x�y�e)~�)W��-(�hny朞�q 3��.X�����Gd�bjF��ɟ��%J����Ԣ���dkWBJ�J;Ó��g3r[L��V����1�!���#E�M��U6%瑼3�dD}3��u�/1!��|���G���y����WZ�k�
N�t�2 m;]�Q+6����*ޞS��,��Xo�����Gs1>//+qk�ؽi�f���d�-lCrZ_�(s01aHb�X���\ʥ#h;k�9Ďny���	����1�-�sd#m���	j���H��]^a�^r�k��u��y�e�t�����@�n;���x2V�BJh��=u�ȉ�c��4�i���U����V�e.<.NΒ7�ږ�1iљ����|E��}ٞ��'�9����]�t
]���� AS4��Է浼���[�p?qo�Kٸ3�% *�Ҩ"����C��M���0�Ts�K)5]:���w��g��=�;��k5�_r:�Q�sǶϣ��>bP��������@�/�>lk�LE��(��R��Q�=d�]j�����o���փ�>�lL�H��aZ�����|+�\��*�yq�y9G�Z�l��QKX*1a�V��RYɚV��~��GЬY��ve��
��X�E��?L�z֓�u<�g��	=��4v<�-�;����ܺ�w�s�m�J�F0$�E7%�%]�I��q�J��Ӭ`)����1��<�^B�I*(۞ܥ#���`�E¯>C��H�5M��A{h�d�;���I�Y�����~Rފ)�0gf�̷z�����b���K�S\S�`�~'���xTs�����rm��:_��&e��oN9iv- �ퟫ�QG�Z��+�7j�:�
���+��Y	��G 1�M���EՄ'u��Z�4^5[m.�Z�O�n	ш�b#z�\��>\���7n����$f��7����W+�D��y6c�Ȍ�'L�>k��3������n��GzW��o|4S�i(Z�h�
Qbl75a�W@US:�s���56���G�A��X�k`3��[V�N�ִ�Q(Ĩh9��?�MY�4,��C�c�^p�0���
�W�z8�#������u�>�f�M�R/登���y��]�_��g�o��_���D���+�7j>ߕ攂�v���P��"x��4ojJx��Qiݔ2J��u�2���E��"�`�o�6�Z0���b���!KZG������+���R���;�����@��g�N�CG�\,�����<HO��[*��g@G��� �`�e�B�	���j9�
�4� ɯ��	A��e�x���0�n'�6����9��2��(��Y�������π�&x��t9����-\p�=z{S��;��
t� �pSP�֛:�(%Ia`�V�^��������ܙ��m���} �$�}U���%$#HԦ�ϓH�h����O|���0o��w؇G�a=jQ�/��W%~]�"�1�8Eo~�C�]:���5�}чeؠ��%a�k�O�r�m�����_�}��W�5�����q���ۀg��@GY�)����S.Bj���&��Iw� V��4$Q����	�*⁠�RK�Gź�SrY�E��(�wx�M�U���Qt�k�.	\���l�h<�x�{u�{�<��-c ����pY3�P@�+�	Ww��>5ߐłEv8���>�2y��>s#�Ҟ��Üx��&�_��� ��F�[�n;Gy���&ٲ�2��}]V�5����+�C`���`R� ��u�����ע�|��K����.t�(��_�\��Iqw��q����ƍ6����d�#�oם���wR}��&QhJ]�v��o�H�@F&j?���3���#������|����SΣ�W�V�FH[���,*�z��l���ea�hOTݷ�i��O���د�s<����F��~��|�i���>fs�s#9�����i�m-UÓG����qv49��}�(��R*�=�X��_4*��Nq�[A���e���Of"���Q>��@��jɛ��}3��'�u%�~h���R�xmZ41�WMAѷ��:2c�w�?�!��3q]���a=�<�#�����Đw['ȵk�nJ��Q�0�����SE�'(���D��u]�+�+�&�`����\��������G �k�=l�	(><8g?`�Gǩ���.��ܸ<p�����%�<��3���蝆H�jÄ��C������M�Rɾ��w��)ql�]��cK�4#4���{t�v�,��ܦ�������q��q����k>��)(ļ^S����!�A�^�k����o�1�kz��{H]���d�?����]A|w8��{0j�l0��.��s��k���է?�{��w�菲v�&��f������v]���Z��1�v�/*�;oF��}��|��C�2U-�]0r&y.���	%K�lxBO֌��$0O���u��|�6ӛq�!���t"�a�?o�?�^M���RG˭����

�K�>��E���< ~�T���L�J�"쌸���2Ȧ50%vRq��Xm��F�ɫ�#a�}Y�?̟�Ӝ�c�<_۠R��x!��fY��u<2i�A��(v��;�*�d�nJ:�E��N�)���Բk�~���^W��a��m%9��6�ƒ\����c�Ҷ�M����M|�9 ��`ՇP+����=�?���Q-~�l�Lדb�鿾�m�w$^�3�-��%��Ƀ֓t�c�ap�X��n�h�q���;Q�Er4���Z�yϛOز�Hf<�CZ���X�@��(Q+�4�"х��^ܯd�^��r/LY\�d'>LmeJWw���W<B��i����K@�1��҃!|U>?�o2���
����g>�~� ����uax���o�)���!��v������� �S	���Z�[p���IL��a��A�圌��;޴���    XZ!�{����;w���x�����M��;_�|��@�)[����ɛ�u_!�;�����в��������TwS�o��u59E0���e5�W}�s����V���;{����D#a�.b�A������9��$�COS�C����?}8���H�yAͺ�JN�sZ�1�/���lC#ḑQ����5R�?һ���x2�獎h�?E�h��N��������ݴ��7��?.FF��
l�Q̛L6Y���⵮RT��:^y��Р(���X�«w��࡬/A���o��X1Gg�����/<�Η$&��^� ���3��ɫ��/� zz�=�z�{@��I�HA�՜6�U?q���g��E��B�q�]�<D��/��,�wz"iԦ�a!��TĠ�.�(�'�s�㵅6�R�7��a	^! ��K+	�@�w@
M��aS~X J[�_�bz�H�����.Fيk�Ig��Ί��f��#da��Ź�+�:��=dCa�=M�-D�J�:�A���)׾]���,�%b�b���N������+|l�$�x�A�Zlq�~8��UQg6�L�:!��p�"��%W��3���8��r+_��K���<@�wGܵ��)w)�V���Lݮ̠�-�p��T����ÿ�3�@K
�;���nIƢq����DF�!}2��f�D�?��l���>�>Hvs�U�V��3�1sS]����^�}���n�b�� �wfh���-9̠�#�t�(�T!�ŀ��.]�§l�n�(:	]4yi���h��Z4^�����9��Xk]R�u5��S�S����g�����������ל��g��`����l�p�\���jcN�,��9�e������1'QS�Ww5�bd�GE�J���Z^E?��F*��A�C�2ON~��7��Y(^*�L�!�L[����F�f�Pd�u��p^�g׉Dl����
d��@�6nC,�������FȦ& �g���L$v"�Owjj�C�w�����*6���ё1�3=l��N��ӓ,ۤ��q�[���y&@�`3���U���hZ�1<"瞑}t=��t�1�>�r��5�Mܤ����f�.��[�ˌBm2��U��
�tmbd�J�Y3�Q <�k��rjظ�J7q�Ğ���I�n�ܸ+�$�[��9cl�9C�F}<����*��l]�m�c��A�t�KB��=0q/4r�bt�L��9/:���`gaw0cC$����a.Tg��8n�9�_�i,Ҡ��צ�~U���b��U~�,����}��<���<�vC�|���|i\(��c�!�a��p��?�V����'-?�l�6���C=M�g�q5,���9�����6��^O����쌿S ����h�డ�jj��{v�d����.:Pw�`��$_ ����*���
��!#Mm�L���~�񘎟�ea��m����~.f[�9��a�\XD���s���.:^<�>�]dO>�L�5OQ�1�2.��Cw,�M����w昙R��XŴ�㬮�OJ^qe���ECh�,�ua��YTY����-:�@O�2>�y�YҜ���i y�/���hX�9 Ի�,�>�\�����e���O��?�X�b>`2��;h�]�.S<Fҥ#J��z%��5�n�K
b��5Ao�bH�k{�L��~�3ȧ��B� �����k�w�Ȏ�����pCte\}+�������K9�:�Ʃp���=�W@�'1��v����WQ]m�A�L��!�#��P�a>��:1B��6�BL�!CQ<O�Hn�q�JX�l:rz%��K�p��"�V�H��	�ܥ��㈆I[R�v &�ِ��pg�,��7�x"1��ئ��X̷�W}x�M-�lp6�g_���҈�vzѸ��C`gjQ��h�cX�w.{��_�Z��!�|�R���j�O��W�
�.0�Cx���;����U�4����6�R�Q���I�-�Yh�'��t`G�˕�Н}+���@A�`���b��MKW���ԾJ�0Am�,�K��8���7s�x��چ�fE�j��F�R�v�����zR3]��`�7U:�I1���r�(�d��O�qNp�C���D�1�X.X��/���k���l?��?����.dlB�13��"��	�+��+X%Iu��K2�0��Yq��{���5�{�4tR��ph��Օ�o��܏_�BW�,�C1]�#��E�h�W	�����5���@�ó�g��L-�e9����/���dDVH\�J���J<YޫG��̟�n�BD{����B%�!F�BS��׎9��x 0_&p�k����t�<������9dm�� �1``�j�e�0�9�g�5��!8�>.%a3$�����3��f�7�G�H��<9{��ėV�h7|�EYA#0l�9Ԅ~ڢ����l�ro]���%�d�Mg�Ƞ����䋛3��]f�����פ���׃��G����~m�]��&�i�����L_��K�4����w���n�&w7�L`f]vȃc�%G��=;�������i|B걠�+�%L��������X7���z�Fk2j���cSA��C��B���� �q�|0l�����6����s��g�c�e��/ť�h�l��3�E�7|��y1��DmV3�o�	P��&Rk���my5�
N�@�h�Z�a��⦝��-�Aѐ�|�����)�|����ڜ)�`*y�ýK�����
�Lq����(����n�w�#m��v�k|WH�����o�W%ET^H�Ļ�n��]�d�"�O?l4���G�;٩9���4�&G��W�����.W@�޸�eΓ��g�,:@���@s��-�.����$C��/�h,�%ح��N�����O9�"HԂH�tő��,��J��Lc����w���6�3��n�`��n1�9#�����ddQq�ɉ��0N��k�!j�]>���i`;�8��qq�� 8IO��������%�~ܞ=A�����HM�x�E�"F��ĝ,']�lSl9��vժ��U`	�f�E�>�x�c�̢�_�K4�3�SHKu��fi�X;�Ǽ�3�G8����5b��hw�wl'[��4+����rm�z��H�`C��[!��p]=P�^|�V0�~��m��>����ド����N~8B��W�� Vx*4Ba�LM��w$d�;f���=̴]U�}+�G�a2=�����̇��?Ј��Z�7�ew�h�ɧ'�4;ѢC�_�b͆�N\���\��M���2�c�W��6)���� ٰ�0�X��;�ӇR(�YP��0x[PW΀�Ղ\5�D���]�qg��{p�|xS�s8s��WLZ��39(wYm�a�M9!fvH������U+a�YK�a?�'���Z"̢��4�5ge�r}�f�4i[ _a��(�5�w�X�E������X��4�M��<�)<oF@��^�����V�,C��o���Y"�+p?ŞYz۾r���N��b0:��,$�ԧ���T3I�cT`C�}���!����3N�o�A�r�<�&
34�v���>����$��*25)��;�2��c��I�"=�d��D��fyB]!ݹ`���LE�1#|YpS�s�,{n߁�NKӍ:�J�ɑ������������ZM��7��jIi�3�1�`��q��As�p�	4�1QG���c�%��}I�OG-x��:���3��m�Co�e�9���6��Ff�fK��u�rP���+5|�[��.ݭ�T�����3�0��
\Yw����v�[�v*�7A]���Jz �('D�K��t��o�6r����C�43�a��Z�>�k������3� �g#ؚ�g<N�j� ǫ��hle�+����@�@�ɲZ�j��;�܈9Hm�s{xE��ܗ8{�d�#\�i�,6�M���U���%'Z7�|�W8@�^ \;%
���c1*uꀂo���Zʸ��������K�0"�(�!5ei��s�@���M    0�p���uU��^I[X���Y�=��A�B�xI}�AW,g��ꮨ�(9��#y^u5�W�B��oR�JMP�dg�|�TYqL����84XfT�@bi 2���b��C�N�*U�(u�<3!d]^`���|A�#C���KC|<���?��L9�Ԉ�E�g�����*�`�"�u��q,�.�'��TOa�N�z*����9(Y���Nm��B"�V�=W����z�"O@,7�TY���?y�1b櫴tj�����wlzH*F����Ρ���F������5��2��d^�шZ��t�.|]i�����圣�ږ�Hs�9F���6s�]��2mlQ����*��'p`����݉�̈́	�	xd�5�Ks�l㤫�%�n���l�w(����)p��(<�+��W]��p/2���D�=`�,a���S�Q˞�{7z��8�t���g��PM� .�A$�M>�W�z�l)C-ڱ8���� ��4P|XDW�T1���.�sab^�ٚt�q�4��������B#�n�.�E��}Wl��΋�w6$���&7=(�<��g��L����x����-m���n��i��כ==�-���(��Y�m"2��ծ?�f�����ֳk�"��iǺw���-gH�sC��-;��L�{!��ܗKs�4?؅J����Wx�z����,�0�熻!��g�"o����03/.�h|s������]�.�E��}w��㓸=��E�u����K�~o��%3�(��taӸ���i�Skq��9���0h�K)�}��=���`YT�o�n�Z�g�ak?Gg��б���g9�_J緗4�}$&���X�G.i$�P'�IW��;�������O��}�+��}�&@�<�Qh�$�#���x�A,k��ݝ��T�@�&TcM�K����.E���.x�
{��+¶5-X++���p�q"H�*ת��ɬ��E�������4� I�����r���]29�5���CTʔF��$���I:j�3k�/@��"�g���;�:��5}E�g���?� N�XT�b�X{nJt��E��Q^�J�ڀ�'��\
�22c?��wMJ��x(����O�D5l�8G_�)0	O>(�C�}Ck�ы�ӻ�܎aC�s�K������ZD���{UW��r�N��t�Xhc�1��I�ܜ���|�䦔�H�h�'��#�	,t�����%2}��'pν��d�Y]{�2�>̋���vZ1�iJϋt���i�P��tzJ4sӅ����ȷ�8͊~�R7v�� $�8La7�	�=Ȧ]�t�.P
�����mq9��i�%�'�O�A}@W�*G��!V:a�8�o윺�85������B�����Z�u�U��DA8�W����b�n9<ml b6@ b黎�(a���t=������/�|Q^Ï f�����am�i񰫫��~�$�>D�@�}�?P����,��&�:�WBO��9��^y���d��;m��@�35�j���#����V��Ц�7�� ^���N!p��~��nBR5N�]�/ݤ5mt�e�9������u�}��s}��d��� ��!�=�D"�u�=;:[Oj�����R_^+S��L�M�u�	ic0�N�P�n����'`�4�&��m����Dw��C‡C��"�L�"�d�GƽS,��u��*`/��2W���;Hx�`���%���Z��+%��.³a>Я�\F�X���{�T���.��4����/U�HA&ĨUwv�4ؒ��l�=���"���h���:l\T��6jS�����#����	F{���ho��p�䬷Å=2n���(:04�I-��2��%y���g8q��z� ��Y����]�mdI�M��c�>��Á�J�LRG_Z:�,�b�
&�Jݙ���M2�Ѓ�
��]�Y�~�(s�����ᐄK�v�A3{���UCo�V�ʠ��J���f��ښm'��T�uS��8];�.Y���NW��X�8�"���	:P�\�f��c��D��4,<�A��p�O~}�l�m��2�6�$K0���)����L�q8O�f��b�ݸ��Z{z���~�.x���ɝ�ۆI�Y���@�\4=���P�����q݉�m1�$ȵ������ڇ��\m.�h1
���FHXt�����'��cF"�aԱvN���vE΅n����K��В���]���~^,P��F��cڍ��H� �'��
]�D9�C�w�;�#Z���^y�pH��^8�J#*�S��a���{'թ7���w�gL��{��jE}��'"j����<���ؗ��}�����LK;�,��]�T� "�=�c��s�EeX���˖��:$�7���gL���p$F�M�����~��]O���v���6�2���ο
��\���T����0�;�e>$����R��[Z�H>.LMc*747���z�?Y��>�	:�g��thF��v�A�Tv/��l��AT��Cر+l�4��X���T+mn��sg�.T�?��0~wΆCh�>�Ic7ʶ��(gl��R��=�=�ʏrc�C��?�!��b{��k��vP;@^55)<����:$Sq�!�Rq�?5� ��,0@;��ڣD��G�E�V$=iZ�&ڕ�Y�a�n���d���я��u]ݒ�H����~��?�����_�QPp����"�~�K��i�ey���.�ؔnĴ��C8��I�gbP����t/;a��� B#�ǜP�L'A���YVˉ��r(�ha6�]-Ӏ9�m�e���-n/�d�4v�O(�,�K8V����4�� RL��t!�2x'�T*�Q�*7@Bl!Մ�6r8�4���Q.�M��D4�ƃ������7�q�I>2��{�Y�^
�S�ݜ����~�卍�6����W����Е}�R��4	��4���;�H��l|N�*:�t�U�m��S(iדժ�lC=��F����֙���^{�Y4�K��QT�E}�e:K��ݵ�|�O�v(���m ~����B&U�ܭ�����a�]�(���J]޹|���=J(����Hۦ��v�ΌRX��k	ܞ�ms�ϴ�4��FH<_�AJ�)���A,cbq��t+X��f(f��/�"�VI�Y�����4_9�*L�i|L���S����W�XR��t͊w�T	 T��b�Q	�[�^mPmg;�����yT1�T��M��=v�	�*TzC|D�%�i���x�e�}>u[��W��7�|�j�i��j$l���W�с�_��wi~iAك.=�B@��[5��(=\ܛ`hz���`�"d�ҍX%���z4���6�r܋P�Be�?���8UJ$�����L{\�������Fi��E��)rfv��ل>|�5Zn�<9���B��y������AT�{����j���%ڏ��Q$����0�� �P	��%�=� �px��K!����/]�!;wS��형8�p�T((3��< ���٬M�|F�C���兕��	!�B�)H?2)3��lro�PؓD%ؿЫ����G��|��ĝ^����K|ڑq_D�Ek��YB��<GkT�ˤ�H�.T&B%!�����}D˞�|Q-��^��^��WSW�iQF/�8���gp�Kp#�94	�Q�_�������h�F�X�&5�S����:ܟ:�!
�iǣ��1�P��J�X�&58`ȄY1�E#�܍{<��u�(7�DEU��Y6��0�^&�%�EؒRQ����W#Q����j�<����ߵ؉%h�[?��5�*��ɵ
!�ބF��wv�����dF�;I��^�k�js��{BD��X�8
�R|�gǨ>?���bB��C�e��h���{��8�%�T�9��ޓ���r_��j�������k����:��;c�8�F������[�� �^��,ȩEn"�赿���h���)�p{N��=��f�$���e�S}����<C[�˸R�ˤ'[�JI�ʝ�����o~^zvC�pY��;�sBH    �n�>�qvy�wW�\0�� q'��@�\�}���n���/�'/�*� ��8�o)�Ș�%'�ʅ�aQ�$>��#�S��.Y;������`��A �,����YH��R����~:'�	�'F�ֽ��b$��%��<'�!E�e�8���
���>]�;����)��(r�`�@�<^�� ���]�����y��
�6'��B��H���;&/��E�*�ID�=��Q����	elY�����/D�m���ƻlO��i�@'�������f�ҏ��%êD�?;�Jo���[%��0.<��i�"be�w�#0��^��qEި�Rp��ZA�U�����P/�Ïݧp8QG�)�sd����'8�ɵ��t�mU�Y��=����_���sau�)�E��j�_�̪�ߘ���P"LA�P�FX��fU6|kcj�Ii!�U*.�oe8�T��o�"�ON~S�x�C�!�ع�/�z�FL'�}QR���eu;/f@�q��:a���u) ������ᤁ͝��=����c_4�9�-�օjU�c&(&�0�	�|1���Ab=f����:���u��AA5���ŚnW;�"T�1�\����vT<�(���w��<z>98����;�i""Q�����ب�-�rI���mXb��ا�9w�iCR��4-Q�o��3Q3�ܣu,A�8e<w���V�l�F��t��4v�z{�g�T,��B���T����K}+A4�T�U]����p�S�}�ꋃɋc'8�ķ�An�lVK�#�B`����
ꪴ�^�ș�
*�ױ�����n�˰�Yy��`A�P�&CFw�}>��F��(�{1�?'�8��s��8��9���|8��fvV�h���j �-bk��w.�Qi\dU7]wK0����;������$M��p�=�TYHX���9��o������t�n��ժ<>��䢬M��bZ�c0�R��3t�U
g�L��8j�#H��b����^͊V�/g�>5O�l0sY�rݸ2��{Q'�y��Y��&� Sƙ%�	�Fv�
�<h�k7G����	�}�n_2��:��5����y��8ӀQ����7�(�[]����u�Ti-fr�*fW	��!u�(�������"*l��k��(�'�몆��.���%�W|�r:f��P8p�ÿ����,
���(��\�"WV�KvpYo�AsA�#���'{��=u�����A(�G=<�%X��8���0Sڂȁ\��'���)���ev�M�1A��\��<W�A¦� {4�;"<p�a�>��__�	��T��R3�!H���3)�̘&ˏ��ή)w�D�`졮wF������y���w�����@�zd`Xm��Rۿ:+��Xx���{"�78{�����Ҳ��
����^��p���w�4�GE7aէ7f���Q�=��h��`Oo���Njy��4�$�U��#���jS�B#�V��dX�^x��3gR5m 4�e�ɔ�	=V@�U�����9�R72�5�,�Ntj��'�Vd�4�%��.UX��= 6�&j��V�
7,������8yn����Ikk��D8U.��b9�o�9����ڢ�<.En�˸��:�qw�1�4�S��*1��L����	��av7���E?��mh*�K� WL�V�~$�&8�-0x[�6�Bz��tUjBj*/r�W�;�<���e6v��J��tI��4h���ؠ��z�(��*��.a1�����͕��}�A"��Gͫ���(���3Xwg(ut^]n�`�Ϫ��JS��
��_����b�V�l
�]��ln�f FR�7
�	�f�n/F=���1jk���-e�,F�j..������ۋXϲv�W:�&/&�n��]�s6��4]�{50�)�诘~����	FʞX�g��C)vhf����V�H�qf����;U۫/i��֛$ۺ���q;��̐D��&�(~N�y|[�Dm�<xv���2��t�\�Zr��	k\w$<�O�3�7v���x�U�ţ�9Wg
��$rn�4Q��yi"|йm��pr�e}�����,eby0����#�	Jv�k�=5�%���Sɘ�7w�q �dY�@wI�Ť�������3���^X��m̗.�Dn��?�����݁}��I�~��%�	"�Ё����,o�'A�n�U���jfi�	k�pv��*૷�r�*�UuK��J��h¤�:�+"�&�ar"J�Yz�7v*-�ya:J�X�=@�t*�\Ov}��<��>� \����*(�Y{�t�D]�FD�s����p�^$S#�6V򡒹YR�����ł�-Gr;ن9� �_����
�<]N�'vcμ(0����xQ�p�g܎e]a���I���oʶ6���ȪI��+ �S'�+1��X���5���`�E��)��(aװ���4�3�����;��e��ù����Q�K��� 2n� ��4���K��.�s5Nb�O�R)��$P�i8�֠�@������$�/9���Փv6r{����w��`y#�=��)M��\��d�4G�;�t��n���|�3t�����,�0�/5n���0K���JM8�j�I���⽠�A�3~���GYߠ�Â�G�W(e4eg:�7�������ǝ�I�!�AM	Ј�(�^[�������Rm��'):�;�+5��x��_�8���G�o��]��Z��B�	8�Vl�7�_	�(;
�!$��1j��}:I�է�b`���6Di���8�6���&�'���#�	9����P6�c��dW�d�։��������9�>�+�{$�\X���0�p���!�z����c�э!����w�+�+F��ך}��������C�=9�|��O��e��T9z��8g�C{��fp������ ������(8�����FawqSK�o-a",R�SvsI�n�_̠
j� Z^���8�e��A�9�[��+H6<ys�d��h����w4!�_�\#������j��F��g�W�C�3�X�EQ��&�T�[v����"�b[.[���w�m�g4Ɩ�	�-����t�<���F����ѕ.��ň���R�Z�AdM�;�Tz��ߵ�V�F�s" g�8PnW��j	>�-ى�D�c��#u%9��⏸+�pQY����4g��<�h�4`Fn�� �әĹ��SvVu|����6�T*5�8N��d6X+^�? *�όF�o�H�`굢��&���<�e�{�~^���q$��P�<��q��!����y1-v�\��
�\q:�7���2o����c=H�)��6z��A6��V�GU��j���ea��Z����u�*x�j��,� �4Q:�N���JG�5�9�F5�2�'K�Nw�.��j�-=nT��ZeX��W�Մzv�����v�XP!sg=!ܜ��;��df���ZpD,z/�O�#\���
��������Gq� ���2�[\�9;���ɪ�ڙ:`1����B�M�\�5���Lwm�\>��C$0�=l?t>��O�v�s5p}"�gǃ�WZ���"4�C�%�z�o+��Ԏ8n�ȁ�%�+��ӵ@Zo�P!���\�riJ��&�z�&( ��Z�����h_��ZKRM��S�0k�zJD�
E�FÄw@tî0�&+ꔈ��2?���û����x�tW,=���&�\\&��`ྙm�j;-�)��}��MթzI�.\��v�9o�Ǵ�z��,:���HM��$:O&X#�"��� ��}�ͨ�V�	a�D*��5�R���M&��~({��9���z�Kq�V()��vA��R��k���֤	���Nw��|w�L+ʧQ&@3�9�(�Ȕ��^�]z�:�W�!��ɀ!�nU�q`(M퟾�Q�4�t�p�h�3�*�|]P��^a���!�,�׷Ec���Ӱ���x�9��O�E@�@�
�%_XwM(Z���1;N�Bl؀ ,  0/�t��[��ɓ;��q���]r����`j�{�Nb�*]�B����FPٕ�#���(����ԗ�z�E��N�I��~'���R��x���z��b�Ko�-Ag��
�r3�r�o�6 �Qb����" ����Ĵ��]�F�#̹7��K�{o��Hrm��<,����̨H�����r��DS=_��b��4)��G�ļ&�D2aG=5��4f��z���Č����>�)wi�`R��
!�fsl�]��׷���',������5�MXj�2�w;�h�ϫ��yk���b:!}T��}f\���v�yu�RnV8U(+{Ta7v��p2U�f��+P?)+�U޿+j�>�v)��;� L�Ī8��;f�̡Ik�_�F��dj���LZ��F�����N�s(�L���}�$���`��(E��Un�S�8x��h�ݘ��!_�ߊ�H!�U:�K ���|v-BC�|,�ȁ����<�n��Pp��+���1Q?|>!O,B�#y����s�wp�v�naV�y��0+��ӼC� �By��Y��9#l�-!��TF��:r�P%�c[W���bғ�usA�Cra檄�D\�!�H��ZQ����f�}	�7NMA�^�=���nV8�̕��Nʏ�4j�5�jO�`�A/�Q9@�,M�(7 *7���}����L��kZ ��Z�$_-�T��Y�֯��X����p�.�Z��)&�e� *�-ծΫ�*w��G��M���5�^5{�:���X9ӷip�N.��^	m�]��*���H�y�0�~�U/F�l�Y���� 2��̰}��4)L��P�o(]{![Kt��V�r��6��Yc�NHEN���)T\��,z��K��=��	:��jb-��S-7嫹&ϓlV�Ż�5_�+��m`K��z�WU��ȸSQ���vK��14���u4�Z��'o���k��j}��O�t�JT¼%��4��I�պ,�1�^Qp��U��5s0SFR�=�n��E����XQ���Yu�n�����	rp�q�_��V�ʸ#�4�g�����r~�8��L�>�r�fe��7K�f��S3�]R�"&@i\O��m<[�h�l��a��	�07�~�Jv�M��i��z�_mq췉����x�> z�{�)�ߓJ-Ȟ{�;eǆ����FP	�hFV���L�|���"���t
�h�L��'�kn���������޾ڪ����#:zJ���o�^��_� �<�-�M�Z�wk���-�Oƣ
�n��n5�G�V����@�Lm'��D4Bd��[��ʧ_m�I��=~db�k�6������Z���En'��,M�4[������5,P��G�^!�C��4ŵ8��.��Ƶ|.U�28��ϑ��8)H�ȱOKL��+h]@��n}�~��%5��Vp�ɨ(�N^��*;��K>uz��V
Qk�K;��$�5G�LoL�<���\�� \B��Y��_�=W�>��d��
��
��El���u��4��N����s�v�*
χ�ʗf�^S�6���|KKf���EZ�����k7n-�$��Ϩ��K����7Uz�%3�N���|�Z���)a� %I3#�-N�o(��X_MA�p����܃tP�~r�G���*��9Ć(_..�Hw �3����\<��M�=K��T����x��	�^��{I�Sq�?H�{C��E{�\2�H���C�kX31�P-VT��Gǅ����u���yPwT�N�f�Ó�{�CQL���D_����J2`�WT^- ~G�&�DZ�"v+��㓲.e:���;����w������Lh#�>�f`��1�>�2�{{�_kc���ǖ*㎝q����ҳ���w�e��á�Uw����������_Mj��!tv�3���!9�\��Gk�g*�F�@���uS��s���,0��d�b�<����+p�y�b=/z��U�Cl��C՝�n�GQ{�<��Q�-��;T��5��ӥ���i��izU,�T=f�C�#t�P$?�4��.�E_�� _�yW��S�Y?c��p�!��R?��G���~:�3�t���u�����4d�u�Q�R��i������`�9�OG�,�5�����N��}eA%���"��#M����>��!�����Q�#����`-��/iUdG��tG_G'�)�Zo��LbAtU�hW��m!�[7�������LCz��͇�A�6���G��H�
��S'��ܵ��ί��	�_@�T�z�tA�9i�fa5a��]b�NB��E^"��%�g����]��7eLc64�80�R�j=1���|�*W�z����N�{�	�L��N�W��t2d�Q˕W��7�Q�?���(�7t��,�͠.����l��K��=��3VM�P�k�ۦBf3��q���n��Y7�ڒGG��<��p�*Ѵ����4�7{�C�|�V"xQ8��P��4�@��_>D`��baմ��:)� �z��q���:�k٢��֤z��E{�1Rq�\��i���HXX � ��*��J���oW{t ��Ф���#�c��|K�G�}����o�]���{�ں��O���A��'SR��kL���'{���Uӛe����t�4O�b�P�h@�/�`
����r�<j�I��a��qˈ���,z���h���ЪxN�V�H��Xy;"�<w�����7jǒ�Z�ͩ�h0b[�� h��9�:�ӨUg��!���A�����PW��_.4b�?d�0�&E]1�'���N�Y-��2�:��@umת�R4��I�� ����`����<�����r+dn�a�)����)��ã`�Qr"��"L4�����:m5�*���X���%��Ev�s�3Z�m��{�-H���Ԥ{Q�K��^�"�`���SI<���q�G0��َ�JQ�mܶ��8~J>��U�����cJ9�Ƥ9u��"�2��zy}�j78I���3���ٛ)EPDW �q��\�I��OU��%�t��k In׶7%���c�mL�d����S��J��O+P�s���A��G=��xs|Wj� ?�I�eK��r����ż��9/�uy�a��퀛�1� K+�B�."��N��<�-�]p�b!]��w��:�b�̤~��6_t�v�h�x^�S���↱�"�������V����>��r �ױݲ}���$�'�\��o�7�e0��F���� |���w��b�5�N��H�.��ȊR(u�hj��a��.�,����-�D	+V�����[u*�0+��A������wma�Y
PP�.��%���)�b���w��ٳ�ew�      �   A  x�=��N�0Eמ��
��}î�FE��e�f�L���Q)�4,�q��OԆ��*�U�+]�E�6u`�m�a���s��(F��MN��g�T��*�z��]�&��j�(����Jl91EXH;QHȮ%���*FX����}���(���盼��*16�>�:da���~���]Qʲ3,�#�+����<>��*��ݖ����:��4r��AO�G��9�AG�D�q���=W�$�,����	z&}yy'�����;��@D/���E�ZJi���͎Gj�J�����`���a�q�^��)���|�»�9J�ߏ �A4�      �   i  x�uUˎ�6<K_�b���b1�$0�rʥ�jI�Rl-I�x��)��F�N���Ū������Ȟ�GV}F�Q=��5�P=��!�^.*��_��E�wc���e�7t}��)Y��A����)n[�;}=$�f�ќM��F]Ŀ�V.G��<ӰW�'�q ��d�Y+:c笠{n&�c��z�B���o`����	��(�U�3ى"�� S
���%x�d^�*l`��3�P�X���׍�%>(k^X�gj�٬��yfC��c��X�\����;-9�/C��]�o�J�v�%~P��*���7�G��Akl�W��ˠ���B��<�lo��������t��d��7����q�>����9X�����9�ܻ��lK��f?���\�<���`BX�Zp�;����ֿV�%��	-�&?42�֚'%��5�"�p/�+8}����^<��R��D�gLdQCc�x`���dpCj}D�����O�p�⟸�P �W��L
~;wh�EI)��t	���垲���5#\��5�h<��̍=�7�HMϐ��ڤ3F.bԺ,�u2�����g��|[IG癪�4���;���
�>+�{����cȿpT�������İ�'���J$59�:q��g�`���Q}�����lҲ��He��s��Z$��%e�u
��Cb1��w],��̯W.�Q��gJ���q��=�\�!G��0��±�X���xq���۳$ޝc+�����w�$v�{�gη=�~>�@6�&��׭HaD<�!�Q�&��X鲠]����O�'����M���ƙ�������v��~x����ُЌ�rD�u�qS��7���c]��<���      �      x��ZMs�F=K�Ǥ�Rm6�MrTle��$�Z��e/C`H�`�@4���u�| i��f������lLmt_��n���t?\���J��j��ag�]5���[��O������W�V�j��iEoؽvj0�Wm��.������^9��A��V=}Ԏ���n�������~Um�ou���`�z������Sך����y�����6��ڃ��Um�}�I������=j]=A6�Q5���n��*�W:��Y�Z�+~����@V?������.���BU彦����h<��hl=@Rd��ܴf���jU_kQށ@�B�U��rӎ�4�s��G��irh0ī���T���(���,А$�;��m���%'&9�!E	��+��o�݋�i*��U�V��3G��J!`�״Hk�u�(�����1:��l��>"L���K�;2^����~o�@����/��1*ڠ�[�_�|CaE��j`/?B:	7^J�a���#�;)�@j��c˟�xR㇏�q�*§��X��<�H�cH�����Z�E��GVwz?1թ�&<Ո��I[���OF�f+�߂�z}H��2�Q{bʃF#K/qQS�֣G�⣭��a��~Q�������Ms	!�jh��/�B9�ZE�$�:�5���%m�B"���|�5����>���x7�����Y���V��lQ۞҈�O{5�5��P$FS��)�(�+�"��t-,�AQ�)�Fw6x0�@		;�ߋ�$b��dJ�t�=�6/��z��k�\D�9;nw����ǺY��Y"�=T��?K�>Ֆ���ǧoɖO�Mc�"lĻ�&I2Ql�F7,O��uL�s��5I����2��j�,(J�-��C��i�%�����7	���Q�A߃iQ��K�P� �L?n�$V�gG;�N�NoZ�Dh�Bg$C�k5 ��@��,�u��Sվ��A�TF��-vJ�! 'T5=%!�O���)߉3�_Sn��Xo�=�,O;�>��f��7��q��+��d ;���Pg��H���B��l�)��D��s5�8��S�f��Q �j�.R?d��8��ΐ��}��?5ĺQmF�Z�r��=[w���>�P �ZLR g��O"���Y�?�����_D�����]rv������=�e���V���T,��9"E���&蟴-�?+�%�b�o+g[�3"1B�X�IVL�/�I�Ls�X�AC*z�$cW�r���*��sQ�8��?�;�F����b>�x������ib�� ʌ�3-�ug��h�U-fh��bh�;.9-�ә�8�(ɭd�����@���Z����e������A�w�-ig�E�MT�9�i�?�;$�۽���*z�����.���W��C�� H��`� �-x��f�d�=��T��H������I�-Euzb��g�zW4:���Y\һ�V��P����|�����9��)q�,�+2��O	M@v
�3�J�� �7��|6��%�}�W�,3K�Fx����k�R�͊�$�t�v*0�D��`V�'�@n2SO֊	��@�a�P�s�G���������x����=e��Ƽ�,�[8�t����,B_�~�MtB�%�p���g��C_y�Zb��]�L$����oZ�>B�kR��S�Z�!9�3Vs9��3�y�+�rCK��8�:ټ����ϒzJ��+����/�(��c�}o֣i9D��uP��M�JK(U���k7��4�g��mCLƢ�����u�313Db�Ӑ�yѳ>و|M��[q!t'<�\|�֤|����4K�E�ߒz�&[�ğ'�$m����SZ�VS��%�4vl)v�myC	s�H��`ղ�����_�(�Q�4��'��CY���s[	8]=4��&�U���s�u{/0G�{���V���0��M���&\PH��=E	@"���ojI��`!ԯ�X��(?U��GO�#j��l(qҖ�pU���5��dVR������qH�j���C����	�#���� ��S�V?���B���W�H�)V��S�"-���8W��u�lm�u]@�5M>��ek�Uu��e�,b��q���ȴ� �YUc
��OD��+r���G�}#���m`���`�����N~M�S��t�R�o�O��ڨ���5`�*�i��9*f���xw�6;��sXR\E(�;r)����1	�Z��j> ��쳍�����?Q�h�7�_���_;�/����� U��U�
"�azU�:��m��'Ӛ4?9��p���3�Z2�,�%KoԠ�\���Ӈ N�m��3��t�&5q4�${�q����(,\<-��I1&c)(f���d4�7/�ێ�*dBK��-5��)p���!K�����<l77.�����6�"#�W�����뻉xk��QD=<�����tfCDz$�F�|M^z/	/�5~�Q�$h7�Q� ��5���Q������I��wB�'�G�Z��4"�L�0\��������uĆh�	=��r-�&�x��k��RL�d��y|x�64q�F^C��Q �q[Ğx:����*�`;6����;r�ǻ���ZSI%�����ZKn�Ǔ�A6k¡�O����`.6w�R�û�}CE�E�<2d�_��H�(�Qj���'�	\S�kJ���j1[�d�DC`�
]�=�W�C�Û8���G���q�I�p�HЫ�F�O<?��yI�xW�CJ²�|<tdl�%-���:�ݩ�|6���_]�ö�w,��86�fT����fy�z���<9{[��>��,wנ�>��Tz�������E�Y��?^=����1��9�L���J����7;3j
�l ��<���+ u�f�$���,�>so
#�
��xi&0����@l֢�E]�B�jw����"�a20H*����+.��$�
V���(Cvf�4+W ���H�I<���� ���j\�����1���Ü8!�V:�LH�|�$iz�sAf�ŉ��$s�9n�߹����Nu����Cq!`ɟ��1ܹ1Z�i*�����-�wvl�JN]�Pr�3�.����fm�iwq�}uG�yfg
��ek$�(�&H�y��ښ����0����r6��&�[K2P<4&��0�����!y&�4�-�������I�{ఝ\9S�Cq*�\��ݍx�Lq�1c�B�C	����zЪ:P@�'9vh'�	�����`Q�e�¥�a�L�E{F���gp�H�/��G7i&4�A�BO��ȇ�~N�)�e��1Ce�&�!{~�~��:��g˄��s��dyG�&s��Ub���,��O�\nb&|,R��ꧫr�x���N1�U�g}�Й2�N� ��ӚĈxh��S���ŕE�[ܘ*G�s;��/�;�RL銵|$�<�"��Kq`�]����6{&��z-�G�&i��sPН���=����	cL(nK�k�t����4sH�moq�>Iw�j��.�D�sT�n�/\��+����Pp^��O��a(;��skg	���We�O�q��Nq��d�QHh��a'M�?_���)�Q�Y�8��+�d�
������nv|�"R���N<��Y1�5�'.�k��č��P�Љ2T��f%7�xs%d¶�k��h�'Һe��l��Z�/��ʫt+���ŧjF}z��21�T�|���؅|b:P��R|g���7##�y�s����EY�3�y	��A�_�")���D�X�T_�Km���7(0����U|�Dƭ]��[�6��#��&� ����.�*��}@�&�l-� �9R#�ɯ���R��(��T���Tv泖��ץ�mY�x�)�E�HW�a�5�#�5��UK:�bl��%��EQ�P� ���U��~y�:uէ�5%�{��6|1cB� !b��
�V2�.4��sCCb�@��H��}y��i����o|iEfa<r��]�Md� �2����5�؄H���zZ��"=�RW�"l�n.��K��f>P*5W�	�����]��5�r�â�}�%0�;B��*ƴ������'/�Ku� �   R9�P���w��^�L��n1�T�b�7��\N�O��<E���M@z���5��a:=�E�;#el���������y>�O�B����M��u
�*�%�F�z���X���tf˃�0���ɗEb+z�QE��.+�E!�/^�O��-�z�A�S7S�+����$����������i      �      x������ � �      �      x���[sܸ�.�L��z��"����l�mϲ�Z��=��y��(��KEM]����;o  X��~�*?� �K�s�,�w�v�?��f����7�$M.�ݸ~�v��jq��6/�a�,�=쎫�q��yr��?��ŧ����u�a�ߋ�f7>7{�s�רL.���a����a<�<��~�7��c�= �N���ð�_t���{�֦Q�|��0�^��ǧ���{��7�F��Oz|ڍ�=���{.�/��4�����~߯� n6v|O�<����4��u����S��C�;���LƆ[ӰLn२��þ����7D�����Y^�kX'7��p!��M��~�u<�3�u0�/Dl���/����%�TF�O?/���'���/i��|<����aݯ5fix�o������F�<a��|�{�\��vC��/n�M���Ҵ�w��ǻGh:����]�zYmz=y��غDJ�?�`���0�ۢI.�~��Y|�u���1Hi��v�:|D��;����~5����&��v��O��o��w�ȳ�r}��[?{�����'�~�����z�>�P��G�C�O������`��cj?�<v�Ňqׯ:�2�so8�װ'a�_���� /��o�����q��-/a^�ha����������Cw� �O-��ߎ���&��=iv������n�d�L����q�P����[}�qm�?��]$�T>v;�2��aCC��%���Ӻw�/���������c�vk��>�Y�����_�ɳ>�� �%LŰy�������=M���)%l���&ʓ�����;� �������>'Ra7�L��+@��&}�5㛍O�:���m����l�3+iM��Ͱ����;�@�]�ܚ�����}��q����j�\ëݻ#BڨU�08��_�øY�;|�=�;�
?�����6�hs�>gW�n�	����<�?�a�Ox@8�V�~O8���gԺ{:��ҭX�nn����Dv��T��'P=s�!���m����#g�n׻F�=�v+3�+x����pDwpt���C���pM㋚��b2X~�Gw;=��{�5@+��Z�B<,�<���W\ݏ�7���pxPGu��Sc:x�f�M�U��?����o��� ��\'�߮�)�'��$_����v[|Kӂ�p��\|�;�pZv���Y&o�{:���a���({�s����'_���z���j�${����M7.�滽����x|�Sf�k�w��axR�_��~�>Gl%'����@�����"���I�Ü"5����86ZDx�=�;ِ٫��6�����ḹ��Mᦎ�|���������ͯ9�����4�:���?g�����2��p�G����=鞟�� ��~�`���	��O�aZO���m�-�j�_���T����c?c'ի�:�Nï�p6�u��tL1b���nw���g�k�X��ǑN>��5�ss�.�x;�ȏ�D�1C�g�S}����?�L�~�����{_��<?��~�Rj<O��(�j;^���,�<�`�Jﮖ�:pC�K}~F������Yr{�1Q��?���+�V_�ώ�������O�`;��yw���9��F' O����_�YZ���J�d��q�t=_������|�K��}��0-���V�է���e�����I@�
60+[y����B���B�TLm݂nC���aA�5Ǎ�yBC�݌�a�"C�7B�����9?wAWip(���~pMv��}��t��Dy�`���r������U���:H��-��%/�b��?���⊀���J9����8�������	�J��V�'4��w�`鬧�����b�^��ǿ�~��	�&$�:n4��$��{�K���l��Ԭ#��,G��i��E�L�z�	��6W�m�����H�w��0�D5�� @�G�`��˟�ʷ�&�a��Q�S�e:�~	�Ș`7�
3n���;�[��jڐX,�wVی�)3��'��L�o�T.�݀�A��<mp�o�J�@p��P1h�k�;��ҭ7�D���ͭ(ۦ�l�'�n֡���&�p��EF�T.�ۤ�ҮM%隣qAe���)�N�
��?<wr�Y햬d�p�Q��|�˙qe|mD��9&i�>p.�t��!$^�(�F��[�������W�1�EQ~���d���X�	��A���hi������"
��M�4�����P���Ie<��Z�SP��-�{_������07 0iU'�����at���~}�rv}s{.]�����=w�CVJ)i�QQN��8�)B��_��9��XY�����9akқO�Ϟ�RS��������%o�l����}�i"9�c���;<��,��F������g����y�^'\9�"�@�i�ڌ~�2t�|3�t�6�Ԝ��R�05��p�	�������s2&��
_�W�������Jᳵ�˘�����e*SKCU�T�G��p���%��[X�����7\�#B
R����������~�=!��`�����o���?�Ȃ������~/ݴ���?_�N�K�v	c<\�^g(�n �����n�L0<x���EhY��h�Ƌ0� 2��F,f�3,B7��W9�	�#+X �yD .>�9��i�Ċ[���a��!�j4Ħi3p���b�շ�~8�2~ߌ���PgD�����j{�a���a���
v�cg_;�����x2ض�3��p�y����hԬH��:���{�X�=�l,�T"��f3�<��Ɋ�F�.p�ps�I�&IB�r�q��#r��m�zn�5N4��Έ����:�n���G��v=�����Y[�?�z9K�f)�{@4�^���~ibW|�>�� ��$Uf~Pn=t&�����f�G�"j�dP7Lo��%Z�0�熹��0��*'D��,<0¬N�lD��W����|оB�+������x��/[k����ҖDs�޳�V��$"9�F� �Г[�}�C�i���F��rΞQy��2��Gw��p�q��q�A0fE�m����O{�K&�4���n�׻���
��� U���yk(.�赛����0��xe;�	�i�Zm��wV���TZ}���$�>E��=�1�#����_�����4��n�~�%K�����eO�6G�v�H��8ݐ�'D.���{��	�9�n�m�o?G�O�SD\$s����Z�O]����q5�ݶ:�w�ϥV��z���M��d���@-�����M��d�S � T�Q��	���ykZ�ElTD�ݣ�$}Y|�%������^����v-sR�n�*�)�6]�b�������k���/��<�Q���u��_�\F�%�a�D�R�Z0{��n����� �k ���X�Q�R�;loZ��(�gSI��C�C¤2��6p�z'Q*�J��K�0�[�*�f�^W}����@ %�"#��Q�<�^'���5�GN�4�E&�'��P`j;I��&La�7*^�N���zWK�՘1#b5!*"�èܶξ~8Q�����D��B��,�Ȉ�]j���:�3%{;��륅 �:U���&%M�}=�e1f��Շu8C(Ć��>�Sg	�0l��f�"�}Kĕƿ��s�HU�g���$qE��Nԏ(�+-���x|Z�Gro�Z�~8l���i�4#�`���G�s�z�~��a�р��d~H T>�Á�yrӽ�Ԟ�D*��ǋۇ�;����A�G�I��&jE�
�=�6���-\�e�05��=hݚs�A:�_���ð�u�������J��0�!J{�]����ۋ�9*EЗ m��9N�{�Ջ@�!�\�"0�T	�Xx��5��w���ys��%*84���������g��qyΨ:�sk��x{�Id@��8"J�|���� GlJ^-�{�\&����SC�3-M�`ey��3+�
�=)6�!�����|x�\X�g8>�g�/KT���.�E\l��Za�VKkO9�G�'0�=/3O�������    �%�R�O��^�H蹱�u3��!���D�����kx̘�.7>�Wwp�t�{�GB!��N�w=Gz��s�{���5,��erw�ݸ�+Co$��o��dj"��]ݢ@��li�h�o�m��� ���S�-śĕ#��>��?�B��3��bٕ�7�@d�n;�|Z�y�|��v�߽E���X����1G�glNKC�J�N��R'r��Ŗ"}-
I�-�م�¬>���g;Q�ݬSGK�����X�7G%�\���y��X�����Yj�%�����7OHΓ�� g�\�}8 �9���J�I�-&_}o<��݃�Jt�ιY/D��ݥ��&�7�졾��0�Mk��*H]n�D錍7đ��Vw����P9�x������;�얭#,�p����
w��߿�~�US�6�^O��c�����Rπv�R~r�7�)�H��8�4KJ+���"��;�(�nn�6m�{:�u��E�"z�L�H\�Y���
W3F�"/+^F�qry<<���@h�\�K_������Y�.�?�kK4�[��:X`��|�3}��،?Y��QQ�����=,�;��	B�����hYB��C��5|@��h�w+�B�� �n�v���?6� $���6�2=DT�U�xŌ
��۰AXz�3�I������&W(��0��qX��S\\Ыq��^g��e�-�����г�J���#h�3?�>�'��H��`�Ų�nv��a��vW�&F^�T̘~=��F�ǐ�=`�����+1���!p+�A~Y��{X�U�̈H�&��];9���Q�����h7��z�%�ru��Z��������@3!.p��
���S��S�S�7�2����BrK̄�c��=�Z��9��%������Y���aDN+ɹ3�3��#<�\�GA���uA<�E�"	���\�;�)�/Q��gR�YŽ�}7�f���ճj>�n�M�;1N�4b�bj��ٗ������P�_��b�9�H]���:��FR��W��!E,�/�e�# LɆ�X�#ѫЙ �L�:" �G��̾L�Y�W" �g!P��B�v��E�t9�BԔ�$��Y@��	X��HT>w�N�V�ZLik��FH&�[�b��|�D�%h�f%��pl6Qj_v�^<�A��2����F\��0�$kW�݆���YDą�GGp�t���� �~-^J�$�����!_@r~WZ �a��������o@ȡ��\�E�_ ����H]f��o��L@����v���ȆG�����\W��7�%���p%�G<�����@b%!wF�4��AjRUn��,�<��_�Avm�7�rx�����/>�CHĐ��;�Q��;�`�Mb^��4��
��ijn��w����+I���=Y�� �Bv�����R�>A�EM�^]H9��A�1ᇀ�b�eO�6#�e�^�p�&@3=�������dL�DkUD�߇^Ԁ,��z�1v$��< ���0����~�ڋK��6��H�Q��`.�@/bğ�l�0��A,�O�jT���ݣ/���;U<�ڦ���z����?{B5p|�@-�r�j��""��=�8����:AK�Q�����i�>BR��N���%pl�����Q�@��8 \�t�ޔ�e��2��c|�[��(�Z��;sU����AV�I�f��Cjk���+���{���B��?^�0���[� �YO}��#²���ylv>m���V��[�t%��'	�pc"��W�0jC�HO�7YJ�wt��/L���)l��a�OuB?B��Ĝ6 �P�� ���q����"zc������7�4e��e茪^� x���x���5�
�f��ϯ��OtE`��kO
����>(�/�����K��>g� dE���Ԋl={��q�.��QM<x�h-�l��1@!'��\�<F1p9�,4�5�]�!��'\遻*(�����z�_W��h� ��b�Ls�uW��c�XL}Ascތl�/[�|��h�LL��M}"�*'�9�0�jo���'�u���]�6j�q��<uAB�����������]�i>��W�a�+c.\#� 3�(�yT�(�'�5�E{��z�_���>��m��ڱ��$(�Ȅ}�,5�{�| 9%g�p��4�z;�p}uy��
/�qC.���g�7��ߴ��	���<�W����aq�R^���� 1*�����V�J$�+�W���"3JtzB��������_���I�l�,�?�w���]�\�3d��w�nB��h.��>�>�]��h�	�f�/�{��sD�������n�3�3C�v�}ܠ��t��!I|�hz�1^����\����i�d`C ��)�3|�$���Xd59���~245�����q8�[^�WC�Fd�W1|�u#�Ϡ9n��ݿH3&I:��|!�SK��&�P��QC��E`�|����&��]dL�!�I$�8k����i��"ˉ�P����b�fDa�պ�x�4� �!�܌�B����3Y���ёpL��=ǹ��ۇ�	�tx�<|��٫���H��o3]~H�� hٗ􅆆�*�W�{���s����0����eb:4�p��vGi�H�mK�-�g�!*�:���������{F��$&L+�=)�u��p���O�T,�vb�uQ�	c��FPY����C�dJ[�?������Dj��\:3"T�l���)u�u�����5B�%5��n�HO�%S����R	ʎկ<!/$/���4�)��׉QY��͸M*�Џ�`�[����)��ԸwC\��5�I�-��T�4Z^�mvL���!�HD�&��~��Z��v���Z9 �"���4��Bs:i�|��+!�X��-�T�Û{)ˎs����K��5r�}�tu.M�Q6l�B��2��a2P��cFɿM7��O��+��">��</D�}�ݦ��ݝ'����-
�f���g_��C	$� �-�&\/p0�	��6(������oL7���O݀�46ݒ��&����n�ó*�Q��B���b����ױSK�$W���	�����F�#�	[z��j��M�$a�a����;�����"p�`��$�!6�F-9�,[���à�g�m���p�a=^�k�,�;��a6���(駆����1}+�l�ɓ��V��L.0a ��`c�&�.e�Pʁ��3�nx�I�!�$!����V=�A�/��G?ʕL�c���_Di���L̩(b�e�>���8��b`�f|
���3�~�!�mN�	��t�haʂ뛊�jY�p\=�Ñɚ��B*�~Jͩ�8	UG�*L[��!�3i�*OZ�\�G�@2ճ<�Z�J}p�U���E�5��@��6��1�]��tϑYF��&����p|�x����ŹqO`���3���iVzt:���惠u�}�QRz���=�����0֊Д���p[�h�bx�}������'Y�ny
:��`�� �t^|�[�?ޟ,w��d�"�E/��s�i��Edo$U�)����dtaPi�Q�V����[��G�o۽�>�C�}��%(�,���gt����2I����1e'��S�>���.2����:v^�$6;6��{֤�b&󛷵�A��Tib��ăW�r#�S�B$V������Y���̊.���P`s�H��Ѷ���y�L�q�z��$��^(6܃�HW� ai�*a:Cc�a|8#4�ciĘ�*F�3�����0�{ �}"`{$�Z�!�h��/�0��5F��5���@t���(:_u7�1�t�5��FvUV�{c�d���}K�I �"U �O�����-��Zۺ�����c�T�H$�1)��D�lF&|mD��`��-���=g������u9J���5��ۚ�wc�[� �9�U����G}z�n5��̶(Z�����&�|x�����U~ۀZ�i&T�|8���rLx��b� �������KJ�J(L>�?\\��׈�ɳ��ӽ� �T�    *����c���"������A���;�o�!�wP�E�k4(;��l�U����=�?3iӉX���e	#����?�Xu9�܃Xp4L{w�~v/�Y�7�*�����ۇA�N�!u�ٹV&�.�wF-�?�6Q�w� �P�Xɘ,"D�
�gIŝ�8UQ�9��D�����O��4�Of�����(�)���5to�~apz��w^n��AަI#� �-��#�eQ%�&!�v&�! r \}�a����	<�@ۗk V��K��0.�:bT��1���G�6r�y��`� ��=܏�2�z,]��-����L߄��n2��}��^E����s.���i����$.l��������F�:3�y�٬\�m*��u���.Н	��c�?���`d�%^`;����������#k��G�P���۬��)U=�dW�Ey~��o��뻇~���S;��.#8Q��>�R��	�"S�M}��>�������� ��e2���!�@�Z�����0q��NJ7E<),�zi�[����f)AԎC��*���[��~!��r��K_��T1!�'d7��'����0�3p�d&�
�]Dw�{�I�l�"���9����Q�
U����}!�:��<	ވ�'���m�/7��S�>�)�C�>������a�t��bS���r��������5)��g8�'ѴL)Nz=���o@Ϊ�nM5�L�牱QU�Ǟ\PM�4%�Y�B��pD�EC�S<�)��q���9T5cu��qw|�aR9��P�w���Fl�o;���,X�FԤ	�<�	�_Nz��̰�5j�>�;��s�cWEty�$�bH������NL�ڣJm��d�M�ѣ3�M�7�d3$c��y���f���wk+�!2�h��Hy����+�Ŀ�K�
��gaRk��w��{����Z�G��ub�t��Պ��o,N˥���e
�9�~�`$��)]��]"_��A�ޕ0i�C��PHAC�f��Ӂk>���M���򕵞�P�+18�䭍�%�(��t��TQ�M�haFljx�bh��� RC��NE�/=x�(T���s�^�?v���+)�2��V�������^W1y���\��������"&�S(~�_�c`�o+��Q'3Yc�����6�::_WJ`�\ 7�ZJ�����c�`5�/}��ճDH�k�y2&US�B����4��R��Q3��2�� �6�}���^J���;��Ǥj�!�Y� '�����
l�n �QO�/#@*���7�H�fO����a�rW~��&�\H�&��ĢU	UD�۟Ȣ@�2�}�g�J��8t�TGC~ !�\TQ�TH�+$��#��;����ZHE*������ব�H)Vn��~ ����y�̢.��آ�	 �К�uQ&ߎ�73c1���(�̂�탄�.�NK������ӌi�*5]���o6~�����T�8�c�W=6��>5�3�d�7��#�,�i�1�"B��%d/b�S	Q� :���*��{����#�T0@��"
����!��:-�Cl�-�D@�ףAy�=�;�q��M��
�\��6��Ӏd�J�RB��(�\��2%"�~P0������i�?m��"�F�����@m��^ j&�kV|���o�e�5@���,jj��H��Ы9�֣+	�D�}�7w���iٱI��~<솉ui��[O~F��*��I��ΥuO�U%֤��X�s8���3��q�k���&M2����'�Q�v:�I7K��~����('$��w�[ɡ����r���sFe��/r/�v�T{�y"a[����=R*@�^ȧ�E��[',W�U�'�2cy�����Z�B��[}*b�.�t=����pU�{��b���U�4�r.&QS����G��GȬO��8�ǒsy�� *t
�izK��㸖 ��wo�Ү� �J�}��&_�Z!��S.�����6����pJ���u�s��F�)�:Ö��-�
;$f�ԅ��K�H�
�K�IQ�0*~H-���Ž�e3�8|�zE��q؄�L�85�_}[���:��aͫ��x�7)1�NM��&��{t3�Q��,���@d��>  ���=HK#�F�.�HO��06�C؃�B�9@�@��٧y�*�#����_q��~��Q�|Ю��+	�x �Զ��tԒ�E�I���&�Mhvb!CT`i�+�ɷ 6��"��=�i�i���`��b��UMFX�\]�8.�~ӄV�����8�8c�'2#� ��p3|��i�A�Vp���B�h��!�N838�R66�5���<(a��`{���B�f���rq)�l���,�PCdfc�%
�}���N�E�	n�e�+pj�)_���r��21��覍�'��, *���u���������x��&�"�<�
�[/�����P��x*D!s�i@�&b����D�o�ƪzjEA&���3g}�x�H�+b�i$�8�#����3{
Au�;��6�����4\6��I���f���%+�-Q錝�l�ר�DF��sU�Й	����^�)�����@��i����i-_�~�������`�V�s5s�k������} �U�5M,�O��7����D�1",]�b��]�A]�o{Gj�����ES~��#\��ءA��m�g��)	M��wT�
�.	`�p���(��$�D�5w�0+��g5q��rUl�D��q�s�j,���v>o
�A@�ڮv/΃[��DDJ�S"�B�SfQ?U���8��H�N��R��D��6M̉�2�/tf5��aۯu��TTx��UR# �^�g��F�@W��j������A�d��T��2��Ԁ��K̑�O��b�:j�0��K�3��i����.��-�Eƻ0T�4��{T�����}�B�+�B0U*�~���O�(���5��h*R�f�] ��Uφ;7�4�R=l&m�fs&T$�p���w@6
}�.(�Ͼ=w{1%i��Ep�7֣���H�NE��逭b1�7kF5:�7ֿA�0&!�j�;QD��  �	@�\Q�]^~=�]�h���U����\�tW+@ى:�@��^�F?C?�c�*9�\���x������߭�|�l�q@�܂G��t�p�{E�g� ��a�:�W_k9�\�Njj6��p4jm�� oul~����k��J��I�I$f�N�,>sN��:ӿ9t�+��j6"��չ!Je�zl��ɵ~�(E�ff��l;)hbr���+`��V���Kz ��,����A L�j�De�9G�4#4����r�HIX8��7ɶ��j�H�_꧘+�@]�����8JA�x�;"Zo4���lS�IO��j������B��%I}ֿ������3��{ͼB5W��[������q�r�T�&��d�ޑ}Z:�3
v�B���>��I�l��\�`y��NpY ,�g�(񊨁���yv��n��A+�.����Sn����p
�.����0����!�Żw �l�[���@ �.Ub��[��ʤ��L�w2IW`.y$5ΦkR�z`Ln��~����h];�0N����Z�*�J?練�� U���5=�K�#�U���� ��v.��OO�[ԓ]ܡ7�z3��5"̒�1�T����R���]Y�2�S�Z��!�別�R���>���~���"qY���G����e��*�>���w Uo�m��=�n2&m.bӱ��c�*c��Wu��pv k}s�uV *��IQ��BIN���1��u��0-���öO�q��l``i�J2��C���.�Z�=���q�\���jBs���3����sv.��-ޫ���K%#�=^eqv{��\����T��m�0%��}"
��o�cB�'-kaL��2��	�(��h3�?,Uȹ|��7u��je'z{6d)`g��)�&^h-{uK�e��=!��36cs#�����p �����Q���Ǔ����W����� ������ �!�-�UFD9U�l�-Q0՛~�����o��NgY�b5ks�aL�Zg�.VeeP��S    �lv[��Ɓ'/�
�S�Sa�ݘ�r���=I15}���	�gs��F���I�]2��9Q|�ʕ�q<��t���Pt��=����~��N�6��ϷV�N��AfA��ӂ<��,�vX�TfӊQz	��X�mDjB�,Y�rdX���X�[�Wb3��\9B��jKN��=�Ԝ��F�*{�1�&6�S�P��#<�0Ad�Y���k����DE~Xf�3��ݡ��~k��օul��#`ar?E�R�2�Tf�i��T3AŪ��=0���DsK�B'hs�1CZ>�o��d�9�%���q�����K�aY�����_�u�f���Y'Lyr�	R�Ҭ�>9�i^���f�B��ǽaӺ����6��N��d�w��7�6�{�Ll�,��ˬ�����<����~jJsSR~ZI���2�N�C�|�^P�/��;(TBYjĥʴ�{�Xv���$���>�0̉��Ћ�AU`^Q����g�c��}�=�K[����S��#���h�h�$���ɷ��@z��AJ}�+��<�Q��o��20�����W���1�Q�q���d��7X��y�Ĵ�Hz�����f�J��� I��4 �b꟧*n��Y��a�m�u(E̤��n⁮��D jiC�����&����&� ���".��	i�t�4�%@��i�ϧ�}�q�i���E��%F�g��B�:;˸*Α2����F�LuҼƥµA�H��І�����8�k�5X?�[�!��%f�nӥ+S�|�pO�y���~|"�n*��T�j{8�͸g/M�k�m��_:�ţK���i�
pq��\@.�4���qዳ�/�^~O~j6��O�q�6^+J��Gc��V�Z�?͵t�9Y�.�����E���S��}ǧ#C�$��I����l����>kY�1�[��֍{�y�h%Wٖ@�w��&ٌq�o����i�W�vs�RN;r����Rg' 4�tzN�����;�};��d���<σX�6��V)uξ_c�\~�Wq��]�j	*D�0����ϔb��D�΅J�#�E��0����Z�Nz�cΆ�$8�N�Bn޳u^���]}����=�2�*���$I}���A�t� C�e��Eo�����?��3��Δ����LVe^�o�����Xǒ�1��ݺt^Ll� �_�U[t�,�2J�}�����s����`���jE���Ə�
�k�y���/��Z��� J/��Ot��?�O���C u����ǯs)4I�Ǆ&�rpύsbf%�w�q�V*�5�n�(CcPź��\��8�_��T.�X6�"U�l^�,����*;%�s�Y�rSJ7I�Ml�c����?�/�<!+Qa��Ҭ煺(l0�4.tԂ�y�\J����tY�0�L�f'O�^=ѩ�z�
��&b�aJk�y�W�n�"���
F�Ei��tR8BY<-?�	 Ne5!EB�t�%cN��O3M��R�n�6���PL�;ypq�zw^Fk^I�r� ?�|��&�jV��qTs�Ⱦ=^����)����B�^����iP�.��îC��J2�Z;�G�p�����k�HZL�:2��J��`��yb;5��Cڰ�����뻼n-2��4�Z/岝��xL��>QQ�_	��ז(�3����w��]�<�ţT��2&Sw�;��͈�{�����.���'q�bp�"��v���&����r&D_ȕy��"�>��I5 ػ�|mt8?��lL�t�����rI�`;L��d�s�Ǆ�Zj�]>Mv ��B�)cb���jHUaa�+J;A�g�wQ��ՙ;t���a����E3�i�6�0�!��Ά�r�wZ����SI/����N�T��z�q�T糔ssr^V���c~��[ӓ��
�lrs���I_���#��u8�`����`�i�B�剪3y듨U"#*1E������0��kȭJ�c=	��([Z��=���t�?���+�,�����A6G������㠷�=B�nn������ݳ�m&�q�� ԧ��y��n<gM�J�X�&����V͙P�j�z�l�n�y�\у�˶{d��	�MT�� ! ���+)U�5N��mwX=\0����������zS���:��H�'ޗ���f�~w�_�}�^��9exA�⦖�YBj�f�ʙ:Lu��Cųs�5�:�I���*�#�Iq�@� q�H�	�-�Ԃ
�F� �Q�4ȸ&�W%��/����@��\��H�I���Cۋw:E8�3�%ҭ��-���ػ@��xj��\C�1љs?�~�.ۢ ��h/���P/!���.���d`���H�����#0Y���=L�S����7��&� �A|�(��Z&X�wq�j)�sӢ:�~3�6��6��`B��v}�8�<���c"o���A��$�6��.��"�ㅈ����C?)�C�(\Z)gZ��8�	���I�6�5��S�>�]yl_���2���ĭ{2gȖ0�z��X��3UxQEN��c� ��ӱ�B)���(.ջ��%�V:l�F��D�YƇ�)��,tҍX���N�� �������?{������Jp_��s/#wVMk���0�u�"g���^�Ӓ0�Cm{P	]�Dߌ)��f�Zu���1��k�& �ZھoW�_iN³����:��H�Wfv�9��K\y�=���XN�;�d����ǫ/_�M��HJ�|%L��E��x_�E`iơv�Z�g��\�X�a/�.�K��u��ۘPMP�JPD�+gx��9��Ի�R/�<���p��������(�\�W����Q�'惈���������k�ő��55Q�)�X �,5�_k��T(�ٟoo���ˑ��9K����*���Ecǫ��3������SM:F�ĤR2&N�V��`>�%�܎�JJ����ܷq˒)p�t|����N�3FE3�HU0%�έ+�m�(��Z�ʆ��v����H?�ʛ���l�hLRF>�0��U~��Z�S�&�`j<�Im�i-�"��]��c���_�F����E�2�0�-���k�$����<��8O�h]q�1��c�鿘���%���.>R �ՎI*���.�*o��M0��G�y��A?�&���q�ڝ9jUS�F��q�7'%(��ѡ)	p�5��i�u �/�Ǌ��T!ԂM��t�L�B&��+�X�.7B�q�5�0�4ܗI6�E@��~9	�c\�u��.�S��!~&�f�%�&bg�op2�ww�)��3%��&�������As"Obҥ��J��/Z�D��za���SE��̄W9�i��6aUR�C<�0��r ,�G*w
��\2s�������&pc�ɿ�������v�S�l�J�;F�~�������7�f�F,�[
UZ����^\�g4�I�Ti�-�<#z7޻I��-K����e8�[2�UaW�W�T%�a���օ~��	�4���ݛ+�`��`5����5jF]�\����*n�	�v-��/I��������	�2d������e�4���EB��mN(?��Q=�u�(~p9��XN�m���T~ظ_�TI-E�詳>Sj��LGLmBc��F��Պ&B�~(SR��O�*��5��43*O~�\8��d�����_$<�{W������A1;�2���k�:*m�WäJ�)��N�<�,�[��b )�����0�6�ME4mt1��.|��(�JP�D��C:)��m��=[6L�f�@�N�C�BrYp���kj�Cn|Dމ�i�'�?�U"������<g.&���+I��f&���[�|�����m��g�I�7�r#�^���AO�K̀��X(�2�-T�&-�ɐ�sY��5	��tI���BW�L/��X��&�A�����:��M8��ܚTT��6�q�;o"��f"X�[l��z9ai<�C�Y�im�ܰ_oA���0�v]��(j9]�mI�xyn��Ұ���+��C��3���q������W$�`QY�}F7O�fICfh��M<�-�2Q!L)��)�P�.�O8(��n�ܨP�R��k�ÀHZ\�N-�A	������k 2  �{��+�	�	U��C�ȂAժp�t̘Y���Z����^T�M̟��̄�K���W|�r'mPAQ��[��I�֏�	{)�č#7K��%�2�u���M��ۖ�a�y"�ѝ��v�\;Uj�1�����4���݅��r5W��� ��&��p@^ t~Ìy$V��Jqɖޚ5���&O!w�p�6^�[��u����,����Woɕ�kԆ�M�X�1i�Z�-r�P�,Z7�[g�i�4)������]>��I��E4��KۖR�>�n]�j�D�R%o��
�>�k0��([���Un�V8��匱���Cr���>Q�Q��xݪ�0��� ����hEM=����h��^z��v�_ԉ�wWͪ��&��tUj�~���b�����:�x��ހ*�aS������;M�M76�%��ѓl��n���e�CT��bt�d�F�'�5͋-(��^��JOZ�������+��fP�z�d��2,?+�)�z��� c�\�Z�j�:���K�%wB�Z��A=���h8c����mm5+�ls{��D˜7�d����amZ�13�|GI5}L���1>���L����ϗ��~ƌ�m��{��M�-c��W#j�ܒ�*�!0�sÖRv�B���V~UFjǎ*]ę�Z"y�1Vh�+��
�"��A~3�iV��,R�+P7��V<�ؘ�FCV��j7�,L.D������)�sta^�KWpS��<��[Vs����ߏ�?(�sw��Lӡ{0E\X=��ύ]ʌ�H�s���#j����GCR5�R�=�C������Φ�ɫ�����&�߮H����9��#���=3b�do%����!կm��@��C������~؟��W�^D��2��+VQR)ZN	�I�H�x���&@QH���)L����+OVhP�����Ԯ{l;uc�CC�7�vR�A��f��xu��o��N9�qSU�a���M�:�r %�9����f�eM�"���2��D.����&2q.}�":�6����d��`c�ra)ӿ����0��T�Ҕ̫�Tu:���p�m��l�5��Ĳh܃�`nX?Pj~��bm~�t���ɓ�n�3� �V�0)�0�A�:x���q�i��$o�Xfg��S�5�"��&Ty�?܈�._���ihxS�Ȳt�����I�\0�� �ZUS�Rf�4�צ�;ɓ���N,J�0JFS�~����W�s�rª�6e$Z��T��Sϥ]z�wdw��K�f2Za�sm�]�yIx�J����L_�U;��1�۶ߊs.l�������k�;6{�#	�:I��#�\.��~O=-,��	K5�[FDE!z����W*�v��$�V��#�'X50a:�^ږb��q�d�Nj)�*,!�� 5^�T5T��X���02�����kͯ�3 D�5]��bP����O�H�.��a(�A�T��#	0Ár���X�f�a���x�G�q����7��d�z�Կ:��&��r�K
��n=xt�%�ϝNe�L��V�'�$m�B(���ԏ�����y������*�      |      x������ � �            x������ � �      �      x������ � �      �      x������ � �      z   �   x�u�͊�0���Ä����A�b��Z�
��t�~ӃK���a>f�9pf�owi�����Se����S$���M���V�����Rǹ������&c%�����=[�If��V��`B2߾�F���2��u����bz!:��,t�U���^�b�LM�a^��U�Ge�oDKc8�r�	t�PO�n���0��e��W�g�����a�<�^@�
��\�Ι��X��ǵ�,�m������o&7���1���9J      y   �   x�U��N1E����7t
4�`�	9��M�*I���$ӑ����kɓ��B��+c��uh�,����@��h&L�R�H^�L����SU;���)��I������NW�&{������E��˚��Â0��2����z�1&�g�hw%�5y��ܟ0g�2��-W���cj}rk:��[��^0W�j����������x�}�����DU�����1��      {   1   x����,�L,�/���,I�K)J��K�L�v(H-���L�������� X�     