# :calendar: Day 50: 12/11/2020

---

## Topics

:clipboard: Measuring Performance

---

## Resources

:star: TBD

---

## Tasks

:white_check_mark: Create a copy of the `movie_search` application from Day 43, in the Day 50 directory.

:white_check_mark: Setup the `movie_search` application to accept search keywords as command line arguments.

:white_check_mark: Determine the 5 slowest methods in the `movie_search` application.  No significant latency found, outside of HTTP request delay.

---

## Notes

### :notebook: 12/11/20

- Setup `movie_search` application for profiling by allowing the ability to pass keyword search input as a system argument (in `sys.argv`), bypassing the manual input of keyword search text.
    - This allows profiling to run without waiting for user input.
    1. Added the `keyword_argument_check` function to [program.py](movie_search/program.py).
    2. Added and successfully tested the `test_keyword_argument_check` function to [test_program.py](movie_search/tests/test_program.py).

- Used the `cProfile` module in [api.py](movie_search/app/api.py) to test performance.
    - Only the `requests` module elements returned any significant amount (> 100 ms) of latency, and this latency is likely the HTTP request and response time.

    ```bash
          5772 function calls (5711 primitive calls) in 0.472 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.472    0.472 api.py:64(get)
        1    0.000    0.000    0.472    0.472 api.py:16(request)
        1    0.000    0.000    0.467    0.467 sessions.py:470(request)
        1    0.000    0.000    0.431    0.431 sessions.py:626(send)
        1    0.000    0.000    0.409    0.409 adapters.py:394(send)
        1    0.000    0.000    0.398    0.398 connectionpool.py:518(urlopen)
        1    0.000    0.000    0.392    0.392 connectionpool.py:357(_make_request)
        1    0.000    0.000    0.220    0.220 connectionpool.py:1002(_validate_conn)
        1    0.000    0.000    0.220    0.220 connection.py:356(connect)
        1    0.000    0.000    0.167    0.167 client.py:1333(getresponse)
        1    0.000    0.000    0.167    0.167 client.py:313(begin)
       15    0.000    0.000    0.158    0.011 {method 'readline' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.158    0.158 client.py:280(_read_status)
        1    0.000    0.000    0.157    0.157 socket.py:690(readinto)
        1    0.000    0.000    0.157    0.157 ssl.py:1230(recv_into)
        1    0.000    0.000    0.157    0.157 ssl.py:1090(read)
        1    0.157    0.157    0.157    0.157 {method 'read' of '_ssl._SSLSocket' objects}
        1    0.000    0.000    0.118    0.118 connection.py:161(_new_conn)
        1    0.000    0.000    0.118    0.118 connection.py:38(create_connection)
        1    0.115    0.115    0.115    0.115 {method 'connect' of '_socket.socket' objects}
        1    0.000    0.000    0.093    0.093 ssl_.py:355(ssl_wrap_socket)
        1    0.000    0.000    0.085    0.085 ssl_.py:481(_ssl_wrap_socket_impl)
        1    0.000    0.000    0.085    0.085 ssl.py:494(wrap_socket)
        1    0.000    0.000    0.085    0.085 ssl.py:983(_create)
        1    0.000    0.000    0.084    0.084 ssl.py:1302(do_handshake)
        1    0.083    0.083    0.083    0.083 {method 'do_handshake' of '_ssl._SSLSocket' objects}
        5    0.003    0.001    0.030    0.006 request.py:2486(getproxies_environment)
      190    0.005    0.000    0.027    0.000 _collections_abc.py:849(__iter__)
        2    0.000    0.000    0.027    0.013 utils.py:791(get_environ_proxies)
        3    0.000    0.000    0.022    0.007 utils.py:730(should_bypass_proxies)
        1    0.000    0.000    0.020    0.020 sessions.py:430(prepare_request)
        3    0.000    0.000    0.019    0.006 request.py:2517(proxy_bypass_environment)
        1    0.000    0.000    0.018    0.018 sessions.py:273(rebuild_proxies)
      179    0.004    0.000    0.016    0.000 os.py:674(__getitem__)
        1    0.000    0.000    0.016    0.016 sessions.py:701(merge_environment_settings)
        1    0.000    0.000    0.012    0.012 utils.py:175(get_netrc_auth)
      2/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:1002(_find_and_load)
      2/1    0.000    0.000    0.011    0.011 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
    ```

- Used the `cProfile` module in [program.py](movie_search/program.py) to test performance.
    - No functions/methods return any significant amount (> 10 ms) of latency.
