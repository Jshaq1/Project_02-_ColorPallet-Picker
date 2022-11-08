import psycopg2
import os
from flask import Flask, render_template, request, redirect

DB_URL = ox.environ.get('DATABASE_URL', 'dbname=colorpicker')

def insert_data(query, params = []):

    conn = psycopg2.connect('DB_URL')
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()


def sql_select1(query, params = []):

    conn = psycopg2.connect('DB_URL')
    cur = conn.cursor()
    cur.execute(query, params)
    row = cur.fetchone()
    return row

def sql_select(query, params = []):

    conn = psycopg2.connect('DB_URL')
    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()



def delete_pallet(name, id):
    conn = psycopg2.connect('DB_URL')
    cur = conn.cursor()
    cur.execute(f'DELETE FROM saved_pallets WHERE (name = %s AND user_id = %s)', [name, id])
    conn.commit()