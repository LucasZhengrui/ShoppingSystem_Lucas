import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
import sqlite3
import codecs
from shopping.models import basicinfo,detail

class Command(BaseCommand):
    help = 'load data from csv'

    def handle(self, *args, **options):
        basicinfo.objects.all().delete() # drop the existed table(data)
        print("Table deleted successfully! Cheers!")

        # base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with codecs.open('shopping\data\product_data.csv', 'r', encoding='iso-8859-1') as file:
        # with open(base_dir, '\shopping\data\product_data.csv', newline='') as file: # Read data
            reader = csv.reader(file, delimiter=",")
            next(reader) # Skipped the first line - header
            for rows in reader:
                print(rows)

                basicinfo_object = basicinfo.objects.create(
                    Unique_id = rows[0],
                    Product_name = rows[1],
                    Brand_name = rows[2],
                    Category = rows[3],
                    Selling_price = rows[4],
                    Image = rows[11],
                    Amazon_seller = rows[21],
                )
                basicinfo_object.save()
        
        detail.objects.all().delete() # drop the existed table(data)
        print("Table deleted successfully! Cheers!")

        # base_dir = Path(__file__).resolve().parent.parent.parent.parent
        # with open(base_dir, '\shopping\data\product_data.csv', newline='') as file: # Read data
        with codecs.open('shopping\data\product_data.csv', 'r', encoding='iso-8859-1') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader) # Skipped the first line(header)
            for rows in reader:
                print(rows)

                detail_object = detail.objects.create(
                    Unique_id = basicinfo.objects.get(Unique_id = rows[0]), # Foreign key referenced by the basicinfo table
                    Model_number = rows[5],
                    About_product = rows[6],
                    Product_specification = rows[7],
                    Technical_details = rows[8],
                    Shipping_weight = rows[9],
                    Product_dimensions = rows[10],
                )
                basicinfo_object.save()
        print("Data parsed successfully")

        # Initialization
        # connection = sqlite3.connect('db.sqlite3')
        # cursor = connection.cursor()
        # cursor.execute("DROP TABLE IF EXISTS disaster_message;")
        # cursor.execute("CREATE TABLE disaster_message (id INTEGER NOT NULL, message TEXT NOT NULL, PRIMARY KEY (id));")
        # cursor.execute("INSERT INTO disaster_message VALUES (1, 'Welcome to the management system, if you have any questions please contact l.wang.22@abdn.ac.uk, r.zheng.22@abdn.ac.uk，t05bl22@abdn.ac.uk，t16cl22@abdn.ac.uk');")
        # cursor.execute("DROP TABLE IF EXISTS disaster_user;")
        # cursor.execute("CREATE TABLE disaster_user (user_id INTEGER, user_password TEXT, user_name TEXT, user_level INTEGER, login_status TEXT, is_banned INTEGER, is_delete INTEGER, is_approved INTEGER, PRIMARY KEY (user_id));")
        # cursor.execute("INSERT INTO disaster_user VALUES (1, '21232f297a57a5a743894a0e4a801fc3', 'admin', 3, '1', 0, 0, 1);")
        # connection.commit()

        # print("Initialization data successfully")