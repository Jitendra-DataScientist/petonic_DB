PGDMP         !    
             |            postgres %   14.10 (Ubuntu 14.10-0ubuntu0.22.04.1) %   14.10 (Ubuntu 14.10-0ubuntu0.22.04.1) 1    G           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            H           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            I           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            J           1262    13761    postgres    DATABASE     ]   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';
    DROP DATABASE postgres;
                postgres    false            K           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3402                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            L           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    49185 	   challenge    TABLE     �  CREATE TABLE public.challenge (
    challenge_id smallint NOT NULL,
    initiator_id character varying,
    initiation_timestamp timestamp without time zone,
    industry character varying,
    process character varying,
    domain character varying,
    creation_timestamp timestamp without time zone,
    name character varying,
    description text,
    contributor_id character varying,
    approver_id character varying
);
    DROP TABLE public.challenge;
       public         heap    postgres    false            �            1259    16399    challenge_json_data    TABLE     d   CREATE TABLE public.challenge_json_data (
    json_data json,
    challenge_id smallint NOT NULL
);
 '   DROP TABLE public.challenge_json_data;
       public         heap    postgres    false            �            1259    16409    challenge_status    TABLE     �   CREATE TABLE public.challenge_status (
    challenge_id smallint NOT NULL,
    challenge_status character varying,
    json_data json
);
 $   DROP TABLE public.challenge_status;
       public         heap    postgres    false            M           0    0 (   COLUMN challenge_status.challenge_status    COMMENT     ]   COMMENT ON COLUMN public.challenge_status.challenge_status IS 'UD, RA, RS, CC, dup, reject';
          public          postgres    false    211            �            1259    40960    contributor_approver    TABLE     �   CREATE TABLE public.contributor_approver (
    challenge_identifier character varying(255),
    contributor_id character varying(255),
    json_data json,
    approver_id character varying(255),
    approver_comment text
);
 (   DROP TABLE public.contributor_approver;
       public         heap    postgres    false            �            1259    65541    domain_list    TABLE     a   CREATE TABLE public.domain_list (
    domain_id bigint,
    industry_id bigint,
    name text
);
    DROP TABLE public.domain_list;
       public         heap    postgres    false            �            1259    24595    industry    TABLE     H   CREATE TABLE public.industry (
    industry_id bigint,
    name text
);
    DROP TABLE public.industry;
       public         heap    postgres    false            �            1259    24576 #   industry_domain_process_key_factors    TABLE     \  CREATE TABLE public.industry_domain_process_key_factors (
    "Sl.No" double precision,
    industry_list text,
    domain text,
    process text,
    "Description of Process Category" double precision,
    key_factor text,
    suggested_values text,
    description text,
    "Required (Y/N)" double precision,
    "Weightage" double precision
);
 7   DROP TABLE public.industry_domain_process_key_factors;
       public         heap    postgres    false            �            1259    65536    industry_list    TABLE     M   CREATE TABLE public.industry_list (
    industry_id bigint,
    name text
);
 !   DROP TABLE public.industry_list;
       public         heap    postgres    false            �            1259    65546    process_list    TABLE     a   CREATE TABLE public.process_list (
    domain_id bigint,
    process_id bigint,
    name text
);
     DROP TABLE public.process_list;
       public         heap    postgres    false            �            1259    16496    score_params    TABLE     A   CREATE TABLE public.score_params (
    name character varying
);
     DROP TABLE public.score_params;
       public         heap    postgres    false            �            1259    16501    score_params_user    TABLE     3  CREATE TABLE public.score_params_user (
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
       public         heap    postgres    false            �            1259    16504 
   user_login    TABLE     i   CREATE TABLE public.user_login (
    email character varying NOT NULL,
    password character varying
);
    DROP TABLE public.user_login;
       public         heap    postgres    false            �            1259    49159    user_signup    TABLE     �   CREATE TABLE public.user_signup (
    email character varying(255) NOT NULL,
    f_name character varying(50),
    l_name character varying(50),
    role character varying(15),
    employee_id integer
);
    DROP TABLE public.user_signup;
       public         heap    postgres    false            �            1259    49169 
   validation    TABLE     b   CREATE TABLE public.validation (
    email character varying(255) NOT NULL,
    active boolean
);
    DROP TABLE public.validation;
       public         heap    postgres    false            A          0    49185 	   challenge 
   TABLE DATA           �   COPY public.challenge (challenge_id, initiator_id, initiation_timestamp, industry, process, domain, creation_timestamp, name, description, contributor_id, approver_id) FROM stdin;
    public          postgres    false    220   �9       7          0    16399    challenge_json_data 
   TABLE DATA           F   COPY public.challenge_json_data (json_data, challenge_id) FROM stdin;
    public          postgres    false    210   �9       8          0    16409    challenge_status 
   TABLE DATA           U   COPY public.challenge_status (challenge_id, challenge_status, json_data) FROM stdin;
    public          postgres    false    211   :       >          0    40960    contributor_approver 
   TABLE DATA           ~   COPY public.contributor_approver (challenge_identifier, contributor_id, json_data, approver_id, approver_comment) FROM stdin;
    public          postgres    false    217   8:       C          0    65541    domain_list 
   TABLE DATA           C   COPY public.domain_list (domain_id, industry_id, name) FROM stdin;
    public          postgres    false    222   ;       =          0    24595    industry 
   TABLE DATA           5   COPY public.industry (industry_id, name) FROM stdin;
    public          postgres    false    216   E       <          0    24576 #   industry_domain_process_key_factors 
   TABLE DATA           �   COPY public.industry_domain_process_key_factors ("Sl.No", industry_list, domain, process, "Description of Process Category", key_factor, suggested_values, description, "Required (Y/N)", "Weightage") FROM stdin;
    public          postgres    false    215   2E       B          0    65536    industry_list 
   TABLE DATA           :   COPY public.industry_list (industry_id, name) FROM stdin;
    public          postgres    false    221   8�       D          0    65546    process_list 
   TABLE DATA           C   COPY public.process_list (domain_id, process_id, name) FROM stdin;
    public          postgres    false    223   ��       9          0    16496    score_params 
   TABLE DATA           ,   COPY public.score_params (name) FROM stdin;
    public          postgres    false    212   $*      :          0    16501    score_params_user 
   TABLE DATA           �   COPY public.score_params_user (challenge_id, desirability, feasibility, visibility, innovation_score, investment, investment_in_time, investment_in_money, strategic_fit) FROM stdin;
    public          postgres    false    213   A*      ;          0    16504 
   user_login 
   TABLE DATA           5   COPY public.user_login (email, password) FROM stdin;
    public          postgres    false    214   ^*      ?          0    49159    user_signup 
   TABLE DATA           O   COPY public.user_signup (email, f_name, l_name, role, employee_id) FROM stdin;
    public          postgres    false    218   �*      @          0    49169 
   validation 
   TABLE DATA           3   COPY public.validation (email, active) FROM stdin;
    public          postgres    false    219   �*      �           2606    57345 ,   challenge_json_data challenge_json_data_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.challenge_json_data
    ADD CONSTRAINT challenge_json_data_pkey PRIMARY KEY (challenge_id);
 V   ALTER TABLE ONLY public.challenge_json_data DROP CONSTRAINT challenge_json_data_pkey;
       public            postgres    false    210            �           2606    49191    challenge challenge_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_pkey PRIMARY KEY (challenge_id);
 B   ALTER TABLE ONLY public.challenge DROP CONSTRAINT challenge_pkey;
       public            postgres    false    220            �           2606    16528 &   challenge_status challenge_status_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_pkey PRIMARY KEY (challenge_id);
 P   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT challenge_status_pkey;
       public            postgres    false    211            �           2606    16550 (   score_params_user score_params_user_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_pkey PRIMARY KEY (challenge_id);
 R   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT score_params_user_pkey;
       public            postgres    false    213            �           2606    40966 '   contributor_approver unique_combination 
   CONSTRAINT     �   ALTER TABLE ONLY public.contributor_approver
    ADD CONSTRAINT unique_combination UNIQUE (challenge_identifier, contributor_id);
 Q   ALTER TABLE ONLY public.contributor_approver DROP CONSTRAINT unique_combination;
       public            postgres    false    217    217            �           2606    49153    user_login user_login_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_pkey PRIMARY KEY (email);
 D   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_pkey;
       public            postgres    false    214            �           2606    49163    user_signup user_signup_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_pkey PRIMARY KEY (email);
 F   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT user_signup_pkey;
       public            postgres    false    218            �           2606    49173    validation validation_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_pkey PRIMARY KEY (email);
 D   ALTER TABLE ONLY public.validation DROP CONSTRAINT validation_pkey;
       public            postgres    false    219            �           2606    49192 $   challenge_status fk_challenge_status    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT fk_challenge_status FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 N   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT fk_challenge_status;
       public          postgres    false    211    3238    220            �           2606    49202 !   challenge fk_challenge_user_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT fk_challenge_user_login FOREIGN KEY (initiator_id) REFERENCES public.user_login(email);
 K   ALTER TABLE ONLY public.challenge DROP CONSTRAINT fk_challenge_user_login;
       public          postgres    false    220    214    3230            �           2606    49197 &   score_params_user fk_score_params_user    FK CONSTRAINT     �   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT fk_score_params_user FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 P   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT fk_score_params_user;
       public          postgres    false    3238    220    213            �           2606    49164     user_signup fk_user_signup_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT fk_user_signup_login FOREIGN KEY (email) REFERENCES public.user_login(email) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT fk_user_signup_login;
       public          postgres    false    3230    218    214            �           2606    49179 #   validation fk_validation_user_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT fk_validation_user_login FOREIGN KEY (email) REFERENCES public.user_login(email) ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.validation DROP CONSTRAINT fk_validation_user_login;
       public          postgres    false    214    3230    219            A      x������ � �      7      x������ � �      8      x������ � �      >   �   x���M
�@�u�2k�(]yA�4h���(�xw��Н����ɋ��|dZ4�jG��8�3�	52yG�]l�����zt�v$����l������9L��GRd[[<AH-���AJ�(+`F���������	Ys��������[��5ߧ�l^��T��l����GW~ꆟ��J�tƘ��      C   �	  x��YKs�:^�_�e��f�2�6˄��T�	Μ���bhb,J������Z~ ���T�nK��u�A0x�:�|]�O������
D��;QT#��T��Jy,+�+��e���G���g��a>��G�sY����5/2a����>��Ӌ 4Ç�(��o�B�Կ����[^���l�� ���'&ʒ�0R֕1�#�Zӝs����ؐ�Y���CQi��_���\��O�Ys�Q�UQ
o���C費�د�Z�7⽩lu��]�C�`Yl<F>�Y���Cv�jm�X�|���$�j-�y�\L�ȢVu���Jim�z�W�2�/�\�������=F�]�9"4�s�+�{ۗ������ϝ���չ��c����o���k�<<Kl0�joG��A|�QV*��9a �\�L���-�:'gx!�V�!�$}�,M�yᰣ̸��Aad�(+|�?r�?�>x��/U^��H��%7r<�$a��,���a:a�Z�Ye�f�p�I.�P�,*6Ph��U��a �Y����-����S�t�F"��ͪ��l����0㢞���u%�}��R�lݪloC�I@F;�% _�U�X��zUzC���m���5��խ��&��;5��`Yզ��2mrً�o�I�Ӈ=?�a��e��ô@�țӇ���J�dF.�B;����~e�*�}]���z�J+Uk4-���?�=���gT��L"�,�h+]u�)�hn���~���Z:�u�@$[*��:C��3�Q�[ aFCp��m�Ū�n�An���eJ����h�	�S�<�t�r+����M3o�î��(�I��~��}R������-4��`L��<����{tBϏMO㥺�f�0��cL>F�[I�vv����p02}�̞h��4��O�����NΓ���$YW��dt5����h��(������|�Ё�F��Ͷ��)�og>�A~Ԋ�2^V��^4^*�$ gz �-����V}�j˶X�u/	�Y�^w�`�=D�!��B��Z ;�܋ԳA�tu2%��2����N��p�}����(���T)�wj��k�V�%cp�Z!��$u'����9.�nq���2�����7�Gk]�z�2�&D�9�Ge�������j�[S���iL<'w�����R�+�tQ7�q �Y����Xe���<��acr�B  ����� �ȏ��4�h����ĉ<�� �b��1�=s������:��;�㱹��m3h+���c?^���r�-�Z����7;�͂���9������ �,-LuX#�N8��_��\b$tU6��łL7�p�N��1�7�ߘ�{���b �l;FA&���m�M�U�7��n;T��>�f�M�bb�4�a�����B}cC�~)��������MB*m�A�jt�c���1��j�&��r���07p��Ŷa���sG�	�"�L���p۬��X�0��3f����׾-}��1Z�	�;�Wr�0;,�r8)ș�EP,9��ső1��Z
96�3!x�]Ol�yv{�`@�`w���xp��<x��o��c���I�M�Ev^�n����7�ث��O,� �j=]B4"���7p>��&ӵ��f�^|(�M�g ��pg��)q�|-�����g\��'��$a�i��B�]S@�+�x�6�(hԅ�E��o]�# ?��I�j8�����B�av	�� }����EĻ\y��"y��>>@ &'D &D��T ��i��� X�7LO�QqB�^	�ys5R�}�h�)1��G?�g����`� ���o5 ����{0`zF�����������C�zF�/jP��Z�fup��Z	j+���+Ȟ$_g��(4�¶� ��v���0$oԽڕ���l�Xl<w/�'�ظϭ	W2pdt� ;���p;x'��e�Z���Q`���;��o%�<����E|M��P	P�Hc�zF{�I��ښ�c��O��a�,��Յ�y��a��Ս��c�~�d [�� ��O��lǂ��.1��s�$x�g��rB�$$s�0d.R8o�������Q�r@��%��i�x���3|����:�a�""	�B&$�k���^&��`j�y�!ſ{3j�������l�j{�4𡠓X-D�M�fja]��7c����;�=�GE���PK�1Tf�m�Jk?�����̰9�z��	v
���5v�9�K7N���Ƕ���u���J}6V$�~F'��^�����~��/���}w���-J���q������H�Eե�bo�`������� M���`���!V:�j�12@g����էO�0��~{z�����E�}�On�9ƅ�נ]�>V�@����z��7�Ƕ��+�"�3��\��f���/�Ŗ���"�9M�'j��L!-+8Rz�`�_-�iSIی(��mZO��/�����*riVH+��~�&�v�r�C��]��{��_�؟S      =      x�3�J-I������� �N      <      x����r�J�6z���Xkڎ&ݒl-۳W8B>���>h,�317	Ih� ������p?��SUe
�	t�L/�@&�*_f~y<z�.~䋛�ߒ��"]L�H.��.�fu�����ǣ�i�#k�Qr�j�y�d��mڤ���^�E��i���京{mr���ۦ�ϧћU�eUr6��*�s��MY7ɣ7go�~99:J&�/�GG��YZ��,in�d����I��U��Ev�L�i�8I�9����]_��<[4|�|H�T�uo�~�_�>�_'?Y��5�;ϒ�i��@��A��񑈌�}[�@�&]�H�\�L���'wt�V�qr�K��|�,���@��ſo��'|G���ᷰR?�IR߮�E�n��
��:�Z��$�2������.cRd�<�[΢��oJ��%��	U���M��~���xV|����5��+��t�׏^຾<J��iROӂ�=>:zl7��=�M���Y�I��7q=q[T�uVUiae<�I2Ve]O.���w>/�eլ��zt�������|�_��!)�(�jYý	<JO���U9[M��$��W�_�ϼ��`7����#.��\ަU6:�=|{�c	�M��k|W���M�||���q)��[Η��&���_�:2�<�9�|�������x%�K8��h��z�OP�6��m>��9�����/@.�q�%(3V7xUr�-���h`X{�b/~����]���%�f��|G�[O�_�r����z�5$��r��װ@UVg�iFrn?$ʦ��xB�\/��+���WQz�t`;�~y<z���wƛM+<h���1E(\C�g
�]�7�z�,Q��~�,h��K&$�q�F���)���'`a�6UYxf��,�t�L�i�y�'��,���܊t�sD����k��|����#�"�儡�x��Ua�Zeoq;,�7��"����~�Λ�*/���J��<�@a��~��·��r逕`��oˤId�,��
� �F��ٓ�'�>l1ˀfa����)l��VП䬼��y&-3���=��O	�������I+�O�?.Kz��l���;{���e�(qPҲ�1�Kؚ�7�0ݤ+Xͫ
5FDS�$w�ҋ�����]NK�o�>]��������h=�@�CZ4���GV�e9C��L0�0c{l�+���(J8�Yr�\&o��EQ�Zam���GNghaተ��{��~��C�x:�\��oI��܋7��9��x�h@G/i�|����Լ�kr�����2�'P�V3ڋ�]��@�,`i�[��\��U��[���#�����1JF�W�-�pMw����C�dp� Z��k�@J����ܦ��_\��|�Q�̚*�֣�i�Ó�qq^˦\��QB�E�}�܂ f�YG^�lV�����������Ot?&M99_���p9�rtJV�7В�٥S�W������(�EzC៰+A�jVY��;6�G[�~�b���?���5��k
��3Bn�2���>��V��v�-��l눜/����*�o�OSٺ��_�����j��:��h���mv�.!�a�l�Or�%wj��l�al!���q��}��/��x��}(Y�M䷠�68Jl��Wl�V�mݍ-�y_�ļ)W�����jt	��B����~-�b5��;P�����o�U1Kn�;wd�u0��@_�"�Ck3�;��Jܖ���z�/���Np1�@��6��$�`��^�Rl�Tl!Ņxk�M�t��U:'�ŏlv�pg�yw�
��­P�����`�ڶϡ+�H�p�hKo�>ym����Bзټ�/������oOJ��t�"��nƿ�Γ�p�M��Z�{�f��V�m]�-��P�;����(ʫ���Q�Q���fb~��K�g����Zj���������2�.�P:��YVָ_��/8�$=�@���	ە���O�S����(��@7Zpz[?`+1��I��{�虌ޯ��!1W4�%�+[x>3Ƈ�����Σ�^��m��݌����<��Y��׫����\1�-�q���p����dQ6�?Ab����!�����J1�슢�O�A�I��l1Y�"�_��R�V����E�TH���ӣ0~0�&�A�k�|�Z|s�ߤE���?������b{_Oo��J����^:���S�W���f�C(�Z9h�_����eS��9�~��m�)���q�׵������	�'-ˢ�Q�7�*@��Ѐ'���[�j��E�3�w�F��4��6�*�ְF���t��7�� ��ھ��@�p�a�>V��su)�m�x���Y���9�N�_��NJ*o��"�>U�5¦�`W�J���s��D�(ҫ�C`vĦ`�s���4�m��:��r����6K~�V���6_�O?o�w�����"p[�_���tK��|_���A`�|�2N�|>�'��`��d�_gH��"�u��g4ݯW3�܋¸���h�Iʍ�]̅԰H��]�z��=��f���u�5�|2~���H����\��^`��6�$��s�C|�rW?I>e�t^R1ݥy��;�x�����R�����9��3��Ȑ./�t��ni巕,|���㔏�|={��^5��5���F(+0-��B��'�V�$�,�V����,��ے�n��mX���}��v�L;�ceq2�G�*ب�)|p���)�t��)h�?��,�
"����0���^��}B�<��� �y���l�
��4���V�*����N�<��k�V�3�d�@P�>x�Z����x6�؂�>�L�ph+P��$�ADK���6`��˷t9��|#AI��1�~J�s�|�O�'6��Y�Ը ��j�M�����O��Z�N���j2�n?�ri��H�d����4�St3����w��w��ݎx��yK7f�C���d�����e�3wk��\8�m�zuUO���q��-Ӈ	<b�=���3}6�h�l�1ßn�m������J\9��j���»�cgr-ފ��1p�����L�v��	�ܦ��DP��aϩ\5 7V1��h��M�Kֶt�v��\��d��KQ�NT֓b^�/����~ )ǫQe���T�@>�i�a�3X!������.WW�����Ń=��kj��iH�܀�(��
�/�^6^�3�&�1%�J8�֣�O쪁㌆ȤȤ�$�>dw��N�������\L�k1�hA���ʭ�3̗-1J+��]��g�{oaӁ�I�=��R'��x7�!��5�e�4���Q�-�ؔ�̱�d�\\�y�� ܙ
��nw`�k���%�FX$����
��UMƌ���
#���P����w�Xif���dՆ��U�ǅ�a�O�ѽ��sv;.�%VR�� �z���K�Z�:�ρ5~���U���о�Q���[Mf�6���(t��lB��8��q�կ�`�k�N6	�ϡY�{uo�
D��K�g�!P�;F��븥^M�(�4���g�����e�= �ɲ�q��*P�#C�]|�����7t0YǓ����=��r�7�Ɛ?z�e�+L%z+��S�{<���l)������@������	������*�k�U�������
oI�"��	Yz�?��}+����2�@�*�����Sv<��Q����<+ ���P�'�	�X�UU�t}.�6��P6|+I(�����������=��n�`�?jf�����=��R���+פt�6P7�P� <�MqhW1}���y�?���cQ�,p����C�a�7X3 ����l��цn#`�؀��&�0��#7U��oۺ� 5e��"[��m`}w*.}-���;)XYͫ����[x&zMx����"�͊��3�'�F�,]r5�m�uFS���ay�8R��۶�]�0�-I�b�������������������b
��w�E��]�Zۅ2�]j��V�m��%ep���q��3K�[`%(�Ξ$����M��N���V2M%n����e['�G��W].����f����;=��y����S���8���D�8u��v��)̃���cտ���n7O��tg     �e7���|��c������%Q*�F(HF;����������.S����щ���;�)x�S��ލ$��nUj?�V�����nO��96#��Tv`Я�+?��!�l3��X6��;�d8�׸ $�qs����o�֍�_ߦ\%�]<ӥ� ꅟ�p���pS 1-����W%��Iby�D��m��5[�+`{4��j�hϏo�b+X��W�Eb�0��gb��!��x���=
.F��,-�rvb���9|.D���3orײ1T וZ�S��TT�}�)?E�6�H��n��R�X�{��ϭ��Oeie�U��ە��|S� _&��� 6��Ǔ�j�&�
O���C�9��x�χt?�'�"�	_�R'�M��a���CpZ�tA$��%��Xt�k#垕}Q`0S�CΡ��\�c[3)��K�k�!V�٤ l����O}������ +�
��0�l���Ӥ�d�)���kؐ	c�+h�Eż�УuC-w��3A�|�z*�FC���I�RBN�Db�}&��́�����$�]-�F��꘶��a=����Bw�t��s������H(�5_�|�tn��&t��&h곃����nV��]
6	��`PV��x���}Y�8n������6a�:<�?�����H�點��6��r޺ ��{1���as�P$�5�i����bU�
�:ql,&��AȬ������������/vx�{��TO�D��{p�=�r��c��8jC�"��Ή�^9��b[��|�jAP��#َ_(����M���iC���*���>A1�KX��p�-��Hr����1�t'r[/�[Z9��%���T���tPު]�$��DǾR�b�E���.�m��tI��¼:�]�/Ҥ�=F6������:2k��S�g��<�y	����}�qv�[ur�n�p^:c��]����fT=o�E��ܙ��Q�I�!E6�"�C��&����`���J�.ζI� �Zf�a��dW�/~b}-��M�Դ�ń���Jw�)^n�_tH�#�K��1�Bh�������CylI���Jg�4Uݮ���ZѶ�/:D���7��ĝ�J����(�.��[/�J���"}��٭lj�SX���&:�
�г��K%�P�y1��-:O�8� ��q��峕���)X3\e��]^Z8�嶾C�p�هZ(u�Be����l&�O�S%&��U�A/��>�V�����[�]�l��]	?=�RxY{D�Ӆ��ŋv&�-%��<%SLXAul�l�U��`�����7�fi��1"�?���y��H�_�����Ӻ�@+�PN�|�_��\ǥ�X�*@�UƄ��rI켞���:���s�i`ς�����c\�X�AB�
1n�CT8n�!,��jU4���t �ˁ|
���D��;�=>��J���\����jհ<}��ˁ� ��b�����,�G�hd1�	��j9�Y�Lp�N�0�7%7ȾR-M{�9&�-����3fUy�8yS�=�kw��V�Yٌ)
㒻�����a��"�4�ˌ�κ��6�'	s`�ݝ��dp�w�b��w�`��6��q��s��Ӻc�lq�������EF8c�7�Ώ�r%�e`:vҵ^�?�Sh׀Qt�UFX����ݜR5���G���Q�5�[\|���`_�Ӥ��X��z������t/�	��v���9�ҪiӴ������u��>VX�Ap|���q�a����;;	K������.h���';!vv�	���g�?��gG��Q���q2�3E�qL����f�x��^| u��wr� E5�}���b�;��X'���~����L��2��Wzɐ�Iٖ#v�#�XL�
Jo��j{��hqp�w·���럡�C�æ�YykШN�t��E�VTlΉ�X5������6�ɱ�EZG�3���<%�t����E��s����һ�b50��Ⱥ�1+��|��v3�T9#��<���r����YI7�x|����H�Y��N\��-�ҩ#BH���`V;D��˃�چ�وn�,[ו�8���CG�t��ک\��eK�p>g�TQp���Iq0�m������Q�R�c*�U��ĤT`��-�gjt{��+S��M�p�Ί�l �����9�o��I����ʦ���w�	j+��qu�]/z�}�ɠO��Mv8��Z��%W�B
��/0�<�@�O���Ɛ����h����`�[���jaXM��z5x����2��	� �ے�� 
Q�^`�7}��c�3�^�����a��T��d9���w�_�tI�!��5��}�8�i���`�=ޤ�?���8���������GǤ_�
�;>W7)�vx���؍�,����IW/��[Ky���4�.D>;��ToK���T�I����r	G'Z	o�8�.��c�o3�
8ޖFus�����B�'�u3VC*�/��y��q���oz?ޖGu��>�wyDQ��\��L�vتna<�dc����X+�_��|1e��]��=�X�ɮ׵��̃qY�*a�G�pY}[6�w�-���Ұ�<y�����O�ѱN��"�G�S<Q��"�ʡ���:vu֊����0dl��"�=yz��
�n��W�Q��]��TI�,"?r�hp�-��VF'.Zyvzr�����k���ɍ-6�I�d��Pܙ7jqvu
�
��n�/~Ԇ�>41����V�+{��U&]���[��P�mU7��f>�e�/���]v�K`s���xYf�xWʈ':�ڬ�i@2��f�߮�Y�.'[�X���~?���3{�K;"�B�{12*;����l��ń-^�w��u�d���&뷘,�]�[���3M9:��m�FIs0����x�w�T#��)�鲶Ƽ��Z�c���2�I�m��a
�9�5�^�D�FF�8ϝ�#:z����U�m�ߞ/��*�@�m)T7��k6�]��G����/j��`�]�ҵvL����S��㙳��2�no(ޣ�@�P>�R����D<��}*S8�Q0��{�\rw[&�m=�{��ˣ�aCp��c[L��;��-�t� �2�nq"�h!��N�q`2�X�^����ӯr�p���Z����T7�/0��[[�vrt�W-��uyz���0 |�D���.��	q0��X��2�'a�ܺ$�2�e��!n\��Y����ٚ�tc��MH�TS6r_�_�:WOʒ�K�|s�ܮ�9�짶GoMnj��֗���=�Β>%R���5�~���8��&22�\�'J O��D��zn��ƛ�w�u��w6�1[�[}~����1�D"�v�5��j^S�dn�	���q��nR�����k��~,�5_i�����e���l�H1�ؖ���>�%�p���`�&u�L��N��􈖔;{	)���jNz�#c�D�p4Fj�_���H�4b�ߔpW���nyulP�<u0@���tuk���t�Hv��)9�4z�u���I�1�qA�F>p�7�"?i ql��qg#"��
�>�sw��8�N��Lo�����]u��-[� pǱ�+��9��(	wv?"*rw.juB��p�ہJcU�_i頊�1����M�mj��0��mg�$"[��!���df"�W�L��dD�1��=ޭHV�C�lS�#���[�ȧ���ȏ���������y�y-�n~V^�>��uR�����' ���g��k4�Ǿ�'L|B�<C��7�W��{������ͦ�u���b���<zs�c�'�`%HR1}wYQ{�Q\�ӽ��\�Ha>�s|(1�1T�X|'�.�	���{Z߂3�U�i���Y���1��� #�Z�8W�>���ҩl2�㚷����/c�E��������=�5C�,��2���j�.}.z��9�{c��ڲ��T�[�c9N����5��<�72���Nقg`k6P ;��0O!ә�Jʭ�6{�i��k�f��N�aP��5c�U+/�*����H`�F�7���.�$S�8��ʖ+���	8������㙒�4��ce�UC��bjYi���    lz9!u	�S�(��i,��t
Q�_�&��9O��w��f���<�i�Ӡ���R��(��VD�7�:���$�k1o� !��������&��W8\.t�*�^K+�S>�3�����&-�4]z=��`gM���v�����łx�<��\�}�|�����_�{ְ��/�L1�U]�h
�a[�nȝ}�X�'Z��l]Z^E�Bsk����[�ig�p���v�O�l�����āg�[ԟcK�1O�T�r:�����Je�2�x85y2!\��+��N�@�5]U�t�Q�%�#��tg|Ls�A�A�8-�<ۻ=k�i���"+|	K�&��5'UO��,DpS�_<�'��YlJX�e�k@gk�̵"�".��9�H"����h��?�jĺ�c<h��p�Y��dM�^R!�g`�&�\�I�ZT�	��Goΐ�U�]c���b�0S�y;t!�œ���Y4�
�M�z��/b��Z}Q�fzQ��_l��jNX+���кE종6v{(D�Y�t��?NJtSX7�/~pP"0.�}��=�SnM�����6���d5J'�G��7K~{<��5�i���[� V�V���|يZ�s�f�\/�k�<��[��� q�jL�s������I��@�֬��͆����>Y����w�[`1;���Y�P�ݠOf/g�mrk*͵r| +�Uqy���i?c�ۆ2QKKq�6�+�ؼ7���dN�vC��t��[�.�L{��]sJֆT�(4�2"{��c�@�`�xk��>�*5��R�����)#�]i6�2�W�:�ٖ2q��z�*�d�y�����&��<ub'f��^�2�,���6Ch�<��Ax�
����ۚBs��<8�3�0��xj��Z�ӈ �2ǯF
�F�)'�Y�M\e���o)��>[��F�f�\+�)9����uQ�����]\ΆL���M��Y��X�y���ƣHD�y�;"�6������k��7&K�o�[q-_�J|�Y����+x�86�Wȏ%�Ɍ�� ��~��̛�{F�q���LF��7)��<�,�Q�!C~;BeK�P8�wb=t��b2�	�3G����߯��q�4�1�����2 g�Ť�.�axS ;pr����ՙ�Y^r�4<i)���P
�B�0�&���i޳�n*RVU���s߁��H���G�>����c��l��	��?���=�� �T���(d�Lw�����1M�\ᘘ��kf��,���q������ݧ�\�0�?�d��{����U��礍�΄��<'��^��Ҵ�R��G����&�P�=��RӢ�3���V��q�����cځ|s{�T�9+�)		�P�jEX�@���Ţ)�fQ���[,L�2�����H�g#�w�Y*3�E�V�@����9%�k���N91vw��J8�ћ�u���O��1鮪�q��n�7�ǡx�"?4�TA�ͅ��%�Km��h�����H?ށ)sO�lr�1uf�w���Es��o�����q��}g;�c��ҭ�cܙ�}i�_R�b�ہs{Y.ʐ��YL|��1`�D�Re�����\3���1���;pb�Jҟ~�	s]G��_;�vq��(��p(��gz8�3m��\6X4N.!�{h�9����&�#�C[Z���0�������$ZdWa����|�R�o��1��T8�)���t�?�^Z�j�\�:z����ƺB�����WUN䚰����0�Tܔ����94D';�b��̫oW�q�6} ?U��#b.5�fc���
G���;jIڙA'���l���s����TZNI�@��hԠ$� �V����;Dp���|w�9k���56#��8�l���.w��{3Z�Y�%R!�9G�d���U������	����Z됒���d�����Nݍ�!�"�wR�����)L��؈\��bb�|�<LC���3C���`~�5��e���t�N��bCk��К8��l�	;vX.�E';�c��wH�"S5�~����q�|_�x9��Ę��'��j���M_L0�aj�������';Pc��+����%����BA�I��O)�T�-�en�M�����f�Q��L����$J�=&���ф�����	�����[u3�j��2{��X�%�����;5s�-����56�g5�(�CP�d��5a�=�C&�D�'^�����)uU}#�1�v[ͬ';0g���+!��pݜ/Ǫ�fp"�`M�B� s���8���db�5���V�Z��W��yV^�F��*�l��L�3�ڟ:�$��CXgx�q�q�SOs�30��U����~V��=Nv`�\#^�,M�:\���inʓse<yK�klf�����`N���}#A����c�eJ�Ѝe4��ȨLWAs�*��pj�5v�2�g��X������'���LO�(�>=�m�����`@��8=����O���2$ů�P�7n�j���D<�ǡ3��������x�n��䣧=�ΜV]��,��C���P  RH]7�n�GM�ݺ�϶��Ir!�z���:����H�`�+A<�b桨���=���@�>��&R���1�;�,��Jm���P7χV��gl�)r �(�Ր{�$�m�7>ف�s������<v\"���\M%�Ѿc���(QQ8�d�7����Hm��y!��"�o��D��uo�?���ܣu��9U�
U�Ry���>kŽ��';P�����\^�_I���:c���
�7�2M�Ȧ,>{m3���k�TK���E7;P�2�i����Up�K3ݤnU�V�[���5w�dr��߿x�f�k�a}�� ����|.��4����Ⴟ�K����lT��I���°�K �pot)��uJ�[j�caG�_G�8D�K�9j��ˣ�&.sZBR;=P��}�Ƌ:���=bk�'~��ذ�W�d8��
i��^bq.��������bZ&.apul��թbFͰ@�۳C������R�QBy� -�W77�biq�эW����3D���f��o�嵧0hK�Į��6Yӳ��v8"��/dW�K����TȐ��!2��"�榍���Z|���T{�]�Iv��O��g��o�3�M�6(��q��D�۱��k�DEﴈ��=;N�"�-.�5w�8ˆ�w)�E�����j�ptT%��$�ظoh��=���,�p4�s]X�H#L�';0�n�żP���ɫ��lh��ڙ�57��H�i (���j;P���<�-�*� �B"\��Th�2,�\�(��ٳQ<��m��p20o���S쯞����V)��p�dRK�+o�D�q�O��̧��=j��q�]k�AIA��ts-7���dbKMkd�j�P;�s��G��W�����	)�~���J�&��h��%�8�\k:��d��%����RZP�{-\�3U�������;;�h���R[��U9t.�!�����l�|y,΀_�>Ef��^��=�*JL����F
n/��	�Z�Z�.7S��pR�Q��˼O-P����d�?V)ؖ&˜v��)8�n_,�B7�q�#�*/f�*��:)����@���Pa�1�$������Q`����h∋�@,��눂<2�g]�!�S{zw��5�m}�>�VmR�⵶-�yӮdفMu#y� Af+~��)/鏌���X��O&Y+�ˉ����+ƙ�"���F��
f�WH�f���JM���dx�]�F❣��`�,����#�c��OT�Ք%c�5a�-7��V��N�ݝ�͎�`У�G�J�4��zF%ݤr�h ��N��}�~I��_���wMt��_f��Q���';p�n���Lm�zJM`bE�����1���u��&b��*�݁�t���<��K�^�[�gu�L�\��i��Q�i�6�S��(��X�����sD9,�i��,���ۋu��q�,�;��|��L�织��&�R��0ǣ:f}�'�4+�Y�15����f��ow�!�ly��g��C;��؟KdSv��)�ï��&m��e�эDq6�h�/�m�UT0̄���,	�8+ٶ����A��)    +�r����F�uR�p�o�.�%�pj��d
�5��@v�z'/�L�]��w"fP*N)T�J��ͨH����К:��_=��C�Z�}<��<�:j,ʖE���A-3�:�#����EH=���g����4�ڸ���+g�N�U�pb����	�t�	��
.����kmM0�W��Ȼ������������ �6A��@>��*]�Ѳ�C3˽Lt��7kf��kz�����;��	�\r���d��CŜ�!����t�03V*3�7P�^�ж�؁|����^]9�4I=�#��01 '�(c�i[h��Cc	�M�4oa�/��7>�����%�̩��U�����~�%7�%��iw�N��/�k}���	y;� )��n7�S����L^�����J�D���?�H�����M���΄��md�W`!M��nY��S$R���"��	�ezB�� ���:��ߣ��/�B� G���?�ګ%�~0�;��!�ԥ�4bR�Z��1 C��Q�F.�P�x��'A�YC��ۺ�p�2��K�an��n��u��|�`�����ZY��:��\��#úԸ9�cx�6W%���^#��Ugف��2]���PkME�W�fVk4L����\�J����*��1D�L=M��*L�Ǆ�4���LL���Mt&M��T}�b)L`
"����iCx�3��í��r�e5s��Ko�N՝��cD3��^D��1����lR������u�-jf�CTџ�S�fC�9��#�t雕��x�.� +f�w��k�c;U. �Wu��O��A�V-Orpq�-�I��=�6�=���X-��?�݈b����B�E�"d*Fᵅ�#pZ-7��/��B�:��Mh����������p�Ʒ�2�6ytƬ��ت�·׎�L)���x]y��7��@��冏?�5sCo,E����d��T��*�������SR��%V13�"�3�t^b3`�^_~�v��^�
+H���Z�ի�s�����������<	W���kY��^����K��/9���������p�`B���/��c'��gDZxa,�B�\���l�V�� {0�}X��|j�k�J������=�9�zi�q��6��gm-(�E}�3�'x��a9�������z5-:��	�ܻZ2�p����~+'���l�w�()o7,J�-G&�Ƀ[=b���gKձ�b��Ѽ �I���ɺ3p�+kd��ѫ��zH.pL��:*�`������҉�� �3/��C֠�1䘑mk�9k0�N�'Xg���r���*-��(��E(4ȳ��7Xe�8��~��;�����H]�Ҳ�D�A�v�)���b�d'��)��u=~��sϖS�zqG^���m v��~V���s&?��u���&�Fhf؉��.͢K��GH�#9�5#�!�g�zWeₑ"���7rl.�mО5u2�T�U��gd�����Xi��H[{C���� >���l����q�����\�Gی���F�Rv'-�d{��k7A�p��i"�YX-���g��r(���qD�Tn��i�ip�`-������&�0��wY��vwKɱ�	��*'١ܗ�"<xz�+Z����p�+���|hڞ�j9K�Y,������97�L� X��X�����sf�J��U��^�Zjn�Z8,`��b+��,�����|���Lkћ�����x�s��M�7�Yi=kC(��whH�7,��:��b޻ ���MM�K&JXʥ��5d��K!�pB'�A�����0|_Q�kx��R�[cu^��]2���[��&��Ap��)Rn�SH����5��f��	.�f�hw`��p��؝�p#�e�L*G�y��9�Mi��h僣>AHlUM33�6ף*v���xb-��w�;�T������y��v3�,��c]�|*�?9lґa{���8E�/��
��F�ε��^{�y[�%&�R�A� >�����O�[���'�z�i�%&"uŚ����5.a�	����pf\jUS�$�5u��S:6a��R͞��0�C�>bV�����9����{j�,����%����Wv�-:��w���ZY�8���3&$�jqo3{��b��#r��:Q/��|7ș\넩<s,�7����Y"�����Ԓ�]e��YQ��(�`>c-��|#�k�8�H���F�����G
z̍��L��sᇘ��!/��9��ѷ�z�uAM��	�l$��A��*�5%������Y]��m¨��gr�'�#�N$N'�	b��K٨9i���)���nuLsa�jfnb�A��%�l�v�>{ D�c1��N6^t�&�Y=)I ���`��Xg"��y���«�yꑴ��t��UWⷵ��?V�3�V���cՔ<���:.��]{I{���l���}���L�����:��^��/�]��ףgON�d��������}3J�NZiCP�4���1��\ّm-N�݁�.{�y<�kӠ�AE��
�z���fWI2k���;�Ե�>Q���LY���K�K�W�}b�(l��x3]�v���g ȩC�δ�6,�1�]��y܎I�b	'��F�������0��i�H�-W�ew�GG)��R�����8���7��G���=��_�B��Bz	���������[�)g�Ef	��u�n'�6 ��!�+����n��+�2~�c�����X�,	�'\�Uh��CL�����6N�
���I�9P�G������FZ;3ǧ�,<s���!�,��zC�X�6����*y���(��J�����������OZӯ|_�]+Gf)&�$�RC[G\�=�MD?y�v�\=���V������X�	;}`���;�id��<+fF搚w�i����~���i8�_hƢ!�<R%5��~~�K���f�@�6����Z>9=��<2ܙX�(��ݞ:�H7��~6������ �נ^* �6��I�Ã�Sj;�W��ϼѼ��|��x�;���"����N}�!P�M���I҉-?%�v����0��O��ץ�G�!8�pr��b�򝽅M��T[PgD�'���Ծc�b|��"�����>��-37�����|;����I�ŀ��:���F���3&'�
��v�cיwG��h+��1�MD�$���l�&��Տ�GfL�c[��*�R8-5T�4�w��@��:fr6)���g#o��	�/�*5�'�Ꟁ�����@�v�跙7��ܳ���}o��� ��|�\�'|A��e�?&}ZN#&�
���,�xlLo���(���l$8�o�S3�Ǔ�����+�}'��}y�nc�ϝ�'��֦���	��; ��� O�FMg62zy�&���wm�����E��n�$QN��;ʳ��ϴ�>1C�l���Z�<�)��Ѓ䘌��3����Z7|��Q���?��u�_i.~��Y�r<>:"Ew�����u�z	���>ɸ�}�+��g����1շ;����^�Ag����艍w�m��4ƥS{�`�E�v�<�иW�5��u0h#��2�9-��8�n�$]����n.�;4ܹ�l@x�A&�Հ��;~�$�f�'qt��(oh.�q�S���.N��<�OpP�|@�NO>+�-����.���Z��()����5`�<�� �O��*½���o�����/?����b�{6�(c^���ԇO�'�|H2���|��?@\���5�(Έvg�KH���;�3�k��Gs��K8K�� ����͚�Z���1[]���^ɑ9��� � �Z�z�zO�^�3gx�Z��~zw�fw\�K�M-;�*蹴n<�t�n]���Y{��  T�|��K]|�a>PP��w�v��ւ��s�یQ����dq$��EՇ�� &�Hσv��7���Th%���P���'*�7<`;��L�w҂�_��P��GA̪�
-g���MN��6��tQ2ZS�h���@)���4�i2k������/��w�u:D    <�E@�-���^��)��-
��-�I��C5�Gm]�����$�/Z���ao�WD�4 �!�{�]ZG�Z�L�-Z<��:�I�x�; �� �K�i����ǎ�Z�fKL�SB���K: ���Sֵ�<f�ћKJ�I�k��c��9��31 vҥ^T����>�p�N%���]g�%�PT�
)ҩ����ݱ�N;�DOu��Y�D��@�y'x��ҴKN��UPC{2`*BFX:�/;ûV��xB
.gR�+�ϙ0�vx3��=p�!� ��(�]Y����K��n9+n��	�aN�4)�A� ���X�}�0�:���h-p��י�a-�^ڶ��Ў�7�l��ݜ��g_s�7Ǜ���~�R��Oow��:���D��ޑ֝݁��J��ɳ�=OR���(]�c��.7��޲3X��P-��՗.l,H �ٰ�"rp�zl�VX~��O�Z2��7R";^���n6��;��}-�-sK3�6_E��dg�ic9�~k��9�j�yR'Z1S��g����l(�	W�J��j�6c�m&��ړ$����A�` �fC�xlt�,H�E���:�Xr�T;&w�pH�QJD������Vt����7�:#��4 J��(^ݳb�q��Q6d��-���馯i�����r�}!��s>���O�ZLV#Xz닟P!bC����9�A��w6�����E*qo��<�E����`��P�A����s�������7l@����;�ܝ��lB_���8�v��k�3�b|������+'8���n.�}Fɱ �S�eu�.��S�;�-s��|Nc��� {l���R�rkh��f6��� Π-.:����vd�E�<��r��-�E����r"�r�������y� �ǆ�p�d�,r�A~ł,��[tc��s�x6����gE_����c��y�:��*[�!2J����Ir��j����m'�@"`�#1�;(�q�X4`�*D�L(NR�۝kDa�"OPW:K�|���e�0�n�Q�ݯ�b�E��YXvS7�Oᭊn�9.@<6u����;:�͒Sꬱޚ[Zb���>-����'����Äq-\N�%����+�4�=B9�mJ�0B�*��w4������3��� p����iw'�.�	��>dg���F�_Q�ث�[_*��e�#�&VV%Rn�@'��"�$�jʥ� zE�y, "��J�"4���\&�����&jL�ݨ
���c7�Z��sB 
��bPVt��X�:j�z�;�uzr�u�r�oh`&���& �i��x���g�Lm�پov�uEGON��ʪ�Hj���q����1�u:E׉�A���&�W�~B�W/��3�M��$��|,ի��#��� �G��n�+&ʔ!X9�e�z����>�ޱ�V
��	p֚�e7�V3�Z�{�$�mg����&�z~j�q?�ĳ���,�o��ȱ��\������Q��(���8I���Bǉ�w�����XZ�@oT2�5nuj�^)-�<էؑr�ѫVjj�q.b(�p��th��������:s�k���ϵ��A�ߋ��'E�H�K^!�P_�]�j�
(#c
f�\q�:Ө;��PI�8Z��;p�+v��uZ��i�FoU�� I
����M?]{�!�o�r&�������"��F?�
˶pp����_y�cB���	j�nDee&�@Q6��ͷU�,W�mB
��"v&W�B���0�
TskU#O`� P6�H�����ƞT,a�Y�LT����5��:�<��P#��I1�| <eSW��c~ ��y�y;J���8Q�^�kT���P��h0���oE�� hJ��?�G����Td�g3D�bZ.&��x��R�N��A���WPfH1c{�k���6x�R��T-���� �K$Dƌo�f$w ��JX[��)��06�g�œyV�l����&
���^��O"�m�{r?+>�E�*����_�kim=�el�ԍ.���V�A!w��u��{�{Y�`C�j�c,��d�I�ӽt���&]�.t����UΤ���՞�9C�|�ߓ�Gc��;9���u$ț��vW8��J(pR��7����q4< 7iE���ߍ!�u��z�Bd��Pޏ��f5S���F9e�(��e����xW��f8m�N�������{T��Hh��Q
���¢2(?N.�R�n��rr�-߅߸�`�_'˲to۱� WYA2[]_��}�u��T����NRF�`{��0Nh9iuǊ˷�r�ߙ�M8N 2���J-�q��`g���h��3m|43�ٔ�;_�� ,M@��Ԯ ߩ��L�ǝ�sw�h��_�lF��ܠ��Q|�gJt�^��&[���R�v�)�{���7����
�P�= ������wN���p\ �D:�b]��D`6�)?���th�/<E5 ��������H^F:�p݊���@1�Í�#���^COXKp4ܴV���7y��#Fv����i����.�J���ʗ��m�Z�X8��Mi}�P�����ڵu$����"k[�^�l6�"�YV�o(W�8�[1;��8��B!��L��CX]�*y��[ؕ4^��L����Ei=z���͗������yfA�d`�«C���-�G�o�`=�o��?�vR�!/V-m���wD���ܚh�cD��r"���a]tf3��Tc�yqVa��1�{�p�M+[12�\�ؒ�h^"О�<�~�:��pΌo�֎\2��4Ec�#����c��JCN�A�&�s%$��ٞ{`=�|'���w�����d8�K6�)�֗	(���S{3J�%�쬓��⪔0�����>팽>�L�Y��=Q�o�N ���� ��:�:�`�����;�>�A)�	�	:�����ud���p~JX8C*rBI|R���xpϐ�F$ѫ�-�"Ă��_������� ٬��ۙ/?��m��s����a�;l��ԙ+P�����>.-�_cB4(7viN� `�FR��j�FԶY(3��<�_u8�t �a#9���5f��0a�7���7 )l��Ui���!O�v���!5�B\��BMg]�������+������i���Ϯ��R�&�N�
w1�xkw\`#z�u����[&�?=¦ipj[5�:�[��d�Â��!��$
�lJӞ�]�TAѦ�ə�`f�8@t����AX�]���2#�ɬ�{k��j�w�Oe�� �Fua
���a�)��y��"C0�l�|�O	&8�\T���@�D ��U�r����� ��f[m�ٺ1I��P���z6D�����u-�QoR������l�,�]�0D�FR|(ә�ğFi��Z�����)����r)�f�K�`��� ��V�V�qxxz�ݟL�& �Q�X�������/��~b��{y�Zˇ|"�F�Gӛ��ڌ�x�����w��7t�gadH��AP������a�q����:^�R�5�����.��N��a��7+�'�lD{��!�;aB�;���VT��Ք֢�*1E��rO7ݓ�_կNz�|'���o%�3��ji����߭��ܒ�%��G��������"����r��ʳi�Et��.��;��_��4j��^w����T�Y7�ry���Uv�m����@(���H%��̮{8��7�[H��(���i&bOw�
�7C�xx�4�>Y���e�O)�'�(�e����-{��[������'���{1�EP�X����q^�]V�K��u�9���7ZMX<�1S��(+i;���$*��#��w�"��;��X,Z9lX}R1�tM����
L3'|��i����2�.l�S(��YS���/Q񷮣��nTo�֔\s~"��b�VW�<]�`�����^1�ͰMKG±@�ŏ -�OYZM�7�JLVSHU�S��
��&V��:�����~��w�q�ȩU� Onϙ2[� 1���Q&3Td5�saY�iJ���m���7�]��j��$w��%F�,W��L�,�w|>mO�I�S�=��cm=��@��cc˳�T*�-s    �z"��YE����JxK��N�`��WE�e��.>���u��d*�0d�;��O�B�S.&n�q�9j{Om7;b4�բΗ����8#2�a'{;����,*=�>1?�F��2���UZ���Τ*]r��b2˖ͭ.[��`�V�|��,�4�mF �󯄝X
��
D���o�z���n�":������>wmR�gG��,T�T�/���ȸ�Hfu i�b&$>�^B�L\�V�ε��Y������:ƻVC�ߊd���2��eS�D������G�������
kH�����v
� ��W��8�f�s�.���˭)e��F�Kv�-��R��SL0u$?
!��4d�*�eh!l�W(��Of��`��Ж����ef���Bp�T��5		VT�E�G��$y��3	"i��k���A�^�5�x�&�����w):�U������t��Z����(�j���wv@�v0���(7�[&�g������z�!Z&�]8����O�X������8�*�z�Z!$Y3}2�/Ga�O�?q�����J#�W���.��+��h��0
�`�W*���ow��ǻ*��l���ְ-yA���ӈ�&�2�� Cn�������E#'�An2����4o�bE���4{����8�����<��SRb�����[�VA:����E �Eh�ۺƶ���Y�c�^yЊ�A�D��o��z����ĜY'f������r=�� 37hn-{g��P�)����yh��<��߫B~����W�}���Ϲ(T�h��<T�>�n�I��t�#xz ���n�p��̔�xA��jn!���t���_������U�x�4��.y$0���`�ؖ�r��)O]����W�^n!s�w]���X�+������0%������!E\i
�'V���m!r�����Ҵ(� [c[�STu��og+� #�������c��Ǔ�����!�P�	36B� ˰&����j��R�2����zu�"j�����c�LtahH�:GW�T�J�Դ�b/�Su���
�媚ނ���.n#y���?zs����㣣q�����?��Luw�amvv2h���Q��G٣��S��3�io�<'m��u�@M(�������ﰪ��ܩ����^����AN����d��q�o1�TT�/f�����F��-���T�d�I�����5^��I��`xӪ���"F��hA�3B�Ytp���V�:>n�u������ә?���\]w�DcG�']�x{ };x g+�|��>��6@�VN�o��a�:{�a[��=���Q7lzċ�)���ᓅR�q�nL��xXT�iʩ�$>�A�7��8y�R��Fk�Zo_t����YHVw$k��z�ߙ��	�ʫ��|-W��q�!u��,8���^�_�Y�u6i�S*�b�V��p�ۂ�!p�m472B�D.���E���'�z�Wt#K���j�A�5p����C>�l��39*���f/�>��?O�)W<��J��<2kM��"���p�T�{)��₩$>��;�Z'�r: Y�����-�Q�7��5�!昗^����Ӭ��EN���|����1�ӂ�M�)�,ux.8�J�a^�~�ERUg���
g�6 ��1Pn'�fM�l͘��&S�[���F�O?�3���/kdP'��´Ս^���M����ӹ㴳���a�d�@�d^�*W��ǔ�<��;M�
��fqi�F��q[@~?�`�0aG�b}id-hX��g@�G���T����}[�8.ӃsL<U#�-�gǰ1�����r�9�����52�����yΊN�9g��t&�&ϟ�$�Z� �sOae�d�^���+�BG6��Pל��M@��_d�鷏�Irƻ��wL�P̣�"�Y����I㼔�y�fT�,{D|�}�+����˄{��y�^_k��Z�3�M9ظ\f�L�����1�o"�mF2��lRP,�7�T{�~�����@�)'���G��rD�p�"�\�ϋO��i6���"ߵZ�H�� ����员��}P�@� ��L $O�/�]#���ׄ�}Ɉ���[��yJR���rϙV*K��<*zX-�;�!����<�L�3�f���	��,0�%ҭtLBg���(L������5�1P���Ʃ��@Y��pkv�hU�~��ZILѲ�sS�k�h[ī]�����ݙ�[�n��;�|k�vNf���k�<��6a�}A��L��k��su,���J^����jZ|Tm��vù�$yz ����]8�׹�!�j�G`���e�ev\�b?�F(��.��^�w�4-"��4aëDO���x|2 ����t�<�s����.ܫܵ_P�G	O�m"�WH�2��JJ3ͼcj���kzؔ�Q�g�C�	��/SFo�H�_R�Gh���qF����ZRվ�|S�Qz��F�
�O�8��+��kE�`�ߤ�M%rIQA�ù�9�׀�ݱ�w5O�8���Ճ��R|)A���BR%̕4L�����͋�{��	BwY�� *��'��	��!����,����U�e�0g	#NWhZ@��:�Xؖ�1��6�t{�d�1�k�Qr�N��rU�#�%�b�~sN9�W��P$Pc�l$P������2y�g3&t0�w.ˎ�>h��J��[2��B�|�f�&�^��t;V�Abȕ]�#��:�����ED�5�.BD�O�����xm���U��(]���p��-�Kb�{E�������j��T�u���j����z��ټl���ʪ���l��T�C��R�;�z�-x|tD~�3F�6�H�VKg���oïNGk5��������a��5Kv��cQ��~�`����M�?��s���"u�a�d �ōW�e��aB�5�I���a��y#��Gg�����:LN᣺�!�W[�{�f���y4zM�D�kdBgǟa���϶S�.X)��#3�PGt���Ӳ3��#�O�-�	��/	��+��̔\����)0Z�,	��Ct�~�B(�9N@仒�D��=�b�s<�D�g֔R܂j��� r�B���c�aV{�e���hP��A�e[3V���;m2����T��V����V�6._t��^��Hm�z�=vi�3��r3�QtmdZ��Tm��}t�=�v^�������YX�|��_"%���Qkj'�U�h��3�)3��9ӑ ��O�Gڝb����n0�Xj�;{�r[���)��n00N��>�����X� ʞj.}����T�[�'�w-&�A|'͉�F��F�ѭe4j�����keݶx+V���[�p<}��7�)��B�d���Y��j�d�2m6�7Պ;H�q�"$�e�@�`�`iz��5��}�l��˯�c��[��9�/��T>s�B��d�OZ�\�:|ϰy���y{�W0�ȿ�[�q���$i�жCg�mr�LPWY��[�̝�N����&�D mɀd��`�^��?I�Za���w�~]\�ց�=�a��+ᅐz�vu� ~��œ���e��S�$�T<Z.�L��w�Q �M�6� g6��͌�Ko�Yc�&́A'�K��I�h�D�[����VxcP��p��ϼ��\�F@�a=2� ;��)_-h0q�m���cp����
�\���8���AW����q��Da�z�#�$.�����uctvm��I�L#����������Rr�P�wd^��QLKy B��3л���Q�K����fʩ�D��\��]���+Ҹ�5����U���d���}�TAcz$�cF>�@�JDY��B�
X=����W���4�cF�9^��;�<�@�	��d�V�k��'���0(�v�Hn��q��_K�Z��9�|���!��4!����d�8��$�G+�N�xT*����س8~��jU`z.�}����Z8��$�nZ��_kf���a0%�tM�����r�1Ƌ�=��)�8.�祣,pM&��E y႐a%�K1_r�	}?���I�8��r��]��a�
���	�-Ӻ�$������W�c�xH=%    �#��{�	�,j1L �nFG��y�> Jҧ��>���6�cv�AT�(��x�_�M����3-u��m�)m�`A��Lݷ$��0�b� � \a���ϲl�M�X��$�N8I+R�Z�}���ΰ��j��X6�d����CZ<�*�ïM�xZH�#qڋ߆%g鼰sib)�=�d� j<����Y��x�O.6�!	�Ǩ�)�\�{��M΍��~R�.ʂ|GD�;��c��U�g�k��a��>q��[�u7�	Kᝠ'��ߦD\u���H��q}Bt,XwIp��tm�wS�ݫQ3�L��6d�?�E�����*������׏��ų*�c���>�IG6q7�A~�O��.�K��~��4sQ}�O/77I�T��ǜR��%dj��#�l�
���Ol�#F��*6�����Yb+�,��W��č��{�@�1����z�uyGÕaH���Y^�>{`�3 L���_�}{wM�	�*�NoX;��c���P?��c�1�U-/K�r�@wk��®N�&��^ ���D�2a
���
<�a����dƍ���䩝'�9�M��#Ƒo��Au�����l?�4B�A쨊C�Lx�o������<�;�VH�-�>H����$��?�^|�*�7g��KI�sL�k����&6 |����	^{�~<�#��p�����Bߓ�ܛ-���h0�a�x�������'�ңӞK������x���K�c�j��Q�`�a ��8��	Mh㭖3��a�	����8��|�*�Q����	xz' JAsf�5[2�t�X����T=h.��&ԡT��?A�G��`>Ad$�Iح{���)�(񩧠�{\��̘ ���yT�
���ڢ+�	��HmZ�v��e�0(���C�[<�6Tԯ$�b��R|��HY#��k7�t��@���%�"���<�qr|49���:�`@�-0�ka"P@����\�K�Ş �G��F�s?N#�T���@f}xEX�N���J*��\rŚ}��c)&&WS0����xXw��RqL��%�!th��(�r��t����6�t�2,_#�@���)�	Į�*�|M�4*|��G<ʵ|H��)Ĥ��\��ty�b<�p�@������y���� u�<BQ���\����lD0�Z�5�Ml����k����g!����0���:X-��s���i���l�4l��!b+
V^óD'���`m��>��Y��2>�E����i^!��� h����8z�,���Cy�)MbEDûC_���l����"�f��^8Ţg*|��='=��_����G��M�^�w��	�L���x��Sn��qG9���߯���(t���sQ��=Խ]���i�e
�P��~�J'_a�^$�B���`�$ԢV��v��
�Ї�<93E������i�]	iwQ������Iq0���7�H��
�$�ߦ%�t�f����d$|1񂡢/W�^��9��|����@����r=�� ס�f�̥��v��
k�e�C3�yU�y�Z���
��L�����e��,g�|���-+�i�T�T0�����D��r���Y^��ЍbC���=�ݰzj!�����:ڍ��S���Aw��_�f��k�Н�#g�c����?}����g���b�Mc�Wd��A�?Mk�'n���G$v�
�3m�&h�[�"�6�b=ɫ!�ή�f^�z��5�=���d�����K�2�T� w�c{���`ź�a��iB��*�_����2*�3y�����a�-@`���	utu�� JhR* ��2������,ʢу���u��o3]�79���[%��v����B+j̈�N��a�{to�1|�*d��YE��q��v'���t�h?ڂ�M�����`o�*�F��SD?#\2�~ߨ���8cJD�p|�����l%]p��y� ;���B�z��`��'m�:CV��D11~�Π���{Xr��K8z�%�`�Ö��&��^�:���j�׼�v=\�x��	=�Q��`0NXu�<�#�P���^��":�hERq�CM�$��d�w�	uK��9���=Ҿ�V��T=ϧ�����McE05���;�D2���8A��{�(��ռE=�"�ԏi���{M/�E��W8ӛ�V\!��xV�U���e����0�}�Y��+,�w��{`�O%�`��e 鰙oc��~Ml�oX�����'��t*��2��U�K�Gw��s��,z$�z�W�	.��l1++��+imw��=K���"C��g�1��Z�Sn����F2�ie�)���b��,2a�މM�E�J!�5���R��P�ZO�����2ͨ*��� �F��&�LB6�cjZ���J1�%���H��7�Ke�,�S~O��&��}lu"E� � �Ҧ-�����wcQ_TSR�B�u>��L�f�y����#���@��<`���U8��l���y�	m�b:�ё^�>���Ƌzg�aVӴXу���7����> |��^kaj�������1�0�xB��0N��L�*D��"�!j'W5%�YL���n[����)X:�^����:+���S/�[�[l!{�`G�g5ȆZUm*�h��#��}LԴv�Rs8��4�l>�6�!����V���H��|�����'�KI/]�R��',� ��_IJWp�əc���z�5���'�?r1�Ǌ���A�%R�)���PH���S��8x�&γ.�}�*'dԔDJ�����ô��bL���bD�,!��Ԗ*�Y�~�?E�S���#m�+w�u_[�µ!�G�����y�<�v�^3�N�q������I���X_#	h��y��l�,��7U���kc�*�;O��9$ =�K��.VU��#�=ܡ~AC�ԥ����8}�.q$��zT������i.��|$a��{xC���p��؇�[�����1/�2�3��fl(4�k�'|0��U��ΰZ�Vw�+�H��+�u��n���_��>��%��͗����W��&c�)3��u�ҏq���o�3ړy����{8Mkvx��"�Vce�MCÎ�Vw�tŎ���i�a�f�X�6|�&V�s0/�^z����V�Sf�z���� �,Pl�����fX����2Z���<�m�O�_�pf����\OKn�T+�����2���(���?U���뤠Gu�JA��
�$y���6�����Q�����}g<�FV��W��������C2���-�*���}�5nU��O+3�o��8٪�0�+ �-.�X9MgAWK�m�������,z��A����z_Z��3~�VT.��Կ��1��H�A�6�ϔ���+��uSA���,1����e^d��%��a �����(ѻ��Ɂ,�S�,�P�r�5�p�]�6Pp���Z!��1<�"9�,M��a=���!�5R㷽׿�'�[�a���d�X�m����.iH3VPL��i��@U�M�Ӈi��&љ��K!��A�JtOaｮʹ��95�=���n�G3`�^I���E�L>p&Zj�$���Í�%\*���W����?�M]���h�"Д�U	�1$�Yˎr�N�m��	�61�� �M�xq�g����p"����U-��(g��������i����2�Ƽ���w�~�9�1W5t?�Ϯ�R������
dbZSi�����DAf�رR=I��W�nn��uD�Wդ���� h�-7%��z��4<abEX{X��=�fq���������E�f�#�L��s��+�W���o�q�+�n���R�_����	傰ȫ��^�B�LAGze����֣2'���q�Js���b/��N�ZqY����� �G�	r�� #�C$�/=T`��@�<�qޅ�����%	���R��m�Y�ro�������-��C�a�׊�2�҃�k�Ɇr��R~�^/=�淸�hg|�)����6�t|�>^j��TX/S�cvǠ��3İV+�@%x ij/�7X��ݴ�4L�b�*�;����|��=��me�TLo$&�)��nE�b�  A�^�,K7D�    X���nG��  ��t�6�l�N�}��M57%�F���cުR��o�����p���C�����
������-����x>ŕ+�<H\�+����B�w+�Y�uɻAk������}���b��0�A8r ���[�M ����v�>=����1ÿc$;�4��ƕ�Q��F���=T�A��������1������ӷ�R8��� M>Z7j}����~��-���2y�C��Ǩ�)۫s�)��Q�e��׮�'�
�K��Ǜ�H���6��r�.�9���Dg���c����ԉ�M\�9ƥ�q�^f&�k�l���W�EۄenacnP�@<T�q���Mա;�65L.��U���^3o*k/���wmޥ��i�P�ީ�{�'��x��j���Xn�x�ڞ��T�b$\f[� �T��E�C���Rp��Yv���}�����E��.�+���\�. �_�ʖ\q��(�����@�����M��'��U�x�}��oϓK7j���)�`�`��@s��z�<�nL�M2�t�rS������p��&bf����&^��
W��٭}-R�dn�����4�ޤ�aSS�pϚ��֔���Y��Svr��r�c��vn+�[��m:��|ap�8$�n����ɜ����V�R�L�ɐ`�9����	N7���>w�H��=*�Ҋ)���68���O/:�k3�ې��P�]U)�O���{�<Ĕ;��~��8��:n>GR�i�"P9v������n��81�^kT�I�x�=*V��f ���>��n���R�>*^��ͭ�n�I��]�[���SYrʞ�R~(W�G�Vn�����?���_bW>ϋqsy���.
1��́�b�����$�׉����P���-}������[lPkJ��t��q�d����K�+�V�N�:DD��0FK:���3�
� �b
�@T3]�,t!��pΒ#Bl���h���t���D=I��2�1���S�N�ן��^R�Ϗ�g��N���ҵ�x�	���� K^ǠF�>;��I9�c�Af���"��\U��`�#`9�%��C�?�e(nXޣϯ[�=���y��l�bj�L8��q������ٗU��7�I��)�1�E�~:I�w���3���W�z��*�I���`d�Tt��gn T%"���_�����f�d/<��*煲���^6ԟu�8$b[�nfϮI���L+M��j�ax���1�6�{�gJS��"��d0-٢\L�EC�٨$@�N{�K5{��0nt� ���4�-u�E� @Gl�h��v�|-�9���//��\=��x␨FT�oD}���>͵x��-�3�)F#�]�~ �""_�	j;d��gP����CZ�S�͉l{�FϞ���5�q 8cqm׸9�ވ5�&�x��bM(QkT�nc�$[�Au #�Wm~/[	���T��4B��6�G��f�>��Vu�<�
O��3"�J���r��R��{M#�x�9�ѱ�#\�׮۲j�����F{��P��: 
5#�����1��
�.���V��Oψyf*{���\tn-0L�=W��]0s��ûz�)>;0-���B��������{�jאؙ��k�,!��24��8I2��|,��
]Z�[���j4�J*T��=aH$#�����e��w��H�٣�$gm�"�KK�C��)M�+�Ա�X��ߐ�EDD�v�iVP�H�6����l�]�h�6fU��C��2�]\;�#@���x���틹!��؍����~��00M�-����6��MZL����%z�D�ڠcO�0w�N\��`)ߠ�ݐ��A@s >/�ʔ2AA�� �����wwe�)L|z��r>'������+u�a�(&wq�9#pO^)�u:�����/r�t9w���83S̐��4�Rƙ�ϭ����Tf�����W�¦b��UC��� &��&����-�tV>b�Mn˿�?�F����r{p�6ce��Ji9fv�+m9�p`6\� }y�O���D���4ߜ�i��r,@�#�F�Up���r�k��t���v-���Fw�0SmJ
�Eq��s�'�>��/��΄��Ѯ��Ç͋12e٩��b���������pl���������8�So.k[�2��}$H���2�vjÕ��Xw�G�,�m��;{8<�?�{������D��۟]�E/����𱫂nr�}O��"6�uPh�*��U��)sf��8�rA��(�p]�-��k�L9%~R8�!ފ�(��	����ۡ�U��*�R���ۧ>͑j��o�s�����mi��DG���<���I���}<�,U6�W�H�$U���׾�2X�n�#F}gT��h73|�Vd	�YVA�#'��߰�Tz4���"H�y����U��,{��YLFBxb�/��D��㄰RSO��a
��[� �M̏��B���'�[��,�����W"����� �fa�ϑ���B�;H�jE��U��o��nʲ��_P��efG?�������Oe��J�U������ͼD� h�:�#�s9�����s�F����-~�k��>ӆ�͡3z��S��D�.㚨�؃\Ol��%�/wF�M�pR����u08���`�?X�f�Ȝ������Bk���)<T����S���MՈ�==�����B�!{m�i�T����A!�W	a��[l"7S2'*�R	0>��y�:%���#N�Ve�t�{z4�I�;�'�o�r�Ke!c��Tk�]Q3v���'�u�e*��B����ɓ�������ǆBUCw��T��1�MJ�m/�?G��q�T4\��(=J�ǂ%3fӤDz�ޓnR�u��ȓ���锲ݒ����%V[�Ρ=e���_xH7_Yz0r┟-, ��<�z/h$��k�V�w�3S�b�%;9�28�~�� nE����\�Y��ߝ���	���3�f?(��B �U�F$ȱ����ֲ8�q����qN�8�zB���g�L��Q~���v��� oO|93�:��V�4�J�w�z~:����,��������M�0�L4��^,�)��QEbztJq=1��ʥ[�ӣ�oG�R�`����M;%J X ��5��V�
dQ�2��O��<��b����7'0�����Y9�<��-�> �=5q�DY��a$�"�pP��S�,��"��d8�̱Tč��6Y!d���,�ϼR@�vn��W�Չ��<��k���6�d����~��B��3�x�A��,7l���ވ}i��ޑ�
�d̿��_UY��-5�"&b�����*+��ɓn v^�_�����l�{9��
2d���(J�u���q�d{t�p�8q.kd�EP�mF*L��xS<��qD��͐��<T^�=�:n�!���A*��}ί�$��a0�~��_�?��U����.t�,(?(f�ba���ԙ"ǧ�d�=��5oVj3�ă�ʻ�G�ŕ����#�)���m&���M&s�^,(:J�r4Z�Оx�*{�TVk�SP����!���H~0rO�'�O�[rd�7���kMb4�~�'ǃ���z�̠�GR���|��-Q�*���m�6�Od9�]q�#:'��S��ˊ;�h�ٷͨ���ߤu%�`\%c�[~�� ��ǥ���7Wd��IQSD�մ�ۨ�S�2��uv�(n��^o]u����Q�uWu\WȲ�P�m�����6C٨W�0����x�|$S��4�v/K��bg���y�w<��u�q�O>�A8R��Դ�n�BՕ�֤[b�� �T��󃭶��$�^6�n�ZI���^����մ��ژ��F�9T�F�p�~Q���=�-��e���	d�π�M�9�L U�wSK��o_}��|r_.L=�ŦB,Ʀػ�K�z��$��&~��	b��z�'3MZ��.���j��0���X9�f�T��O{����t�R�i-�D�◔��Ǽ��N$�ff�����)`�w˱��&f1vs��x�$u��>GaW���VN<�@�]yn�	;MM�$[/ �Z�<�S    ���u9 ���8L�\��(�D�"�f��Wt�!�_��N��[;=f�d_`?��p�<��\��ck[ė����=�c .�9@����V�@�	Y������P���$E��@�Z�׵K~�{���Ȭ���L����|�[	R"�=��O!��N�����­!�%�(q��X}�/ y�����&���Q��'���嘃$K�O|Y6"%�6���2o��'9�Z�`��,�F�;\��6q
\̤��������~qlh���5i�dE�M��̄;󹨨��ö3��(c��y &�E�0�.��B6(�e���T���$ �{��1���� �V�g��Q��8�����r����N��ef��_И���t�/gMsP���x �穑Q���#�D-TUHܧ`�&!T�:"�=�W����a�S��1\L�R
�sQ�!��XW���m����M��|.�;���bf}�Nj�k���B��1�����J����R ��L {f'�n��{�Z�mǷ������
า���턄��<�0�co��Ы������:�ʩE�c8�~��.�����V�P�Ϋ��ͥ�/Z��<��&QG ���Iϙ#��q���Ae7��Ą����1��?Fml�d).2/�G����`�C�8)}r�V���[3�j�S���Zެ*o��r��;�EFZ�u��*���m��P�,�N�B�Sk*'�)�����p�&�/��f��a��>eq������ٚ�B]/9H}�W8o��۾ ���O ���[���G���[A�H=�W�xWL��P���4p��w�?�� ��t��E4��y7����oX��D>��J�&���O��L�YQ��8�Ѯj���=���:�M}�����fA���A�ބ;�s��6������	}�Sk�jS�>��`G]8��/�J�4"�����ju�j���܉ �4[�V_ �4Z�N;j���@�5�(�J�gT�|�KV�_|���ZbJ�3^Ӽʂ��H�]��S���'�'��}��n�Bt-~�[s.��y}a���>9�b^�	���]Tk���pEN�2T�x��lNk�|a�n��r_���zĂm.RY3y�y����}̽�Z;ʹ)���S�b�x\��Z5�]����l���ȩ3�"�/sO�8u4򟵽�=���j�T�lS��AXi�_�5"�U/��j��5���`P��ׅ c�߮ie���P��A	J����'f�t�w�;VqKU7M5���@�UΞ,���J��5�)Ї���)F0������>�
���s�w�m�F��3����TRRX�DY���n� �l���bLo#�t7���Yf;�s�����(a�p:»�G�v�K< ����UX�f:7���&�3ɶ˟kg�) ���b\���2��X9�R8wӰ�A�������{3a]����WQY��5��h����TT��,�e�r�|B�"�\�8�����W���--נP���ݺ�� ]��%;�:E�3��>��mC���Yf�2HX���ͅ��n-�ɾ-`pT�	��S���`	<��f	?�uOq���M�A�s=p� ��K\s��;	 �B�+�� }kn������acYUTӌzopňfNb���v���VXpF�[��� ���Ho�ԀC�5����
�C�-�_&EI��5br�3<�Ym�q}��l���^,C�~GU5c��`�[�jq��"��� M�Ĵ�̭�r����F�Y]� �u�*i��?1��d[���'�$~�U��*�SsC�%��-K�=��l�V�O��w������yG��p��I$~_F�������쒉���65�޿2q��R��%D{���jk>#��įV���ɔ�~�r�G�Q{F��=	7ّ�l`�$���U]İ�������CO�_w�."�<o�`l�'��mf�բ�V.Ja۫�a��I���X���&PX�e;v�w��!����{�}�=g�f�aM�~�����q&G�7���6#�s�<�>�Ťh��S�lO
�d�x�w�[�s���j�PY��݆�Av�)T��3mS��f�w49�	O���AU�\?��*G�Dl'1��n�,� ����	��� pИ8?�
��:��gUi������B=�y�a&3���|��ǐ�<��v�@h�9���V�d�1�V�_��T,�ejXTS��X��͘%6+�W������h�ҍ�Tj�5n3N�>'ސǶ�5.�c��7s��H6ʰ����>��I�gs)�E揑x^4�Y���E��u�9ˊ���Dv�xU�,%���'��+œ-'��T>�-�?���Ƹ&�*<�r,�#� ��zͪ����rM��m#�@`���q�ZMU��a)R�u���?��T��AjY�]�\���q
���)��5�Ԕ���������Qd�ֻ��XY^j8���A	�M�S�/�y�=��XTs�yߢ��e�_q�i�d4�*+1I¼��s�{"���蛊e9���${���������C�<VU}���|�$%_s�1��k�I�S�ʛ��e+��i����9���G0�����x�"�(*��^���rJ�0��X/*��=|��h2�Ҭg(\˅h��\��z�*����.c�#�x)�u�A��9�Z�jf���Y�ߩS���3��w	������`k�A��Ɂn>������h�j!�r�I�����kl����v벱{fR�q�|�'\/�sm-bA�0]@*��F��^��n��dwN~y�> (�#���I��n-9B�.�@z�V ΍���3xK͘	�(�k���j�I;/�|��{N�|P,�
s'n(�|�9n�ÊO�i��Rۋ�$5�ew�wĻM�\/�vT#X.��J�̘-�$g2���^Ί�EM���gĢ<��U�ղ�&M� զ���-�g�ւ��8M߇���oK���Uu�.u1�����,W��~d!�ZmyF."��S�23�p0�I�.$��
ݫ�nwb}�8p��r�L 1��� N�t���xE�����~�>��g���lW8�{;�N��&_p�G��gz �.�} ���,��y8���<
�T���.\j/1���q�Z6�d3�RݝTʲb�w����w~r�2a�S�Zb��{�I�Y�����Gጂ\���s�&���%�.����~��GX�wiS؉sq��U��	8��r��(f4w���$�D"��UeC��3X��@�&���/��AQx����$��l�}a�-���c6A�C�J5�[k�-D�����b���p$�u��M
�)d1�;t��`�C9�涹�.WZ��L��T��eŭ�!��t�Bfy&�d�v.F� �c]�"ӲF�校�#�g��n(���p!�)���\�f�z���<����`(��]i,}rP�'�b�wnN��vL�I �5!�=�d�����J_�����*`� S�AF����`K�.U7�ev_T,��ՁL��D���%��8����e'F^�\�b��4Zp���	L Q����<��vE2$�3n�5��i��i[kk�����4.|�;E� H�Qg�`:�l�=��K��ډ1��=���c��s�T�0���O�+0�ǉ�T�+����\!k��qM��xl�'fb���r�-z\�}і�h^W`�Y�0�,k��/tkR�(BZK�Dϴ��[��'.l��pxe�̳ʙ�@n'�{�L��p�is�DT	�먨+�ڢ�4N��*c��u@{�����	�U�?P� �M'����K?�Ŭ�M�F�؉e+ZYC5^�2��˱w�����^����Z(k�3D@��A���^���ބA�����,��I�uڃ|G�W3�y�������c���ĸP�����=�Kx7a�p&}��U~��|<����k��E1��[
L�����ץ�&C8�c����T&��dO]ab�2/@��\L�W��׮��-�zuS�.
�H���Qk����7�?�Ѹlg<u�mW�Ø �  $b��ӯ$~�'�{�o�i�p��g���r�av�&�/:��=�]���ת�^��&z����^'$wa���Ѻ�ؖ�{D��嬦g<Ŵ4����x��u.B�4l3�b
1�4�#Dz;� ��V��Ŝ�yrW/��!:�d��M'�����ˮ����\�DH]q�2�o�IY���p�Z.=k�:�ͬ�7�j
vWP��0t�*yT����+F��	F�lj3�j��'�_R�9��e�9<��S�R��3�ώ6�o�6|����g�߁kM�>�x�2�虓X�Y�F@�bnV���W#_�s��eR9�~	�BM�!P�Ww�y�|O𼥢m��#Et��6����^)�..�v�U.��jh����'%.�������>��g$Z�6XC�ݓ�k��(d�g]@m	������������_���o^��1̘,El�~¿����vK��}�<n��zۃ�MQ��O�}���ήMo~2�[���}햣�� ����֍��FK��<I�<�J�mL����ٹY��qgNL����ys�uJग़�Ӑ�KN���-L�0��Ju�ng��%Eݶ�RTaK���qT����P�íIG�ٽ��t|��/,������T�A�L����cmg/���W�fz��R�?R9T�����g��f7�^�����õ4�w����-唩V�ڦ�>ᶣ�l������\��6�x)�e��y.CSG�Ξmm��q�Ww�Jq�:�m���������<�'N&v&N��W�������s���Y���:��@�T�~��Z20��x6��oK��[K*NA$A^� ��j�D�ILx���Zғ`�}Y-1��^�ٛ�w5%��~+R-|ōR��!�?�=��+s�اJi�M����=���W7������wP���>��O1[L�V���B{^^]�����o=8����|g��Y��3�k;�+d����:\�������l�S���ˆ��@�ߕ��%��g��e���[���i��~��G�����Z����@s�ܵ�T���5�����4po�^�#��I�_�Dj����[nTs`�S)$��:z��]������M�m�6e����v`_���q=r�ڪ��M�yYa��N*�uc?��������72�V���Z�f+K���d��3�;ȏ�:��C)��go�m+�1����Xû�_L�o2�������� ́��!2�}Bg�i]-���1��k���QO�T���nҼC�P��C���?zxA;&xŹ�r5[%���T�)@:�;O�9'H�[T�:;~��`X԰�~O΅S.���2#�I~S.���7�|��$N����hURNK�� l#�O~k^ڽx���J�k)E�LH���.�G�}�R�<�����q��M�7���y�b'*�5w�j����2��O�75N�q�Λ������� ���BC���
l�S`C���Ȭ4p��N�6�(^�
}T�Ր�YO��:�\�ݘ��-�uO2X㑓�����#�V{M��]t��J���q�\Vq=�����Qla��wN <�yc��m�#im���?]�ٗ��f��"��0j�)nKju��R�_ۈ�H�8PqP�)�n�Ag�M	6bbѫ0C��\Aqan�y�Ī{��2M�>��+��^?w˘�h�g5N��#$Y�F�,d�� Y�{��6�:�z�s���xԾ�����4�+��ȡ��*Jx���Y����lQ�R�M�&�l����ϗ�����͌Y���0o��6�3DS�U^m#xR�RW>���kq�o�cX��KA7��R�
s�~U���l��J����"a��<쿅f�ŧ�E(]~�}^��(���:y� �Nd ;guX����5%�&u�L ���r�[���d7V�́D�5�|-�(*)�ӛ������������ȓ9��C�Æ����{��P�9Y�MC�Q�8��9������Uv&�i��!��X|���%:'�r&2��%k�»��MQY�G�=ӿJ��U�8��Ԑ��uʭCX�&�Q=r��;�����\} �%��DȌ21$�$@(����#?D$����*U��q�;���'B_�m5�4��u�s���Fq��	�p�8N�ږ��1��#��F^�q-�V��Ej���e��/ˑ�]N�f�c���
���X܌�A���Ԁ�21�Ά���� �P>uSd�����g������|�
O��*����	��a��18Ѓ7�F9��JH)"Y�G��j��Q�Gx�� e%���vCc�[��q4-�1�Y�ݜ�������$�eC4�$��������V��
���=	�v����o`���:?��cl�1�>&�AK��EO�
����+cr�Tyj"8�֙x�j��}ȵS�O��`܉�ǖ���BN���s�=�*p��9��*�[���ٰ�&5�=�f_.v@\��p&G���R�u��.D���<�ЎwC_��w�5�\����ܗ$*Sp*�FֻWp@��K*[��%�.���
l�㮻̊�a�:��8#yD"���#��>�����:��LCc�I<r^��T0iT_�UmK��$��D���б<b^��՚L^t&�cLw*5С㲆
���jd���M����9�>�cN�D'&��/H�a��9M���~_�J��(y���J,������*�e$��c �cyb�
M�Rq���t5�t�ަdZ[h�M�Λ����5u��0�]^䋑����[�<���>�|��ꀧy:��u�AΌ�7�ν������@��O�E*����e.Bc��Dz���v�Z�턾�U[�u��Ԓ``K�g�4�iv�6���tt���`�����tt���]�͓o�.��\vM�j�����e�fP�S0�7���� m�f��[�5����x�b��;:	��m�fE~iz�*�����y&�R�5E�]c�@.�𱸇���W����dB���:���ڒ�+�]��S��r�P�m �U��U�Hu��"���~�ut� h>�)����ܰ�~`���՞o�W���������Q�qP>���ow�ZV��R�l݌�vt1S�WHn�a1���b�.��tt��(\�
�BC?��Ow���E?��]��7��d�S(ξ�R!p<HB )�P�FM6utuPW>��it�RW��M�0��>�;�|�:���h�0���D�?`�ٺ�w��
��P�=�����h�~�} ��:k�������O�F(9&      B   =  x�M��N1E��W�
�BM�,[hU$*!Zvl܌;c�q�<*��qg��Ҿ����Ȭ(�tAGJ]�ҙ$X�j"��s��r�O%�PJ06��CN�z���o01��8��f#�[����93%�i;S��ґ�^�S�sU�C�G�+ݫ�x��o�0[L�n].��ҬQ~X����8V�����q�=��نP��5])b�'Z�G)gtz�����G��S%�C��L���Cs;5���<ؑ���:�v�}}w���@�%�b)��ag��o�\+O.t]�%�s�%u����~�]�cDI�������pҨ	�� ��q�h      D      x��}[s�H��3�+�4!G�v�;�(�rY�VY-�\�����)�P��\�_�疙' 嚍���x�L$y9�����y�]���C�Y|lw����2���v�ׯ��[-ζ��u�퀐D����O���ݾ}�-.���ah�]��g���?6;�s��(��^��n�*�վ߿>��~i7��S�������}�}X4���{��֦Qݴ�M����y����x/��������IO�C��Rq���ER�����^�m�f כ;~ R]C�@�Y\5���=%�>�þ�t�f26ܚ�yt/E~�vm�k8����>7Ë��װ�����T��3���~q��������W"��?�{w����n�g*��ǟ~O������8�I>�����[�k��Y��[�s��1��?��EW0��k6��m�iW������oy�op���"��ݷ��զ�s�-�4�.�R��L��&zc[T��~�n�8#�oC����:�eh��#�%��a-n�U?�w! ����n5t���/��u�H��l}��[�t;�����'�ah���a�q��}(|���!�'�V�o`
W0E���?�r�|���S?�����\�v���I�E��2�z�����߫��v������%�� 5�	~;���as���~ϟZ6@��q�!&���z6�>���v�j�b������w? Ti��V70�M��g���d�ʧf�/� 864Dn^$Q�G����	+����[�+#|��]�k��>�Y����Ӟ�ɳ>�� �0�O��	��O^B��8�Xۧ䰩���`�)��w;<�/�a�w�����(���2W�6,�㋴����/�?����v��WYwoҪ��Q�n�3��s�?�[�\������}ګ~����b]��=�BڨE�08����c�Y�����I�����-}����쩏����-!S�^��=��� �Ù�jw;B��c�=����{�n��s�ts/���]%��̕*'>�ʙ{i�l���58��u�j{,.��+3�x����p@7ppx�Б�?��5���E���� 1	,���K
G��d?���e~�������Ց��wu����
V�~�����J���̺�����}���^:8���2:�v���I�o}�����l�-M��E;pq	7ߴ���H��>�e�t\�����t����g8����i����Cs���ߛ++��|��v����p�LSҹ&�;���3�0=7-_����Y������
�������Oy��+���h�|�^��,	�7C:J��{?t�d��h��=����q0o@b8[�:�:���t��wrU��!��9�����d?�\���}s���U��M��#�݉_�-�~�&��~L�X�˞}X>��G��w�a�Æ���nV<��&��8�:9J��:3�R�D��I��e��I/��߫韱��͝C�F3�3���p��?	+'/rŴ��~o�$�^�g�0�aCww�#�pm�_��B`'�r�7h��ݱ4/Ӕj�	<n�/z�0��v�q �mDb�������E�D��1X��������3��j�3u��l�w��S�Y��R�۝5��T�i�4+dS�"8NJ�NT'����n����=��{�L�ANf>����7�ɛ��m�{�����O��w'4������c�'���W�f�u;�(�DL�U�������˝4W����V�KC~+��ћ��U������G��60�[y��.ǯ�,���!$�Q�05qx6}��K�~�o�ի����"�hK�4r]/�j���wX Dޛ_�K��N�_]��A���&O�޲�_�K��샎�A�z�=�w�ZV2��Ba��m�lqE 陣�Pe����i����
��jux�1@��m���nj��:��ܑ����4��t�.�Z(_]��8"�Gp��^��L ��j�hS����"'b���
�I�L/z�	����C��ks����1��D��7����,�~���-,I�n��}���Ӣ�Z�˖2&�o�������؍�X���7�&�[��N��?����3�;!g�7f��������P��\�۝�_�"*Q�.°{�yX閝^�D�Y]��j���l6�Cj7�����|�N	8f�<�ߙ�L�d�>�*U�s�v�Ae��� ��N���p�w/���V(k�1\��N��2���f\9�H&��������	u��Y��:���-s����X,��{l��"�A1*?:z���QV#j��'��#��>���-��O�WQH��҅,� �F��T #�#{G�kݎA(Q۝ħ�L	��ٻ`a�����V����!��%c�2��,CM���]h?�\]߾��!.��yGN��:��J�T�7����+VOqrus-��4;��t�
�y�B�V����C���z����B��pj6�z�'<1��E�w`=N/��D>�����Q��c�mj(h�ڡ��]��D��hb�)i�H��������>B[�?<<������J�T�nX\h��_A
b-���"���d�����5�C;RB3�4TeGbJ}�c �_Uu/N>�X�_9�*�R/���W����]?<#�o�(�7����o�������������tx!Q7(},�����I	q��Oy���ک�ч�j�?`~��+��W�e�'��qO�`�A�VV'Hn�^�ͦG�_���B��
>�y��oh�6u&"��V�y72Q�k5�un��������}�7C��۷2~��ŀd��߉wǃF|�}���Í�Zμ�~q{�I�3��	l@������w���H�y;	>�ޱvԤ�nh�_��;�o��۱V��m6���'�x��
oq����dk�%����޳*�}
w>� �el_���_��q��X��ZT%n�k�p�@���_�?<���!�d%a�y�{���i��!��s�ّ��[x�a3�ЙT��J������I�1��r����V�������k����������A&��c �%]���F?� ��GU�FH��֚<�-�I<�9ZJ4�%<�4v*":��F� Q�d���r���Na�C�gǨ<�^���Z�LR�d�6�d)ʙ�vcE�ߞw��;<���7=��9?�!������f�K�!/�E�v33-�,E�}�w��;�k�Bk�߃��Ӵ�S��;B����D�S�S�R�wL�$�ҿ��j���kh�G!owB�.�v}�"&]��}��8G���\��ݐ�'���������Q��oV�]������u�x�!�ѱ�����@Utۯ:���]���:��,�)�Ȗ��}����lO�� �!V��m�$��5W�����|Խ.>�s'�O 2�Z���rך�9�������w�9�F<Oƽ��2�lG�.��M=�'z�'V���&a�|�~Nf�p����9�����ֽ� {H�r��ߓ�+m'fW��!O�>8�0	�f��'�%��|7}�6�#j���������B�22�ۼ
�NPw�9���	{)b�l��LM���۔�I�nE%�öS�g��͕^� �&En=�&d[B +��z�rvr��}�*m?��g����7tJS����)���u^.-X��(.�f�1�u��:���,���~ gE��ڇy�%�f�9uV$Q*�o	;�̍w�E�K�HE�{����aE�	��ԏ()+Q� U���ϋ}O�9�RC@�w{��#��H3�c���z�b����6H���Nz ���DN����p��W�HY�kz���p�/��	�C�1n?�7�n=X�t���o[����!aJ�-|�J.疄tRv��ŧnK�J�:!w����,L���~R���(�����w^� Y�[�E�\V�d�vx�]��BO�+��A����5�Yg�W��ͻ�$�[�CÇ��f,L.f��8���3���Z�"ǋ��U$����Q��������'y����r}l�Ha�F�cZ]� ��D?'Vr2JB;�:H�4�ܮ����%x��
9��pz�)�k(e*Ϧ��A��uZF�VJkOA�a���W��|�rB�    �n��y��P�2r���t��ܮ`�t;�%�+<��och���b|��.5���p�tt�{@B�����-�)Zt&t�{rs~�Z���p����0�6BL�J�%B�_խ	$U2W�V�[{�Sg�Ab��o��K��$H}:����p���*D
�j��`v�=~��C&������'5O�o͟n1�˾���E_:X�������36�	!T�6�]D)#9MX�a���	�G$p���_aV;��x�g�O��iy�N�H������o�z�S�ZO�����^����$��6d�"�o��B]���	�k�v��7���	��dG��נ2{� �=���֋�wsy�jH�"{���`Ꞔ�V�:AE{�]9����.A-�a�nt9_�/�Pg9�U�ÎnWp��-SG��vʉ��G���v�)�&��Њ�i�/G��.eTƎ>6�3�y��ߎB�~�F��m<J4CJ+��=���<�(��a��e�u:�u��E�l��v8���� .f��LENV�������{��*:��>�����/�Y2P�]}y�m�9�gҤ`A�����M{���Q��%������w����&#X"�#�
�Z�t�rh�ĸ��].����`K(�A
���f�O��o���s�D��f�	R�v���4;N0��fÖY�s'�J��=�
��:�@Yf�pD<��ne�O��rQ��-�}�{(Z��H���$&� ��M��P�ߐO��h�F��|7_�'j�-��0�4!$���.�\����)�K�n��(�?��!@�?����N�[Q��;WK��[FV� $��2���wd$TG�7۽2n]���$ K�I7Rl���>7�����(Dh���"9 �Jqk�5������ƨ�=l�^��Z����!1_�BO���p�eq����ѩ�Jy�D�� �x���5��Dg\ė��`D͢`�9x�.�q���ԵD-�_z�Oe������!�!���|)�ݰ��w;i�o��rh��a���g��'P�_�L"�FsL���6#�u���T߾N9C4���o�e1i�'LΦ��pN����E�����n:�2��%N�p��@�cE�R@l�q#��0��wT~)�l8q ��O�����Ӝa.��q"�bt���]<$�iA[3+�ض��c�Sz�uxh�>����H������ R��d��3Y�g�k6.x��q"�/L<:gۧ���'>�k�""u!1�&��p���P�5JK
�}�+X������Ā�:����%��Pgy�ҀLf��rJ��)J�w�A��l��Z!H�<or��*��	�����L$�r;4
E�z�$5�v���x�L8>H�Jzs+�g�kP����ōD��m����i�l�Q0/�G�sA�<M�-����pO�Ibq�G���*��O?���r�"Hf���zu!��V��N�F,;.{b���d��c����s	�X����h�
r��Ћ���[�:���Ľ!�&�5׶��P�Yi/¦���|i��0�ʋ����ދ�#�,{��}S�Z��p����ze@�N��iM�]���tC���3�P�w���Sn����^D$|��g=N�V'hN
L�^_�V0m�AH�}ܱg����=������"j�}&b�)=�7%n!,�����1���-6jn-�����[���d؅s�CL5���z0�W<o�{����/��ݫ���_����xN�Ǭ4t9l�C�����\n��ю��-��6�9d��``���j�F�h�Yj��p��o�a�=5�+�Ȅt�PL�~�#�Ja n1a�6����恋)5A�_y�H�Hu��<��'4��ͼy��o��x�r���I�is�HSp��<`���n�L�zP�qpf��xq��b�vC�3|��(Owԙl=[ѫ��^��Ϩz&0h��4���(qt���6����KT�g��i���Ϊt��J-S�����S���[^�l�c��&\>'��(ȅRbXً~/�S�Μ;��C+��݃2�YB5�oA�EdfĀ��
=#"H ��ϭ�ܮ���q#s�~�P��4>��8�����	6<O#�˱����E�����bo�&c��OWg�0�8c)}O��ˠb����9���8�H���q�t$���x��� S^CVUL>��YM us��/]����/��(���5a@�3^LÀ�ċ�!X��V}1v��]�	>�>���_�L9]x�}8�����4)f$P�X;�e$w�D�D�^�����mG=eMfX�����e�v�߀/Y-B���qq$T<�F����8oH��xB�t��8�� E�������4ԁhɬ��M
%r�c>�ȭ|���3�
F�A�D�K���*�磛/$�3J�@�Glb�D�YB�YHG�J�ea��Dg��b��dm�0���F� �!e2.��ɜ(��FV2�"��YU��V莦�yX���֦�BU���}H����@�{�&�'����� �"P)��q�G�>J=��r��t�hxb�}I�%�GV����c7���z��a�OFĨ+h��f݅�W��ۖ�[��ΎA�"B�j_n {"��/�D���0��Ŷd����>�A~�{?S�c�fd˖GL��O �	�`!,��aJ�?k��hp3Dj�Y�KCF������=��.��Ɨeu@.�EqC�ݾ	����qju�jG�Ze�Rf�v��	y*������|��X?F�:��n4	,C"�%��g{Ъq���Scߍp��4D�돞���Sy�4��9-��Ϻ �!��z��&�V�c�n���R����;�M�Y�;���^���~�E�Apxs/�F��HMRL"u/.�Φ{���B��t������]ױ�����'����h���x)}�-槤��2��uh3�o����xb�$�(��=܋��|�L�s��iU�����=��pZ�������/��!q�.�Ss-Ɋm.�|ʘ��=T�s�	�@fHfy΄x��؉���~c��/<�v���B���d�fޕ��qS�@�h�.O���s�����en"0�ʮ�N�S(�����d�*����u���ڟ{�����F)�]���Zjˈ�^*)�U�ʥ������9�F$�M�3�2�R�U�)���L&	u{�H?�i�'��;���0>h?_��C�XS���}��Vy������L��h�b�$X�O�s�N�ρm�MA�u|�3��Cpbvǈd:^�&��ĵ��jM��#�ؘD���!$��t�^���Ia	3�� x��dL�
�B@�4��(�H�z�����R|ܴ��̩����@�3��A2*0a��y<˄�x�@�z��ς#-�K���87�	��<{��K�<����4m�\0����>�ö���&+�U8���x���������0sR\/���f�����;��&%��zv�t���H���zW�M56�:�@YhlF[	���f�ݚm���rJ�>P�bұ"���pc����Rt�|	5*7�ؙ�j9B�{��s�s5i}`X�;c�������Ȁ=~"�♜cz�qN�32�pR��>o	��m ��ˊA�L]��s�1�{x�n��j�W�`�~ך�
�NW�w���HJ��OmL�.�ª�U�t`N�8�IL�z�� *;�.gN���g����@��D��H��*2A��T$�/�00��7z�TW��h�g��TGCf7\3o�MeU}46WA���ݷ�ݘ�����aV[&T�銑bۺ�3H����ƤXH^���J�1ɥ��T��n�p�)^��ѝ1g�;JZc�����9�c�\y��k�K����z0�����wwUD���Q��[M %�Y��""鉿w(X���P3j�VV�m�F=�Qu���n&]��	�z�S�� P<v;1sq��=�D_�8��H�$�1��_�O�fs�g��T���G���3*k'�~���0���a����q�ea    �\�;U2�0�Oj���L�r"&ft3~����(�{3���4��i����= �u�7?�W��&���P��"�n��p�>v,a�����MXh0At���\.#�W��I��x,�y�E�(�Yϒ��Ɯ=E����K}e~�	o����U�/
��+����?\�eD�v���W���٦��m���k�-��Փ�ȄJ�����4�A��pqs�r�͕����=!3& ��R"�E!�0�l��!�����)��%��%Ç�_��|����xk/	4�u�'FVҳ��ԫQpc,�#N�����Pm��B�?������~�.6��Dg�4�6��؃�'���>Г	5�c�?�!`d�5X`;��^���Xx���}�
����fu�h E�����(B�cw�៿�=H����AWv|߭?S��>������"S�M}�Z.��0�x��P�����Tl���6|��.RZ#�I1X�4�̭Rq߰J����
i�▢W �Et�^S ��rb�bB8�nPwO
�̀��.�:�!E>1v��ؐ4k�fr͝�5Q?w�69�Z!`�:���m!�ɺ2S�%å��L[W4����Xx^(���3��zD�+j��ʥ�;[���U�B�9:oM�n�D�q�(S��{���;`�K̡�5�L��YQi�ێ\)M]3%�Y�Bf�pD�EC�s� 8��C���s
������'&�8lV�
����~h(��`M|�Qm�$�%}F�~58�)0æ�Q�e�ܡV<����r���b���I!E����N�K�̣J�f��d���Q�3S��o��fDƜ�6�1Ϻ5���[[)�Q�E��H�����+�ĿK�{<8�[9HfX�	���z������G��Yd�_t5�Պ���-N˥��^d
XD�B/l�z=���.����
� O�J�*�Ԡk�k(��Ub�7k��* �g ���]-M�����R�P�+8㬬ly0�%�}j{�J�HJ�>�p�0#69Q��~�>)��n�b�5zp�Q��O2秠�%�0�wj���@J�lc��z=�=�:����C�H{B��!��v%�%L9}�
����T`�>�m�#�*�pDj�;f�� �h|=*��an���m{��w��A~��п��b��$B*\�/�1պ�p���AY�@2Δ�����Ȫ��^m�P�OH�t�ڵ�I�w���}�t��`j>?y�(&��G
DͪV���tfV���{�wp� Y4�2R�(���`?����qt�܌�)�q螨�}��=B�9�{�f&-�^4H�ǥ�PI�b�4� #r������`p� Ѝ�rۑ;��ܱ-�l�t�HB�^3؅����o�x���Gq5��9�_]V�ŕ�\��1�|�隯�v��#{\��	{>RL�^��}jNq�>l�ć۬�+g�c�)�P�8��[�;����Dy��]�^�'�4��FL"�1Jc�a��"�	�)�-[C<���C����u�����71�
7Y��)�PV:�8 bU ѽQ3�au��ɿǮ$s�V��h�\u@ w#�3��m����Z�-�tM�L���*(���|:�
+ ��1E�a�Zڲ��1���R
%]��H�
m7����MSd�h;����~�F�e���hX�?'(3�Z�!�ś;�Y�CTY˕���^�K�/x����d����5ɢQ@8��OEd�܃�V�l�\߂�n����;���B)6Ԧ9�~�A���t����vbDI�&�k�'�j���X,�>���EJ�M�6�!�����H�*ON��G"2U�P��Vk������Q��w�x<���HmhS��u$jɵo���5���|l�\A�z*є��`5Y/��8Q#a8�_Kd�ڻ@	�hoq�yw�Z%E&���|î�'��|�5] �:$w�NJ�0�~.&�̈TR�_���C�+U:�Z�%H� �D��d����b�do ��~y;���F1�%R��W�gD���M�J�9S���h���9����������W���^�QP���S_�t�;8Ġ]�SW�	Et� "Q�9}�)�襰��Ɛ�{p�����LZ�\^˛�~��ݹ�[ sfљ��[p�8u$D�9u�9\x�:��M��t��2�
�u�.�7"GqA,k��� �|�]$�E��+"v��PF���IJeX�s��[�z�L0�,OW�ӕĻ=JkL+����0��͘xƁ�0po!v+|ŧQ�<�&p���B�(�"�g�&s��V�E�tb"��EL�s���h)=�a]T�;j�[(���}M�}�DDi���#�d}l#X(��F�F�,y�	DN�/J_�S4L����#��~ט+�K�p�k $��fK�޳�y~��L]���)��x'�Uȹ��U���cTq<�!����tnC����o0��ġ� �hݨ��̠D�OŮ&G���:R�;���F����o��XH���t��F�8v4�K ��/�(���t/g#i���(P��U5=g
DZM�l���/��Η���}���~�d���az�Du�'�>��3���M���\mPV8�$,�cs��sr?���`�T�k�p�vFP���בZ�d�e�V���Y���3�up�a��=�2���&~#����F7���1^��	`�cmn��/=��Kh|d\�jxu~ؒcԦ��4WQ8z�ӏ�ӿ���m���_�g�����<Uy(f�DϷ�d�Hϣ��7�9��m��I?TP��;�P�RK/I��}x��*u^HEk�}9��/�Xу��-�(�ۮĬ)�+�1�0���
gL;X�"��}M�<FQy�Ir��2��#DaN���E�>O-BJ;f�I�[�P�q��0 X4�.��~�R�??�t��t�ъ�EJ+Qf�K%,�:��ǒ���ԫ�1HM=�Ze�
����Zõ!"���ׂk����{e+APN
+w�\����
3��Jz���� .#bk�?k��qd����B6�L�b	U�7��ҹo�l)��5�����;�vH�9���n�<�1>�K2�?���F�L̀�1ȫ�=Wk�y4�M��?�n�T%����� �\1�O
�Jk&�A�tVKA9�������`�$V��Q��.�N�R����Nήn˃�*�DL���>q|рp�u�?��gN�V�A��S�b�R�!�HA�cr�_ƹb��꼲�<Zw��QL6�fQ�����jU�¯�Ԃ5_�
�]"&~������%z����vk9w��)A������zk��'��(g�u5FRL牣�b�[I�ҜQ1`�Z��l��K�nv�q!�>�l�yGᅎ����t,�m�fC�-�����\=��G�U��r9Z��d$��w��]حP_ܭ��5�N$A�6i.�C�4�G�*
�-���M�gguxt^H�/��IE�BLܺ��a�c%aKux�Sxr��Q��Gt��? gm�K�d�VK�cGo��h?3�U<ŝġ���d��Tf~�\&F� 5ia?���y@.[�#Lf��:A���2(��zi<	PL	�VB�Z- kU���� �\.ȋPO�kTĝޣ��z3��viDNh�m�v�fw�����^*��i�Y��%�S�Z��	�{<�C��'fK-��X��ۑP�w��#>�tU��C�ؼt��KI�ɅҪƌ]�-��T�@)�W]WafS�k���� "&A]����!!^.�g�׹��B�K�X�%�kÄ��ʔt���'�Y��m��|��R���~�W�W�X��#�*]�U�]e�mL��j�>���@�R�ǰ,Nn/�
�X��9j����K<�6�'b�h����C���d�O L���.�"��?i���
ez�p�6k7�&pN\}�]3��2�C��^�v�U�:.Ń��4~���Y�ck'��g��p�3��e�K��[�c|�1C�H��?v��о�P��uCq�t/��%�����9S��E����^c�LO�)�����L���
#�r�2��w��V`aH�V��]�ip��ڠ:"Pr�~���ˊ��8L���󎈉�Nj�HM'�!�    `\6����)�&�����n"��B��|$L��&)���XEg��������I�@<-�,#ה}��ހ�x\|I� af���o@ήe��a٤x$���)������Bi[���}C��؍@��u��h�&�މ��O*$�c�GAj +�p'��d��"c;�i7~��/1}J�d ���&��(_X�f�<f&��Q�(u.#re��e��R������U��G�h2U%/t�V�j�2D���IG6��0�ݭ\~�1C�!���g���۳���Ȭ3";:�ɏ�:C���u���f�!ձYgH�3���X9핛,�)���1��p$�4�MJ�1������J���* )9����[_*~N�B�������E_���LƋ��3�����:�a(Z����^�}~����Dܟ��%��Y�>�ʘ�{{����>�^٢���1G�pyZyl��������YU\X ���Ui'S�q�'�T{�	Š01aah.�0JiXa²S^y�M�2G�Ƶ�MF㨭��X��yy�a��D���։�֌Qe�R
3H�/�BX Adc�@]�9K�5���[�1�{��)&�i-� ��6�	մ��đ��&�����p0L��N�Q�$R�S8=�rc�x��f�[�'�2�xNe_�^�7� ���dgWLs�L,5G*��uGc�?^
u5 �]To1��C=
h��l��u]��:����)��[��-ֱ<	��!dR72��J����^�[<8Ny�:� �@�>��X��N�����$2*թ �����;�V���Az'c���GB6w�rN�� �����[/�(1�;cZ�sA���l:���O��M(��'L�G��i��P��Ծ�S3NSΩpy,�lȠ�+㧕�T~)m:�>��E�<�؆�:���`+WW6�g����ù��&~�Q%�o���\h��[L��_c�v�6tT��,��;�w��w������8kr��|�
�x�Y��?'߯.͐߄qoT*a-��|B%��j\���T�m��������&�	̤�9�tP�q?�K�s� y������&ʓ6������4(t!�J�tR8�Z�����$��~��<��$�!e2g�`��v��������$��)C-���4_�����5q*m��jݭ�A"<X�}���0��rZ,�&K�n}��ՙ������0֩c���Wj"�{Y�������s?1�W2�����":��yƀ������!:weU'�d�(e�����5����%�&BU����u�)@���왲H5Z\�"�&\H���|�ْҌK�T�����
u� >�m�,�i�< �(%�J�i�y���)�#ڛ�ʂY�#�6�I�C-<8n�ۀ'�K1ÀK���2�P���/�<�+�ͽ�ATs���v &�K���Jܬy��>��ٮS&OUX�+9N���12��53�0Y�A)z&��J!M��.�/��V9��A<�V�6
�����M��hu�D����M��<���*�H7�ۿ������I9Y�LZ�
�Һ�W�!Ttk�k����^�7n3d�t��}�����[��sq�=<5��ZE�el��YTh�����)��L�*�*w�:S�|�t�<#�ɐ�8+��P�c��b"OM���/�a���s�����y\�b�V��2&S��9<����wC{�H��X�`&!�7���]#��ەs�	�Y9WvpTu����0\�W3�Y�6^�2�)Ցp������6a-<�L���%+�e�����Hϝ3�8�C���7�L,À'VQ��2���+��T����G:K��u��Z*m��R��H�s��CGy�$�ʱe��g|gk�ys����ě�v(e�s*��FP�T'��ntΥ�3�c2��[C�Ԫ?Ȳ���I��zv\iI	V����`TT�L1���iU*���>�*nN����P��. #1��O?f��9Q�����8J���៳9q�b�����s�o�j��.��!ņ<�g�=FO��/��.��1Hea]:�8�%��.^:X �1�t^ޗ�W �e�qi�?]ͣ{��ɳ�و�y�5O��,��ѓ��w�1,����yb��,�TҚ >� i����[I�@�1f�߯O�2��d�=�� �"p��o�co/j��E䭲��������WxIB+prTY�Bf9��B#���L���0�T�w����F��2�L�\�;�qb�1�-t)
�ͪ�6�W&�猫�x�+�{��,�g�����wʧ�lF�9]��9qÃ�b�=�P�8ݹ؞���y�C53<C�1���õ�.�%�%�\�E?y 3�;��tM�s�O� � ���=�r��<w��ĝ��2�!3��kO�缟M���@d"2�/J3���?�s�:ɦAu�egPmr�m��D,�zu�8����Qb����_��V�f�Tg�Āݥa9�8��FH�<�7|��};�SĀT&��S"��i����O~+Q�i�c�� ���#�5�L-���b�eO&��^�0+dp&�7{��4�I�ظ,}lM`�P��@�Q�ޜ��A�n#5���NG|�����Z�(S����
#�^��E�^3�_�,N�Ѣ16/�K��{Y3\��yA�q�tS�g\��zȗ�U1�IqdSZ}@۴m��;�NŨخ��O���}�bWSs�\�~y�S$J����7��	�ЕW9Up6����o��:le���_oL�GG�{�p�t#=�0o ��0��R����3%�vwB*�*�w3*���p��5�=�aFh����CR<�����|ò7YFa�0VSKeBv�U#*"�9D�b�c'Ƚ������4��/���ME~в�~د�5�AT�N~� BbE�ɤҦ�"�,��z��qBl_M��Z2��fHi�m䉎���Ōr�ĭr�.~6�Mz)�ȑQ����[�ϨV%�ze5��E�Uѷ�a�����G-�/w{�(�&.x�Lh���Oϫ��8x�*���+��^��7�ȞUI=l�T�+mB�YXI���F�'ٝ]{#:'I�|6��3�}����->c)d\�Y����}��5[��1���,�A��Q��d(cʹ�IyH9�_PH&�.>S�%Sj0Gv�����I�z�m;�o��l��r`�����:m"?�;��Q��H���!�t�I�!�k,V�i�w�+�8׽��A��ϰ�Ĩ*�\���!~~"�!�h��VrA�ˍ�k����B֘)o�n����3N¯a�;�ȫz��Ҫ!5ńU4zYVT
�	G��:�ۿ��g>��S��I�}\�߳��*y����@����L@`a/�&��nr��en�J{s�P��F|*p? )#���J&^����c��F0��Tav0�_��1N�^b��AS<b1�?'���ś�x�2���1���|�'S�P;�-��a7������o�~F��O+8�-mC���kD���-V��3d�@[/J�y܋� ��B�����?vV��f�b�!V��a�A�-4��֕��Vb�j�m�bL<J�|��}MF=I�D�gn��.�������y��Ӊl�����=���l$7W�(3
+v�^� ?��?�C)ǡ�6��`�@z���]0�ѣ����KEY����������pz�!��bJʾ
㾲��Z���з4�mTɸ�<����s�1��~{޵��,;��/��bj�D��P��2�44���,ˍt�XHD���O��������J[X�C��!cZ�G���	�k�w��7B��.�e�K�jئ�4,�+�K���FY�H/$�zW&~.N]��<2�S���/����1����$x�U��lA5l�MB�n��}����X��y�s/����x�yl/����7�P�i�s��Gܸ�yN���)rނ6!��\�:-�����+:�5C0WK�5�8j�ޚ$\~�1�>@���4M���t�fbX�X���̅�XD:�"�lڍn������#��®+����^"��ιm9^�����h��[W*��~=jg*i�����\?^$\7���%>���l��"@��3�x{d��,9�§�%�� {  Әh�C�P�i��d$-.SX�Q���k�tf��F��!�D"
�5L��0�Z�*����֧���⟇vxuO��s�`��:�T&�[2�/Zi~��@���+��:�рa_�4QK�f�u�F���|�%7�<�N����D��G�f��<D��)NV�9�+,x���<�i�20���6ڈ��\m�/$�c���5�:"g���{�B�;���#ɪ%#B�WfC�C:�Щ}0R�詘0�$�d�L�(e���L��0�����}���9�OF�i��,(N�}���w�br9��H�.���Q�:wp����b]�Ƒ΄ɖ�#���5P2���N3e��Θ��LPn�X���?�D�Ӏ*t	d�f�j�'�oLo���*1�ܩ���w���3=�ڭ-�ϩ�����Ԭ������vU�Hu�r��İ9_M�}�`,�����5���f��)`�y��SЉ���N�[�J�2�q��Ł��?w�qzrA��
�Vz>2��Q�Wp:�}��l�p��"��^�Y�W�a�^��Ձ�,�����'1g°-䤕��4|�ʺ�3���\��hv�!�ɷ��n���n)�Co�D�'�_D�4����I���w�3G.Nn�����:��̈����&@;p��J ޵r.6���)yD�]`ᦞ��dP�cJm�
�]�5�b��.2)�J�+}�K3$���Vj���������L���g��_���մ��ņl5s��ۭ��.P�3�����ע#?����%�M/���M�j�xU&b9��;
;��n��i3"7���L�avϥZ���;�0��(.���wL��>;_��j�9_P��D����!���䟽���� &?kTϢ���Z��3���H?�upn3��I0���و�����v�vJ��2��`a�o���5#b�*����ۛ���(�f<��hGa/7�噋�w��L�#�|��� ���02]�����!SUuT��aI���~{d;�a��k"1�;��G�9T�s�$����ɻ�Lf��Ƚ��K����*/3&����Oi��'1K�l��	 ���e0rLd/��/!��j�W��҉���rk~�q�Oʯ�t��Ә���)�%��)GǪC�W6PZ���x�6����`	Yd͂6��A���K/`���E�~r�a����k�L-H�U2,��)#j�>�M_q�{��QqV-��^-k�����-LM#��W)\�)��\B�խ�q�v)D�*?:�<�,f�P�
�Q#J�J�5��ݥ�F4줌>�g/��(Q�($��
�Ww�9@�W#'!�#��tV�C$�M��@-��t�;��GO�D��h�M[�P��p.���%mc���� |� Xpo�n�#����Y�K��-w������S��<'�Pק�p����؅%�0�����L��E�W�~�(%�'��[U�\&L��U3:x��D����i<��Z�!��&�%_.�Ҿ��	�L�\E���ĩQ0	�9�� ��,i~M�sd@� 4�fGõ�����B:rZJ�S�^����v0�z
�|��Z�S�Wqr=uV��X��ΐ����|f)��f��/���������,�6gΨ���;�R<I*�I�<)cO�0*�'�����{�����j�      9      x������ � �      :      x������ � �      ;   /   x�+J�JM-�+J��J�s(H-���L�����N���M����� %      ?   <   x�+J�JM-�+J��J�s(H-���L����K )�gbAAQ~Yj�����W� ��g      @   (   x�+J�JM-�+J��J�s(H-���L����,����� �`
�     