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

def sql_select(query, params = []):

    conn = psycopg2.connect('dbname=colorpicker')
    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()



def delete_pallet(name, id):
    conn = psycopg2.connect('dbname=colorpicker')
    cur = conn.cursor()
    cur.execute(f'DELETE FROM saved_pallets WHERE (name = %s AND user_id = %s)', [name, id])
    conn.commit()