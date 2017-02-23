# Spark stat analyzer

POC to generate consolidated statistics from json files (generated by navitia-stat-logger or navitia-stat-exporter)

## Pre-requisites

* Spark 1.5+ (may work with previous versions, but untested)
* A repository with exported statistics files where stat files are stored in a tree like

```
  |
  \- <year>
      |
      \- <month>
          |
          \- <day>
              |
              \- <files>.json.log(.gz)
```

The files are json logs (one json per line). The files may be compressed using gzip.

Create config.py file from template config.py.dist and adapt them

## Usage

* For requests_calls consolidation
```
<path/to/spark>/bin/spark-submit  --conf spark.ui.showConsoleProgress=true --master='local[3]' manage.py -a <analyzer> -i <your_export_directory> -s <start_date> -e <end_date>
```

where:
* analyzer: analyzer name, possible value : token_stats, users, requests_calls, error_stats, coverage_stop_areas, coverage_modes, coverage_journeys_transfers or coverage_journeys_requests_params

* start_date and end_date is in YYYY-MM-DD format

* For coverage_journeys consolidation
```
<path/to/spark>/bin/spark-submit  --conf spark.ui.showConsoleProgress=true --master='local[3]' coverage_journeys.py <your_export_directory> <start_date> <end_date>
```

where:
* start_date and end_date is in YYYY-MM-DD format

Note that the results are stored in the export dir


### Shell ZSH users

Launching 'spark-submit' command , if you get error :

    zsh: no matches found
    
You can replace in command line `--master='local[3]'` by `--master=local`, or use *bash*.

## Tests

To run tests, you can build your own image and launch them using:

```
docker build -f Dockerfile.test -t stat-analyser:test .
docker run -e USER_ID=$(id -u) -it -v $(pwd):/srv/spark-stat-analyzer stat-analyser:test sh -c './run_test.sh'
```

The docker image is also hosted on our registry under the same name:tag

