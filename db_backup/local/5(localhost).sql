PGDMP  '        
             |            postgres    16.0    16.0 0    5           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            6           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            7           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            8           1262    5    postgres    DATABASE     {   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE postgres;
                postgres    false            9           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    4920                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            :           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    18439 	   challenge    TABLE     �  CREATE TABLE public.challenge (
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
       public         heap    postgres    false            �            1259    18069    challenge_json_data    TABLE     d   CREATE TABLE public.challenge_json_data (
    json_data json,
    challenge_id smallint NOT NULL
);
 '   DROP TABLE public.challenge_json_data;
       public         heap    postgres    false            �            1259    17842    challenge_status    TABLE     �   CREATE TABLE public.challenge_status (
    challenge_id smallint NOT NULL,
    challenge_status character varying,
    json_data json
);
 $   DROP TABLE public.challenge_status;
       public         heap    postgres    false            ;           0    0 (   COLUMN challenge_status.challenge_status    COMMENT     ]   COMMENT ON COLUMN public.challenge_status.challenge_status IS 'UD, RA, RS, CC, dup, reject';
          public          postgres    false    216            �            1259    18390    contributor_approver    TABLE     �   CREATE TABLE public.contributor_approver (
    challenge_identifier character varying(255),
    contributor_id character varying(255),
    json_data json,
    approver_id character varying(255),
    approver_comment text
);
 (   DROP TABLE public.contributor_approver;
       public         heap    postgres    false            �            1259    18487    domain_list    TABLE     a   CREATE TABLE public.domain_list (
    domain_id bigint,
    industry_id bigint,
    name text
);
    DROP TABLE public.domain_list;
       public         heap    postgres    false            �            1259    18036 #   industry_domain_process_key_factors    TABLE     �   CREATE TABLE public.industry_domain_process_key_factors (
    industry text,
    domain text,
    process text,
    key_factor text,
    suggested_values text,
    description text
);
 7   DROP TABLE public.industry_domain_process_key_factors;
       public         heap    postgres    false            �            1259    18482    industry_list    TABLE     M   CREATE TABLE public.industry_list (
    industry_id bigint,
    name text
);
 !   DROP TABLE public.industry_list;
       public         heap    postgres    false            �            1259    18492    process_list    TABLE     a   CREATE TABLE public.process_list (
    domain_id bigint,
    process_id bigint,
    name text
);
     DROP TABLE public.process_list;
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
       public         heap    postgres    false            �            1259    18407 
   user_login    TABLE     i   CREATE TABLE public.user_login (
    email character varying NOT NULL,
    password character varying
);
    DROP TABLE public.user_login;
       public         heap    postgres    false            �            1259    18419    user_signup    TABLE     �   CREATE TABLE public.user_signup (
    email character varying(255) NOT NULL,
    f_name character varying(50),
    l_name character varying(50),
    role character varying(15),
    employee_id integer
);
    DROP TABLE public.user_signup;
       public         heap    postgres    false            �            1259    18429 
   validation    TABLE     b   CREATE TABLE public.validation (
    email character varying(255) NOT NULL,
    active boolean
);
    DROP TABLE public.validation;
       public         heap    postgres    false            /          0    18439 	   challenge 
   TABLE DATA           �   COPY public.challenge (challenge_id, initiator_id, initiation_timestamp, industry, process, domain, creation_timestamp, name, description, contributor_id, approver_id) FROM stdin;
    public          postgres    false    225   �8       *          0    18069    challenge_json_data 
   TABLE DATA           F   COPY public.challenge_json_data (json_data, challenge_id) FROM stdin;
    public          postgres    false    220   v9       &          0    17842    challenge_status 
   TABLE DATA           U   COPY public.challenge_status (challenge_id, challenge_status, json_data) FROM stdin;
    public          postgres    false    216   �9       +          0    18390    contributor_approver 
   TABLE DATA           ~   COPY public.contributor_approver (challenge_identifier, contributor_id, json_data, approver_id, approver_comment) FROM stdin;
    public          postgres    false    221   ;:       1          0    18487    domain_list 
   TABLE DATA           C   COPY public.domain_list (domain_id, industry_id, name) FROM stdin;
    public          postgres    false    227   ;       )          0    18036 #   industry_domain_process_key_factors 
   TABLE DATA           �   COPY public.industry_domain_process_key_factors (industry, domain, process, key_factor, suggested_values, description) FROM stdin;
    public          postgres    false    219   E       0          0    18482    industry_list 
   TABLE DATA           :   COPY public.industry_list (industry_id, name) FROM stdin;
    public          postgres    false    226   s�       2          0    18492    process_list 
   TABLE DATA           C   COPY public.process_list (domain_id, process_id, name) FROM stdin;
    public          postgres    false    228   ��       '          0    17863    score_params 
   TABLE DATA           ,   COPY public.score_params (name) FROM stdin;
    public          postgres    false    217         (          0    17868    score_params_user 
   TABLE DATA           �   COPY public.score_params_user (challenge_id, desirability, feasibility, visibility, innovation_score, investment, investment_in_time, investment_in_money, strategic_fit) FROM stdin;
    public          postgres    false    218   7      ,          0    18407 
   user_login 
   TABLE DATA           5   COPY public.user_login (email, password) FROM stdin;
    public          postgres    false    222   T      -          0    18419    user_signup 
   TABLE DATA           O   COPY public.user_signup (email, f_name, l_name, role, employee_id) FROM stdin;
    public          postgres    false    223   ?      .          0    18429 
   validation 
   TABLE DATA           3   COPY public.validation (email, active) FROM stdin;
    public          postgres    false    224   l      �           2606    18471 ,   challenge_json_data challenge_json_data_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.challenge_json_data
    ADD CONSTRAINT challenge_json_data_pkey PRIMARY KEY (challenge_id);
 V   ALTER TABLE ONLY public.challenge_json_data DROP CONSTRAINT challenge_json_data_pkey;
       public            postgres    false    220            �           2606    18446    challenge challenge_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT challenge_pkey PRIMARY KEY (challenge_id);
 B   ALTER TABLE ONLY public.challenge DROP CONSTRAINT challenge_pkey;
       public            postgres    false    225            �           2606    17848 &   challenge_status challenge_status_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT challenge_status_pkey PRIMARY KEY (challenge_id);
 P   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT challenge_status_pkey;
       public            postgres    false    216            �           2606    17872 (   score_params_user score_params_user_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT score_params_user_pkey PRIMARY KEY (challenge_id);
 R   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT score_params_user_pkey;
       public            postgres    false    218            �           2606    18396 '   contributor_approver unique_combination 
   CONSTRAINT     �   ALTER TABLE ONLY public.contributor_approver
    ADD CONSTRAINT unique_combination UNIQUE (challenge_identifier, contributor_id);
 Q   ALTER TABLE ONLY public.contributor_approver DROP CONSTRAINT unique_combination;
       public            postgres    false    221    221            �           2606    18413    user_login user_login_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.user_login
    ADD CONSTRAINT user_login_pkey PRIMARY KEY (email);
 D   ALTER TABLE ONLY public.user_login DROP CONSTRAINT user_login_pkey;
       public            postgres    false    222            �           2606    18423    user_signup user_signup_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT user_signup_pkey PRIMARY KEY (email);
 F   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT user_signup_pkey;
       public            postgres    false    223            �           2606    18433    validation validation_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT validation_pkey PRIMARY KEY (email);
 D   ALTER TABLE ONLY public.validation DROP CONSTRAINT validation_pkey;
       public            postgres    false    224            �           2606    18477 #   challenge_json_data fk_challenge_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge_json_data
    ADD CONSTRAINT fk_challenge_id FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id) ON UPDATE CASCADE ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.challenge_json_data DROP CONSTRAINT fk_challenge_id;
       public          postgres    false    225    4752    220            �           2606    18447 $   challenge_status fk_challenge_status    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge_status
    ADD CONSTRAINT fk_challenge_status FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 N   ALTER TABLE ONLY public.challenge_status DROP CONSTRAINT fk_challenge_status;
       public          postgres    false    216    225    4752            �           2606    18457 !   challenge fk_challenge_user_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.challenge
    ADD CONSTRAINT fk_challenge_user_login FOREIGN KEY (initiator_id) REFERENCES public.user_login(email);
 K   ALTER TABLE ONLY public.challenge DROP CONSTRAINT fk_challenge_user_login;
       public          postgres    false    225    4746    222            �           2606    18452 &   score_params_user fk_score_params_user    FK CONSTRAINT     �   ALTER TABLE ONLY public.score_params_user
    ADD CONSTRAINT fk_score_params_user FOREIGN KEY (challenge_id) REFERENCES public.challenge(challenge_id);
 P   ALTER TABLE ONLY public.score_params_user DROP CONSTRAINT fk_score_params_user;
       public          postgres    false    225    218    4752            �           2606    18424     user_signup fk_user_signup_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_signup
    ADD CONSTRAINT fk_user_signup_login FOREIGN KEY (email) REFERENCES public.user_login(email) ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.user_signup DROP CONSTRAINT fk_user_signup_login;
       public          postgres    false    4746    222    223            �           2606    18434 #   validation fk_validation_user_login    FK CONSTRAINT     �   ALTER TABLE ONLY public.validation
    ADD CONSTRAINT fk_validation_user_login FOREIGN KEY (email) REFERENCES public.user_login(email) ON DELETE CASCADE;
 M   ALTER TABLE ONLY public.validation DROP CONSTRAINT fk_validation_user_login;
       public          postgres    false    222    224    4746            /   }   x�3�����K�OuH�H�-�I�K���4202�54�54V04�26�21�tr�J-I����.M�p����CF\&��Tf����&�b�9�lAE�,�h��3�O����C�XcDkb���� 3y�      *   \   x��V*,M-.���3T�RP
�H,Q�,V(�HUH�H��I�KO�W�Q�+3)��/W��IQ��/-R� �{�ZNC�j��KLO�g����� _�3�      &   I   x�Mɻ�0�:�"J�,��h�5� v*���U�sԮc�3�W�P[K�a�t��S�	�LD7H      +   �   x���M
�@�u�2k�(]yA�4h���(�xw��Н����ɋ��|dZ4�jG��8�3�	52yG�]l�����zt�v$����l������9L��GRd[[<AH-���AJ�(+`F���������	Ys��������[��5ߧ�l^��T��l����GW~ꆟ��J�tƘ��      1   �	  x��YKs�:^�_�e��f�2�6˄��T�	Μ���bhb,J������Z~ ���T�nK��u�A0x�:�|]�O������
D��;QT#��T��Jy,+�+��e���G���g��a>��G�sY����5/2a����>��Ӌ 4Ç�(��o�B�Կ����[^���l�� ���'&ʒ�0R֕1�#�Zӝs����ؐ�Y���CQi��_���\��O�Ys�Q�UQ
o���C費�د�Z�7⽩lu��]�C�`Yl<F>�Y���Cv�jm�X�|���$�j-�y�\L�ȢVu���Jim�z�W�2�/�\�������=F�]�9"4�s�+�{ۗ������ϝ���չ��c����o���k�<<Kl0�joG��A|�QV*��9a �\�L���-�:'gx!�V�!�$}�,M�yᰣ̸��Aad�(+|�?r�?�>x��/U^��H��%7r<�$a��,���a:a�Z�Ye�f�p�I.�P�,*6Ph��U��a �Y����-����S�t�F"��ͪ��l����0㢞���u%�}��R�lݪloC�I@F;�% _�U�X��zUzC���m���5��խ��&��;5��`Yզ��2mrً�o�I�Ӈ=?�a��e��ô@�țӇ���J�dF.�B;����~e�*�}]���z�J+Uk4-���?�=���gT��L"�,�h+]u�)�hn���~���Z:�u�@$[*��:C��3�Q�[ aFCp��m�Ū�n�An���eJ����h�	�S�<�t�r+����M3o�î��(�I��~��}R������-4��`L��<����{tBϏMO㥺�f�0��cL>F�[I�vv����p02}�̞h��4��O�����NΓ���$YW��dt5����h��(������|�Ё�F��Ͷ��)�og>�A~Ԋ�2^V��^4^*�$ gz �-����V}�j˶X�u/	�Y�^w�`�=D�!��B��Z ;�܋ԳA�tu2%��2����N��p�}����(���T)�wj��k�V�%cp�Z!��$u'����9.�nq���2�����7�Gk]�z�2�&D�9�Ge�������j�[S���iL<'w�����R�+�tQ7�q �Y����Xe���<��acr�B  ����� �ȏ��4�h����ĉ<�� �b��1�=s������:��;�㱹��m3h+���c?^���r�-�Z����7;�͂���9������ �,-LuX#�N8��_��\b$tU6��łL7�p�N��1�7�ߘ�{���b �l;FA&���m�M�U�7��n;T��>�f�M�bb�4�a�����B}cC�~)��������MB*m�A�jt�c���1��j�&��r���07p��Ŷa���sG�	�"�L���p۬��X�0��3f����׾-}��1Z�	�;�Wr�0;,�r8)ș�EP,9��ső1��Z
96�3!x�]Ol�yv{�`@�`w���xp��<x��o��c���I�M�Ev^�n����7�ث��O,� �j=]B4"���7p>��&ӵ��f�^|(�M�g ��pg��)q�|-�����g\��'��$a�i��B�]S@�+�x�6�(hԅ�E��o]�# ?��I�j8�����B�av	�� }����EĻ\y��"y��>>@ &'D &D��T ��i��� X�7LO�QqB�^	�ys5R�}�h�)1��G?�g����`� ���o5 ����{0`zF�����������C�zF�/jP��Z�fup��Z	j+���+Ȟ$_g��(4�¶� ��v���0$oԽڕ���l�Xl<w/�'�ظϭ	W2pdt� ;���p;x'��e�Z���Q`���;��o%�<����E|M��P	P�Hc�zF{�I��ښ�c��O��a�,��Յ�y��a��Ս��c�~�d [�� ��O��lǂ��.1��s�$x�g��rB�$$s�0d.R8o�������Q�r@��%��i�x���3|����:�a�""	�B&$�k���^&��`j�y�!ſ{3j�������l�j{�4𡠓X-D�M�fja]��7c����;�=�GE���PK�1Tf�m�Jk?�����̰9�z��	v
���5v�9�K7N���Ƕ���u���J}6V$�~F'��^�����~��/���}w���-J���q������H�Eե�bo�`������� M���`���!V:�j�12@g����էO�0��~{z�����E�}�On�9ƅ�נ]�>V�@����z��7�Ƕ��+�"�3��\��f���/�Ŗ���"�9M�'j��L!-+8Rz�`�_-�iSIی(��mZO��/�����*riVH+��~�&�v�r�C��]��{��_�؟S      )      x�̽�v�H�6z������W�nI.uٳky-�T��}�H���/!��&	6@Z����a��~����D��E@�ך�H �@f�#�x�/�����߲��2_N�|�]��rZ4ٓ��/��>���b���ͺZ��b����y�G�l�y�������UUg���tٔ�7�f�f��ME��L��)���}S5��ɛ�7OG?d��ッ��"o6u��o�l��TWY�����eq�M�i�8��~�?[\]�ӲX��j��f]�Z�ˢy��~<:?�W�բ�������Py8>:��ߗ3 b�/gD�Z^O�E�Ⱦ�MH��u����X��VuY�@���7����)���ԛM������@�����/u>�J���z
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
PP�.��%���)�b���w��ٳ�ew�      0   =  x�M��N1E��W�
�BM�,[hU$*!Zvl܌;c�q�<*��qg��Ҿ����Ȭ(�tAGJ]�ҙ$X�j"��s��r�O%�PJ06��CN�z���o01��8��f#�[����93%�i;S��ґ�^�S�sU�C�G�+ݫ�x��o�0[L�n].��ҬQ~X����8V�����q�=��نP��5])b�'Z�G)gtz�����G��S%�C��L���Cs;5���<ؑ���:�v�}}w���@�%�b)��ag��o�\+O.t]�%�s�%u����~�]�cDI�������pҨ	�� ��q�h      2      x��}[s�Ȓ�3�+�4!G�w�Q��α�:��=��/	I��Hʭ������* �;6�;�b~U(��\F��߮�����,>���a�n��Y;���m�ԭg�f��v@H���pX�������n�>���}�04���߳�z����`�k�Gg/�{�
[�j��_�[@��������RF��ݾ�>,��z��tkӨ�nڇæ�����z�t�Pj|Cht���i�������")�n�n���߶k3��M�?)�.��{��,��m����E��a�m������a]�KQ��]���x�7D.����"��5,��~�?r��*:��_��{~&|�f���u�o����uq����ęJ����ߓ��$�p�%�p��v8=���Z�a��'��\|/�jDL#F�χ�g��o��nq�nڕ���}?�[��鰈�t���u�i�dK$M�K��0�� S}�����Ut�߷�5����Ь��� ��~�u��t	3vX�_��v��]�#�f�[��~�K�m�(�$:[A����/�N/��<8�	{�vqvXw�gf
�� {��	�����L|`�O퇜 _�f������/�?���zq{v�������B����*�����?�hy	�2@D��No�u�F��9l�����<l{�m���������OC�?�v�z��1ItS��
���4R~�צk���E2L�S3��A�"7/�(ˣ�u���E_��-v���>���o���v��,�U��iO��YV� Tŧn��'/!�{]��Sr�T��M0��F߻���������O�E���o�+o����E�vk����_eS�lq����7iU�ΨM���W�9�٭H�MSx�u�>�U��F�������	!m�"A�����߬�_eKƎ��o����>��tm�������)�/]���u��w ��L[��!����Q��y߽x�`��E����®�o�J��@�̽��
n�������кF�=���������J8�8��z���a�\���f��u�����%���]���Ҳ�vs��[�����Hn�ݻ:E��j�u����K�cgkf��ZD�ݾ�|�/�Q�s�}����$�ni�}h����Sᢇ�����oZu���ZF�{:�b��w�f�cx��3�J{��4���롹����͕Ux>�m��j��9B��4Z�>=<���s��{�Ջ-Nno�Z�y��������B6I��t��η.`�U|��-;���Av06~��Z�������澓�:.f8ة��a���O6���^�/bY��8��vx�w��t�M��M�
=$x��eϋ��?,�G�#i�;�<h��x/�5`����qG�0A��������Y��J�g��3��WG6����FӰ�7���O���?���g�'ZN^�iL��pI,�(�O&�a�Æ��@G����������K�A[�펥�)��4��k�Ofٞ ���p�"�!���v��1Z�/��Gp��`�7��Cƛ���g4���g\���/���M���� J�nwzl�x�R���yl謐M̋��6�:Q��G���n����=��[ΓQ�=Bƹ i~���C�H����i���v�G�qϯ?���;���(��v�{8���_��@~"&�mv������N:U����V�KC~+��ћ��U�����QJ��60�[y��.Ǐ�,���!$�Q�$H���t�WyȃQ5(ɕ{I���N_R��Լ�0�v��|���ǥ���.`8�aY� }��no��/�$n�&��(���;|-+�ʋ��x���}��"����C9���S���ܷ�����Z�i��s�l����0���4w$�172M�ݥ˱�W!(�H������')� ��j�hS�^���"'b���
�I�Ljz�	����C�ыs����1��D��7����,�~���-,6�n��}���Ӣo�0���	���p0�F�8v�,�/��Q���v'@��L���ț3]L��t��c(Q��.��Nݯ�A��Faؽ�<�t�N/{�Ѭ�Z}5��i6��!��~xD�O������l��S�;���l܇]�J7`�Ѯ�!��_ ��������C�jeM3���qՉ�R&�_،+��$����;8����?KYG���e.��?���7{���WD2(F�GG��=<�jDm���x�q�}������
"
�4P��%4���8�
d�v�b�h}��1%j����)!r5{,�]��:�>���rW�9Dա��dLZ�ݞe(�)�]=��������wx9��2:o��)P<i~�+��M�?�N���8���,I��!��g��.�p�,��z'�eчf������J��pj6�z�'<1��E�O`)N/��D>�����Q��c�mj(h�ڡ��]��D/��^OJ�H��G����G��`~�������b�&�ڬ�W��XK������9Yͽ�D���H	���P��)U��8||	��Vս8���V`5e��R/���W����]?<#��(�����o���?���������tx!Q7(},�����I	q��Oy���ک�ч�j�?`~��+��W�e�'��qO�`�A�VV'Hn�^�ͦG�_���B��
>�y��oh�6u&"��V�y72Q�k5�un��������}�7C��۷2~��ŀd� �߉+ǃF|�}���Í�Zμ�~q{橱�����9�;��w3\j��/�95+�Z��C������Ƣ���l��W?��CFWx��޸m�$[C.!д�?��UI�S���> 8-c�*|���>@�C�Ʋtբ*q��v�@��Y[�?�J:K�f)Y�@l^���~ibZ|s��iv$e�~Pn�=t&��������I�1��r����V�������k����W9�e��rc� ���s� %�[�7�G���(��~f��|�Z�gL��i�ܙf�j���M��,��2@T�����6ī\n�r�S�h�P��1*�<��~��)��;Y�M3]�r��XQ����%��M�q�O@�~C���*���.���\A���̴B���=���E\Ai�~�ڎ�:KD����<�x����8�o��D_�W`�_�	w�q��q�1�[�]ߡ�I��axi_w��c4R.с�n���XP�r~�I�(��+nz:��sD��h�4����{L.4U�m���[w��#���p�egO�E�t��'�����g��p&���X}�f�=����\1�.K�3��{]|��N���#s�Eyo0-w����^�^~W�#.i<o�+G��r,n�7 4��zP=�j��<)_��ӂ�,�"+dbN~��}�u�<P�*��Wn^�{}����j����#���j6p�yRQr9�wӷa`=�6ޟ�\}��?�A($�(#C��˫��� up��#�XN|���"��&�_��dj��MI���VT�<l;�{��\�e�hR��smB�%���W.g'7�އ����&9�N!�a
QpC�45�H�����\���B�����h��Z�-?���\0�2Ak�p�P�!�}��ZjfXOgE�����S��x�85�4�TD�7�?NAV���H�����	PE��(�������-5��}�q|?��ˏ4�=v�O��*�}��a�р�||��^��@�4�n^wh���E������w��잠:��#KQ�փ�N7 �K����ٸ�D��G��rnIH'e��]|궴����q��(���?-�'�z���n�~�u�5�%Z$�e�!@l��Ջ@� �T�"0��q,<^�u�{��ۼ�aI���u;4|�o���bv����8cP�5*r���\E2|�����.��.>��{���.�����fjd;���b��A�sb%G!�$�#�4L�������[�w/��3����"��R�T��l�;���^w��h���tA{�;ky�y�-7     ��&�g}@	/#���KI1��
�M��X�N����6�fk�.��W��)�R�.|q�LGg��$ڭܡ{ޢ��EgB��'7�W�`���7�}��Co#��o�0��^"��Uݚ@R%s�m�a���9u6$&K�vJ���L��ѧ��>����B����fGك��>d.ny�y�P�4������{k1Y����x!ؑ)��<cszBjsڅ@�2�ӄ����K�PxDg�N.�f��Ø�ǡV>�DM��g�$�������樇>����w�>�0��[PAJM��lCV/���	� �5O��_q���,�`��c��`)Hv��|��!�7"ѳ:�l�hQz7�稆�*����IHmu�T�gە3	���Ԣ��F���x�
u�^u:��vG� ��2u���j��hx�ٿo��l�k�����r�]�Rf@e��c�9��J��(��iD���ӠD3��"_��H��ӍR�6k]�[�3_��^��&���k��9�{B�b���T�de��}��@���ް��3x�Sy�����!��՗��&L蚃z&M����Lߴw��Y^"*:|l��}����}`��1�%�8"j�Щ�K��)�FL�J��Yi���"���ov����Ƹ�!=�L�1[yN�)d���B�'��aˬ��R%��}�}j]�,3`8"��}���؊W��W�پ�=��l$Q�	SU �Ϧu~	(�oȧǍ��_#c�	�[���,�[��a�iBHa34�]��]	S0�8�8ޛQ2�C��̛"T;B�
��ȓw�������v@H�ez����H��'�Bo�{eܺ�{�H ���n�� �^}n$�i��P��̉�Er* ���k���*��Q[{��&>#��F �ECb��9<��D��������=z�����܉���^�k6�θ�/�����E�<s�.�]X�r�5N�k�ZD��8��*����}'ZB�CXO��R ��aW��v8Ҭ�2P��2ЀY�,Q=Ϻ�O���l�D���*u;lFX�0�'I��}�r�h�����b��O��M�S�D/Bs���.a�	�?�t�e*�J��0�j�4�,d�0��8�FBԘ�?��@w���9�[>���V���Lir��FH"�[��}�\���D2-hkf�vւp�{�B��G���<���"%.MF=�5|��f���Ǌ'"��ģs�}:�Mb�s�/"RCi�y�� �\���@ �7ݰ�������@H����QY�_ u�g/�df��o��D@蜢$z���
�Fk�����WQ�רB���p9y0<�����@b!!�C�P��AJRcn��,�G<�������7�rx�����<\�H�X��;�Q��v��6@���qt!:Tx����"o��wߙ$��{t[�rl���/�*.�d�O{Q��W�A�ju8�hD�B��'V�M6L?�M�j|0�0��=!����V� ����-�����HP�y@�"aXsmk����R!l:��G�V�8ì�(^@��?�̲���7��EP�w���+8zj ������BU��坺)�����63vV��y��[<���J�ED{nq�C�Tou������n�F}����{�(�����-��|�(����g"F�p���{3���n���/�!P�pk���%���,/'�.��b�9���փٽ�y���� �~���^�0�/�
$d&�s�=f��ˑ`3�LL�f�r����v�f�o1Ė���!�F�"6�W;5JE��R�wp�#�|����I^�G>��ōb�SўP
q�	���A~f|��4\L��B�ʣDD�Cg��� G_<�Yoh���5~S�Ɠ��>�=H��dH�cG����>(�Gv#f�(Ճ���{0+�ě���{(���აlGy�۠�d���^M��:�F�3��@�0ħ�.�D��������g�}��^�J<�oMk�`H����gw��:�R��'B�S��g;�}�|N���B)1��E��)vg��������A��,��� ��"2�25Z��a�8�1��Ł�A�Y*���������)�����M�ĵ����{�^�u���,��5nW�x;H6{l�|��8c8	�{��]�vOn���a�O�C�H���q�t$�,���G�0p���f�kȪ���T���P7Ǩ�҅9����2���}QD?��4xJ����/h�c�����������uȔ7���ϚK
	��Qs /Ј{1z�;\;-p��Hz'��!zd�QOY�VEx;�mل���7 �KV��:�j\	�9�5�4ΛF �1�0|�h���Mj$��߁�B��@�o8t{{:���d$#�����(3|!�O}.�ҪȞ�n��P�(]Q��9mf	uf!�+Y��%J��c�9>��1��
"XM��x��ɸ`�&{� 2Y�{D�܏fU1TF�#X�;��e`�"�3\[�^�"U��q&�!�귃���<��;��@�L���]8i�f�(��>V����=��-��%=��	XR�b���v�k��=?x������uJ_E@�o[:oq�;;Q�٫-|=��q>��g�b�Tے�^w� �e���xLup��M>��-[1Y@?�'�-�=���R�)]���Z����af�C.�#�j�����V_�U" !)l��7��8z�,�WǬv��U�/e�iW�����^(��w
����aT�S/�F��2�!"XBYx���fJ:;5���aJLc@d���)�(;��q����=��r���.���i�h�]1���V�q8!�?\N���܄��%��S�|0�
b��آ� 8��I�@O�&�	&���Ug�=�|y!-�Q�Z�@��l:�'�����b>���F�1sS����^`<?^
�C�1�|��v��{� �pG����^�����t��*�n�S�Ξ�fo8-��v���Q����@�˩��d�6\>eL[���9τx 
3$��fB<�m�Q�U�1}�X@�p!�~X2a3�J�^͸���D z�@�����9�e�~�27}e�c'�������dy2���@�:�҇v��=��k�\��.����Y-��e�I/��y�RA`�U�לw#��|�L)�*ۊ�l�s&���=�\��q/4�LXI�P���Z�}wA�)�J�>ދ����v��Qj�~&�Qt{�^�֧�9�c'�����&� �:>��!81�c�2���XP�Z�
j������]lL�k�����S:@/F
QŤP���y <d{2&V�u!�R�G{t$P��G�J}t)>nZ�s��Q��h V��� ����<�e�x<r�f�m��g����[��L��fn�=[��%`}�Jo����`.���kM���a[������*�w}`��_�r�mL���0s�
\A��Q�ҝ�߆p��sB=��o�a'��|��B}�R���MB�,46���G�S���nͶ���9��t(RZ�:��9�)ńdE,���6�#ީa5���[V�ib5!ʨ��>0�熝�|u�M_M�dd���4�gr��}L@��9��Ȩ�I�.^��%��fp��Ȧ.+�3u��c̙�,�I����s�	_��]k�+ ;m\��a�")ͮ?�1| ��.�"VӁ9��D'1A�9�E���� d��9q.���G����#a6̻���&S�������>��9�P]	�΢i��SILh��p�d��7�U���\YD��v��3vc����s�"��Lo�����-��A�矽�7&�B��V:(�I.��z�uk���`0���v��\�c"rg�uJ��Htw��������^�fP���G}~o5���gm:����~�P�$�7ޡf`����z2���ӡ�L�" �����+�A�x�vb���{2*�� pzՑ�I^c<&߿�������۩`9ߏ���g4T�N&�����a� ���V�A|����0��w�dDa    �������HL��f��F�6m�?�4SB�1��h�t�͏�U����;3T�����7\��K��C���sL]��FG?����U�8AR�2Kn�`!J�Eֳ�b�1gOQ�jg��PA��ni���r���E�䩽��uѽ�7���2?z�i��y�j"�sK.�q��<2�B!x�r1�Cb0q \�\�\useem'3�GO���IH����(A�B�&�64oH�q��r�yJ�`� �@�����0֫`�"Ú��KMh�ቑ���7�*B���a8=o�T�$��i��gpl{d5���˅�0:љ0ͫ��z����ɡ���dB��X���C�c����?�.�a F��B-�y�Y6@���r��)����u��/}���c��CЕ�w�O�<���<%�8���tS;��K�A>�^Fp�:T�`?ur� �h���_��B����yRLV.#s�T�7l�D�8�BZ�����
 0����k
$�TNLTL������IA��a����RG:��'�����f-�LN��s�&���&'Y+�\�ԙ��-=YWfJ�d�Ըi�f�6З�E���`[�`W����c�Cm[��rg��>��]h6G�Iލ?�h:�eJ|�{���{�z�9Ըf��0<2� *�~ۑ+��k�D1�AȌ��h�w��'�}��=�@��� ���px�a�Z���f��p���	����R0��ķ��HY�g��W���2 3l�5Y���a�#J+�.w�+v(I��R�o���D�<�$l&
L��x��9S0��F�lFd��i�q�[3Y�λ����Y4���$�/?.��I��Tиǃ����d��0/�@���?���y�:1��E&�EW�Z��!����\*��E��E�+�b�ƫ�S�0����zد�򔬄��O�־�B
Z%6}�fX��|@Y����To��y/_Y+�	��3���N3X�ܧ�������c
G3bS�5��� ��r*n�v*�Y�w�*�$s~

^���p7��_��T�6�Z��30�s�S���<ĉ�'D�"zlW�^��$�ӷ�P��q�H���#�Vn�1"�¡G��c:p��ו����PK�ݶ��~7��X�k�.��M"�µ�2S��
J��q���0G�fqd�[� �6�]�ŧ^6���v�cR:�� �q_7*$���O� �����Q���{DÀ�;�w��&%�|��� ���In]���B��C�g29�n���A�2�3�U���GH:�|O�̤�ы	���*	Q̛�`Dn�~z�� #�UW�Je�l�t�HB�^3؅����o�x��Gq5��9�_]V�ŕ�\��1�|�隯�v��#{\��	{>RL�^��}jNq�>l�ć۬�+g��c�)�P�8��[�;����Dy��]�^�'�4��FL"�1Jc�a��"�	�)�-[C<���C����u�u���71�
7Y��)�PV:�8NbU ѽQ3�au��ɿǮ$s�V��h�\u@ w#�3��m����Z�-�tM�L���*(���|:�
+ ��@��{K��tu*�|�̶�{i���vsO��t0E����!��~=�nd\FZ��u�s�2����1��������
���Z�T̥��&X}��t߯&�45��I����|*"�����@f����v㼖�PF�A<%'J��6����o���_�[�О��#�H��0]3<QV;^�H�b���}%.R�hl
�Y�,�G2Vyr�WV�����ZS�d\}�h���G�3���}0|Ej�@�b.�#QK�}��D��GH5�c��
��S���v��z��Ɖ	�w�Z"S��J�D{��̻��*)2A���v-�E8����囮��2 �!��pR��af�s1>F����Z.�w��X��	ֲ/Ab�'�Đ�/%�&���'{5��ۡW�60�!,����<#�m�m�T&|��oF�-Nα,p�`\�7�^ߨĖ:]$����ʴş�ʦ���!�Z��BvH(���z��3�N�D/�=5��}؃��Ǆ~�����Z޼�������p�3��T?߂����#!�Ω�����)�mR����9OTH�;wi�9�b)B�\�g��nS��X��ǀ2��MR*��J�[l��ף����t�9]I�ۣ�ƴr�k���ߌ�gȌ ��`��W|��Cj�(�-4��� Bq�k2�ll�[$M'&rZ��:�煮��c��A������,�J����IDԑ��j>9@��6�a������W�4�)a� '�-��w4�]c�.��b/ �d��u���<�^@�.���a��E^�����KѪD{o�����3�j@�Fҹ�#j���TL��-!�8Z7�j.3(��S�����ѭ⭎�Ć���)�ѯ t��)5�3;�� ��5���*�� �8J@��e��7��@9��V���)i5e�1�g~8?#�,^:_�	d�3�u2��Z�o��eչ�t����
'���v7�G�K��f�r���R,����6�)Tt�o3�SU�������S��I�[M��f�GXz�U��G�t#�xɡ	�|`���T��xy,� ��vW�-t���5�M����o�����^���� ��q�P�O�����#�0|����'���MUH����3l���D�J���?�֜�wݶ]�*�R���[���$��

�[�U��:���5ھ�g�z��A�S�v�mWb�͕�E��p
J�3�,C^Ѿ�Q���<�$��~G��0�h�آV��!���$ޭH��8_H,Tv{?o��P:dd��hE�"��(3٥��^��HiX35�U�D\ �Ze�
����Zõ!"���ׂk����{e+APN
+w�\����
3��Jz��M��2"����YG���:N/d��$*�P�y3�*��p�f^5a̽�[5�~OA0�: �h�O��n���$�n�#�X�l������
�s���Gc>�D1����QNU2[Ka�����y�� ���fr��9t$��{r�9���l���� ;��R)��zu'gW7����QD$&��N�8�h@�Ժ럇��3��y�� ��j1D)��M� �1��/�\��V�,F��m')MԏV�zV�r~e����T��w�&~������%z����vk9w��)A������zk��'��R3F�!g�uH &��� ���Ez���r��ͮ6.�ԧQ�-0�(����S��T:�R�!�Vb�L}j�C��*E@���{2�K�;F�.�V�/����B'� [�4�!X0�c���MT�&�ڳ�:<:/�����"h!&n]K԰�ʱ���:��)<9�x�(d�#�	����6�%2b��ʱ��GE����*�	��N�P�0�e�'�%��F0&5ia?���y@.[�#Lf��:A���2(��zi<	PL	�VB�Z- kU���� �\.ȋPO�kTҝޣ��z3��viDNh�m�v�fw�����^*��i�Y��%�S�Z>�	�{<�C��'fK-��X��ۑP�w��#>�tU��C�ؼt��KI�ɅҪƌ]�-��T�@)�W]WcfS�k���� "&A]����!!^.�g�����B�K�X�%�kÄ��ʔt���'�Y��m��|��R���~�W�W��e���f?czh���+�8ghcJTC��X՜�%�*=�eqr{�Up����Q{�t�7X⑴�>CF;�,Ȅ,xMZ-�&Ø�'t�Y�{Mb%���t�*N|����wW(CՇC�!S���vNѽ4�B��u\�3{h��Q����N��?΀��hg%���I�����Xb�$�~m�6��}�)�"/0QD���QW�����"g�7�4+;y�_��1f�<27�^� ���I^ZXadU�T��.�k�,��j�3��
TGJ�~�O{�rYS�ɱ� }�1��I���>D3 ��&|8�w;��ĸ������B䂒!Q������>�$OT    ���??X�?�0I��E~�e䚲��_�P��/�$�l������%k2@1,�����;�׸3�]8B(�bK���=�T�1��܄98ѱ�I�d̘�؀&K%��A� }��p��.�K�3���a�}�i��a[{o�/�w3W3�M�(C�:������2��
)R�a�u��*��#{4���:A�c5}"G���#�o�X�q������5fX����o����Yg`zd���u���f�!���:C�c�ΐ��Y�fVc@b�t+��r�e:2��&W�@̔��o6���`Xg��_be��;I�_(��837%��y�v+�j�=d���)���D��L�e�F<�Lk�7���?�kIR'qO����s�n�K{3��/jQV~o�v8���\�`el�[�/�M�����+dL2�^�|�E��$�1$�Ǟ|B1(LLX��)�RZVE���W�r��1�Q�q���h�Ւ�8/�� L��ȁ��:Qۚ1���TJa	��V �l���S g���!��p�<"frOp7�d4��ST�C��}1���r�8���d!�^�. �	���4j�DJ~�Ӄ7L�6kɽ(wG�'�^�75���:���{��dgWLs�L,5G*��uGS�Toq���aqTL�Gmߚq�.��<��"5�G�v�)v�u,�D�aw�ԍ�Z^��q�6���K�#��L�U��d\�|�?h�#���a2�K�Ȩ����c��ػ�dr3�t2��;J99'�c�����뭗����~.(��̦��03��m�d<�j�8
��\3����Qa��B%�S{�OX���T)m�ǖ�!��G%�e*s#j?6�KO�TV:&����}��L�lQ����:*f��t9�kl��݆���y �5vn��s�T14�fHG� ��Xg��x�
x���*�����K�No¸7*m��^��{@5���w*sd��m��\b}�NtKy�f���R����R�It�������e�F������H�a��*��I������R<���!e2g�A��6����_��Ɏ�OΔ����fR����ɾ�v��8��NH��ֹ�,b�>uH�b9-ZU%e�����������o�Ա���+5���,`0b�r��﹟�˫	̈��r�Efs�<�����U���?�*�\2j�P(u4f"}��ɚu�����gJZq�^J�q�� ZM��J���ȳ5����v9ѹ��'U��UzLZ�.ӉjOɲfRh���f�@�ea�)L��I��㷲`��k�t��X
�Ǎ��6�ɴ($�3��V�p�B.gGnR�y�SG՜�F�����I��ff�����j"�e[fAǗN��-8�pƊ$����E#�P�LV`x�7(3!�b�4с��xI y���4K����<�h��D�"���M��<��)�H7�_�͡ɏ)g�Z�<^�!�^&˓�(���L�*3�*�:�ǃ�8�֦�ℵ�z&�A������{xj̀j�01 Ψ,:����$���H|G*��xd��'��р�e4S
K�S�(�yp<*�Ə�2�@�I���>af�F�BlNϧcl���3���vHeL���sҝ�b)X��6�\��I�b��NM��v���ň)��˹a�@yN9���ɕ�+���j�1��9����/W�(�P���1���cʜ����RNؒ��d�����Hϝ3�8�C���7eL,À'VQ��2���+U��XR���|�s��N��R9&V-��18gXTt�'�t�n��Aļ�s���d\��ě��u�D9�zI#�m��wʡ��O:����/nMO����3�� ��h�(�êՑS����W�)�Y��"j�ԅ��$��9yLfJc�C��ߺ ��(z>�L��7�D%"�����(5�{���ٜ79s:ƿX�y������.K��uH�1M��bOٓ���-���e~���]�R}���7���P<"�Or�i����߃�=�CA�:G�8鐼rͯ���	�<�R�~[��O���>���~�6O�8�%�JZ�G ���v+��7Ƽ�����CF���}���`�j�=��y��EM���U֐����pxX�\�
�!IhN�*+S��,g�[@�X5SD��TS&��j�.t@�H�YƐ�KzG3NL5���<�NXD4�7j�q��,��_�bj�cb�"��|:xfTp�������@N�\�w��4{n��5p�s�=W-���j�5���s��z|���L�lr����P�|��5���?��L~&����L���rƍY/�d��~�y?�(i��D�]_&tjL-#,��[u�M��8�Ϡ��^��ˉXZ��zq�y�����9��������';�xV0j���"����3��6Ș��Q�"�2�����LM�l���#X��O$#W�6��9dj9�����-{��Ȏ0�zĀY�� �idCmQ�O=��e�ck#���L:����I����6R��Apq�}�t�W1 (?���	P��/KFġV�U���_'�j��3]��｜��Y5�-�v!\��q�~`�j�Q�Hϗ��*�1)�lJ�h��muG�é�%۵��	�ھoW�jj��/�u�Di��� ���=!��*�
��q4F"q2Y��v����iU�����G���*F����2�PK�ӓ�����m�a�	ig��`�Ų8�&�B����H�t���#V_sI�<��[��}��d�Y�XG-�	ٍV�����}�-�n;)#Um*���F�0�Ԛ5fp
I';l`���5z*q���@H�6�T��1C���r\�6?N��pU~n�%��h��F�6��8�f�('I�*w��g#ؤ�9J�Ι����4jU"�WV�YZ�]}k�։���Ψ:��������3��Lh���O�UKI�C�T��7�)���}�)��9*v#�n�Xڬ!h7 RIlT~��ٵˡ�k��g�=3��]2&����!�q9f�^{4��O���l�Fyk�����>�.�C�餜��ʉ��B�0	�v�
.�R�L��Q~�y����mޓ����v�xD�ǜ+j�fL�/�3*
-��≻&p[�3S2rblv�\�&�R>�&��hr�fr���E����!�W�[�.7BX�i�Nĸ�p_Êwh�" ET��;�;�p^Ջ�V�)&�ڠM̲�rP��K82��S�78��{�`O>5�D�ǅ����AK&OaRw(%���	,���¤�ߍ��P��	��-�B%c��� ��LD��+�x��;��v���jwP���\~y��8��E�-�L�Ů�����o�)Cȴ�k0�8���}l�L5C��e�Pm�����N
NQK��d����}�J`�8���XF�����a��O;�]2Х�W�n&��G��;�tV3N1�+���� 5Z	u\/J� �Q1?0�
�*w�/d�-�&����d"�3�KI����no���uq�V�<3��(�{��Q�2 eFa%�N��`��c�g5����~�o0A �_CV�.щ�Q�Pj��XDMGFm~c.@����L�g1%eW�q_��e�KfcD[��6�d�C���﹎�G���쐊��]�ѲG��b@e�ihk�0+O�.L�Yc'�TG_��ew5e! #��052�4�bƴď0F����F��1m�g]�Ұ~������J�i�E�k�B�{p�5���nЃ�>�/�*�����DD���pi�5!�����a�J��b�-����IR���]��'��Ō��>��e�"P<�<�}C@�fm(ɴ��P�#^��<M�=�9oA�_~.tOq��r���R�!���w*5_oM.��� �b*U��Q���i��Ĺ� ���9���t:�E�ٴS��96e���=F��]W�1�Z���<˜!�ѹ�J�*��3q�͕I����_ઑ�˥q�E�u�j~�Q�31���fh*Pd:1Ìc�2��
]G�,)��A9���K�F�*O;'d�%#iq�����R�m�]K�3{o6��	&)P�p�a�K���AժV�x�ut�>�ܯ� 6  >�ë{z��[�S'�ۙ�21��Ēa~�J�x�:��\�O��q�&
������8�Ud?`Mh���|�%w�y̝N/o� ��y'���a6cY1,�JS
��_1Öǥ0MU�����D	���V⅄~,7��\G��C��~��A�G�zy�"Y�dD��l��W�~��j�:�&}�=�*�*�&�����i>���5ָ���z:@":_��)��?M��Ń�/�|�.RL.'�	����t�/�[�-�4�U��:7g&L�\�g6��h������g��)�.�t�����h`��r�����!�'2�P��[}#�� �zɢ�4�O.>ߘNK�W�FvI�Ԉ��f�,�=oB�LW��aP')wQE�@D|tJX��	O�n�P�<1l�W�|�!X Kla� y�_28��<y��{e�tb̛��g�R�h�?fq  ��Ɲi��\PF/�B������o��\��N�z�"$�,�\��~���WoV�`X�ׄ�pu`A%ˠ��h�I̙�0�9i%�%����z�
��6�T�]��>��ևə`M�O��������H����>"S�"�_�q����헳�VG��Q�>?�� h�T	�[[��fxp#J��a�2%�����0��櫐�冱[�u�ۑK3����T�\��oX��9y�3I�ìj�y�y?��^w����Z~n��Y����j��(T|����v�K �^�i��������r&[�i����(h�j�+�V+��>���K����w2a�%R\?���:a}v�<I�s��@����,s520�^Z����#��W��g��[TW�X+�vF�"� �G��m����	BTv^"�13R�֮�N��"_F�,���ߴC`�fDl_�3�11q{�^�Ԍ���(��γ<s��.2�Iy���4�0�F�+� 7��=d���*]�",���o�l��!L��qZ$&qgP�x��qΘ$�~��Qx��"u��w�x��|\�eƄ�]: ��)͔b��fb隍�5`w�&"���enw�E"�"d:]����>�T�^n��1��I�U�csy��6�d��5��Xu�V��
-����`����q�,2�f�=������o/i��]7�zҍ�YF�/��3� �V�0�\x0������/���8	���ZN��Z<�b3!��[��FTԯR��S��+����_s���R��U~ty����0�F�ΕBkܷ�K}�h�I}B�^vWQ��QHpo��<M����Nܤ�QJ�z�ټ� �8������X�� �r)N��Ls�j�N�ڸ����t�v�I�L�%�)��۶[�Յ-�Rio��-��7�+O�:�[�o��O!d�Ɠ�sϱ��a*WC-�יP1��ι�˯���dRr�J�˄闰j`F/ؙh�[z:���\�=dV�D���eX��:Ab�����(ⱼ׃85
&�9�$n�%ͯ)v���&��h����:Bx^HGNK)t�1݋#���a���Ri_�!�ʷ�dz�[p���e����>�>�g�b���z��2��Z�M����j��y����! œ�r��1�gg���k#������w���?�j�      '      x������ � �      (      x������ � �      ,   �   x�u��N�0�3�0V)�[�*NU/����^�u�u�v����	"59ϧiB����M���<��s��=B@��p��0��0T�$��	�T���g��a�'�X��*M�t�Ί��<���x��Q��B��16����.$N�ް޵T��5,��-��٣�=��:V��u/��@1uFQ����8�,?�?���}y�o���ܣ�~�_�| ��x��      -     x����N�0E�3�~�h)�ׂ6gD&q<�����i%���3��Jn�v��Q��\�`3X(�8	BA=cC��NB����R}��k�{8A�b����2c��X	u�K�N�Xj��o̵��1�:C�*����n ��4�s��&o�K�����-�y"ٜ��d8r/������̺D�6ԓ����S"0ۡl���A�#$�^G �#�^c���5mM!��YqP'����-��-�~�zj�����o�����T8��v�-w^������(~��d&b      .   �   x�m�=� �k9g�Al&��X�5�퍅E�����'��D���L+Y��b.�$��D/Ե���j$Zz�_̠GD��6��9Z(�ٛ"onn�˨�	Z�fm����} �@;�|n�Q�li`�#�C"�i�7F���~W��٫w�} %9�     