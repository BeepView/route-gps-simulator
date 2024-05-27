# Driving GPS Tracker Simulator

Simulate a GPS tracker moving along a defined route, sending GPS coordinates in defined intervals.

#### Capabilities

- [x] Simulate a GPS tracker moving along a defined route
- [ ] Send GPS coordinates to a defined webhook endpoint at defined intervals
- [ ] Simulate GPS tracker in an infinite loop when duration is set to -1
- [ ] Simulate GPS tracker inaccuracy
- [ ] Simulate GPS tracker blackout
- [ ] Add custom departure time
- [ ] Simulate congestion and traffic delays
- [ ] Display alternative routes and select one

#### Installation

```bash
$ git clone
$ cd route-gps-simulator
$ python3 -m venv .venv # create a virtual environment
$ source .venv/bin/activate # activate the virtual environment
$ pip install -r requirements.txt # install dependencies
```

#### Usage

```bash
$ python3 gps-simulator.py --from <addr> --to <addr> --interval <seconds> --duration <seconds>
```

```bash
$ python3 gps-simulator.py --help

usage: simulate-tracker.py [-h] [--start START] [--end END] [--interval INTERVAL] [--duration DURATION] [--api_key API_KEY]

Simulate a GPS tracker

options:
  -h, --help           show this help message and exit
  --start START        Start location
  --end END            End location
  --interval INTERVAL  Interval in seconds
  --duration DURATION  Duration in seconds (0 to simulate the route once & -1 to loop the route infinitely)
  --api_key API_KEY    MapBox API key
```

#### Attribution

- https://github.com/theanuraganand/gps-simulator
