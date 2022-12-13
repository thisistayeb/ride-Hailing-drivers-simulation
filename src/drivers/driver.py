"""Module simulate a driver."""
import datetime
import os
import random
import sys
import time

from src.api import distance, snapp, tapsi
from src.utils import destination, logfile, origin, tehran


class Driver:
    """Simulate a ride-sharing driver.


    Attributes:
        location: location of the driver at each step, initially chosen randomly.
        finishedlunch: a binary variable indicating the driver finished their lunch.
        start_work: each driver starts the working day with a random delay between 0-60 minutes.
        end_work: each driver works at least 10 hours.
        lunch_time: the driver has their lunch at the end of the last trip after this time.

    """

    def __init__(self):
        self.location = tehran.random_req_tehran()
        self.finishedlunch = False
        self.start_work = datetime.datetime.now()
        self.end_work = self.start_work + datetime.timedelta(hours=10)
        self.lunch_time = self.start_work + datetime.timedelta(
            hours=random.randint(6, 8)
        )
        self.name = logfile.generate_unique_name()

    def log(
        self,
        event: str,
        dest: tuple[float, float],
        minutes_to_origin: int = 0,
        minutes_to_dest: int = 0,
        minutes_for_wait=0,
        km_to_origin: float = 0.0,
        km_to_dest: float = 0.0,
        snapp_income: int = 0,
        tapsi_income: int = 0,
    ) -> None:
        """create a unique log file for every driver containing the trajectory of their work in the day.

        Args:
            event: indicate the situation of the driver, ex. TRIP/LUNCH/CANCELED/END.
            dest: geo-points of destination.
            minutes_to_origin: indicate the duration of driving to the passenger's location.
            minutes_to_dest: indicate driving time from the passanger's location-destination.
            minutes_for_wait: indicate the duration of the passanger's delay.
            km_to_origin: indicate the distance of driving to the passanger's location.
            km_to_dest: indicate the distance of driving from the passanger's location-destination.
            snapp_income: indicate raw price will be paid by Snapp company.
            tapsi_income: indicate raw price will be paid by Tapsi company.
        """
        dest_lat = dest[0]
        dest_lng = dest[1]
        cwd = os.path.abspath(os.path.dirname(__file__))
        logpath = os.path.abspath(os.path.join(cwd, "../log"))
        filename = os.path.join(logpath, f"{self.name}.csv")
        print(f"filename is {filename}")
        headers = "event,snapp_income,tapsi_income,minutes_to_origin,minutes_to_dest,minutes_for_wait,km_to_origin,km_to_dest,origin_lat,origin_lng,dest_lat,dest_lng,time\n"
        if not os.path.isfile(filename):
            with open(filename, "a", encoding="utf-8") as csvfile:
                csvfile.write(headers)
        with open(filename, "a", encoding="utf-8") as csvfile:
            csvfile.write(
                f"{event},{snapp_income},{tapsi_income},{minutes_to_origin},{minutes_to_dest},{minutes_for_wait},{km_to_origin},{km_to_dest},{self.location[0]},{self.location[1]},{dest_lat},{dest_lng},{datetime.datetime.now()}\n"
            )

    def lunch(self):
        if not (self.finishedlunch) and (self.lunch_time <= datetime.datetime.now()):
            print("go lunch")
            self.finishedlunch = True
            time.sleep(30 * 60)
            self.log(event="LAUNCH", dest=self.location, minutes_for_wait=30)

    def trip(self):
        """Simulate the trip of the driver.

        Driver eat their lunch in the first time available after `lunch_time`,
        they do not accept passengers far than 10 minutes driving and after
        `end_work` they do not accept any trip.
        Delay time of the passanger model a random intger between 0 to 5 minutes.
        """
        if not self.finishedlunch:
            self.lunch()
        if datetime.datetime.now() <= self.end_work:
            origin_geo = origin.near_req(self.location)
            dest_geo = destination.generate_dest(self.location)
            distance_origin = distance.distance(self.location, origin_geo)
            km_to_origin = distance_origin[1]
            minutes_to_origin = distance_origin[0]
            if minutes_to_origin <= 10:
                time.sleep(minutes_to_origin * 60)
                wait_for_passanger = random.randint(0, 5)
                time.sleep(wait_for_passanger * 60)
                distance_dest = distance.distance(origin_geo, dest_geo)
                minutes_to_dest = distance_dest[0]
                km_to_dest = distance_dest[1]
                snapp_price = snapp.get_snapp_price(origin_geo, dest_geo)
                tapsi_price = tapsi.get_tapsi_price(origin_geo, dest_geo)
                time.sleep(distance_dest[0] * 60)
                self.location = dest_geo
                self.log(
                    event="TRIP",
                    dest=dest_geo,
                    minutes_to_origin=minutes_to_origin,
                    minutes_to_dest=minutes_to_dest,
                    minutes_for_wait=wait_for_passanger,
                    km_to_origin=km_to_origin,
                    km_to_dest=km_to_dest,
                    snapp_income=snapp_price,
                    tapsi_income=tapsi_price,
                )
            else:
                time.sleep(1 * 60)
                self.log(event="CANCELED", dest=origin_geo)
        else:
            self.log(event="END", dest=self.location)
            sys.exit()

    def run(self):
        """execute trip function unless the driver reaches the end of the working day"""
        while True:
            self.trip()
