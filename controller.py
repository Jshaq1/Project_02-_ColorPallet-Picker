import psycopg2
from flask import Flask, render_template, request, redirect

def insert_data(query, params = []):

    conn = psycopg2.connect('dbname=colorpicker')
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()


def sql_select1(query, params = []):

    conn = psycopg2.connect('dbname=colorpicker')
    cur = conn.cursor()
    cur.execute(query, params)
    row = cur.fetchone()
    return row
