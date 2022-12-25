# Drivers Simulation in ride-hailing
This script simulates one or multiple drivers of ride-hailing on a working day.


## How it works?
The simulation works on strong and super-optimistic assumptions.

1. Driver(s) only work in a [district of central Tehran](https://www.google.com/maps/d/u/0/edit?mid=1ZnnRTYkj8N6YZyg5LM-kA1Fg1aoloEU&usp=sharing), where most companies and businesses are located.

2. There is an infinite demand in this district.

3. Driver(s) only accept trips inside this district.

4. Passengers are at most 1 KM away from the driver and if traffic is supper-heavy and the passenger is too far than 10 minutes, the driver cancels the trip.


After running the script, the driver(s) initial location will be randomly chosen in a district in the center of Tehran, and they start the work day immediately. A passenger's location will be chosen uniformly randomly from a 1 km circle around the driver, and the destination of the passenger will be chosen uniformly from the district in central Tehran, which is more than 2 Km away from the passenger.
There is only a 30 minutes rest time, and each driver is chosen randomly between 4-6 hours after starting time.

The price of trips collect from two main rides-hailing companies in Iran,  ([Snapp](https://snapp.ir/) & [Tapsi](https://tapsi.ir/)), and
real-time traffic data will obtain from [Neshan](https://neshan.org/) Company.



## Usage

#### 1. Number of drivers
Indicate the number of drivers in `main.py` by `NUMBER_OF_DRIVERS` variable. 

#### 2. Authentication
The request's header of Snapp/Tapsi API and the API key of Neshan should define as environment variables.
Snapp's authentication could be obtained from [Snapp's webapp] (https://app.snapp.taxi/pre-ride) and Tapsi's authentication could be obtained their [webapp](https://app.tapsi.cab). Example of Snapp/Tapsi's header avilable at: [Snapp](https://gist.github.com/thisistayeb/2aa5d9acec6db1355af94ce80ab58ed6), [Tapsi](https://gist.github.com/thisistayeb/118a0905fa85c478d72b9acc5a0c1605).

#### 3. Run script

Run `python main.py`

#### 4. Trajectory log files

The trajectory log file of each driver could be found in `src/log` directory.


## Subtools

- `summary.py`, generates a summary of the log file of a driver.

- `summary_for_all_logs.sh` run `summary.py` for all logs in the *log* directory.

> **how to use**:
> in *log* directory, run `./summary_for_all_logs.sh`


## Licensing

This project is licensed under the BSD license. 
More info at [`LICENSE`](https://github.com/thisistayeb/Snapp-Drivers-Simulation/blob/main/LICENSE).