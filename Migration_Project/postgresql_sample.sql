--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- DB to file "pg_dump -U postgres -d WorldSQL > postgresql_sample.sql"

-- File to DB "psql -d WorldSQL -U postgres -f postgresql_sample.sql"

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    id integer NOT NULL,
    name text NOT NULL,
    countrycode character(3) NOT NULL,
    district text NOT NULL,
    population integer NOT NULL
);


ALTER TABLE public.city OWNER TO postgres;

--
-- Name: country; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.country (
    code character(3) NOT NULL,
    name text NOT NULL,
    continent text NOT NULL,
    region text NOT NULL,
    surfacearea real NOT NULL,
    indepyear smallint,
    population integer NOT NULL,
    lifeexpectancy real,
    gnp numeric(10,2),
    gnpold numeric(10,2),
    localname text NOT NULL,
    governmentform text NOT NULL,
    headofstate text,
    capital integer,
    code2 character(2) NOT NULL,
    CONSTRAINT country_continent_check CHECK (((continent = 'Asia'::text) OR (continent = 'Europe'::text) OR (continent = 'North America'::text) OR (continent = 'Africa'::text) OR (continent = 'Oceania'::text) OR (continent = 'Antarctica'::text) OR (continent = 'South America'::text)))
);


ALTER TABLE public.country OWNER TO postgres;

--
-- Name: countrylanguage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.countrylanguage (
    countrycode character(3) NOT NULL,
    language text NOT NULL,
    isofficial boolean NOT NULL,
    percentage real NOT NULL
);


ALTER TABLE public.countrylanguage OWNER TO postgres;

--
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.city (id, name, countrycode, district, population) FROM stdin;
1	New York	USA	New York	8008278
2	Los Angeles	USA	California	3694820
3	Chicago	USA	Illinois	2896016
4	Houston	USA	Texas	1953631
5	San Diego	USA	California	1223400
6	Phoenix	USA	Arizona	1321045
7	Indianapolis	USA	Indiana	791926
8	Jacksonville	USA	Florida	735167
9	Washington	USA	District of Columbia	572059
10	New Delhi	IND	Delhi	301297
\.


--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.country (code, name, continent, region, surfacearea, indepyear, population, lifeexpectancy, gnp, gnpold, localname, governmentform, headofstate, capital, code2) FROM stdin;
USA	United States	North America	North America	9.36352e+06	1776	278357000	77.1	8510700.00	8110900.00	United States	Federal Republic	George W. Bush	9	US
IND	India	Asia	Southern and Central Asia	3.287263e+06	1947	1013662000	62.5	447114.00	430572.00	Bharat/India	Federal Republic	Kocheril Raman Narayanan	10	IN
\.


--
-- Data for Name: countrylanguage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.countrylanguage (countrycode, language, isofficial, percentage) FROM stdin;
USA	English	t	86.2
IND	Bengali	f	8.2
IND	Hindi	t	39.9
USA	Spanish	f	7.5
\.


--
-- Name: city city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pkey PRIMARY KEY (id);


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (code);


--
-- Name: countrylanguage countrylanguage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.countrylanguage
    ADD CONSTRAINT countrylanguage_pkey PRIMARY KEY (countrycode, language);


--
-- Name: country country_capital_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_capital_fkey FOREIGN KEY (capital) REFERENCES public.city(id);


--
-- Name: countrylanguage countrylanguage_countrycode_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.countrylanguage
    ADD CONSTRAINT countrylanguage_countrycode_fkey FOREIGN KEY (countrycode) REFERENCES public.country(code);


--
-- PostgreSQL database dump complete
--

