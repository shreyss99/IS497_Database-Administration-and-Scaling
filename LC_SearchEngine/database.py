from django.db import connection
from .models import LeetcodeData


def get_data():
    # with connection.cursor() as cursor:
    #     cursor.execute(""" SELECT id, title, url FROM "LC_SearchEngine_leetcodedata" """)
    #     rows = cursor.fetchall()
    # return rows

    """ TEMP QUERY
    Need to make use of user parameters
    """
    data = LeetcodeData.objects.filter().all()
    return data
