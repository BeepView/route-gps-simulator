# Driving GPS Tracker Simulator

Simulate a GPS tracker moving along a defined route, sending GPS coordinates in defined intervals.

> This script is designed to aid in the development and testing of applications that consume live GPS data from other devices. You should treat this script as if it were a GPS tracker device. It is not advisable to use this simulator to test the actual GPS tracker's webhook endpoint or any device-specific logic. Instead, use a separate webhook for this simulator and create custom logic to handle the simulated GPS data.

#### Capabilities

- [x] Simulate a GPS tracker moving along a defined route
- [x] Send GPS coordinates to a webhook endpoint at defined intervals
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

#### Configuration

Duplicate the `default.json.example` file and rename it to `default.json`. Update the `default.json` file with your MapBox API key.

```json
{
    "start": "Bishop Cotton Boys' School, 15, Residency Rd, Shanthala Nagar, Ashok Nagar, Bengaluru, Karnataka 560025, India",
    "end": "1st Cross Rd, Xavier Layout, Victoria Layout, Bengaluru, Karnataka 560047, India",
    "interval": 20,
    "duration": 0,
    "api_key": <your key>,
    "webhook": <webhook>
}
```

#### Usage

```bash
$ python3 gps-simulator.py --from <addr> --to <addr> --interval <seconds> --duration <seconds> --api_key <key> --webhook_url <url>
```

```bash
$ python3 gps-simulator.py --help

usage: simulate-tracker.py [-h] [--start START] [--end END] [--interval INTERVAL] [--duration DURATION] [--api_key API_KEY] [--webhook_url WEBHOOK_URL]

Simulate a GPS tracker

options:
  -h, --help                         show this help message and exit
  --start START                    Start location
  --end END                         End location
  --interval INTERVAL             Interval in seconds
  --duration DURATION             Duration in seconds (0 to simulate the route once & -1 to loop the route infinitely)
  --api_key API_KEY               MapBox API key
  --webhook_url WEBHOOK_URL   Webhook URL to which the simulated coordinates JSON are POSTed
```

#### Webhook Callback Details

The simulated GPS coordinates will be POSTed to the webhook is as follows:

```json
  {
    "coordinates": {
      "lat": <floating point latitude>,
      "lng": <floating point longitude>,
    }
  }
```

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"coordinates": {"lat": 12.9716, "lng": 77.5946}}' <webhook_url>
```

#### Attribution

- https://github.com/theanuraganand/gps-simulator
