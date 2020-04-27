# paths
Optimizes the paths taken through campus and ranks schedules based on shortest distance

Should be called in format: 

- {
  "weekNum": #1-16
  ,
  "schedule": #one json element (schedule) of scheduler output
}

## Unit testing 

* Create a file "api_keys.json" in unittests folder and add the following keys with your values.

    - aws_access_key_id
    - aws_secret_access_key
    - aws_function_name

* CD to unittests folder and run "test.py"
