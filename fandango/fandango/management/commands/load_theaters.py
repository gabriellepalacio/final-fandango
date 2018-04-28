import datetime
import json

from django.core.management.base import BaseCommand, CommandError
from fandango.models import Theater, Showtime, Movie


class Command(BaseCommand):
    help = 'Load row data into the database'


    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)


    def handle(self, *args, **options):

        json_path = options['json_file']


        self.stdout.write(self.style.SUCCESS('Loading JSON from "{}"'.format(json_path)))
        data = json.load(open(json_path, encoding="utf-8"))


        total = len(data['theaters'])


        self.stdout.write(self.style.SUCCESS('Processing {} rows'.format(total)))


        skipped = []

    #this is where the loop starts
        for i, row in enumerate(data['theaters']):

            theater_name = row['name']
            try:
                th_name = row['name']
                theater_id = row['id']
                th_address = row['address1']
                th_geo = row['geo']
                th_city = row['city']

                theater_instance, _ = Theater.objects.get_or_create(
                    name = th_name,
                    theater_id = theater_id,
                    address = th_address,
                    city = th_city,
                )

                theater_instance.lat = th_geo["latitude"]
                theater_instance.long = th_geo["longitude"]
                theater_instance.save()

                th_movies = row.get('movies')
                if(th_movies):
                    th_movie_list = []
                    #where the nested data starts
                    #so much nesting
                    for m, movie in enumerate(th_movies):

                        movie_instance, _ = Movie.objects.get_or_create(
                            movie_id = movie['id'],
                            title = movie['title'],
                            poster = movie['poster']['size']['full'][2:],
                            # rating = movie['rating'],

                        )
                        movie_instance.theaters.add(theater_instance)


                        #this is how we get date and time
                        variants = movie.get('variants')
                        if variants:
                            for v, variant in enumerate(variants):
                                amenityGroups = variant.get('amenityGroups')
                                if amenityGroups:
                                    for a, amenity in enumerate(amenityGroups):
                                        showtimes = amenity.get('showtimes')
                                        if showtimes:
                                            for s, showtime in enumerate(showtimes):
                                                showtime_instance, _ = Showtime.objects.get_or_create(
                                                    movie = movie_instance,
                                                    theater = theater_instance,
                                                    time = showtime['date'],
                                                    # tickets = showtime['ticketingUrl'],
                                                )

            except Exception as e:
                skipped.append(row)
                print(e, theater_name)
                continue


            self.stdout.write(self.style.SUCCESS('Processed {}/{}'.format(i + 1, total)), ending='\r')

            self.stdout.flush()


        if skipped:
            self.stdout.write(self.style.WARNING("Skipped {} records".format(len(skipped))))
            with open('skipped.json', 'w') as fh:
                json.dump(skipped, fh)

            # for theater in theater_name:
            #     location_name = code["name"]
            #     location_address = code["address1"]
            #     location_geo = code["geo"]
            #
            #     movie_time = row['movies']
            #     for time1 in movie_time:
            #         variants = row['variants']
            #         for time2 in variants:
            #             amenityGroups = row['amenityGroups']
            #             for time3 in amenityGroups:
            #                 showtimes = row['showtimes']
            #                 for time4 in showtimes:
            #                     time_date = row['ticketingDate']                 time_date = row['ticketingDate']
