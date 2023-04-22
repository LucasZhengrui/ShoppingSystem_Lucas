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